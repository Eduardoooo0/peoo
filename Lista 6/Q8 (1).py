nome = input('Digite seu primeiro nome: ')
nome_matriz = ''
for _ in range(0,16):
    nome_matriz += nome
    if len(nome_matriz) > 16:
        nome_matriz = nome_matriz[:16]
        break

matriz = [nome_matriz[0:4],nome_matriz[4:8],nome_matriz[8:12],nome_matriz[12:16]] 

for m in matriz:
    print(m)
    