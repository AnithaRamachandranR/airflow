#from datetime import datetime
from airflow import DAG

#from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime,timedelta
import json
from airflow.operators.bash_operator import BashOperator
from airflow.models import Variable


default_args = {
            'owner': 'airflow',
                'start_date': datetime(2019, 1, 1),
                    'retry_delay': timedelta(minutes=5),

                        }
dag = DAG('slacks_variable', default_args=default_args)
#hello=BashOperator(task_id='testslackbash',bash_command='echo hi',dag=dag)
#dummy_operator = DummyOperator(task_id='dummy_task', retries=3, dag=dag)
anitha= BashOperator(task_id='testslackbash',bash_command='python /home/ec2-user/airflow/dags/hell.py {{var.json.buckets.bucketname}}',xcom_push=True, dag=dag)

