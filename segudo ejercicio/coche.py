from vehiculo import Vehiculo

class Coche(Vehiculo):
    def __init__(self, _marca, _modelo, _ano, _puertas):
        super().__init__(_marca, _modelo, _ano)
        self._puertas = _puertas

    def mostrar_info(self):
        return f"Marca: {self._marca}, Modelo: {self._modelo}, Ano: {self._ano}, Tipo de puerta: {self._puertas}"

    def hacer_ruido(self):
        return " *Tralalero tralala* "