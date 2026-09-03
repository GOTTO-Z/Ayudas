class Cliente:
    def __init__(self, _nombre, _id_cliente):
        self._nombre = _nombre
        self._id_cliente = _id_cliente
        self._lista_libros = []

    def tomar_prestado(self, libro):
        self._lista_libros.append(libro)

    def devolver_libro(self, libro):
        self._lista_libros.remove(libro)

    def mostrar_infor(self):
        return f"ID: {self._id_cliente}, Nombre: {self._nombre}, Libros prestado: {self._lista_libros}"