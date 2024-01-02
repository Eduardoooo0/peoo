s1 = input('Digite algo:')
s2 = input('Digite algo novamente:')
for i in range(0,len(s1)):
    if s2 in s1:
        posicao = s1.index(s2[i])
        print(f'a segunda palavra esta presente na  primeira iniciando na posição {posicao}')
        break
    else:
        print('não tem')
        break

