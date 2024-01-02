dep = float(input('Digite o valor do deposito inicial:'))
juros = float(input('Juros mensais:'))
juros = dep * (juros/100)
cont = 0
while cont < 12:
  cont += 1
  mes = dep + (juros * cont)
  print(f'Mês: {cont}  Saldo: R${mes}')
soma = juros * 12
print(f'O valor total recebido em juros é R${soma}')