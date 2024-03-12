#dir, hasattr, getattr

string = 'joao'

print(string)

#hasattr verifica se o metodo existe
if hasattr(string, 'upper'):
    print('existe:',string.upper())


#getattr executa um metodo dinamicamente
metodo = 'lower'

if hasattr(string, metodo):
    print('Existe:',getattr(string,metodo)())
else:
    print('nao existe o metodo', metodo)