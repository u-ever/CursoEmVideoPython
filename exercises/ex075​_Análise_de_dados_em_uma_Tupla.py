l = (int(input('Digite um número: ')),
     int(input('Digite outro número: ')),
     int(input('Digite mais um número: ')),
     int(input('Digite o último número: ')))
print(f'Você digitou os valores: {l}')
if 9 in l:
    print(f'O valor 9 apareceu {l.count(9)} vez(es);')
else:
    print('O valor 9 não foi digitado')
if 3 in l:
    print(f'O valor 3 aparece na {l.index(3)+1}ª posição;')
else:
    print('O valor 3 não foi digitado')
print('Os valores pares digitados foram: ', end='')
for c in l:
    if c % 2 == 0:
        print(f'{c} ', end='')
print('\nFim')
