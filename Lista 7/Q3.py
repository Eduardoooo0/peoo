estoque = {}
for i in range(0,5):
  lista = []
  print(f'Produto {i+1}:')
  produto = input('PRODUTO:')
  codigo = int(input('CÓDIGO:'))
  quantidade = int(input('QUANTIDADE:'))
  preco = float(input('PREÇO:'))
  lista.append(codigo)
  lista.append(quantidade)
  lista.append(preco)
  estoque.update({produto:lista})
  print()
for p,q in estoque.items():
  print(f'Produto: {p} | Código: {q[0]} | Quantidade: {q[1]} | Preço total: R${q[1]*q[2]}')
  