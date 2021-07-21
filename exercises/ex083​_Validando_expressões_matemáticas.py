expre = str(input('Digite a expressão: '))
verif = []
for valor in expre:
    if valor == '(':
        verif.append('(')
    elif valor == ')':
        if len(verif) > 0:
            verif.pop()
        else:
            verif.append(')')
            break
    print(len(verif))
if len(verif) == 0:
    print('Sua expressão é valida!')
else:
    print('Sua expressão é inválida!')