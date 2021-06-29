l1 = float(input('Primeiro segmento: '))
l2 = float(input('Segundo segmento: '))
l3 = float(input('Terceiro segmento: '))
if (l1 + l2) < l3 or (l1 + l3) < l2 or (l2 + l3) < l1:
    print('Os segmentos acima NÃO FORMAM um triângulo.')
elif l1 == l2 == l3:
    print('Os segmentos acima FORMAM um triângulo EQUILÁTERO.')
elif l1 != l2 and l1 != l3 and l2 != l3:
    print('Os segmentos acima FORMAM um triângulo ESCALENO.')
else:
    print('Os segmentos acima FORMAM um triângulo ISÓSCELES.')
