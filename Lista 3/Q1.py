print('0.saída')
soma = cont = 0
while True:
  num = float(input('Digite qualquer número:'))
  if num == 0:
    break
  else:
    soma += num
    cont += 1
media = soma / cont
print(f'a soma dos números digitados é {soma} e a média é {media}')