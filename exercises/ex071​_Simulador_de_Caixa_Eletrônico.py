print('='*40)
print('{:^40}'.format('BANCO JUDEU TEM'))
print('='*40)
n = int(input('Que valor você quer sacar? R$ '))
n50 = n20 = n10 = n1 = 0
while True:
    while n >= 50:
        n -= 50
        n50 += 1
    if n % 50 != 0:
        while n >= 20:
            n -= 20
            n20 += 1
        if n % 20 != 0:
            while n >= 10:
                n -= 10
                n10 += 1
            if n % 10 != 0:
                while n >= 1:
                    n -= 1
                    n1 += 1
    if n == 0:
        break
if n50 != 0:
    print(f'Total de {n50} cédulas de R$50')
if n20 != 0:
    print(f'Total de {n20} cédulas de R$20')
if n10 != 0:
    print(f'Total de {n10} cédulas de R$10')
if n1 != 0:
    print(f'Total de {n1} cédulas de R$1')
print('='*40)
print('Volte sempre ao BANCO JUDEU TEM! Tenha um bom dia!')
