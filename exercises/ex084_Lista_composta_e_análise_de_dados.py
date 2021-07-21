pessoas = []
dados = []
resp = ' '
pesad = leve = ''
maip = menp = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maip = menp = dados[1]
        pesad = leve = dados[0]
    else:
        if dados[1] > maip:
            maip = dados[1]
            pesad = dados[0]
        if dados[1] < menp:
            menp = dados[1]
            leve = dados[0]
    pessoas.append(dados[:])
    dados.clear()
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'S':
        resp = ' '
    if resp in 'N':
        break
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maip}kg. Peso de {pesad}')
print(f'O menor peso foi de {menp}kg. Peso de {leve}')
