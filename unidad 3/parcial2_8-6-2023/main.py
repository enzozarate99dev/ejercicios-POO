
from Casa import Casa
from Departamento import Departamento
from claseLista import Lista
import unittest

def run_tests():
    loader = unittest.TestLoader()
    suite = loader.discover('.', pattern='claseTest.py')
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == '__main__':
    li = Lista()
    
    band = True
    while band:
        print("")
        print ("[1] Insertar inmuebles desde archivo.")
        print ("[2] Agregar un inmueble al final.")
        print ("[3] Mostrar todos los datos de los deptos")
        print ("[4] Mostrar sup cubierta, direccion e importe de venta de todas las casas")
        print ("[5] Testear")
        print ("[otro] Salir del sistema.")
        op = int (input ("Seleccione una opcion: "))
        if op == 1:
            li.insertarInmuebles()  
            for dato in li:
                print(dato)

        elif op == 2:
            try:
                tipo = int(input("Ingrese el tipo de inmueble ([1]Depto - [2]Casa - [0]Cancelar): "))
                if tipo not in [0, 1, 2]:
                    raise ValueError("Tipo invalido")
                if tipo == 0:
                    print("Cancelado")
                    continue
                else:
                    loc = input("Ingrese la localidad: ")
                    dir = input("Ingrese la direccion: ")
                    sup = float(input("Ingrese la superficie cubierta: "))
                    if tipo == 1:
                        cantH = int(input("Cantidad de habitaciones: "))
                        nroM = int(input("Nro de monoblock: "))
                        nroD = int(input("Nro dpto: "))
                        piso = int(input("Piso: "))
                        inmu = Departamento(loc, dir, sup, cantH, nroM, nroD, piso)
                        li.agregarAlFinal(inmu)
                    else:
                        supT = float(input("Superficie del terreno: "))
                        inmu = Casa(loc, dir, sup, supT)
                        li.agregarAlFinal(inmu)
            except ValueError:
                print("Tipo invalido")
                continue

        elif op == 3:
            cant = int(input("Ingrese una cantidad de hab: ")) 
            li.informeDeptos(cant)
        
        elif op == 4:
            li.informeCasas()
        elif op == 5:
            run_tests()
        else:
            print("SALIENDO")
            band = False