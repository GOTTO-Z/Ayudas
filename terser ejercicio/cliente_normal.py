from cliente import Cliente

class ClientePremium(Cliente):
    def __init__(self, nombre, correo):
        super().__init__(nombre, correo)
        self.lista_entradas = []

    def mostrar_datos(self):
        return f"Nombre: {self.nombre} || Correo: {self.correo}"

    def agregar_entrada(self, precio):
        self.lista_entradas.append(precio)

    def Calcular_precio(self):
        if len(self.lista_entradas) > 0:
            total = sum(self.lista_entradas)
            return total
        return "El cliente no posee entrada agendada ✍️(◔◡◔) "