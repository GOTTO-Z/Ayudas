from coche import Coche
from moto import Moto
from bodega import Bodega


def main():

    #Crear Coche
    coche_1 = Coche("Toyota", "Corolla", 2012, "cuatro")

    print(coche_1.mostrar_info())


if __name__ == "__name__":
    main()