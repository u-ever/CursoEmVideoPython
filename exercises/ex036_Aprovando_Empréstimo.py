valorcasa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
anospag = int(input('Quantos anos de financiamento? '))
parc = valorcasa / (anospag * 12)
valordisp = salario * 0.30
print('Para pagar uma casa de R${:.2F} em {:.0F} anos e a prestação será de R${:.2F}'.format(valorcasa, anospag, parc))
if parc <= valordisp:
    print('Empréstimo APROVADO!')
else:
    print('Emprestimo NEGADO!')
