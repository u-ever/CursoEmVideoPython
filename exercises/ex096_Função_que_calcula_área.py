def area(l, c):
    a = l * c
    print(f'A área de um terreno {l}m x {c}m é de {a}m².')


print('CONTROLE DE TERRENOS')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
