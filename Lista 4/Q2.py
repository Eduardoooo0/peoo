lista = []
maior = menor = 0
for i in range(0,5):
  num = int(input('digite um numero:'))
  lista.append(num)
  if len(lista) == 1:
    maior = menor = lista[i]
    pma = i
    pme = i
  if lista[i] > maior:
    maior = lista[i]
    pma = i
  else:
    if lista[i] < menor:
      menor = lista[i]
      pme = i
print(f'O maior número é {maior} e está na posição {pma}')
print(f'O menor número é {menor} e está na posição {pme}')