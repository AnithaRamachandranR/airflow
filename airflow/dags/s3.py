from airflow import DAG
from datetime import datetime
from datetime import timedelta
from airflow.operators import DummyOperator, PythonOperator
import airflow.hooks.S3_hook


default_args = {
    'owner': 'anitha',
    'start_date': datetime(2019, 1, 1),
    'retry_delay': timedelta(minutes=5)
}
def upload(filename,key,bucket_name):
    hook = airflow.hooks.S3_hook.S3Hook('anitha_s3')
    hook.load_file(filename, key, bucket_name)
# Using the context manager alllows you not to duplicate 
with DAG('S3', default_args=default_args, schedule_interval='@once') as dag:

    start_task = DummyOperator(
            task_id='dummy_start'
    )

    upload_to_S3_task = PythonOperator(
            task_id='upload_file_to_S3',
            python_callable=upload,op_kwargs={
        'filename': '/home/ec2-user/airflow/dags/email.py',
        'key': 'email.py',
        'bucket_name': 'saksbucket',
    },)
    start_task >> upload_to_S3_task
