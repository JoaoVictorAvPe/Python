import os

def check(string, array):
    for i in string:
        if i in array:
            continue
        else:
            return False
    return True

secret_word = 'hospital'.upper()

discovered_letters = set()

attempts = len(secret_word) + 3

print('SECRET WORD GAME\n')
for i in secret_word:
    print('*', end='')
print(f'\nYOU HAVE {attempts} ATTEMPTS')

while True:

    letter = input('\nType a letter: ').upper()
    os.system('cls')

    if len(letter) != 1:
        print('Invalid character')
        continue

    for secret_letter in secret_word:
        if letter == secret_letter or secret_letter in discovered_letters:
            print(secret_letter,  end='')
            discovered_letters.add(secret_letter)
        else:
            print('*', end='')

    attempts -= 1
    print(f'\nATEMPTS: {attempts}')

    if check(secret_word, discovered_letters):
        print('\nYOU WON')
        break

    if attempts == 0:
        print('\nYout Lose')
        print('Secret Word:', secret_word)
        break
