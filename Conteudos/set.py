# #criar set vazio e adicionar
# s1 = set()

# s1.add(1)
# s1.add('Joao')

# #update para mandar varios valores, recebe um iteravel

# s1.update(('Joao Victor', 9, 5, 4))
# s1.update('Macarrao')
# print(s1)

# #limpar clear
# #discard: remode um valor em especifico
# #s1.discard('Joao')

s1 = {1, 2, 3}
s2 = {2, 3, 4}
uniao = s1 | s2
intersection = s1 & s2
diferenca = s1 - s2 
unicos = s1 ^ s2

print(uniao)
print(intersection)
print(diferenca)
print(unicos)