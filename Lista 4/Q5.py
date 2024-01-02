lista = []
maior = menor = soma = 0
for i in range(0,4):
  notas = float(input('digite suas notas:'))
  lista.append(notas)
  soma += lista[i]
  if len(lista) == 1:
    maior = menor = lista[i]
  if lista[i] > maior:
    maior = lista[i]
  else:
    if lista[i] < menor:
      menor = lista[i]
media = soma/4
print(f'Média:{media}\nMaior:{maior}\nMenor:{menor}')