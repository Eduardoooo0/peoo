num = input('digite um  numero:')
lista = []
lista2 = []
f1 = f2 = ''
for i in num:
    lista.append(i)
for i in range(len(num)-1,-1,-1):
    lista2.append(lista[i])
for i in range(0,len(num)):
    f1 += lista[i]
    f2 += lista2[i]
if f1 == f2:
    print('Palíndromo')
else:
    print('Não palíndromo')
