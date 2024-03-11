nome = 'Joao Victor'
id = 0

new_string = ''
while id < len(nome):
    if nome[id] == ' ':
        id += 1
        continue

    new_string = new_string + nome[id] + "*"
    id += 1

print(new_string)