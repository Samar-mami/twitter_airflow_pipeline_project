from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import timedelta
from twitter_etl import get_tweets
from twitter_etl import get_credentials
from twitter_etl import connect_twitter_api

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 10, 06),
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'twitter_dag',
    default_args= default_args
)

get_credentials= PythonOperator(
    task_id='get_credentials_task',
    python_callable=get_credentials,
    dag=dag
)

connect_twitter_api= PythonOperator(
    task_id='connect_tweeter_task',
    python_callable=connect_twitter_api,
    provide_context=True,
    #op_args=get_credentials_task.output,
    dag=dag
)

get_tweets = PythonOperator(
    task_id='get_tweets_task',
    python_callable=get_tweets,
    provide_context=True,
    #op_args=[connect_twitter_api_task.output, 'tweets.csv'],
    dag=dag
)


get_credentials >> connect_twitter_api >> get_tweets