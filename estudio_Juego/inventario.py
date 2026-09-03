class Inventario:
    def __init__(self, capacidad, oro, objeto):
        self.capacidad = capacidad
        self.oro = oro
        self.objetos = []

    object_total = 0

    def anadir_objeto(self, objeto, objeto_total):
        if objeto_total < self.capacidad:
            objeto_total =+ 1
            self.objetos.append(objeto)