variavel = 'Hello World'

print(variavel[6:])                                 #Imprime a partir do caractere de indice 6
print(variavel[0:5])                                #Imprime do primeiro ao 5 (Ultimo caractere nao e incluso)
print(variavel[0:len(variavel):2])                  #Imprime do primeiro ao ultimo de 2 em 2
print(variavel[::-1])                               #Inverte a string
print('Quantidade de caracteres:', len(variavel))   #Imprime a quantidade de caracteres

numero = 13940.48574

print(f'Numero: {numero:.2f}')                      #Imprime o numero com 2 casas decimais
print(f'Numero: {numero:,.2f}')                     #Imprime o numero com 2 casas decimais e com virgula entre centenas