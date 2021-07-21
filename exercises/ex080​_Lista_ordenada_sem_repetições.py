list = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > list[-1]:
        list.append(n)
        print('Adicionado ao final da lista...')
    else:
        for indice, valor in enumerate(list):
            if n <= valor:
                list.insert(indice, n)
                print(f'Adicionado na posição {indice}')
                break
print('=-' * 30)
print(f'Os valores digitados em ordem foram: {list}')
