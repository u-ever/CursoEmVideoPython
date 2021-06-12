n =(float(input('Digite um valor em metros ')))
print('{} metros correspondem a \n{:.3f} km.\n{} hm.\n{} dam.\n{:.0f} dm.\n{:.0f} cm.\n{:.0f} mm.'
      .format(n, (n/1000), (n/100), (n/10), (n*10), (n*100), (n*1000)))