numero = input('Digite um numero inteiro: ')

try:
    numero = int(numero)
    e_par = numero%2 == 0
    if e_par:
        print('Numero par')
    else:
        print('Numero impar')
except:
    print('Voce nao digitou um numero INTEIRO')