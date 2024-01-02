p1 = float(input('digite o valor do produto 1:'))
p2 = float(input('digite o valor do produto 2:'))
p3 = float(input('digite o valor do produto 3:'))
c = p1
if p2 > c :
  c = p2
  if p3 > c :
    #3,1
    b = p1
    print(f'o produto que custa menos é o produto 1 que custa R${b}')
  elif p1 > p3 :
    #2,3
    b = p3
    print(f'o produto que custa menos é o produto 3 que custa R${b}')
  else:
    #2,1    b = p1
    print(f'o produto que custa menos é o produto 1 que custa R${b}')
elif p3 > c :
  if p1 > p2 :
    #3,2
    b = p2
    print(f'o produto que custa menos é o produto 2 que custa R${b}')
else:
  if p2 > p3 :
    #1,3
    b = p3
    print(f'o produto que custa menos é o produto 3 que custa R${b}')
  else:
    #1,2
    b = p2
    print(f'o produto que custa menos é o produto 2 que custa R${b}')