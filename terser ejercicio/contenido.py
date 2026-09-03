class Contenido:
    def __init__(self, titulo, duracion):
        self.titulo = titulo
        self.duracion = duracion

    def reproducir(self):
        return f"Se esta reproduciendo {self.titulo}"

    def mostrar_informacion(self):
        return f"Titulo: {self.titulo} || Duracion: {self.duracion}"