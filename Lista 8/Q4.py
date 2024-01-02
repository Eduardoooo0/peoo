def main():
    ano = int(input('Digite o ano em que vc nasceu:'))
    print(f'você já viveu {calcularano(ano)} anos')
def calcularano(AAAA):
    from num2words import num2words as chico
    ano = 2023 - AAAA
    num = chico(ano, lang='pt-br')
    return num
if __name__ == '__main__':
    main()
