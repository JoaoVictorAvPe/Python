numero_str = input('Vou dobrar oq vc digitar: ')

try:
    numero_float = float(numero_str)
    print('Float:', numero_float)
    print(f'O dobro de {numero_float} e {numero_float * 2}')
except:
    print('Isso nao e um numero')