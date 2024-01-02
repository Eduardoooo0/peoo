matriz = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
for i in range(0,4):
  for j in range(0,4):
    num = i*j
    matriz[i][j] = num
for i in range(0,4):
  for j in range(0,4):
    print(f'[{matriz[i][j]:^5}]', end =' ')
  print()