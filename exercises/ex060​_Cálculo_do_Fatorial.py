n = int(input('Digite um número para calcular seu Fatorial: '))
d = n
f = n
m = []
while f != 1:
        f += -1
        n = n * f
        m += [f]
print('Calculando {}! = {} {} {}'.format(d, d, m, n).replace(',',' x').replace('[','x ').replace(']',' ='))
