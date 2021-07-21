from random import randint
from time import sleep
from operator import itemgetter
c = 0
game = {
    'Player1': randint(1, 6),
    'Player2': randint(1, 6),
    'Player3': randint(1, 6),
    'Player4': randint(1, 6),
}
ranking = ()
print('Valores sorteados:')
for v, k in game.items():
    print(f'{v} tirou {k} no dado.')
    sleep(1)
print('=-' * 15)
print('=== RANKING DOS JOGADORES ===')
ranking = (sorted(game.items(), key=itemgetter(1), reverse= True))
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: {v[0]} com dado no valor {v[1]}.')