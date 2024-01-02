nome = input('digite seu nome:')
print('DIGITE\nM para matutino\nV para vespertino')
mv = input('digite o turno que você estuda:')
if mv == 'M':
  print(f'Bom dia!,{nome}.')
elif mv == 'V':
  print(f'Boa tarde!,{nome}.')