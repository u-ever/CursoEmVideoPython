from time import sleep


def contador(inicio, fim, passo):
    print('=-' * 20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
    n = inicio
    sleep(1)
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    while n != fim:
        print(f'{n}', end=' ', flush=True)
        if inicio >= fim:
            n = n - passo
            if n < fim:
                break
        else:
            n = n + passo
        sleep(0.5)
    print(f'{fim}', end=' ')
    print('FIM!')


contador(0, 10, 1)
contador(10, 0, 2)
print('=-' * 20)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
