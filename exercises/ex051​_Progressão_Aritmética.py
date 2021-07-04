print('='*19,'\n10 TERMOS DE UMA PA\n','='*20 )
priterm = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
print(priterm, end=' ➜ ')
for c in range(1, 10):
    priterm += razao
    print(priterm, end=' ➜ ')
print('Acabou')
