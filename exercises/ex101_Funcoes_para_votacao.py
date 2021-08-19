from datetime import date

def voto():
    idade = int(input('Em que ano você nasceu? '))
    idade = date.today().year - idade
    print(f'Com {idade} anos: ', end='')
    if idade < 16:
        print('NÃO VOTA')
    elif idade >= 16 and idade < 18 or idade > 65:
        print('VOTO FACULTATIVO')
    else:
        print('VOTO OBRIGATÓRIO - É A FESTA DA DEMOCRACIA')

voto()