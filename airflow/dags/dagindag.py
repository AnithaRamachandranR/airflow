from airflow import DAG

#from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime,timedelta
from airflow.operators.bash_operator import BashOperator
default_args = {
            'owner': 'airflow',
                'start_date': datetime(2019, 1, 1),
                    'retry_delay': timedelta(minutes=5),

                        }

dag = DAG('dagindag', default_args=default_args)
anitha= BashOperator(task_id='testslackbash',bash_command='python /home/ec2-user/airflow/dags/hell.py "{{ ti.xcom_pull(key="value") }}"',xcom_push=True, dag=dag)
