class Historico:
    def __init__(self):
        self.emprestimos = []

    def adicionar_emprestimo(self, data):
        self.emprestimos.append(data)


class Livro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.historico_emprestimos = Historico()