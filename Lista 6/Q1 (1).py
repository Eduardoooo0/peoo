matriz = []
matrizt = []
m = int(input('Digite o numero de linhas:'))
n = int(input('Digite o numero de colunas:'))
for i in range(0,m):
  linha = []
  for j in range(0,n):
    num = int(input('Digite um valor:'))
    linha.append(num)
  matriz.append(linha)
for j in range(0,n):
  for i in range(0,m):
    print(f'[{matriz[j][i]:^5}]', end =' ')
  print()