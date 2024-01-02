nota1 = float(input('nota 1:'))
nota2 = float(input('nota 2:'))
m = (nota1 + nota2) / 2
if m >= 7:
  print('você foi aprovado')
elif m >= 4 and m < 7:
  print('você ficou de recuperação')
  rec = float(input('nota da recuperação:'))
  m = (nota1 + nota2 + rec) / 2
  if m > 7:
    print('você foi aprovado')
  else:
    print('você reprovou')
else:
  print('você reprovou')