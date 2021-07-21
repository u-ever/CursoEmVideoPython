from random import randint
print('=-='*10)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-='*10)
c = 0
while True:
    n = int(input('Diga um valor: '))
    pi = ' '
    while pi not in 'PI':
        pi = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print('---'*10)
    pc = randint(0, 10)
    soma = n + pc
    gp = ''
    if soma % 2 == 0:
        result = 'PAR'
        gp = 'P'
    else:
        result = 'IMPAR'
    print(f'Você jogou {n} e o computador {pc}. Total de {soma}. DEU {result}')
    print('---' * 10)
    if pi == gp:
        print('Você GANHOU')
        print('=-=' * 10)
        print('OUTRA VEZ!!!')
    else:
        print('Você PERDEU')
        break
    c += 1
print('=-=' * 10)
print(f'GAME OVER! Você venceu {c} vez(es).')
