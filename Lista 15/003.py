def Verificar():
  senha = input('Digite uma senha:')
  if len(senha) < 8:
    raise Exception('A senha deve ter no mínimo 8 caracteres')
  elif senha.upper() == 'INTERNACIONAL':
    raise Exception('A senha não pode ser internacional')

while True:
  try:
    Verificar()
    break
  except Exception as e:
    print(e)
print('Senha criada com sucesso')