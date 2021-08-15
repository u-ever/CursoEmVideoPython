
def maior(* num):
    count = larger = 0
    lista = []
    for c in num:
        lista.append(c)
        larger = max(lista)
        count += 1
    print(f'{"=-"*30}\nAnalisando os valores passados...\nForam informados {count} valores ao todo.\nO maior valor informado foi {larger}.\n{"=-"*30}')

maior(5, 6, 7, 1)
maior(10,5,7,6)
maior()

