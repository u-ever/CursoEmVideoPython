c = n = m = 0
while n != 999:
    n = int(input('Digite um número [999 para encerrar]: '))
    if n != 999:
        c += 1
        m += n
    else:
        n = n
print('Você digitou {} números e a soma entre eles foi {}.'.format(c, m))
