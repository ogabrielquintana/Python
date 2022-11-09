print('-='*10)
print('SEQUENCIA DE FIBONACCI')
print('-='*10)
n = int(input('Quantos termos da sequencia quer mostrar? '))
t1 = 1
t2 = 1
print('{}, {}, '.format(t1, t2), end='')
cont = 3
total = n
while n != 0:
    while cont <= total:
        t3 = t1 + t2
        print('{}'.format(t3) if cont == total else '{}, '.format(t3), end='')
        t1 = t2
        t2 = t3
        cont += 1
    n = int(input('\nQuantos termos a mais quer mostrar? '))
    total += n
print('\nFIM')
