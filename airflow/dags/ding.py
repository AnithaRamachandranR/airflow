from datetime import datetime,timedelta

import airflow
from airflow.contrib.operators.dingding_operator import DingdingOperator
from airflow.models import DAG

args = {
        'owner': 'anitha',
        'start_date':datetime(2018,8,11),
        }

dag = DAG(
    dag_id='dingding_example',
    default_args=args,
    schedule_interval='@once',
    dagrun_timeout=timedelta(minutes=60),
)

text_msg_remind_all = DingdingOperator(
    task_id='text_msg_remind_all',
    dingding_conn_id='anitha_ding',
    message_type='text',
    message='Airflow dingding text message remind all users in group',
    # list of user phone/email here in the group
    # when at_all is specific will cover at_mobiles
    at_mobiles=['9994692674'],
    at_all=True,
    dag=dag,
)

