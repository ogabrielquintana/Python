import datetime, random
print(datetime.date.today(), '\n')
robo = random.randrange(1, 11)
chute = int(input('Pensei em um número de 1 a 10. Qual tu acha que é: '))
tentativas = 1
while chute != robo:
    if 0 < chute < 11:
        if chute > robo:
            chute = int(input('Menos... Qual tu acha que é: '))
        elif chute < robo:
            chute = int(input('Mais... Qual tu acha que é: '))
    else:
        chute = int(input('Chuta válido de preferência... Qual tu acha que é: '))
    tentativas += 1
print('\033[32mAcertou!!\033[m Tu precisou de \033[33m{}\033[m tentativas.'.format(tentativas))
