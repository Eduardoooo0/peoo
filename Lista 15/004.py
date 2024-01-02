try:
  import matematica as math
except Exception as error:
  print(f"Erro: {error}")
try:  
  print(math.sen(30))
except Exception as erro:
  print(f'Erro: {erro}')