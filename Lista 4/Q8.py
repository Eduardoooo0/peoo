lista_nome = []
lista_sob = []
nome  = input('digite seu primeiro nome:')
for i in nome:
  lista_nome.append(i)
sobrenome = input('digite seu sobrenome:')
for i in sobrenome:
  lista_sob.append(i)
num_nome = len(lista_nome)
num_sob = len(lista_sob)
print(f'Número de letras do nome:{num_nome}\nNúmero de letras do sobrenome:{num_sob}')
print(f'Seu nome completo é {lista_nome + lista_sob}')
  