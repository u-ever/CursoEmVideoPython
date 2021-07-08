from random import randint
comp = randint(1, 10)
count = 1
print('Sou seu computador...\nAcabei de pensar em um número entre 0 e 10.\nSerá que você consegue adivinhar qual foi?')
player = int(input('Qual é o seu palpite? '))
while comp != player:
    count += 1
    if comp > player:
        player = int(input('Mais... Tente mais uma vez?'))
    if comp < player:
        player = int(input('Menos... Tente mais uma vez? '))
print('Acertou com {} tentativas. Parabéns!'.format(count))
