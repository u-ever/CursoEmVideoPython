p = float(input('Qual é o seu peso? (Kg) '))
a = float(input('Qual é a altura? (m) '))
imc = p / (a**2)
print('O IMC dessa pessoa é de {:.1F}'.format(imc))
if imc < 18.4:
    print('Abaixo do Peso')
elif 18.4 < imc <= 25:
    print('Peso Ideal')
elif 25< imc <= 30:
    print('Sobrepeso')
elif 30 < imc <= 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')