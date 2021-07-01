from random import choice
from time import sleep
print('{:=^30}'.format('JO KEN PO'))
print('Escolha uma opção:\n[1] PEDRA\n[2] PAPEL\n[3] TESOURA')
player = int(input('Qual sua jogada?' ))
lista = [1, 2, 3]
computer = choice(lista)
if player == 1:
    player = 'PEDRA'
elif player == 2:
    player = 'PAPEL'
elif player == 3:
    player = 'TESOURA'

if computer == 1:
    computer = 'PEDRA'
elif computer == 2:
    computer = 'PAPEL'
elif computer == 3:
    computer = 'TESOURA'

print('=='*15,'\n             JO')
sleep(1)
print('             KEN')
sleep(1)
print('             PO!!!\n','=='*15)
sleep(1)
print('Computador jogou {}\nJogador jogou {}\n'.format(player, computer),'=='*15)

if player == 'PEDRA' and computer == 'PEDRA' or player == 'PAPEL' and computer == 'PAPEL' \
        or player == 'TESOURA' and computer == 'TESOURA':
    print('EMPATE')
elif player == 'PEDRA' and computer == 'PAPEL' or player == 'PAPEL' and computer == 'TESOURA' \
        or player == 'TESOURA' and computer == 'PEDRA':
    print('COMPUTADOR VENCEU')
elif player == 'PEDRA' and computer == 'TESOURA' or player == 'PAPEL' and computer == 'PEDRA' \
        or player == 'TESOURA' and computer == 'PAPEL':
    print('JOGADOR VENCEU')
else:
    print('VOCÊ JOGOU ERRADO!')
