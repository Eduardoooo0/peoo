f = input('digite uma frase:')
lista = []
lista2 = []
f1 = f2 = ''
f = f.replace(' ','')
for i in f:
    lista.append(i)
for i in range(len(f)-1,-1,-1):
    lista2.append(lista[i])
for i in range(0,len(f)):
    f1 += lista[i]
    f2 += lista2[i]
if f1 == f2:
    print('Palíndromo')
else:
    print('Não palíndromo')
