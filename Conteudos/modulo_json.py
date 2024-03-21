import json

#pessoa = {
#    'nome': 'João Victor',
#    'sobrenome': 'de Ávila Perasol',
#    'enderecos': [
#        {'rua': 'R1', 'numero': 32},
#        {'rua': 'R2', 'numero': 55},
#    ],
#    'altura': 1.8,
#    'numeros_preferidos': (2, 4, 6, 8, 10),
#    'dev': True,
#    'nada': None,
#}
#
#with open('Conteudos/dados.json', 'w', encoding='utf8') as arquivo:
#    json.dump(pessoa, arquivo, ensure_ascii=False,  indent=1)

pessoa = {}

with open('Conteudos/dados.json', 'r', encoding='utf8') as file:
    pessoa = json.load(file)


for i in pessoa:
    print(f'{i}: {pessoa[i]}')