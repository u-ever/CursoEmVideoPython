print('-'*50)
print('{: ^50}'.format('LISTAGEM DE PREÇOS'))
print('-'*50)
prod = ('Lápis', '1.75', 'Borracha', '2.00', 'Caderno', '15.90', 'Estojo', '25.00', 'Transferidor', '4.20', 'Compasso',
        '9.99', 'Mochila', '120.32', 'Canetas', '22.30', 'Livro', '34.90')
for c in range(0, len(prod), 2):
  print('{:.<38} R$ {: >8}'.format(prod[c], prod[c+1]))
print('-'*50)
