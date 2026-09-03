class Sala:
    def __init__(self, numero, capacidad):
        self.numero = numero
        self.capacidad = capacidad

    def mostrar_datos(self):
        return f"N°{self.numero} | Capacidad maxima: {self.capacidad}"

    def hay_disponibilidad(self, entradas_vendida):
        if entradas_vendida > self.capacidad:
            return "No hay disponibilidad"
        return "Hay disponibilidad"