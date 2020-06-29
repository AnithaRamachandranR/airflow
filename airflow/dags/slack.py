from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.contrib.operators.slack_webhook_operator import SlackWebhookOperator
from airflow.hooks.base_hook import BaseHook

SLACK_CONN_ID = 'anitha_slack'
#slack_channel = BaseHook.get_connection(SLACK_CONN_ID).login
slack_webhook_token = BaseHook.get_connection(SLACK_CONN_ID).password

def print_hello():
    return 'Hello world!'
default_args = {
        'owner': 'anitha',
        'start_date':datetime(2018,8,11),
}

dag = DAG('slack_example', description='Simple tutorial DAG',
          schedule_interval='* * * * *',
          default_args = default_args)

dummy_operator = DummyOperator(task_id='dummytask', retries=3, dag=dag)

hello_operator = PythonOperator(task_id='hellotask', python_callable=print_hello, dag=dag)

slack = SlackWebhookOperator(
        task_id="slack_msg",
        http_conn_id="anitha_slack",
        webhook_token=slack_webhook_token,
        text="hi ani",
        username="anitha ramachandran",
        channel="airflowteam",
        dag=dag
)

slack >> dummy_operator >> hello_operator


