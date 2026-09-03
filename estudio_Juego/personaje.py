class Personaje:
    def __init__(self, nombre, vida, nivel):
        self.nombre = nombre
        self.vida = vida
        self.nivel = nivel

    def atacar(self):
        return f"Has realizado un ataque"

    def recibir_dano(self, danio):
        self.vida -= danio

        if self.vida < 0:
            self.vida = 0

        print(f"{self.nombre} recibió {danio} de daño")
        print(f"Vida actual: {self.vida}")

    def usar_habilidad(self):
        print(f"{self.nombre} ha usado su habilidad")

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Vida: {self.vida}, Nivel: {self.nivel}"