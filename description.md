# Judul Project

Analisis Terhadap Automatisasi ETL dan Validasi Data Pada Layanan Pesan Antar Makanan Daring

## Repository Outline

1. description.md
   Berisikan deskripsi proyek, tujuan, dan gambaran umum terkait kegiatan ETL, validasi (great expectation) dan visualisasi dari hasil analisis data layanan pesan antar makanan daring.
2. P2M3_rafi_siregar_conceptual.txt
   Berisikan penjelasan konsep pengetahuan dasar terkait NoSQL, RDBMS, Great Expectation, Batch Processing, dan alat/plaform penunjunjang NoSQL.
3. P2M3_rafi_siregar_DAG_graph.png
   Grafik visual yang menggambarkan alur kerja ETL dalam bentuk DAG (Directed Acyclic Graph) menggunakan Apache Airflow.
4. P2M3_rafi_siregar_DAG.py
   Skrip Python yang mendefinisikan DAG untuk proses ETL di Apache Airflow, mengatur alur kerja yang meliputi ekstraksi, transformasi, dan pemuatan data.
5. P2M3_rafi_siregar_data_clean.csv
   Dataset yang sudah dibersihkan dan siap digunakan pada proses transformasi data untuk proses validasi menggunakan framework Great Expectation.
6. P2M3_rafi_siregar_data.raw.csv
   Dataset mentah yang diekstrak dari situs kaggle sebelum diproses dan dibersihkan dalam tahap transformasi.
7. P2M3_rafi_siregar_ddl.txt
   Berisi skrip untuk mendefinisikan struktur data (DDL) dalam basis data.
8. P2M3_rafi_siregar_GX.ipynb
   Notebook Python yang menggunakan Great Expectations untuk melakukan validasi dan pembersihan data agar memenuhi standar kualitas yang diperlukan.
9. README.md
   Berisikan deskripsi mengenai  penjelasan umum tentang proyek Milestone 3.
10. P2M3_rafi_siregar_introduction&objective.png
    Deksripsi terkait identitas yang melakukan proyek dan obyektif dari tujuan proyek secara ringkas.
11. P2M3_rafi_siregar_kesimpulan.png
    Deskripsi mengenai kesimpulan dari analisis yang dilakukan, berdasarkan visualisasi data yang dihasilkan melalui plot/grafik dan insight yang telah diperoleh.
12. P2M3_rafi_siregar_plot&insight_1.png hingga P2M3_rafi_siregar_plot&insight_6.png
    Visualisasi grafis yang diperoleh dari elasticsearch dan kibana untuk menggambarkan hasil analisis bisnis terkait layanan pemesanan makanan daring.
13. .gitignore
    File konfigurasi Git untuk mengecualikan file atau folder tertentu agar tidak ikut ditrack atau dikirim ke repository.

## Problem Background

Saya adalah seorang data scientist yang saat ini bekerja di sebuah perusahaan startup aplikasi online. Seiring dengan pertumbuhan pesat industri teknologi dan perubahan gaya hidup masyarakat, layanan pesan antar makanan secara daring telah menjadi bagian integral dari kehidupan sehari-hari. Dataset diperoleh dari situs [kaggle](https://www.kaggle.com/datasets/sudarshan24byte/online-food-dataset) berisi informasi dari platform pemesanan makanan daring selama periode tertentu, mencakup berbagai atribut terkait demografi, lokasi, dan perilaku konsumen.

## Project Output

Melakukan proses automasi ETL menggunakan pipeline pada Apache Airflow. Selain itu memvalidasi data menggunakan Great Expectations. Elasticsearch dan Kibana digunakan sebagai visualisasi insight dari segi bisnis.

## Data

Dataset Online Food Deliveries yang diperoleh dari situs Kaggle. Dataset memiliki 12 kolom berupa informasi demografi pelanggan. Total baris awal berjumlah  388 baris data dan 285 baris data setelah dilakukan proses data cleaning.

## Method

1. ETL Automation menggunakan Apache Airflow sebagai platform menjadwalkan dan mengotomasi proses ekstraksi, trnasofrmasi, dan loading data.
2. Data Validation menggunakan framework Great Expectations untuk menetapkan dan menjalankan aturan validasi seperti null check, type check, range check, dan unique check.
3. Data Visualization menggunakan ElasticSearch sebagai penyimpanan data dan Kibana sebagai platform visualisasi data. Hasil berupa insight yang dapat digunakan bagi stakeholders proyek ini.

## Stacks

* **Bahasa Pemrograman:** Python
* **Tools & Platform:** Apache Airflow, Jupyter Notebook, Great Expectations, ElasticSearch, Kibana
* **Library Pendukung:**

  * `pandas` – Untuk manipulasi dan pembersihan data tabular.
  * `great_expectations` – Framework untuk validasi dan dokumentasi kualitas data.
  * `datetime` – Mengatur waktu dan jadwal eksekusi pipeline pada Airflow.
  * `os`, `json` – Digunakan untuk manajemen path file dan konfigurasi berbasis JSON (jika diperlukan).
  * `psycopg2` – Library koneksi ke database PostgreSQL untuk proses ekstraksi.
  * `elasticsearch`, `helpers` – Untuk menghubungkan dan mengirim data ke Elasticsearch.
  * `matplotlib`, `seaborn` – Untuk keperluan visualisasi tambahan di luar Kibana (misalnya untuk laporan lokal atau eksplorasi awal).

## Reference

1. [Introduction to NoSQL Databases](https://medium.com/@mark.rethana/introduction-to-nosql-databases-c5b43f3ca1cc)
2. [Relational vs NoSQL - When Should I Use One Over the Other?](https://www.datastax.com/blog/relational-vs-nosql-when-should-I-use-one-over-the-other)
3. [Top 10 Popular NoSQL Databases](https://reliasoftware.com/blog/popular-nosql-databases)
4. [Great Expectations for Data Quality and Reliability](https://medium.com/@elifsinem.aktas/great-expectations-for-data-quality-and-reliability-e9f4c1ee20a5)
5. [What is Batch Processing? (AWS)](https://aws.amazon.com/id/what-is/batch-processing/)
