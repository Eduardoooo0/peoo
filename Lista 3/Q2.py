num1 = int(input('Digite o primeiro número:'))
num2 = int(input('Digite um número maior que o primeiro:'))
soma = cont = 0
s = (num2 - num1) + 1
n = num1
while not n > s:
  if n % 2 == 0:
    soma += n
  n += 1
print(f'De {num1} a {num2} a soma de todos os números pares é {soma}')
