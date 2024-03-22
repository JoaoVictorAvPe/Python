import os

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

    else:
        tarefas.append(resposta)
        print('\n', resposta, 'adicionado')
        listar(tarefas)
    


    