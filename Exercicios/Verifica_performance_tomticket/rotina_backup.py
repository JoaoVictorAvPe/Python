import os
import csv
import dotenv
import requests
from pathlib import Path

dotenv.load_dotenv()

ROOT_DIR = Path(__file__).parent
CSV_FILE_PATH = ROOT_DIR / 'tomticket.csv'
LOG_FILE_PATH = ROOT_DIR / 'tomticket.log'

TOMTICKET_API_URL = os.getenv('TOMTICKET_API_URL')
TOMTICKET_TOKEN = os.getenv('TOMTICKET_TOKEN')
TOMTICKET_DEPARTMENT_ID = os.getenv('TOMTICKET_DEPARTMENT_ID')
TOMTICKET_CATEGORY_ID = os.getenv('TOMTICKET_CATEGORY_ID_BACKUP')

if not TOMTICKET_API_URL:
    raise Exception('TOMTICKET_API_URL not set')

if not TOMTICKET_TOKEN:
    raise Exception('TOMTICKET_TOKEN not set')

if not TOMTICKET_DEPARTMENT_ID:
    raise Exception('TOMTICKET_DEPARTMENT_ID not set')

if not TOMTICKET_CATEGORY_ID:
    raise Exception('TOMTICKET_CATEGORY_ID not set')

TOMTICKET_URL = f'{TOMTICKET_API_URL}/{TOMTICKET_TOKEN}'

MENSAGEM_CHAMADO = '''Necessário realização da rotina de backup do cliente.
Sendo feito a seguinte rotina de backup:
    - Frontend do Zabbix: Hosts e Templates
    - Backend do Zabbix: Scripts
    - Backend do Grafana: Arquivo grafana.db
'''

with open(CSV_FILE_PATH, encoding='utf-8-sig') as csv_file:
    csv_field_names = ['EMPRESA', 'CLIENTE', 'USUARIO']
    csv_reader = csv.DictReader(csv_file, fieldnames=csv_field_names, delimiter=';')

    for row in csv_reader:
        usuario = row['USUARIO']
        cliente = row['CLIENTE']
        TOMTICKET_ENDPOINT = f'{TOMTICKET_URL}/{usuario}'

        request_options = {
            'id_departamento': TOMTICKET_DEPARTMENT_ID,
            'id_tipoassunto': TOMTICKET_CATEGORY_ID,
            'titulo': f'[{cliente}] - Rotina de Backup Semanal',
            'mensagem': MENSAGEM_CHAMADO,
            'prioridade': '2'
        }
        tomticket_response = requests.post(TOMTICKET_ENDPOINT, request_options)

        if tomticket_response.status_code != 200:
            with open(LOG_FILE_PATH, 'a') as log_file:
                json_response = tomticket_response.json()
                response_message = json_response['mensagem']
                log_file.write(
                    f'{cliente} - Erro ao criar o chamado: ' \
                    f'{response_message}\n'
                )