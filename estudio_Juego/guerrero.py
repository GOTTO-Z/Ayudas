from personaje import Personaje

class Guerrero(Personaje):
    def __init__(self, nombre, vida, nivel, fuerza, armadura):
        super().__init__(nombre, vida, nivel)
        self.fuerza = fuerza
        self.armadura = armadura

    def atacar(self):
        if self.fuerza == "manos":
            fuarz_actual =+ 10
            return f"{self.nombre} ha realizado un ataque || dano realizado {self.fuerza}"
        elif self.fuerza == "Espada":
            fuarz_actual =+ 200
            return f"{self.nombre} ha realizado un ataque || dano relizado {self.fuerza}"

    def recibir_dano(self, dano):
        if self.armadura.low() == "cuerro":
            dano_actual = max(0, dano - 100)
            self.vida =- dano_actual
            return f"{self.nombre} ha recibido dano || vida actual: {self.vida}"
        elif self.armadura.low() == "diamante":
            dano_actual = max(0, dano - 200)
            self.vida =- dano_actual
            return f"{self.nombre} ha recibido dano || vida actual: {self.vida}"
        else:
            self.vida =- dano
            return f"{self.nombre} ha recibido dano || vida actual: {self.vida}"

    def usar_habilidad(self):
        return f"{self.nombre} utilizara su habilidad"