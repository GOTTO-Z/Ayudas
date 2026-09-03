from cancion import Cancion
from podcast import Podcast
from artista import Artista
from contenido import Contenido

def main():

    #Crear cancion
    cancion_uno = Cancion("Tranz", "2:00", "Punk Rock")
    cancion_dos = Cancion("Andromeda", "2:30", "Punk Rock") 
    #Crear podcas
    podcast_uno = Podcast("Ultima Hora", "35:00", "comedia", "6")
    #Crear artista
    nuevo_artista = Artista("Gorilaz", "Rock, Punk Rock")
    segundo_artista = ("Gotoh", "rizas")

    #Asociar las canciones al artista
    nuevo_artista.agregar_cancion(cancion_uno)
    nuevo_artista.agregar_cancion(cancion_dos)

    nuevo_artista.mostrar_info()






if __name__ == "__name__":
    main()