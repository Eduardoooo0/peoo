saldo = 1000
while saldo > 0:
  c = float(input('Digite o valor das compras:'))
  if c > saldo:
    print('Não há Saldo suficiente para esta compra')
  else:
    saldo -= c
  print(f'Saldo atual: R${saldo}')