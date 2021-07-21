n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
     'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
r = 'S'
while r == 'S':
    u = int(input('Digite um número entre 0 e 20: '))
    if u > 20 or u < 0:
        u = int(input('Tente novamente.Digite um número entre 0 e 20: '))
    print(f'Você digitou {n[u]}.')
    r = str(input('Quer continuar? [S/N]')).strip().upper()[0]
print('Fim')
