n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print('Tirando {:.1F} e {:.1F}, a média do aluno é {:.1F}'.format(n1, n2, media))
if media <= 5:
    print('O aluno está REPROVADO')
elif media >= 7:
    print('O aluno está APROVADO')
else:
    print('O aluno está de RECUPERAÇÃO')
