lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

#def ordenar(array):
#   return array['sobrenome']

# lista.sort(key=ordenar)

# for i in lista:
#     print(i)

# lista.sort(key=lambda dic : dic['nome'])
# for i in lista:
#     print(i)

def executa(funcao, *args):
    return funcao(*args)

print(executa(lambda x,y:(x+y)/2 , 2, 2))