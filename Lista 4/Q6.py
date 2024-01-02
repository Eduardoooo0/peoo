lista = []
for i in range(0,5):
  num = float(input('digite os números:'))
  lista.append(num)
num = float(input('digite um número:'))
if num in lista:
  print('Esse número está na lista')
else:
  print('Não tem esse número na lista')
