import random


def cpfGenerator():
    def cpfDigit(cpf :str):
        cpf = cpf.replace('.', '')
        result = 0
        multiplier = len(cpf) + 1
        for character in cpf:
            try:
                character = int(character)
            except ValueError:
                print("There's a letter in the cpf")
                return
        
            result += character * multiplier
            multiplier -= 1

        result *= 10
        result %= 11
        return 0 if result > 9 else result

    cpf = ''
    for i in range(1, 10):
        cpf += str(random.randint(0,9))
        if i % 3 == 0 and i < 9:
            cpf += '.'

    firstDigit = str(cpfDigit(cpf))
    secondDigit = str(cpfDigit((cpf + firstDigit)))
    return cpf + '-' + firstDigit + secondDigit
    


print(cpfGenerator())
