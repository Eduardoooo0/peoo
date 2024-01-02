while True:
  nome = input("Digite um nome: ")
  if nome.upper() != 'PARE':
    try:
      arquivo = open('nomes.txt', 'a')
      arquivo.write(nome + '\n')
      arquivo.close()
    except Exception as erro:
      print(f'Erro: {erro}')
      print(f'Classe do Erro: {type(erro)}')
  else:
    break