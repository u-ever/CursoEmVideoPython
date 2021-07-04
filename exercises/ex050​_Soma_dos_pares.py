count = 0
soma = 0
for c in range(1, 7):
    num = int(input('Digite o {}º número inteiro: '.format(c)))
    if num % 2 == 0:
        count += 1
        soma += num
print('Você informou {} números pares e a soma deles foi {}'.format(count, soma))
