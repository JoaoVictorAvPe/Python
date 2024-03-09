
nome = 'João Victor'
altura = 1.80
peso = 100
imc = peso / altura ** 2
texto = '{pipi} tem {altura} de altura e pesa {peso}. Portanto seu IMC é de {imc:.2f}'

print(texto.format(pipi=nome, altura=altura, peso=peso, imc=imc))
if imc > 30:
    print(f'{nome} é obeso')
else:
    print(f'{nome} é magro')
