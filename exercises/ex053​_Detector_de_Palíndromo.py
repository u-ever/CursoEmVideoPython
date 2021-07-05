f = str(input('Digite uma frase: '))
junt = f.replace(' ','').upper()
rever = junt[::-1].upper()
print('O inverso de {} é {}'.format(junt, rever))
if junt == rever:
    print('Temos um Palíndromo!')
else:
    print('A frase digitada não é um Palíndromo!')
