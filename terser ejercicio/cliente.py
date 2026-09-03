class Cliente:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

    def mostrar_datos(self):
        return f"Nombre: {self.nombre} || Correo: {self.correo}"

    def calcular_precio(self, precio):
        return precio