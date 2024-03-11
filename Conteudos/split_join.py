# texto = '        Ola so, que coisa interessante            '

# lista_palavras = texto.split(',')

# lista_frases_certas = []
# for i, frase in enumerate(lista_palavras):
#     lista_frases_certas.append(lista_palavras[i].strip())

# print(lista_frases_certas, lista_palavras )

qtd = int(input('qtd de itens: '))

itens = []
for i in range(qtd):
    item = input(f'item {i + 1}: ')
    itens.append(item)

csv = ','.join(itens)
print(csv)

newlist = csv.split(',')

print(newlist)