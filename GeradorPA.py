print('GERADOR DE PA: ')
print('-='*10)
primeiro = int(input('digite o primeiro termo da pa: '))
razao = int(input('digite a razão da pa: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos tu quer mostrar a mais? '))
print('A progressão terminou com {} termos mostrados.'.format(total))
