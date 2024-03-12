# def soma(*args: int) -> int:
#     total = 0
#     for number in args:
#         total += number
#     return total


# numbers = 80,90,100,45,1,2,3,45,65,85
# print(soma(*numbers))

def multiplier(*args: int) -> int:
    result = 1
    for number in args:
        result *= number
    return result

def executa(funcao, *args):
    return funcao(*args)

numbers = 2,4,2,3,9,4,5,1,2,3,56,8,45,12

print(f'Total product: {multiplier(*numbers)}')
for number in numbers:
    print(f'Is {number} pair: {executa(lambda x:x%2==0, number)}')