class Pessoa:
    def __init__(self, nome:str, sobrenome:str) -> None:
        self.nome = nome
        self.sobrenome = sobrenome

    def correr(self) -> None:
        print(f'{self.nome} {self.sobrenome} está correndo...')

fulano = Pessoa('Joao V', 'Avila')
fulano.correr()
Pessoa.correr(fulano)