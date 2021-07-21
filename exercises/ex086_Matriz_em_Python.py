lista = [[], [], [], [], [], [], [], [], []]
for c in range(0, 3):
    lista[c].append(int(input(f'Digite um valor para [0, {c}]: ')))
for c in range(0, 3):
    lista[c + 3].append(int(input(f'Digite um valor para [1, {c}]: ')))
for c in range(0, 3):
    lista[c + 6].append(int(input(f'Digite um valor para [2, {c}]: ')))
print('=-' * 30)
print(f'{lista[0]:} {lista[1]} {lista[2]} \n{lista[3]} {lista[4]} {lista[5]} \n{lista[6]} {lista[7]} {lista[8]}')
