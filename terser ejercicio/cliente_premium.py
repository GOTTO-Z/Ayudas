from cliente import Cliente

class ClientePremium(Cliente):
    def __init__(self, nombre, correo, descuento):
        super().__init__(nombre, correo)
        self.descuento = descuento
        self.lista_entradas = []

    def mostrar_datos(self):
        return f"Nombre: {self.nombre} || Correo: {self.correo}"

    def agregar_entrada(self, entrada):
        self.lista_entradas.append(entrada)

    def Calcular_precio(self):
        if len(self.lista_entradas) > 0:
            total = sum(self.lista_entradas)
            descuento = total - self.descuento // 100
            return descuento
        return "El cliente no posee entrada agendada ✍️(◔◡◔) "