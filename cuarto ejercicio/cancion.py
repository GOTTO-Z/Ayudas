from contenido import Contenido

class Cancion(Contenido):

    def __init__(self, titulo, duracion, genero):
        super().__init__(titulo, duracion)
        self.genero = genero
    def reproducir(self):
        print(f"Rproducir la cancion ... {self.titulo}")
    def mostrar_Informacion(self):
        print(f"\n ---Canciones---")
        print(f"Titulo: {self.titulo}")
        print(f"Duracion: {self.duracion}")
        print(f"Genero: {self.genero}")