n1 = int(input('Digite um número: '))
f = 0
count = 0
for c in range(0, n1):
    f += 1
    div = n1 % f
    print(div, end=' ')
    if div == 0:
        count = count + 1
print('\nO número {} foi divisível {} vezes!'.format(n1, count))
if count == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
