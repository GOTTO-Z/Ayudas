class Jugador:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.lista_personajes = []

    def crear_personaje(self, personaje):
        self.lista_personajes.append(personaje)

    def perder_personaje(self, vida, personaje):
        if vida <= 0:
            print(f"{personaje.nombre} ha sido derotado")
            self.lista_personajes.remove(personaje)
        print(f"{personaje.nombre} haun sigue en pie")

    def iniciar_secion(self):
        return "Iniciar seccion"

    def mostrar_perfil(self):
        return f"N°{self.id}, Nombre: {self.nombre}, Personajes: {self.lista_personajes}"