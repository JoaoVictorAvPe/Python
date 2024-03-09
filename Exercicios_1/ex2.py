hora = input('Digite a hora: ')

try:
    hora = int(hora)

    dia = 0 <= hora <= 11
    tarde = 12 <= hora <= 17
    noite =  18 <= hora <=23

    if dia: 
        print('Bom Dia')
    elif tarde:
        print('Boa Tarde')
    elif noite:
        print('Boa Noite')
    else:
        print('Nao conheco essa hora')
except:
    print('Entrada inválida')