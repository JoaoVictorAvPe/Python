def entra_numero(msg):
    while True:
        numero = input(msg)
        try:
            numero = float(numero)
            return numero
        except ValueError:
            print('Numero inválido')
            continue

def entra_operador(msg):
    operadores = '+', '-', '*', '/'
    while True:
        operador = input(msg)
        if operador in operadores and operador != '':
            return operador
        else:
            print('Operador inválido')
            continue

def calcular(n1, n2, op):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    elif op == '/' and n2 != 0:
        return n1 / n2
    else:
        return 0


num1 = entra_numero('Digite o primeiro numero: ')
num2 = entra_numero('Digite o segundo numero: ')
operador = entra_operador('Digite o operador: ')
print(f'Resuldado de {num1} {operador} {num2} = {calcular(num1, num2, operador)}')
