from historicobib import Livro

def main():
    livros = []

    while True:
        titulo = input('Digite o título do livro (ou sair para exibir o histórico): ')

        if titulo.upper() == 'SAIR':
            print('\nHistórico de Empréstimos:')
            for livro in livros:
                print(f'Livro: {livro.titulo}')
                print(f'Empréstimos: {livro.historico_emprestimos.emprestimos}')
            break

        livro = Livro(titulo)

        while True:
            data_emprestimo = input('Digite a data do empréstimo (ou "sair" para voltar): ')
            
            if data_emprestimo.upper() == 'SAIR':
                break
            
            livro.historico_emprestimos.adicionar_emprestimo(data_emprestimo)

        livros.append(livro)

if __name__ == "__main__":
    main()