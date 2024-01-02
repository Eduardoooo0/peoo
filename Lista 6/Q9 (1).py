matriz = [['','',''],['','',''],['','','']]
for i in range(3):
    for j in range(3): 
      e = input('Digite o elemento : ')
      matriz[i][j] = e
for i in range(3):
    for j in range(3):
        print(f'[{matriz[i][j]:^5}]',end=' ')
    print()
dp = []
for i in range(3):
    dp.append(matriz[i][i])
print(f'Os elementos da diagonal principal são:{dp}')