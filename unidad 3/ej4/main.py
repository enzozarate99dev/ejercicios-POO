from AudioLibro import Audiolibro
from Libro import Libro
from Publicacion import Publicacion
from claseLista import ListaPublicaciones

if __name__ == '__main__':
    li = ListaPublicaciones()
    li.cargarPublicaciones()
    band = True
    while band:
        print ("[1] Agregar una publicacion.")
        print ("[2] Mostrar tipo de publicacion.")
        print ("[3] Mostrar la cantidad de publicaciones de cada tipo")
        print ("[4] Informar de cada publicacion Titulo, categoría e importe de venta.")
        print ("[otro] Salir del sistema.")
        op = int (input ("Seleccione una opcion: "))
        if op == 1:
            try:
                tipo = int(input("Ingrese el tipo de publicacion ([1]Libro - [2]Audiolibro - [0]Cancelar): "))
                if tipo not in [0, 1, 2]:
                    raise ValueError("Tipo invalido")
                if tipo == 0:
                    print("Cancelado")
                    continue
                titulo = input("Ingrese el Titulo: ") 
                categoria = input("Ingrese la Categoria: ")
                precioBase = float(input("Ingrese el Precio: "))
                
                if tipo == 1:
                    autor = input("Ingrese el Autor: ")
                    fechaE = input("Ingrese Fecha de edicion: ")
                    cantPaginas = int(input("Ingrese Cant de paginas: "))
                    publi = Libro(titulo, categoria, precioBase, autor, fechaE, cantPaginas)
                elif tipo == 2:
                    tiempoR = int(input("Ingrese Tiempo de reproduccion: "))
                    narrador = input("Ingrese el Narrador: ")
                    publi = Audiolibro(titulo, categoria, precioBase, tiempoR, narrador)
                li.agregarPublicacion(publi)
            except ValueError:
                print("Tipo invalido")
                continue        
        elif op == 2:
            pos = int(input("Ingrese una posición en la lista: "))
            if li.mostrarTipoPublicacion(pos) == 1:
                print("Es un libro")
            elif li.mostrarTipoPublicacion(pos) == 2:
                print("Es un audiolibro")

        elif op == 3:
            li.mostrarCantDeTipos()
        
        elif op == 4:
            li.informeVentas()

        else:
            print("SALIENDO")
            band = False