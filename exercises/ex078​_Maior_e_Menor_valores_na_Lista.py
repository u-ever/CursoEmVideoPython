num = []
max = 0
min = 0
for c in range(0, 5):
    num.append(int(input(f'Digite um valor para a Posição {c}: ')))
    if c == 0:
        max = min = num[c]
    if max < num[c]:
        max = num[c]
    if min > num[c]:
        min = num[c]
print('=-'*30)
print(f'Você digitou os valores: {num}')
print(f'O maior valor digitado foi {max} nas posições: ', end=' ')
for c, indice in enumerate(num):
    if indice == max:
        print(f'{c}...', end=' ')
print()
print(f'O menor valor digitado foi {min} nas posições: ', end=' ')
for c, indice in enumerate(num):
    if indice == min:
        print(f'{c}...', end=' ')