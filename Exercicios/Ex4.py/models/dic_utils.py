from copy import deepcopy

def increase_price(percent:float, my_list:list) -> list:
    return [{**dic, 'preco':round(dic['preco'] + (dic['preco'] * (percent / 100)), 2)} for dic in deepcopy(my_list)]



def order_by(my_list:list, orderator:str, do_reverse=False) -> list:
    try:
        return sorted(deepcopy(my_list), key=lambda dic : dic[orderator], reverse=do_reverse)
    except KeyError:
       print(f'ERROR IN order_by: "{orderator}" is invalid')

def print_list(my_list:list) -> None:
    for dic in my_list:
        value, key = dic.values()
        print(value, key, sep=": ")

