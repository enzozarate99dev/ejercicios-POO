
from gestorEdificio import GestorEdificio


if __name__ == '__main__':
    ge = GestorEdificio()
    ge.cargarEdificios()

    band = True
    while band:
        print ("[1] Muestra nombre de inquilinos.")
        print ("[2] Mostrar Superficie total cubierta por un edificio.")
        print ("[3] Dado un propietario mostrar superficie de su departamento.")
        print ("[4] Dado un numero de piso mostrar cantidad de departamento con 3 dormitorios y mas de un baño.")
        print ("[5] Salir del sistema.")
        op = int (input ("Seleccione una opcion: "))
        if op == 1:
            xnom = input("Ingrese el nombre del edificio: ")
            pos = ge.buscarEdificio(xnom)
            if  pos < 0:
                print("El edificio no existe")
            else:
                ge.mostrarInquilinosEdif(pos)
        elif op == 2:
            xnom = input("Ingrese el nombre del edificio: ")
            pos = ge.buscarEdificio(xnom)
            if  pos < 0:
                print("El edificio no existe")
            else:
                print(f"La superficie del edificio {xnom} es: {ge.calcularSupEdificio(pos)}m2")
                
        elif op == 3:
            xnom = input("Ingrese el nombre del propietario: ")
            if ge.mostrarSupProp(xnom) is False:
                print("El propietario no existe")
                
        elif op == 4:
            xpiso = int(input("Ingrese un nro de piso: "))
            if ge.mostrarCantSuits(xpiso) is False:
                print("No se encontro el piso")
        else:
            print("SALIENDO")
            band = False