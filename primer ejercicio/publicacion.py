class Publicacion:
    def __init__(self, _titulo, _autor, _disponible):
        self._titulo = _titulo
        self._autor = _autor
        self._disponible = _disponible

    def obtener_info(self):
        return f"Titulo: {self._titulo}, Autor/a: {self._autor}"

    def prestar(self):
        if self._disponible == True:
            return "Publicacion disponiblre"
        return "publicacion no disponibel"
        
    def devolver(self):
        self._disponible = True