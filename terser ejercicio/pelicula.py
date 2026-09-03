class Pelicula:
    def __init__(self, titulo, genero, duracion):
        self.titulo = titulo
        self.genero = genero
        self.duracion = duracion

    def mostrar_datos(self):
        return f"titulo: {self.titulo} || genero: {self.genero} || Duracion: {self.duracion} en minutos"