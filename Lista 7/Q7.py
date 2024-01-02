carros = {}
placa = 1
vt = 0
soma = somag = somad = 0
while placa != 0:
    print(f'''***** Posto Roberto Carlos ******
    Valor Apurado no DIA: R$ {vt:.3f} 
*********************************
    ''')
    placa = int(input('Digite a placa do veículo:'))
    if placa == 0:
        break
    else:    
        lista = []
        combustivel = input('Digite o tipo de combustível:')
        litros = float(input('Quantidade de litros:'))
        lista.append(combustivel)
        lista.append(litros)
        carros.update({placa:lista})
        for i in carros.values():
            if i[0] == 'etanol':
                soma += i[1]
            elif i[0] == 'gasolina':
                somag += i[1]
            elif i[0] == 'diesel':
                somad += i[1]
    v1 = soma * 5
    v2 = somag * 6      
    v3 = somad * 5.5
    vt = v1 + v2 + v3
print()
print(f'* A quantidade de carros atendidos foi {len(carros.keys())}')
print(f'* Foram vendidos {soma} litros de Etanol')
print(f'* Foram vendidos {somag} litros de Gasolina')
print(f'* Foram vendidos {somad} litros de Diesel')