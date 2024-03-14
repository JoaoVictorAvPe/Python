# Aumente os preços dos produtos a seguir em 10%

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

import models.dic_utils as modic

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


updated_price_list = modic.increase_price(10, produtos)

ordered_by_name_list = modic.order_by(updated_price_list, 'nome', True)
ordered_by_price_list = modic.order_by(updated_price_list, 'preco')

modic.print_list(ordered_by_name_list)
print()
modic.print_list(ordered_by_price_list)



