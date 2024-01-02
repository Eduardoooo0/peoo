lista1 = []
lista2 = []
for i in range(0,5):
    lista1.append(int(input('numeros da lista 1:')))
    lista2.append(int(input('numeros da lista 2:')))
lista3 = list(set(lista1+lista2))
print(lista3)
