from itertools import zip_longest

def sum_list(list1, list2):
    return [x + y for x, y in zip_longest(list1, list2, fillvalue=0)]

list_a = list(range(1, 8))
list_b = list(range(1, 5))

list_c = sum_list(list_a, list_b)

print(list_a)
print(list_b)
print(list_c)
