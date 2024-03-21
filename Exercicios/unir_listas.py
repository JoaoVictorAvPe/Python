def smallest(func):
    def inner(list1:list, list2:list):
        if len(list1) > len(list2):
            bigger = list1
            smaller = list2
        else:
            bigger = list2
            smaller = list1
        return func(smaller, bigger)
    return inner

@smallest
def zipper(list1:list, list2:list) -> list:
    return [(list1[i], list2[i]) for i in range(len(list1))]

# def zipper(list1:list, list2:list) -> list:
#     max_range = min(len(list1), len(list2))
#     return [(list1[i], list2[i]) for i in range(max_range)]

cities = ['Salvador', 'Ubatuba', 'Belo Horizonte']
states = ['BA', 'SP', 'MG', 'RJ']

print(zipper(cities, states))


