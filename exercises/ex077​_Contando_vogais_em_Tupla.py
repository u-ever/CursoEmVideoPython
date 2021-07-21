palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGUAGEM', 'PYTHON','CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR',
     'MERCADO', 'PROGRAMADOR', 'FUTURO')
for c in palavras:
    print(f'Na palavra {c} temos ', end='')
    for px in c[::1]:
        v = px
        if v in 'AEIOU':
           print(v.lower(), end=' ')
    print(' ')
