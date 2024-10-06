from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

# Definir a DAG
with DAG('meu_primeiro_dag',
         start_date=datetime(2023, 10, 1),  # Data de início
         schedule_interval=None,           # Não agendado automaticamente
         catchup=False                     # Não fazer catchup de execuções anteriores
         ) as dag:

    # Definir tarefas
    task1 = BashOperator(
        task_id='first_task',
        bash_command='echo 1'
    )

    task2 = BashOperator(
        task_id='second_task',
        bash_command='echo 2'
    )

    # Definir ordem de execução das tarefas
    task1 >> task2
