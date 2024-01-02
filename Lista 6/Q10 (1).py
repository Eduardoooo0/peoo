p = input("Digite uma palavra: ")
matriz = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
n = 0
for i in range(0,4):
    for j in range(0,4):
        if n < len(p):
            matriz[i][j] = p[n] 
            n += 1
for i in range(0,4):
    for j in range(0,4):
        if matriz[i][j] == 0:
            matriz[i][j] = 'X'
for l in matriz:
    for c in l:
        print(f'[{c:^5}]', end = " ")
    print()