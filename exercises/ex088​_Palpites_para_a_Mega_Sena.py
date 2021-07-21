from random import randint
from time import sleep
jogo = []
numeros = 0
print('-' * 40)
print('{:^40}'.format('JOGOS DA MEGA SENA'))
print('-' * 40)
njogos = int(input('Quantos jogos você quer que eu sorteie? '))
print('\n{:=^40}\n'.format(f' SORTEANDO {njogos} JOGOS '))
for c in range(0, njogos):
    for n in range(0, 7):
        numeros = randint(1, 60)
        while numeros in jogo:
            numeros = randint(1, 60)
        jogo.append(numeros)
    print(f'Jogo {c + 1}:', sorted(jogo))
    sleep(1)
    jogo.clear()
print('\n{:=^40}'.format('< BOA SORTE >'))
