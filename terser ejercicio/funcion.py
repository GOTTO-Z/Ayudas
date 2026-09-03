class Funcion:
    def __init__(self, fecha, hora, precio):
        self.fecha = fecha
        self.hora = hora
        self.precio = precio

    def mostrar_datos(self):
        return f"Fecha: {self.fecha} || Hora: {self.hora} en minutos || Precio: {self.precio}"