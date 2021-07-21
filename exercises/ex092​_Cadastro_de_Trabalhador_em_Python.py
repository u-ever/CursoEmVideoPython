from datetime import date
print(f'{" Cadastro de Trabalhador ":=^40}')
worker = {}
worker['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
worker['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
worker['Idade'] = date.today().year - nasc
if worker['CTPS'] != 0:
    worker['Contratação'] = int(input('Ano de Contratação: '))
    worker['Salario'] = float(input('Salário: '))
    worker['Aposentadoría'] = (worker['Contratação'] + 35) - nasc
print(f'{" Trabalhador Cadastrado ":=^40}')
for v, k in worker.items():
    print(f' - {v}: {k}')
print(worker)
