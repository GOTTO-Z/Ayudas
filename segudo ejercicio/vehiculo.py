class Vehiculo:
    def __init__(self, _marca, _modelo, _ano):
        self._marca = _marca
        self._modelo = _modelo
        self._ano = _ano

    def mostrar_info(self):
        return f"Marca: {self._marca}, Modelo: {self._modelo}, ano: {self._ano}"

    def ruido(self):
        return "   *RUIDO DE MOTOR*   "
    