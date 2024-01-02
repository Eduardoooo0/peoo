maior = linha = coluna = 0
matriz = []
for i in range(0,3):
  linha = []
  for j in range(0,3):
    num = int(input('Digite um valor:'))
    linha.append(num)
  matriz.append(linha)
for i in range(0,3):
  for j in range(0,3):
    if i == 0 and j == 0:
      maior = matriz[i][j]
    elif matriz[i][j] > maior:
      maior = matriz[i][j]
      linha = i
      coluna = j
print(f'o maior elemnto ta na posiçao {linha,coluna}')