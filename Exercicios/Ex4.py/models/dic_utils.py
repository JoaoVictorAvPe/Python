def increase_price(percent:float, dic) -> None:
    
    for key, value in dic.items():
        if key == 'preco':
            dic[key] =round(value + value * (percent / 100), 2)

def print_dic(dic):
    for key, value in dic.items():
        print(key, value, sep=": ")