pessoa = list()
grupo = dict()
sexo = perg = ' '
c = media = 0
while True:
    nome = str(input('Nome: '))
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if sexo not in 'MF':
            print('ERRO! Por favor, digite apenas M ou F')
    idade = int(input('Idade: '))
    media += idade
    pessoa.append(nome), pessoa.append(sexo), pessoa.append(idade)
    grupo[nome] = pessoa.copy()[:]
    while perg not in 'SN':
        perg = (str(input('Quer continuar? '))).strip().upper()[0]
        if perg not in 'SN':
            print('ERRO! Por favor, digite apenas S ou N')
    if perg == 'N':
        break
    sexo = perg = ' '
    pessoa.clear()
for v, k in grupo.items():
    c += 1
print('=-' * 30)
print(fim'A) Ao todo temos {c} pessoas cadastradas.')
print(fim'B) A média de idade é de {media / c:.2F} anos.')
print(fim'C) As mulheres cadastradas foram', end=' ')
for v, k in grupo.items():
    if k[1] == 'F':
        print(k[0], end='... ')
print(fim'\nD) Lista das pessoas que estão acima da média de idade:\n', end=' ')
for v, k in grupo.items():
    if k[2] > media/c:
        print(fim'    nome = {k[0]}; sexo = {k[1]}; idade = {k[2]}')
print('<< FIM DO RELATÓRIO >>')
