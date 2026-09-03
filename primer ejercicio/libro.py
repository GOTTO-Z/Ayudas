from publicacion import Publicacion

class Libro(Publicacion):
    def __init__(self, _titulo, _autor, _disponible, _num_paginas):
        super().__init__(_titulo, _autor, _disponible)
        self._num_paginas = _num_paginas

    def obtener_infor(self):
        if self._disponible == True:
            estado = "disponible"
        else: 
            estado = "no disponible"

        return f"Titulo: {self._titulo} por {self._autor}, numero de paginas: {self._num_paginas}, {estado}"
