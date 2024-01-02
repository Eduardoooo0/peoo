from math import sqrt
try:
  num = int(input("Digite um número para achar a raiz quadrada:"	))
  if num < 0:
    raise Exception('Não é possível achar a raiz quadrada de um número negativo')
  else:
    raiz = sqrt(num)
    print(f'A raiz de {num} é {raiz}')
except ValueError as erro:
  print(f"Erro: {erro}")
except Exception as error:
  print(f"Erro: {error}")
