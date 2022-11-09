import random, emoji
cont = 0 
print('PAR OU IMPAR')
while True:
    comp = random.randint(0, 11)
    num = int(input('digite um valor: '))
    if num < 0 or num > 10:
        print(emoji.emojize('Escolhe um nro valido de preferencia :pouting_face:'))
        break
    escolha = input('par ou ímpar? [P/I] ').upper().strip()[0]
    soma = comp + num
    if escolha in 'Pp':
        if soma % 2 == 0:
            print(f'Tu escolheu {num} e o pc escolheu {comp}, a soma é {soma}! DEU PAR')
            print(emoji.emojize('Tu :fireworks: \033[32mvenceu\033[m :fireworks:'))
            cont += 1
        elif soma % 2 == 1:
            print(f'Tu escolheu {num} e o pc escolheu {comp}, a soma é {soma}! DEU IMPAR')
            print(emoji.emojize('Tu :loudly_crying_face: \033[31mperdeu\033[m :loudly_crying_face:'))
            break
    elif escolha in 'Ii':
        if soma % 2 == 0:
            print(f'Tu escolheu {num} e o pc escolheu {comp}, a soma é {soma}! DEU PAR')
            print(emoji.emojize('Tu :loudly_crying_face: \033[31mperdeu\033[m :loudly_crying_face:'))
            break
        elif soma % 2 == 1:
            print(f'Tu escolheu {num} e o pc escolheu {comp}, a soma é {soma}! DEU IMPAR')
            print(emoji.emojize('Tu :fireworks: \033[32mvenceu\033[m :fireworks:'))
            cont += 1
print(f'GAME OVER! Tu ganhou {cont} vezes')
