n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
print('=-='*10)
option = 0
while option != 5:
    option = int(input('[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa\n>>>>Qual é a sua opção? '))
    if option == 1:
        soma = n1 + n2
        print('O resultado da soma {} + {} é {} '.format(n1, n2, soma))
    elif option == 2:
        mult = n1 * n2
        print('O resultado da multiplicação {} X {} é {}'.format(n1, n2, mult))
    elif option == 3:
        if n1 > n2:
            maior = n1
        elif n1 < n2:
            maior = n2
            print('Entre {} e {} o maior é {}'.format(n1 , n2 , maior))
        else:
            print('Os números são iguais!')
    elif option == 4:
        n1 = float(input('Primeiro valor: '))
        n2 = float(input('Segundo valor: '))
    else:
        print('Opção inválida!')
    print('=-=' * 10)
print('Finalizando...')
print('=-='*10)
print('Fim do programa! Volte sempre!')
