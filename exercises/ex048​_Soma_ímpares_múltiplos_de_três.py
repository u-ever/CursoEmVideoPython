soma = 0
count = 0
for impar in range(1, 500, 2):
    if impar % 3 == 0:
        soma = soma + impar
        count = count + 1
print('A soma de todos os {} valores solicitados é de {}'.format(count, soma))
