while True:
    c = 0
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('-'*20)
    while c < 10:
        c += 1
        print(f'{n} x {c} = {n*c}')
    print('-'*20)
