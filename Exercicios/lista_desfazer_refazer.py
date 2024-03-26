import os
import pathlib
import json

ROOT_DIR = pathlib.Path('./Exercicios')
JSON_PATH = ROOT_DIR / 'lista_tarefas.json'

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

    elif resposta == 'desfazer':
        desfazer(tarefas, tarefas_desfeitas)
        listar(tarefas)
    
    elif resposta == 'refazer':
        refazer(tarefas, tarefas_desfeitas)
        listar(tarefas)
    
    elif resposta == 'SAIR':
        print('SAINDO...')
        break

    elif resposta == 'clear':
        os.system('cls')

    elif resposta == 'salvar':
        salvar(tarefas, tarefas_desfeitas)
        print('\nTarefas salvas...')

    elif resposta == 'ler':
        ler()
        print('\nTarefas recarregadas...')

    else:
        tarefas.append(resposta)
        print('\n', resposta, 'adicionado')
        listar(tarefas)
    


    