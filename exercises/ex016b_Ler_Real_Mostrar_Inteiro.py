#Importando toda a biblioteca e usando floor (que arredonda para baixo, mostrando só a porção inteira)
from math import floor
n= float(input('Digite um número real: '))
print('A porção inteira do número real {} é {}.'.format(n, floor(n)))