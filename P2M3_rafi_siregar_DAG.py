# Milestone 3

"""
Nama  : Rafi Arya Siregar
Batch : HCK-028
Objektif : Tujuan dari proyek ini adalah untuk mengidentifikasi dan menganalisis dataset yang berkaitan dengan layanan pesan antar makanan daring
          yang terkumpul dalam jangka waktu tertentu menggunakan data yang diambil dari situs kaggle. 
          Proses yang akan dilakukan meliputi pembuatan alur proses kegiatan ETL menggunakan Directed Acyclic Graph (DAG) yang disediakan oleh apache airflow serta penggunaan Great Expectations sebagai teknik validasi data. Saya menggunakan dataset yang tersedia di [kaggle](https://www.kaggle.com/datasets/sudarshan24byte/online-food-dataset) untuk diolah (preprocess) agar menghasilkan dataset yang bersih dan layak digunakan untuk keperluan viisualisasi data sebagai informasi utuh.
"""

# Import Libraries
import datetime as dt
from datetime import timedelta
from airflow import DAG # type:ignore
from airflow.decorators import task # type:ignore
from airflow.operators.empty import EmptyOperator # type:ignore
import psycopg2 as db
from elasticsearch import Elasticsearch, helpers # type:ignore
import pandas as pd 

# Default arguments untuk proses DAG
default_args = {
    'owner': 'Rafi Arya Siregar',
    'start_date': dt.datetime(2024, 11, 1), # Memulai penjadwalan tanggal 1 November 2024
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=10), # Interval per 10 menti
}

