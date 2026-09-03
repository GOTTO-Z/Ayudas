class Bodega:
    def __init__(self, _nombre):
        self._nombre = _nombre
        self.lista_vehiculos = []


    def agregar_vehiculo(self, veiculo):
        self.lista_vehiculos.append(veiculo)

    def mostrar_info(self):
        return f"Nombre de bodega: {self._nombre}, Lista: {self.lista_vehiculos}"