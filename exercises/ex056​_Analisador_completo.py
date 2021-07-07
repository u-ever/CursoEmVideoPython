from statistics import mean
lidade = []
msub20 = 0
idadeold = 0
nameold = ''
print('{:=^23}'.format('Analisador de Grupo'))
print('')
for c in range(1, 3):
    print('{:=^20}'.format('{}ªPESSOA'.format(c)))
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input("Sexo [M/F]: ")).strip().upper()
    lidade += [idade]
    if idade < 20 and sexo == 'F':
        msub20 += 1
    if sexo == 'M' and idade > idadeold:
        idadeold = idade
        nameold = nome
print('A média de idade do grupo é de {:.1F} anos.'.format(mean(lidade)))
print('O homem mais velho tem {} anos e se chama {}'.format(idadeold, nameold))
print('Mulheres com menos de 20 anos: {}'.format(msub20))
