def increase_price(percent:float, list_:list) -> list:
    new_list = []
    for dic in list_:
        new_dic = {}
        new_list.append(new_dic)
        for key, value in dic.items():
            if key == 'preco':
                new_dic[key] =round(value + value * (percent / 100), 2)
            else:
                new_dic[key] = value
    return new_list
