num = int(input('Digite um número:'))
cont = 1
soma = 1
while cont <= num:
  soma = soma * cont
  cont += 1
print(f'o fatorial de {num} é {soma}')