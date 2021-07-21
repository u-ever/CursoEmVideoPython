print(f'{" Análise de Jogador ":=^40}')
jogador = dict()
gols = list()
jogador["Nome"] = str(input('Nome do Jogador: '))
jogador["Partidas"] = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for c in range(jogador["Partidas"]):
    gols.append((int(input(f'   Quantos gols na partida {c + 1}? '))))
    jogador["Gols"] = gols[:]
jogador["Total"] = sum(gols)
print('=-' * 40)
print(jogador)
print('=-' * 40)
for v, k in jogador.items():
    print(f' - {v}: {k}')
print('=-' * 40)
print(f'O jogador {jogador["Nome"]} jogou {jogador["Partidas"]} partidas.')
for i, v in enumerate(gols):
   print(f' => Na partida {i + 1}, {jogador["Nome"]} fez {v} gols.')
print(f'Foi um total de {jogador["Total"]} gols.')
