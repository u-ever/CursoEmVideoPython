times = ('Flamengo', 'Internacional', 'Atlético-MG', 'São Paulo', 'Fluminense', 'Grêmio', 'Palmeiras', 'Santos',
         'Athletico-PR', 'Bragantino', 'Ceará', 'Corinthians', 'Atlético-GO', 'Bahia', 'Sport', 'Fortaleza', 'Vasco',
         'Goiás', 'Coritiba', 'Botafogo')
print('-='*50)
print(f'Lista dos times do Brasileirão:{times}')
print('-='*50)
print(f'Os 5 primeiros são: {times[:5]}')
print('-='*50)
print(f'Os 4 ultimos são: {times[-4:]}')
print('-='*50)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*50)
print(f'O Palmeiras está na {times.index("Palmeiras")+1}ª posição.')
print('-='*50)
