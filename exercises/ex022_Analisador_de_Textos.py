nome =str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minusculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' '))) # - nome.count(' '))) tira os espaços
print('Seu primeiro nome é {}, com {} letras.'.format(nome, nome.find(' ')))
#divido = nome.split()
#print('Seu primeiro nome é {}, com {} letras.'.format(divido[0], len(divido[0])))
