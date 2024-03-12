#if à esquerda do for é para filtrar
lista = [numero for numero in range(10) if numero%2 == 0]
print(lista)

#if à direita do for é para mapear
lista2 = [numero*2 if numero%2==0 else numero for numero in range(10)]
print(lista2)

#for dentro de for
lista3 = [(x,y) for x in range(3) for y in range(3)]
print(lista3)

#dictionary comprehension
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório'
}

dc = {key:value.upper() if isinstance(value, str) else value for key, value in produto.items()}
for key, value in dc.items():
    print(key, value)

#set comprehension

s1 = {i**2 for i in range(10) if i%2!=0}
print(s1)