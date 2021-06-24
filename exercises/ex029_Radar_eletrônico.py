n = int(input('RADAR: Digitea velocidade atual do carro? '))
if n > 80:
    print('MULTADO! Você excedeu o limite de velocidade permitido que é de 80Km/h.')
    print('A multa deverá ser paga no valor de R${},00.'.format((n - 80) * 7))
print('Tenha um bom dia! Dirija com segurança.')