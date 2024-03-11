def criar_multiplicador(multiplicador: int):
    def multiplicar(numero: int):
        return numero * multiplicador
    return multiplicar


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(3))
print(triplicar(3))
print(quadruplicar(3))