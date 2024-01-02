try:
  arquivo = open('nomes.txt', 'r')
  linhas = arquivo.readlines()
  arquivo.close()
  for i in range(len(linhas)):
    print(f'Linha [{i+1}] -> {linhas[i]}')
except Exception as erro:
  print(f'Erro: {erro}')
  print(f'Classe do Erro: {type(erro)}')