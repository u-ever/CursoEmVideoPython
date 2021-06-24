sa = float(input('Qual é o salário do funcionário? R$ '))
if sa <= 1250.00:
    sn = sa + (sa * 0.15)
else:
    sn = sa + (sa * 0.10)
print('Quem ganhava R${:.2F} passa a ganhar R${:.2F} agora.'.format(sa,sn))