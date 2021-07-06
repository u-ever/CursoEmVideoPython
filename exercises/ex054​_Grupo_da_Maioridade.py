from datetime import date
f = 0
maior = 0
menor = 0
for f in range(0, 7):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(f + 1)))
    idade = date.today().year - ano
    if idade >=18:
        maior = maior + 1
    else:
        menor = menor + 1
print('Tivemos {} pessoas maiores de idade.'.format(maior))
print('E {} pessoas menores de idade.'.format(menor))
