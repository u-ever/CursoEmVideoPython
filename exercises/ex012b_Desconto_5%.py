p =(float(input('Digite o preço do produto: R$ ')))
pd =p - (p * 5/100)
print('O Produto custava R${:.2F} e com desconto de 5% vai custar R${:.2F}.'.format(p, pd))