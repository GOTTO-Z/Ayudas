from publicacion import Publicacion

class Revista(Publicacion):
    def __init__(self, _titulo, _autor, _disponible, _edicion):
        super().__init__(_titulo, _autor, _disponible)
        self._edicion = _edicion

    def obtener_infor(self):
        if self._disponible == True:
            estado = "disponible"
        else: 
            estado = "no disponible"

        return f"Titulo: {self._titulo} por {self._autor}, edicion: {self._edicion}, estado: {estado}"