import random

class Filme:
    def __init__(self, titulo, genero, avaliacao):
        self.titulo = titulo
        self.genero = genero
        self.avaliacao = avaliacao

class Usuario:
    def __init__(self, nome, preferencias):
        self.nome = nome
        self.preferencias = preferencias

class AgenteRecomendadorFilmes:
    def __init__(self, filmes):
        self.filmes = filmes

    def recomendar_filme(self, usuario):
        """Recomenda um filme para o usuário baseado na sua preferência"""
        filmes_recomendados = []
        for filme in self.filmes:
            if filme.genero in usuario.preferencias:
                filmes_recomendados.append(filme)
        if filmes_recomendados:
            filme_recomendado = max(filmes_recomendados, key=lambda x: x.avaliacao)
            print(f"Usuário: {usuario.nome} -  Filme Recomendado: {filme_recomendado.titulo}")
        else:
            print(f"Usuário: {usuario.nome} - Nenhum filme encontrado que combine com as preferências do usuário")

# Criar uma lista de filmes
filmes = [
    Filme("O Poderoso Chefão", "Crime", 9.2),
    Filme("Pulp Fiction", "Crime", 8.9),
    Filme("Um Sonho de Liberdade", "Drama", 9.3),
    Filme("Forrest Gump", "Drama", 8.8),
    Filme("Batman, O Cavaleiro das Trevas", "Ação", 9.0),
    Filme("A Origem", "Ficção Científica", 8.8),
    Filme("E O Vento Levou", "Musical", 9.6),
    Filme("Matrix", "Ficção Científica", 8.7),
    Filme("Tubarão", "Terror", 8.0),
    Filme("O Alto da Compadecida", "Comédia", 8.7),
    Filme("LaLaLand", "Musical", 9.5),
    Filme("Velozes e Furiosos 3: Desafio em Tókio", "Ação", 7.6),
    Filme("O Senhor dos Aneis, As Duas Torres", "Fantasia", 9.2),
    Filme("Harry Potter e a Câmara Secreta", "Fantasia", 8.3),
    Filme("Tá chovendo Hambúrguer!", "Animação", 7.8)
]

# Criar Usuários
usuario1 = Usuario("João", ["Comédia", "Drama"])
usuario2 = Usuario("Kim",  ["Ação", "Drama"])
usuario3 = Usuario("Leanderson", ["Ficção Científica", "Terror"])
usuario4 = Usuario("Luciana", ["Comédia", "Fantasia"])
usuario5 = Usuario("Marcela", ["Ação", "Musical"])
usuario6 = Usuario("Lauro", ["Ação", "Animação"])
usuario7 = Usuario("Aline", ["Religioso", "Documentário"])
usuario8 = Usuario("Maria", ["Religioso", "Musical"])

# Criar um Agente Recomendador de Filmes
agente = AgenteRecomendadorFilmes(filmes)

# Recomendar um filme para o Usuário
agente.recomendar_filme(usuario1)
agente.recomendar_filme(usuario2)
agente.recomendar_filme(usuario3)
agente.recomendar_filme(usuario4)
agente.recomendar_filme(usuario5)
agente.recomendar_filme(usuario6)
agente.recomendar_filme(usuario7)
agente.recomendar_filme(usuario8)


