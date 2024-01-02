print('0.saída')
num = 1
somap = somai = 0
while not num == 0:
  num = int(input('Digite um número:'))
  if num % 2 == 0:
    somap += num
  else:
    somai += num
print(f'soma dos pares: {somap}  soma dos impares {somai}')