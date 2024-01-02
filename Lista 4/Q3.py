lista = []
lista_inv = []
for i in range(0,10):
  num = int(input('digite um numero:'))
  lista.append(num)
for i in range(9,-1,-1):
  lista_inv.append(lista[i])
print(lista_inv)