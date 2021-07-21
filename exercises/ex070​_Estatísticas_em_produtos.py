print('-'*40)
print('{:^40}'.format('LOJA SUPER BARATÃO'))
print('-'*40)
r = 'S'
pb = ''
vpb = []
totp = maisdm = 0
while True:
    while 'S' in r:
        np = str(input('Nome do Produto: '))
        pp = float(input('Preço: R$ '))
        totp += pp
        if pp > 1000:
            maisdm = 1
        vpb += [pp]
        if pp <= min(vpb):
            pb = np
        r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print('{:=^40}'.format(' TOTAL DOS PRODUTOS '))
print(f'Valor total dos produtos: R${totp:.2F}')
print(f'Produtos custando mais de R$1000.00: {maisdm}')
print(f'O produto mais barato foi {pb} custando R${min(vpb):.2F}')
