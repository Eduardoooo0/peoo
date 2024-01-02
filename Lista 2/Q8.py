e1 = float(input('digite a estatura da pessoa 1:'))
e2 = float(input('digite a estatura da pessoa 2:'))
e3 = float(input('digite a estatura da pessoa 3:'))
if e1 == e2 or e1 == e3 or e2 == e3:
  print('Há, pelo menos, 2 pessoas com a mesma estatura')
else:
  if e1 > e2 and  e1 > e3 :
    maior = e1
  elif e2 > e1 and e2 > e3 :
    maior = e2
  else:
    maior = e3
  print(f'a maior estatura é {maior}')