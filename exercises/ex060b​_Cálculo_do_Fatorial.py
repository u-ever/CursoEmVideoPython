n = int(input('Digite um número para calcular seu Fatorial: '))
f = n
c = n
print('Calculando {}! ='.format(n), end='')
while c > 1:
    f = f - 1
    c = c - 1
    n = n * f
    if c == 1:
        print(f, end=' = ')
    else:
        print(f, end=' x ')
print('{}'.format(n))
