# FakeStore API – Cloud ETL Data Pipeline

## Project Overview
This project is an end-to-end cloud-based ETL pipeline that extracts product data from the FakeStore API, transforms the raw JSON into structured CSV, and loads it into Google BigQuery for analytics.

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
