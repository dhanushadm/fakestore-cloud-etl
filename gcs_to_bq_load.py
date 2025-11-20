from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator

with DAG(
    dag_id="gcs_to_bq_load",
    start_date=days_ago(1),
    schedule_interval=None,
    catchup=False,
) as dag:

    load_csv_to_bq = GCSToBigQueryOperator(
        task_id="load_csv_to_bq",
        bucket="practice-01",
        source_objects=["transformed/data.csv"],
        destination_project_dataset_table=(
            "probable-analog-477614-m5.etl_dataset.products"
        ),
        source_format="CSV",
        skip_leading_rows=1,
        autodetect=True,
        write_disposition="WRITE_TRUNCATE",
        gcp_conn_id="google_cloud_default",
    )
