from bib import Livro, Estante

def criar_livro():
    titulo = input('Digite o título do livro: ')
    genero = input('Digite o gênero do livro: ')
    num_paginas = int(input('Digite o número de páginas do livro: '))
    return Livro(titulo, genero, num_paginas)

def main():
    estantes = {}

    while True:
        print('\nOpções:')
        print('1 - Adicionar livro')
        print('2 - Mostrar estantes e seus livros')
        print('3 - Sair')
        opcao = input('Digite o número da opção desejada: ')

        if opcao == '1':
            livro = criar_livro()
            if livro.genero not in estantes:
                estantes[livro.genero] = Estante(livro.genero)
            estantes[livro.genero].adicionar_livro(livro)
            print('Livro adicionado à estante!')

        elif opcao == '2':
            print('\nEstantes e seus livros:')
            for genero, estante in estantes.items():
                print(f'Estante de {genero}:')
                for livro in estante.livros:
                    print(f' - {livro.titulo} ({livro.num_paginas} páginas)')

        elif opcao == '3':
            break

        else:
            print('Opção inválida. Digite novamente.')

if __name__ == '__main__':
    main()