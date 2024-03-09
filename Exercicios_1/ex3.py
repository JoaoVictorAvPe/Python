nome = input('Digite seu nome: ')

if len(nome) < 4:
    print('Nome muito curto')
elif len(nome) > 6:
    print('Nome muito longo')
else:
    print('Seu nome e normal')