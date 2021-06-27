from datetime import date
nasc = int(input('Ano de nascimento: '))
anoatual = date.today().year
age = anoatual - nasc
print('O atleta tem {} anos. '.format(age))
if age <= 9:
    print('Classificação: MIRIM')
elif age <= 14:
    print('Classificação: INFANTIL')
elif age <= 19:
    print('Classificação: JÚNIOR')
elif age <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
