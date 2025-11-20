# FakeStore API – Cloud ETL Data Pipeline


## Project Workflow

This project implements a cloud-based ETL (Extract, Transform, Load) pipeline using Google Cloud Platform.

### 1. Extract
An HTTP-triggered Cloud Function calls the FakeStore public API and fetches real-time product data in JSON format.  
The raw data is stored in Google Cloud Storage under the `raw/` folder.

### 2. Transform
A second Cloud Function reads the raw JSON file from Cloud Storage, cleans the data, and converts it into a structured CSV format.  
Only required fields such as `id`, `title`, and `price` are retained.  
The transformed data is saved in the `transformed/` folder.

### 3. Load
Apache Airflow (Cloud Composer) is used to orchestrate the pipeline.  
A DAG automatically loads the transformed CSV file from Cloud Storage into Google BigQuery, making the data ready for querying and analytics.

### 4. Automation
The complete pipeline can be triggered manually or executed as an automated workflow using Airflow.


## Technologies Used
- Python
- Google Cloud Functions
- Google Cloud Storage
- BigQuery
- Apache Airflow (Cloud Composer)

## Architecture
API → Cloud Function (Extract) → GCS (raw JSON)  
→ Cloud Function (Transform) → GCS (CSV)  
→ Airflow DAG → BigQuery

## Features
- Automated API data extraction
- Cloud-based transformation logic
- Scalable cloud storage
- BigQuery analytics-ready table
- Airflow-based orchestration

## How It Works
1. Extract Cloud Function calls FakeStore API.
2. Data is saved as JSON in Cloud Storage.
3. Transform Cloud Function converts JSON to CSV.
4. Airflow loads the CSV into BigQuery.

## Learning Outcomes
- Real-world ETL pipeline design
- Cloud-native data processing
- Workflow automation using Airflow
