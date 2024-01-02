from math import sqrt
co = float(input('digite o valor do cateto oposto:'))
ca = float(input('digite o valor do cateto adjacente:'))
h = co**2 + ca**2
h = sqrt(h)
print(f'com o cateto oposto valendo {co} e o cateto adjacente valendo {ca} o valor da hipotenusa é {h:.3f}')