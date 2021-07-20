n = c = 0
r = "S"
m = 0
l = []
while "S" in r:
    c += 1
    n = int(input('Digite um número: '))
    m += n
    l += [n]
    r = str(input('Quer continuar? [S/N] ')).strip()[0].upper()
print('Você digitou {} números e a média entre eles é {}'.format(c, (m)/c))
print('O maior valor foi {} e o menor foi {}'.format(max(l), min(l)))
