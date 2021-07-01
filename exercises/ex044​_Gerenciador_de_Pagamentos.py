print('==' * 10, 'LOJAS GLEICE', '==' * 10)
compra = float(input('Preço total das compras: R$ '))
print('FORMAS DE PAGAMENTO')
pag = int(input('''[1] à vista dinheiro/cheque (10% de desconto)\n[2] à vista cartão (5% de desconto)
[3] 2x no cartão (sem juros)\n[4] 3x ou mais no cartão (juros de 20%)\nQual é a opção? '''))
if pag == 1:
    pagvist = compra - (compra * 0.10)
    print('Sua compra de R${} vai custar R${} no final'.format(compra, pagvist))
elif pag == 2:
    pagvcard = compra - (compra * 0.05)
    print('Sua compra de R${} vai custar R${} no final.'.format(compra, pagvcard))
elif pag == 3:
    pag2x = compra / 2
    print('Sua compra será parcelada em 2x de R${} SEM JUROS.'.format(pag2x))
    print('Sua compra vai custar R${}'.format(compra))
elif pag == 4:
    quantpar = int(input('Quantas Parcelas? '))
    pagjur = compra + (compra * 0.20)
    parc = pagjur / quantpar
    print('Sua compra será parcelada em {}x de R${} COM JUROS.'.format(quantpar, parc))
    print('Sua compra de R${} vai custar R${} no final.'.format(compra, pagjur))
else:
    print('OPÇÃO INVALIDA')
