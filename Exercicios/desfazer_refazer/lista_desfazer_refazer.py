import os
import pathlib
import json
import logging


ROOT_DIR = pathlib.Path()
FILES_PATH = ROOT_DIR / 'Exercicios/lista_desfazer_refazer/'
JSON_PATH = FILES_PATH / 'lista_tarefas.json'
LOG_PATH = FILES_PATH / 'lista_defazer_refazer.log'

logging.basicConfig(level=logging.DEBUG, filename=LOG_PATH, format='%(asctime)s - %(levelname)s -> %(message)s', encoding='utf8')

def listar(lista:list) -> None:
    print('\nTAREFAS:')
    print(*lista, sep='\n')
    print()

def desfazer(lista_tarefa:list, lista_desfeitos:list) -> None:
    if not lista_tarefa:
        print('\nNada a desfazer...')
    
    else:
        item_removido = lista_tarefa.pop()
        lista_desfeitos.append(item_removido)
        print('\n', item_removido, 'removido')

def refazer(lista_tarefas:list, lista_desfeitos:list) -> None:
    if not lista_desfeitos:
        print('\nNada a refazer...')

    else:
        item_readicionado = lista_desfeitos.pop()
        lista_tarefas.append(item_readicionado) 
        print('\n', item_readicionado, 'readicionado')

def salvar(lista_tarefas:list, tarefas_desfeitas:list) -> None:
    dic_listas = {'tarefas':lista_tarefas, 'tarefas_desfeitas':tarefas_desfeitas}

    with open(JSON_PATH, 'w', encoding='utf8') as file:
        json.dump(dic_listas, file, indent=1)

def ler() -> dict:
    global tarefas
    global tarefas_desfeitas
    dic_listas = {}

    with open(JSON_PATH, 'r', encoding='utf8') as file:
        dic_listas = json.load(file)
    tarefas = dic_listas['tarefas']
    tarefas_desfeitas = dic_listas['tarefas_desfeitas']

tarefas = []
tarefas_desfeitas = []
while True:
    print('Comandos: listar, desfazer, refazer')
    resposta = input('Digite uma tarefa ou comando: ').strip()

    if resposta == 'listar':
        listar(tarefas)
        logging.debug(f'Função listar executada com sucesso...')

    elif resposta == 'desfazer':
        desfazer(tarefas, tarefas_desfeitas)
        logging.debug('Função desfazer executada com sucesso...')
        listar(tarefas)
    
    elif resposta == 'refazer':
        refazer(tarefas, tarefas_desfeitas)
        logging.info('Item refeito com sucesso')
        logging.debug('Função refazer executada com sucesso...')
        listar(tarefas)
    
    elif resposta == 'SAIR':
        print('SAINDO...')
        logging.debug('Programa finalizado...')
        break

    elif resposta == 'clear':
        os.system('cls')
        logging.debug('Comando "clear" executado com sucesso...')

    elif resposta == 'salvar':
        salvar(tarefas, tarefas_desfeitas)
        logging.debug('Comando salvar executado com sucesso...')
        print('\nTarefas salvas...')

    elif resposta == 'ler':
        ler()
        logging.debug('Comando ler executado com sucesso...')
        print('\nTarefas recarregadas...')


    else:
        tarefas.append(resposta)
        logging.debug('Novo item adicionado a lista com sucesso...')
        print('\n', resposta, 'adicionado')
        listar(tarefas)
    


    