from airflow import DAG
from airflow.operators.bash_operator import BashOperator

from datetime import datetime, timedelta
default_args = {
            'owner': 'airflow',
                'start_date': datetime(2019, 1, 1),
                    'retry_delay': timedelta(minutes=5),

                        }
dag = DAG('slacks_channel', default_args=default_args)
#hello=BashOperator(task_id='testslackchannel',bash_command='echo hi',dag=dag)
#dummy_operator = DummyOperator(task_id='dummy_task', retries=3, dag=dag)
anitha= BashOperator(task_id='testslackchennel',bash_command='python /home/ec2-user/airflow/dags/createslack.py ', dag=dag)
