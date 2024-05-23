from gestorCuenta import GestorCuenta
from gestorTransaccion import GestorTransaccion




if __name__ == "__main__":
    gc = GestorCuenta()
    gt = GestorTransaccion()
    band = True
    while band:
        print("1. Leer archivo de cuentas")
        print("2. Leer archivo de transacciones")
        print("3. Mostrar datos de una cuenta")
        print("4. Actualizar rendimientos")
        print("5. Mostrar la tabla de resultados")
        print("6. Ordenar la tabla de resultados")
        print("7. Exportar la tabla de resultados")
        print("\n0. Salir")
        op= int(input("Ingrese una opcion: "))
        if op == 1:
            gc.agregarCuenta()

        elif op == 2:
            gt.agregarTransaccion()
            
        elif op == 3:
            dni=int(input("Ingrese el DNI del cliente: "))
            indice = gc.buscarCuenta(dni)
            if indice == None:
                print("No se encontro la cuenta")
            else:
                gc.getUnaCuenta(indice)
        elif op == 4:
            xp = float(input("Ingrese el nuevo porcentaje anual: "))
            gc.setPorcAnual(xp)

            
        elif op == 0:
            print("SALIENDO...")
            band = False
    
    
