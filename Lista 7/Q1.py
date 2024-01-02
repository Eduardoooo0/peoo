lista_dicionario = {}
for i in range(0, 5):
  nome = input('NOME:')
  telefone = int(input('TELEFONE:'))
  lista_dicionario.update({nome:telefone})
print()
for n, t in lista_dicionario.items():
  print(f'{n} : {t}')