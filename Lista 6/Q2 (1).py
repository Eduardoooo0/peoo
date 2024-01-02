matriz = []
cont = 0
num_m = []
for i in range(0,3):
  linha = []
  for j in range(0,3):
    num = int(input('Digite um valor:'))
    linha.append(num)
  matriz.append(linha)
for i in range(0,3):
  for j in range(0,3):
    if matriz[i][j] > 10:
      cont += 1
      num_m.append(matriz[i][j])
print(f'tem {cont} numeros maior que 10')
print(f'são eles {num_m}')