feijao = {
  'feijoada':0.0,
  'fv':0.0
}
soma = add = 0.0
num = 1
while num == 1 or num == 2:
  num = int(input('1 para registrar a venda de um prato de Feijoada\n2 para registrar a venda de um prato de Feijão Verde\nDigite:'))
  if num != 1 and num != 2:
    break
  else:
    if num == 1:
      soma += 0.2
      feijao.update({'feijoada':soma})
    else:
      add += 0.2
      feijao.update({'fv':add})
    print()
    print('*********** Consumo de Feijão na Cantina ***********')
    print('Foram consumidos até o momento aproximadamente:')
    print('*', feijao['feijoada'],'quilos de Feijoada')
    print('*', feijao['fv'] ,'quilos de Feijão Verde')
    print('*'*52)
    print()
print('*********** Consumo de Feijão na Cantina ***********')
print('Foram consumidos aproximadamente:')
print('*', feijao['feijoada'],'quilos de Feijoada')
print('*', feijao['fv'] ,'quilos de Feijão Verde')
print('*'*52)