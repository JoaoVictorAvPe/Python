from Pessoa import Pessoa
import json



p1 = Pessoa('Joao Victor', 'de Avila Perasol', 22, 'M')

with open('Exercicios/obj_json/obj.json', 'w', encoding='utf8') as file:
    json.dump(p1.__dict__, file, indent=1)