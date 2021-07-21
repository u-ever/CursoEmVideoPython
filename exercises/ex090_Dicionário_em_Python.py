aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = int(input(f'Média de {aluno["nome"]}: '))
print('=-' * 30)
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
else:
    aluno['situação'] = 'Recuperação'
for k, v in aluno.items():
    print(f' - {k}: {v}')