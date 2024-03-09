questions = [
    {
        'Pergunta': 'Quanto é 2+2',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4'
    },
    {
        'Pergunta': 'Quanto é 5*5',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25'
    },
    {
        'Pergunta': 'Quanto é 10/2',
        'Opções': ['4', '2', '5', '1'],
        'Resposta': '5'
    }
]

correct_answers = 0
for dictionary in questions:
    key = tuple(dictionary.keys())
    number_answer = {}
    for i in range(len(dictionary)):
        quest_key = key[i]
        quest_text = dictionary[quest_key]

        if i == 0:
            print(f'{quest_key}: {quest_text}')

        if i == 1:
            options_list = quest_text
            print(quest_key + ':')
            for number_option in enumerate(options_list):
                number, option = number_option
                number_answer[number] = option
                print(f'{number}) {option}')

        elif i == 2:
            try:
                answer = int(input('Escolha uma opção: '))
                if number_answer[answer] == quest_text:
                    print('Acertou')
                    correct_answers += 1
                else:
                    print('Errou')     
            except KeyError:
                print('Invalid option')
                continue
    print('')
print(f'Voce acertou {correct_answers} de {len(questions)} perguntas')

