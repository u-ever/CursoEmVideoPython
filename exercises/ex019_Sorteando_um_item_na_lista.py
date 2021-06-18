from random import choice
a1 =(str(input('Primeiro aluno: ')))
a2 =(str(input('Segundo aluno: ')))
a3 =(str(input('Terceiro aluno: ')))
a4 =(str(input('Quarto aluno: ')))
l =[a1, a2, a3, a4] #PARA FAZER UMA LISTA, COLOCAR OS ITENS ENTRE COLCHETES
e =choice(l)
print ('O aluno escolhido foi {}.'.format(e))