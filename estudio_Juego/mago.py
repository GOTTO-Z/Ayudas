from personaje import Personaje

class Mago(Personaje):
    def __init__(self, nombre, vida, nivel, nem, tipo_nem):
        super().__init__(nombre, vida, nivel)
        self.nem = nem
        self.tipo_nem = tipo_nem

    def atacar(self):
        return f"{self.nombre} ha realizado un ataque con su nem"

    
    def recibir_dano(self, dano):
        vida_actual = self.vida - dano
        return f"{self.nombre} ha recibido dano || vida actual: {vida_actual}"

    def usar_habilidad(self):
        if self.nem > 0:
            self.nem =- 1
            return f"El Mago {self.nombre} utilisara su tecnica de nem de tipo {self.tipo_nem} || Nem actual: {self.nem}"
        return f"Ho no el mago {self.nombre} se a quedado sin nem"