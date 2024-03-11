frase = 'O Python e uma linguagem de programacao multiparadigma. ' \
        'Python foi criado por Guido van Rossum'

letras_array = []
for letra in frase.lower():
    if letra not in letras_array and letra != ' ':
        letras_array.append(letra)


maior_qtd = 0
letra_maior_qtd = ''
letra_menor_qtd = ''
menor_qtd = len(frase)

for letra in letras_array:
    qtd_aparicoes = frase.count(letra)
    print(f'{letra}: {qtd_aparicoes}')

    if qtd_aparicoes > maior_qtd:
        maior_qtd = qtd_aparicoes
        letra_maior_qtd = letra
    if qtd_aparicoes < menor_qtd:
        menor_qtd = qtd_aparicoes
        letra_menor_qtd = letra


print('Maior quantidade')
print(f'Letra: {letra_maior_qtd}, Quantidade: {maior_qtd}')
print('Menor quantidade')
print(f'Letra: {letra_menor_qtd}, Quantidade: {menor_qtd}')
