nome = input('Digite seu nome:')
while not len(nome) > 3:
  print('O nome precisar ter mais que 3 caracteres')
  print('Digite novamente')
  nome = input('Digite seu nome:')
idade = int(input('Digite sua idade:'))
while not idade > 10 and idade < 100:
  print('A idade tem que ser entre 10 e 100 anos')
  print('Digite novamente')
  idade = int(input('Digite sua idade:'))
ec = input('Digite seu Estado Civil [S/C/V/D]:')
while not ec == 'S' or ec == 'C' or ec == 'V' or ec == 'D':
  print('Digite apenas [S/C/V/D] para seu respectivo estado civil')
  print('Digite Novamente')
  ec = input('Digite seu Estado Civil [S/C/V/D]:')
if ec == 'S':
  ec = 'Solteiro'
elif ec == 'C':
  ec = 'Casado'
elif ec == 'V':
  ec = 'Viúvo'
else:
  ec = 'Divorciado'
tel = input('Telefone:')
while not len(tel) == 9:
  print('Digite um numero com nove digitos apenas')
  tel = input('Telefone:')
print()
print(f'{nome}\n{idade} anos\n{ec}\n(84){tel}')
  