# Definisi DAG dan tugas-tugasnya
with DAG(
    'Milestone3',
    description='ETL pipeline: Postgres → Transform → Elasticsearch',
    default_args=default_args,
    schedule_interval='0 9-9/10 * * 6',  # Cron expression untuk penjadwalan setiap Hari Sabtu
    catchup=False
) as dag:
    
    # Menandai awal eksekusi DAG
    start = EmptyOperator(task_id='start')  

    # Menandai akhir eksekusi DAG
    end = EmptyOperator(task_id='end')  

    # Fungsi untuk ekstraksi data dari PostgreSQL
    @task()
    def extract():
        """
        Mengekstrak data dari PostgreSQL dan menyimpannya ke file CSV.
        
        Menggunakan koneksi ke database PostgreSQL untuk mengekstrak data dari tabel dan
        menyimpannya dalam format CSV untuk diproses lebih lanjut.

        Proses:
        1. Menyiapkan koneksi ke database PostgreSQL dengan menggunakan string koneksi.
        2. Mengambil data dari tabel menggunakan SQL query.
        3. Menyimpan data hasil ekstraksi ke dalam file CSV.
        4. Mengembalikan path file CSV untuk digunakan dalam langkah transformasi.
        
        Returns:
            str: Path file CSV yang berisi data mentah.
        """
        conn_string = "port=5432 dbname='airflow' host='postgres' user='airflow' password='airflow'"

        conn = db.connect(conn_string)

        # Mengambil data dari tabel table_m3 dan menyimpannya ke file CSV
        df = pd.read_sql("SELECT * FROM table_m3", conn)
        raw_path = '/tmp/P2M3_rafi_siregar_data_raw.csv'
        df.to_csv(raw_path, index=False)
        print(f"Extract saved raw CSV: {raw_path}")
        return raw_path

    @task()
    # Fungsi untuk melakukan pembersihan data mentah
    def transform(raw_path: str) -> str:
        """
        Melakukan pembersihan data mentah dengan mengatasi nilai null, duplikat, dan format kolom.
        
        Membaca file CSV yang berisi data mentah, kemudian membersihkan data dari nilai kosong,
        menghapus duplikat, dan memperbaiki nama kolom agar sesuai dengan standar.

        Proses:
        1. Membaca file CSV yang berisi data mentah menggunakan pandas.
        2. Mengatasi nilai null pada kolom numerik dan non-numerik dengan imputasi (mengisi dengan 0 atau 'unknown').
        3. Menghapus duplikat dari data untuk memastikan tidak ada data yang redundan.
        4. Mengubah nama kolom menjadi lowercase dan mengganti spasi dengan underscore untuk konsistensi.
        5. Menyimpan data yang telah dibersihkan ke file CSV tanpa indeks.
        6. Mengembalikan path file CSV yang berisi data yang telah dibersihkan.
        
        Args:
            raw_path (str): Path file CSV yang berisi data mentah.

        Returns:
            str: Path file CSV yang berisi data yang telah dibersihkan.
        """
        # Membaca data mentah yang diekstrak sebelumnya
        df = pd.read_csv(raw_path)

        # Imputasi data null
        for col in df.columns:
            if df[col].isnull().any():
                if pd.api.types.is_numeric_dtype(df[col]):
                    df[col].fillna(0, inplace=True)
                else:
                    df[col].fillna('unknown', inplace=True)

        # Menghapus data duplikat
        df.drop_duplicates(inplace=True)

        # Mengubah nama kolom menjadi lower case dan mengganti spasi dengan underscore
        df.columns = [col.lower().replace(' ', '_') for col in df.columns]

        # Menyimpan data yang telah dibersihkan ke file CSV tanpa indeks
        clean_path = '/tmp/P2M3_rafi_siregar_data_clean.csv'
        df.to_csv(clean_path, index=False)  # Pastikan index=False
        print(">>> PROSES CLEANING SELESAI <<<")

        print(f"\nExtract saved cleaned CSV: {clean_path}")
        return clean_path

    @task()
    def load(clean_path: str):
        """
        Memuat data yang telah dibersihkan ke Elasticsearch menggunakan metode bulk dengan ID unik berbasis hash.

        Proses ini mencakup:
        1. Membaca file CSV hasil transformasi menggunakan pandas.
        2. Mengatur koneksi ke Elasticsearch dengan konfigurasi timeout dan retry.
        3. Melakukan pengecekan koneksi dan membuat index baru jika belum tersedia.
        4. Membuat ID unik (`_id`) menggunakan hash dari beberapa kolom kombinasi (age, gender, occupation, dll).
        5. Menyusun dokumen ke dalam format yang sesuai untuk bulk insert, termasuk menyimpan hash ID ke dalam `_source` sebagai `doc_id`.
        6. Mengunggah data ke Elasticsearch secara efisien dengan `helpers.bulk()` disertai penanganan error.
        7. Menyimpan ulang file CSV ke direktori airflow untuk dokumentasi/backup.

        Args:
            clean_path (str): Path file CSV yang berisi data yang telah dibersihkan.

        Raises:
            ValueError: Jika koneksi ke Elasticsearch gagal.
            Exception: Jika terjadi kegagalan saat proses bulk insert ke Elasticsearch.
        """

        df = pd.read_csv(clean_path)
        
        # Meambahkan konfigurasi timeout dan retry
        elastic = Elasticsearch(
            ['http://elasticsearch:9200'],
            timeout=30,  # Timeout 30 detik
            max_retries=3,  # Maksimal 3 kali retry
            retry_on_timeout=True  # Retry jika timeout
        )
        
        # Memverifikasi koneksi ke Elasticsearch
        if not elastic.ping():
            raise ValueError("Gagal koneksi!")
        else:
            print("Koneksi Berhasil!")
        
        id = "pemesanan_makanan_online"
        
        # Membuat index jika belum ada
        if not elastic.indices.exists(index=id):
            print(f"Index ke-{id} tidak ditemukan! Membuat index baru . . .")
            elastic.indices.create(index=id)

        # Menggunakan bulk helper dengan error handling
        actions = [
            {
                "_index": id,
                "_id": i+1,
                "_source": row.to_dict()
            }
            for i, row in df.iterrows()
        ]

        # Menambahkan error handling untuk bulk insert
        try:
            success, failed = helpers.bulk(elastic, actions, stats_only=False)
            print(f"Index: {success} documents. Failed: {failed}")
            
            if failed:
                for error in failed:
                    print(f"Error: {error}")
        except Exception as e:
            print(f"Terjadi error saat melakukan bulk insert: {str(e)}")
            raise
        
        # Menyimpan data yang dibersihkan ke file lokal
        df.to_csv('/opt/airflow/dags/P2M3_rafi_siregar_data_clean.csv', index=False)
        
    # Objek ekstraksi, transofrmasi, dan load data
    extract_data = extract()
    transform_data = transform(extract_data)  # Pastikan passing raw_path dari extract
    load_data = load(transform_data)  # Pastikan passing clean_path dari transform
    
    # DAG proses (Graph)
    start >> extract_data >> transform_data >> load_data >> end
