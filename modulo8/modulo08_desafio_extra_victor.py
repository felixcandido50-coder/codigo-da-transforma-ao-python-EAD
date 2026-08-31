'''


'''

class Livro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.disponivel = True


class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def emprestar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                if livro.disponivel:
                    livro.disponivel = False
                    print("Livro emprestado com sucesso!")
                else:
                    print("Livro já está emprestado!")
                return
        print("Livro não encontrado!")

    def listar_livros(self):
        for livro in self.livros:
            status = "Disponível" if livro.disponivel else "Emprestado"
            print(f"- {livro.titulo} ({status})")


# Teste
biblio = Biblioteca()

# Criando livros
l1 = Livro("Dom Casmurro")
l2 = Livro("1984")

# Adicionando na biblioteca
biblio.adicionar_livro(l1)
biblio.adicionar_livro(l2)

# Emprestando um livro
biblio.emprestar_livro("1984")

# Ver os livros
biblio.listar_livros()