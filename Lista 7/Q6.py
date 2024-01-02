agenda = {}
contato = 1
while contato != 0:
  print('******** Agenda em Python *********')
  print(f'Existem: {len(agenda.keys())} contatos cadastrados')  
  print('***********************************')
  print('''  1. Inserir um contato
  2. Consultar um contato
  3. Remover um contato
  4. Listar toda a agenda
  0. Finalizar''')
  contato = int(input('Digite a opção desejada:'))
  print()
  if contato == 0:
    break
  elif contato == 1:
    lista = []
    nome = input('Digite o nome do contato:')
    email = input('Digite o email do contato:')
    telefone = input('Digite o telefone do contato:')
    lista.append(email)
    lista.append(telefone)
    agenda.update({nome:lista})
    print('Contato Cadastrado')
    print()
  elif contato == 2:
    if len(agenda.keys()) >= 1:
      nome = input('Digite o nome do contato que vc quer consultar:')
      if nome in agenda.keys():
        n = agenda[nome]
        print(f'Dados do contato:\nEmail: {n[0]} Telefone: {n[1]}')
        print()
      else:
        print('O contato não existe')
        print()
    else:
      print('Não tem contato cadastrado ainda')
      print()
    print()
  elif contato == 3:
    if len(agenda.keys()) >= 1:
      nome = input('Digite o nome do contato que você quer remover:')
      if nome in agenda.keys():
        agenda.pop(nome)
        print('Contato removido')
        print()
      else:
        print('O contato não existe')
        print()
    else:
      print('Não tem contato cadastrado ainda')
      print()
    print()
  elif contato == 4:
    for n,d in agenda.items():
      print(f'Contato: {n} | Email: {d[0]} | Telefone: {d[1]} ')
      print()
    if len(agenda.keys()) == 0:
      print('Nenhum contato na lista')
      print()