import math # from math import sin, cos, tan, radians
an =float(input('Digite o ângulo que você deseja: '))
se = math.sin(math.radians(an)) #se = sin(radians(an))
co = math.cos(math.radians(an)) #co = cos(radians(an))
ta = math.tan(math.radians(an)) #ta = tan(radians(an))
print('O ângulo de {} tem o SENO de {:.2F}'.format(an, se))
print('O ângulo de {} tem o COSSENO de {:.2F}'.format(an, co))
print('O ângulo de {} tem a TANGENTE de {:.2F}'.format(an, ta))