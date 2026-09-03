from libro import Libro
from revista import Revista
from cliente import Cliente

def main():

    #Crear Cliente
    cliente_1 = Cliente("Gotoh", "12")

    #Crear Libro
    libro_1 = Libro("El gato", "desconocido", True, 12)

    #Crear Revista
    revista_1 = Revista("Los 7 pasos", "los patos", False, "de verano")

    # Salida de objetos
    print(libro_1.obtener_info())


if __name__ == "__name__":
    main()