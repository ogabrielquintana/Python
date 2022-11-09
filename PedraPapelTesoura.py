import datetime, time, random
print(datetime.date.today())

seq = 'PEDRA', 'PAPEL', 'TESOURA'
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogada = int(input('Qual a sua jogada? '))
computador = random.randint(0, 2)

if 0 <= jogada < 3:
    print('JO')
    time.sleep(1)
    print('KEN')
    time.sleep(1)
    print('PO!!!')


    print('-=-'*10)
    print('Tu jogou \033[33m{}\033[m'.format(seq[jogada]))
    print('O computador jogou \033[33m{}\033[m'.format(seq[computador]))
    print('-=-'*10)
    time.sleep(3)

    if jogada == 0 and computador == 0 or jogada == 1 and computador == 1 or jogada == 2 and computador == 2:
        print('Isso aqui ixquece né, deu \033[7mEMPATE\033[m')
    elif jogada == 0 and computador == 2 or jogada == 2 and computador == 1 or jogada == 1 and computador == 0:
        print('BOOAA, tu \033[32mganhou\033[m!!')
    else:
        print('Ih, \033[31mperdeu\033[m pro bot mané ksksks tá de sacanagem')
else:
    print('Escolhe uma jogada válida de preferência né!')
