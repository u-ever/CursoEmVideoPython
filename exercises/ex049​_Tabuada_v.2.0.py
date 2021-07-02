n = float(input('Digite um número para ver sua tabuada: '))
f = 0
for c in range(1, 11):
    f += 1
    t = n * f
    print('{} x {} = {}'.format(n, f, t))


