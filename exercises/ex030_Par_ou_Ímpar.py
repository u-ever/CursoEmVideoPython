n = float(input('Me diga um número inteiro qualquer: '))
t = n % 2
if t == 0:
    print('O número {:.0F} é PAR.'.format(n))
else:
   print('O número {:.0F} é IMPAR.'.format(n))
