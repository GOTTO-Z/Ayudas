class Contenido:
    def __init__(self, titulo, duracion):
        self.titulo = titulo
        self.duracion = duracion

    def reproducir(self):
        print(f"Reproducir cancion/podcast {self.titulo}")
        print(f"Duracion: {self.duracion} minutos")
    def mostrar_Informacion(self):
        print(f"Titulos: {self.titulo}")
        print(f"Duracion: {self.duracion}")