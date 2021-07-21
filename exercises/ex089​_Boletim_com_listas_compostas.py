query = impr = ' '
aluno = [0,0,0,0,0]
lista = []
cont = media = 0
while True:
    aluno[0] = cont
    aluno[1] = str(input('Nome: '))
    aluno[2] = int(input('Nota 1: '))
    aluno[3] = int(input('Nota 2: '))
    media = aluno[2] + aluno[3] / 2
    aluno[4] = media
    lista.append(aluno[:])
    while query not in "SN":
        query = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        cont += 1
    if query in "N":
        break
    query = ' '
print('-=' * 30)
print(f'No.    NOME        MÉDIA')
for c in lista:
    print(f'[{c[0]:<4}]', f'[{c[1]:<10}]', f'[{c[4]:<4}]')
print('-' * 30)
while True:
    query = int(input('Mostrar notas de qual aluno? (999 para finalizar): '))
    if query == 999:
        break
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')
