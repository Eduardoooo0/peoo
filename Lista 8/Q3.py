def main():
    while True:
        print('1 - Codificar\n2 - Decodificar\nsair - Para sair')
        pg = input(':').upper()
        if pg == 'SAIR':
            break
        else:
            pg = int(pg)
            if pg == 1:
                codificar()
            elif pg == 2:
                decodificar()
def codificar():
    import base64
    string = input('Digite algo para ser codificado:')
    string = base64.b64encode(string.encode('ascii'))
    string = string.decode('ascii')
    print(f'A mensagem codificada fica : {string}')
def decodificar():
    import base64
    string = input('Digite algo para ser decodificado:')
    string = base64.b64decode(string.encode('ascii'))
    string = string.decode('ascii')
    print(f'A mensagem decodificada fica : {string}')
if __name__ == '__main__':
    main()