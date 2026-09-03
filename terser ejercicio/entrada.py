class Entrada:
    def __init__(self, numero, asiento):
        self.numero = numero
        self.asiento = asiento

    def mostrar_datos(self):
        return f"N°{self.numero} || N° de asiento: {self.asiento}"

    