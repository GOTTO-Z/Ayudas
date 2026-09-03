from contenido import Contenido

class Podcast(Contenido):
    def __init__(self, titulo, duracion, categoria, numero_episodio):
        super().__init__(titulo, duracion)
        self.categoria = categoria
        self.numero_episodio = numero_episodio

    def reproducir(self):
        print(f"Reproducir podcast {self.titulo}"
              f"Episodio {self.numero_episodio}")

    def mostrar_informacion(self):
        print(f"\n ---Podcast---")
        print(f"Titulo: {self.titulo}")
        print(f"Duracion: {self.duracion}")
        print(f"Categoria: {self.categoria}")
        print(f"Episodios: {self.numero_episodio}")