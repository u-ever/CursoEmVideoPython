lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = tc = maior = 0
for li in range(0, 3):
    for c in range(0, 3):
        lista[li][c] = int(input(f'Digite um valor para [{li}, {c}]: '))
        if lista[li][c] % 2 == 0:
            soma += lista[li][c]
        if li == 1 or lista[1][c] > maior:
            maior = lista[1][c]
    tc += lista[li][2]
print('=-' * 25)
for li in range(0, 3):
    for c in range(0, 3):
        print(f'[{lista[li][c]:^5}]', end='')
    print()
print('=-' * 25)
print(f'A soma dos valores pares é {soma}.')
print(f'A soma dos valores da terceira coluna é {tc}.')
print(f'O maior valor da segunda linha é {maior}')
