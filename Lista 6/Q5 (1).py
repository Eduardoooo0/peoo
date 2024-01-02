matriz1 = []
matriz2 = []
matriz3 = []
for i in range(0,3):
  linha = []
  for j in range(0,3):
    num = int(input('Digite um valor para matriz 1:'))
    linha.append(num)
  matriz1.append(linha)
for i in range(0,3):
  linha = []
  for j in range(0,3):
    num = int(input('Digite um valor para matriz 2:'))
    linha.append(num)
  matriz2.append(linha)
for i in range(0,3):
  linha = []
  for j in range(0,3):
    if matriz1[i][j] > matriz2[i][j]:
      linha.append(matriz1[i][j])
    elif matriz1[i][j] == matriz2[i][j]:
      linha.append(matriz1[i][j])
    else:
      linha.append(matriz2[i][j])
  matriz3.append(linha)
for i in range(0,3):
  for j in range(0,3):
    print(f'[{matriz3[i][j]:^5}]', end =' ')
  print()