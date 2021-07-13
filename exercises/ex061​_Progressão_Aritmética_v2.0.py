print('{:=^26}'.format('Gerador de PA'))
t1 = int(input('Primeiro termo: '))
t2 = int(input('Segundo termo: '))
c = 0
while c < 10:
    print(t1, end=' ➜ ')
    c += 1
    t1 = t1 + t2
print('FIM')
