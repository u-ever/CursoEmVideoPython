from datetime import date
nasc = int(input('Ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - nasc
print('Quem nasceu em {} tem {} ano(s) em {}.'.format(nasc, idade, anoatual))
if idade < 18:
    anofalta = 18 - idade
    alistamento = anofalta + anoatual
    print('''Ainda falta(m) {} ano(s) para o seu alistamento.
    Seu alistamento será em {}.'''.format(anofalta, alistamento))
elif idade > 18:
    alistamento2 = nasc + 18
    alistpassado = (anoatual - nasc) - 18
    print('''Você deveria ter se alistado há {} anos.
    Seu alistamento foi em {}.'''.format(alistpassado, alistamento2))
else:
    print('Você deve se alistar IMEDIATAMENTE!''')
