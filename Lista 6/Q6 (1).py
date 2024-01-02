matriz = []
soma = 0
for i in range(0,3):
  linha = []
  for j in range(0,3):
    num = int(input('Digite um valor:'))
    linha.append(num)
  matriz.append(linha)
soma = matriz[0][2] + matriz[1][1] + matriz[2][0]
print(f'a soma da diagonal secundária é {soma}')