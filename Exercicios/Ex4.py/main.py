# copy, sorted, produtos.sort
# Exercícios

# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

# Aumente os preços dos produtos a seguir em 10%
import models.dic_utils as modic

new_list = modic.increase_price(10, produtos)

for dic in new_list:
    print(dic)

