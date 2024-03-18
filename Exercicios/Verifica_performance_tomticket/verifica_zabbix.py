from os import getenv
import csv
import dotenv
import requests
from pathlib import Path

def write_in_log(message:str) -> None:
    with open(LOG_FILE_PATH, mode='a', encoding='utf-8-sig') as log_file:
            log_file.write(message)

dotenv.load_dotenv()

ROOT_DIR = Path(__file__).parent
CSV_FILE_PATH = ROOT_DIR / 'tomticket.csv'
LOG_FILE_PATH = ROOT_DIR / 'tomticket.log'

TOMTICKET_API_URL = 'TOMTICKET_API_URL', getenv('TOMTICKET_API_URL')
TOMTICKET_TOKEN = 'TOMTICKET_TOKEN', getenv('TOMTICKET_TOKEN')
TOMTICKET_DEPARTMENT_ID = 'TOMTICKET_DEPARTMENT_ID', getenv('TOMTICKET_DEPARTMENT_ID')
TOMTICKET_CATEGORY_ID = 'TOMTICKET_CATEGORY_ID', getenv('TOMTICKET_CATEGORY_ID_ZABBIX')

enviroment_variables = TOMTICKET_API_URL, TOMTICKET_TOKEN, TOMTICKET_DEPARTMENT_ID, TOMTICKET_CATEGORY_ID

for variable in enviroment_variables:
    if not variable[1]:
        error_message = variable[0] + ' not set\n'
        write_in_log(error_message)
        raise Exception(error_message)
    
TOMTICKET_URL = f'{TOMTICKET_API_URL[1]}/{TOMTICKET_TOKEN[1]}'

MENSAGEM_CHAMADO = 'Realizar verificação de HEALTHCHECK no servidor zabbix do cliente.'

with open(CSV_FILE_PATH, encoding='utf-8-sig', mode='r') as csv_file:
    csv_field_names = ['EMPRESA', 'CLIENTE', 'USUARIO']
    csv_reader = csv.DictReader(csv_file, fieldnames=csv_field_names, delimiter=';')

    for row in csv_reader:
        user = row['USUARIO']
        client = row['CLIENTE']
        TOMTICKET_ENDPOINT = f'{TOMTICKET_URL}/{user}'
    
        request_options = {
                'id_departamento': TOMTICKET_DEPARTMENT_ID,
                'id_tipoassunto': TOMTICKET_CATEGORY_ID,
                'titulo': f'[{client}] - Rotina de verificação Zabbix',
                'mensagem': MENSAGEM_CHAMADO,
                'prioridade': '2'
            }
        tomticket_response = requests.post(TOMTICKET_ENDPOINT, request_options)

    if tomticket_response.status_code != 200:
         json_response = tomticket_response.json()
         response_message = json_response['mensagem']
         error_status_message = f'{client} - Erro ao criar o chamado: {response_message}'
         write_in_log(error_status_message)

        


