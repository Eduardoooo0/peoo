while True:
  try:
    nome = input('Digite um nome ou [FIM] para sair:')
    if nome.upper() == 'FIM':
      break
    else:
      for i in nome.upper():
        if i == 'X':
          raise Exception('O nome não pode conter a letra X')
  except Exception as erro:
    print(f'Erro: {erro}')
  else:
    try:
      telefone = input('Digite um telefone:')
      for i in telefone:
        if not i.isnumeric():
          raise ValueError('O telefone deve conter apenas números')
    except ValueError as error:
      print(f'Erro: {error}')
    else:
      arquivo = open('contatos.txt', 'a')
      arquivo.write(f'{nome} - {telefone}\n')
      arquivo.close()
      print('contato criado com sucesso!')