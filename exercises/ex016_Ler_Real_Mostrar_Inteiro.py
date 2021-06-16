#ERRADO POIS ARREDONDA PARA CIMA
#n= float(input('Digite um número real: '))
#print('A porção inteira do número real {} é {:.0F}.'.format(n, n))

#CORRETO UTILIZANDO INT DENTRO DO FORMAT DO PRINT
n= float(input('Digite um número real: '))
print('A porção inteira do número real {} é {}.'.format(n, int(n)))