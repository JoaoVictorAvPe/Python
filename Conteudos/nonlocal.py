def concatenar(string_inicial):
    valor_final = string_inicial
    def interna(valor_a_concatenar=''):
        nonlocal valor_final
        valor_final += valor_a_concatenar
        return valor_final
    return interna

palavra = concatenar('a')
palavra('b')
palavra('c')
print(palavra())
