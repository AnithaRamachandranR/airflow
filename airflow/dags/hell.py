from airflow.models import Variable
import sys
import json

value=sys.argv[1]
print(value)
j=Variable.get(value)
print(j)

#var1='anitha'
#push= context['ti'].xcom_push(key='value', value=var1)
#print(push)
