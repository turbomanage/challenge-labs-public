from airflow import DAG
from datetime import datetime
from airflow.providers.google.cloud.operators.bigquery import BigQueryExecuteQueryOperator

DATASETS = ['raw', 'optimized', 'views', 'functions', 'models']
PROJECT = 'your-project-id'

default_args = {
    'owner': 'cl-student',
    'depends_on_past': False,
    'start_date': datetime(2021, 1, 1),
    'retries': 0,
}

dag = DAG(
    'create_bigquery_datasets',
    default_args=default_args,
    schedule_interval=None,
)

for dataset in DATASETS:
    create_dataset_task = BigQueryCreateEmptyDatasetOperator(
        task_id=f'create_{dataset}',
        dataset_id=f'{dataset}_composer',
        project_id=PROJECT,
        dag=dag
    )
