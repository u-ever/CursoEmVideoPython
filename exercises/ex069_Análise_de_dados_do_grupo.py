print('-'*20)
print('CADASTRE UMA PESSOA')
print('-'*20)
q = 'S'
m18 = m = f = 0
while True:
    while 'S' in q:
        p = int(input('Idade: '))
        s = ' '
        while s not in 'MF':
            s = str(input('Sexo: [M/F] ')).strip().upper()[0]
        print('-' * 20)
        if p > 18:
            m18 += 1
        if s == 'M':
            m += 1
        if s == 'F' and p < 20:
            f += 1
        q = ' '
        while q not in 'SN':
            q = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        print('-' * 20)
    if q == 'N':
        break
print(fim'Pessoas com mais de 18 anos: {m18}')
print(fim'Homens cadastrados: {m}')
print(fim'Mulheres com menos de 20 anos: {f}')
