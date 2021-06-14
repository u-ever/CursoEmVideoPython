a =(float(input('Digite a altura da parede ')))
l =(float(input('Digite a largura da parede ')))
ar =a * l
ti =ar / 2
print ('Sua parede tem a dimensão de {}m² x {}m² e a área da parede é {:.1F}m² '
       '\nA quantidade de tinta necessária para pinta-la é de {:.1F} litros.'.format(a, l, ar, ti))