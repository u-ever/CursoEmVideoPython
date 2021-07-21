list = []
resp = 'S'
while 'S' in resp:
    list.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
list.sort(reverse=True)
print('=-' * 30)
print(f'Você digitou {len(list)} elementos.')
print(f'Os valores digitados em ordem decrescente são {list}')
if 5 in list:
    print('O valor 5 FAZ parte da lista!')
else:
    print('O valor 5 NÃO FAZ parte da lista!')
