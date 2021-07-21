resp = "S"
list = []
while resp == 'S':
    teste = int(input('Digite um valor: '))
    if teste in list:
        print('Valor duplicado! Não vou adicionar...')
    else:
        list.append(teste)
        print('Valor adicionado com sucesso...')
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while not resp in 'SN':
        resp = str(input('Resposta inválida. Quer continuar? [S/N] ')).strip().upper()[0]
print('=-'*30)
print(f'Você digitou os valores: {sorted(list)}')
