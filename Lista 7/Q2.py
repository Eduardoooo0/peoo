dicionario = {}
nome = ''
lista = []
lista_r = []
while not nome == 'pare':
  nome = input('NOME:')
  if nome == 'pare':
    break
  else:
    media = float(input('MÉDIA:'))
    dicionario.update({nome:media})
    if dicionario[nome] > 60:
      lista.append(nome)
    else:
      lista_r.append(nome)
print('Aprovados:')
for a in lista:
  print(a)
print()
print('Reprovados:')
for r in lista_r:
  print(r)