n = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(n))
if n > 200:
    v = n * 0.45
else:
    v = n * 0.50
print('O preço da passagem será de R${:.2F}'.format(v))