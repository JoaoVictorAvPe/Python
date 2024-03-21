import os

ARQUIVO_PATH = 'Conteudos/teste.txt'

lista = ['banana', 'maca', 'pera']

with open(ARQUIVO_PATH, 'a') as arquivo:
    arquivo.write(','.join(lista) + '\n')











