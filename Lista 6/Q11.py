matriz_v = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
matriz_c = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
consoante =['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
vogal = ['A','E','I','O','U']
nome='EDUARDO'
name = []
for n in nome:
  name.append(n)
for i in range(0,5):
  for j in range(0,5):
    if len(vogal) >= 1:
      if i == j:
        matriz_v[i][j] = vogal[0]
        vogal.pop(0)
    else:
      pass
for i in range(0,5):
  for j in range(0,5):
    if len(consoante) >= 1:
      matriz_c[i][j] = consoante[0]
      consoante.pop(0)
    else:
      pass
for v in matriz_v:
    print(v)
print()
for c in matriz_c:
    print(c)
print()
for n in nome:
  for i in range(0,5):
      for j in range(0,5):
          if matriz_v[i][j] == n:
              print(f'{n} = Matriz vogal posição {i,j}')
  for i in range(0,5):
      for j in range(0,5):
          if matriz_c[i][j] == n:
              print(f'{n} = Matriz consoante posição {i,j}')