print('\033[;;42m=-=-\033[m'*13)
print('\033[;;42mAnálise da possibilidade de existência de Triângulos\033[m')
print('\033[;;42m=-=-\033[m'*13)
l1 = float(input('Primeiro segmento: '))
l2 = float(input('Segundo segmento: '))
l3 = float(input('Terceiro segmento: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os segmentos acima PODEM formar um triangulo!')
else:
    print('Os segmentos acima NÃO PODEM formar um triangulo!')