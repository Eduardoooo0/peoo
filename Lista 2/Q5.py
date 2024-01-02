a = float(input('digite o valor de A:'))
b = float(input('digite o valor de B:'))
c = float(input('digite o valor de C:'))
ab = a + b
ac = a + c
bc = b + c
if bc > a :
  if ac > b :
    if ab > c :
      print('com esses valores pode-se obter o triângulo ABC')
else:
  print('o triângulo ABC não pode ser obtido')