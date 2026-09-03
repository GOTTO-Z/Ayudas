from vehiculo import Vehiculo

class Moto(Vehiculo):
    def __init__(self, _marca, _modelo, _ano, _tipo):
        super().__init__(_marca, _modelo, _ano)
        self._tipo = _tipo

    def mostrar_info(self):
        return f"Marca: {self._marca}, Modelo: {self._modelo}, Ano: {self._ano}, Tipo: {self._tipo}"

    def hacer_ruido(self):
        if self._tipo.low() == "scooter":
            return " *Run Run Ruuuuun* "
        if self._tipo == "deportista":
            return "Tun Tun Tun sajut"
        return " *PUn PUn PUn* "
