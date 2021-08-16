from random import randint
lista = []

def randList():   
    print('Sorteando 5 valores da lista: ', end='')
    for c in range (0, 5):
        lista.append(randint(1,10))
    for c in lista:
        print(f'{c} ', end='')
    print('Pronto!')


def somaPar():
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f'Somando os valores pares de {lista}, temos {soma}.')
    

randList()
somaPar()