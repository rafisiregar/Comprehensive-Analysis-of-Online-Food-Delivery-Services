
# Analysis of ETL Automation and Data Validation in Online Food Delivery Services

## Repository Outline

1. **description.md**Contains the project description, objectives, and an overview of ETL processes, data validation (using Great Expectations), and the visualization of the analysis results from online food delivery services.
2. **P2M3_rafi_siregar_conceptual.txt**Contains explanations of basic concepts related to NoSQL, RDBMS, Great Expectations, Batch Processing, and supporting tools/platforms for NoSQL.
3. **P2M3_rafi_siregar_DAG_graph.png**A visual graph depicting the ETL workflow in the form of a Directed Acyclic Graph (DAG) using Apache Airflow.
4. **P2M3_rafi_siregar_DAG.py**A Python script that defines the DAG for the ETL process in Apache Airflow, setting up the workflow that includes data extraction, transformation, and loading.
5. **P2M3_rafi_siregar_data_clean.csv**A cleaned dataset ready to be used in the transformation process for data validation using the Great Expectations framework.
6. **P2M3_rafi_siregar_data.raw.csv**The raw dataset extracted from Kaggle before being processed and cleaned in the transformation stage.
7. **P2M3_rafi_siregar_ddl.txt**Contains the script for defining the data structure (DDL) in the database.
8. **P2M3_rafi_siregar_GX.ipynb**A Python notebook that uses Great Expectations to perform data validation and cleaning to meet the required quality standards.
9. **README.md**Contains a general description of the project, specifically for Milestone 3.
10. **P2M3_rafi_siregar_introduction&objective.png**A brief description of the project identity and the project’s objectives.
11. **P2M3_rafi_siregar_kesimpulan.png**A description of the conclusions from the analysis, based on the data visualizations and insights gathered.
12. **P2M3_rafi_siregar_plot&insight_1.png to P2M3_rafi_siregar_plot&insight_6.png**Graphical visualizations obtained from Elasticsearch and Kibana to illustrate business insights related to the online food delivery service.
13. **.gitignore**
    A Git configuration file to exclude certain files or folders from being tracked or pushed to the repository.

## Problem Background

I am a data scientist currently working at a startup in the online application industry. With the rapid growth of the tech industry and changing lifestyle trends, online food delivery services have become an integral part of everyday life. The dataset, obtained from [Kaggle](https://www.kaggle.com/datasets/sudarshan24byte/online-food-dataset), contains information from a food delivery platform over a certain period, including various attributes related to customer demographics, location, and behavior.

## Project Output

Automating the ETL process using a pipeline on Apache Airflow. Additionally, data validation will be performed using Great Expectations. Elasticsearch and Kibana will be used to visualize business insights.

## Data

The Online Food Deliveries dataset obtained from Kaggle. The dataset has 12 columns containing customer demographic information. The initial data consists of 388 rows, which reduced to 285 rows after data cleaning.

## Method

1. **ETL Automation**Using Apache Airflow as a platform to schedule and automate the extraction, transformation, and loading of data.
2. **Data Validation**Using the Great Expectations framework to set and run validation rules such as null checks, type checks, range checks, and uniqueness checks.
3. **Data Visualization**
   Using Elasticsearch as the data storage and Kibana as the data visualization platform to provide insights for the project stakeholders.

## Tech Stack

* **Programming Language:** Python
* **Tools & Platforms:** Apache Airflow, Jupyter Notebook, Great Expectations, Elasticsearch, Kibana
* **Supporting Libraries:**

  * `pandas` – For manipulating and cleaning tabular data.
  * `great_expectations` – A framework for data validation and documentation of data quality.
  * `datetime` – For scheduling the pipeline execution times in Airflow.
  * `os`, `json` – Used for file path management and JSON-based configuration (if needed).
  * `psycopg2` – Library to connect to PostgreSQL databases for data extraction.
  * `elasticsearch`, `helpers` – To connect and send data to Elasticsearch.
  * `matplotlib`, `seaborn` – For additional local visualizations or exploratory analysis (apart from Kibana).

## References

1. [Introduction to NoSQL Databases](https://medium.com/@mark.rethana/introduction-to-nosql-databases-c5b43f3ca1cc)
2. [Relational vs NoSQL - When Should I Use One Over the Other?](https://www.datastax.com/blog/relational-vs-nosql-when-should-I-use-one-over-the-other)
3. [Top 10 Popular NoSQL Databases](https://reliasoftware.com/blog/popular-nosql-databases)
4. [Great Expectations for Data Quality and Reliability](https://medium.com/@elifsinem.aktas/great-expectations-for-data-quality-and-reliability-e9f4c1ee20a5)
5. [What is Batch Processing? (AWS)](https://aws.amazon.com/id/what-is/batch-processing/)
