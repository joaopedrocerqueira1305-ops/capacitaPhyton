class Filme:    
    def __init__(self, titulo, genero, anoLancamento):
        self.titulo = titulo
        self.genero = genero
        self.anoLancamento = anoLancamento
        self.notaGeral = 0
        self.notasUsuarios = []

    def adicionarFilme(self, titulo, genero, anoLancamento):
        self.titulo = titulo
        self.genero = genero
        self.anoLancamento = anoLancamento
        self.notaGeral = 0
        self.notasUsuarios = []
        print(f"Filme '{self.titulo}' adicionado com sucesso!")

    def avaliarFilme(self, nota):
        if 1 <= nota <= 10:
            self.notasUsuarios.append(nota)
            self.notaGeral = sum(self.notasUsuarios) / len(self.notasUsuarios)
            print(f"Filme '{self.titulo}' avaliado com nota {nota}.")
        else:
            print("A nota deve ser entre 1 e 10.")

    def exibirDetalhes(self):
        print(f"Título: {self.titulo}")
        print(f"Gênero: {self.genero}")
        print(f"Ano de Lançamento: {self.anoLancamento}")
        if self.notaGeral > 0:
            print(f"Nota Geral: {self.notaGeral:.2f}/10")
        else:
            print("Ainda não há avaliações para este filme.")
            
