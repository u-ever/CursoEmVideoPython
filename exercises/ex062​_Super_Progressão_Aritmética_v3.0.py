print('{:=^30}'.format('Super Gerador de PA'))
t1 = int(input('Primeiro termo:'))
t2 = int(input('Segundo termo:'))
c = 0
r = 10
while r != 0:
    while c < r:
        print('{}'.format(t1), end=' ➜ ')
        c += 1
        t1 += t2
    print('PAUSA')
    r = int(input('Quantos termos você quer mostrar a mais? '))
    if r == 0:
        r = 0
    else:
        r += c
print('Progressão finalizada com {} termos mostrados'.format(c))
