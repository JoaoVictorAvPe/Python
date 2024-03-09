nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print('Seu nome e:', nome)
    print('Seu nome invertido e:', nome[::-1])
    print('Seu nome contem espaço:', (' ' in nome))
    print(f'Seu nome tem {len(nome)} letras')
    print('A primeira letra do seu nome e:', nome[0])
    print('A ultima letra do seu nome e:', nome[-1])
    print('Sua idade e:', idade)
else:
    print('Desculpe, voce deixou campos vazios')