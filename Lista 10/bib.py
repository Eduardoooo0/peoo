class Livro:
    def __init__(self, titulo, genero, num_paginas):
        self.titulo = titulo
        self.genero = genero
        self.num_paginas = num_paginas


class Estante:
    def __init__(self, genero):
        self.genero = genero
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)