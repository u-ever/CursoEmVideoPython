var = [[],[]]
for c in range(0, 7):
    temp = int(input(f'Digite  o {c + 1}º valor: '))
    if temp % 2 == 0:
        var[0].append(temp)
    else:
        var[1].append(temp)
print('=-' * 30)
print(f'Os valores pares digitados foram: {sorted(var[0])}')
print(f'Os valores impares digitados foram: {sorted(var[1])}')
