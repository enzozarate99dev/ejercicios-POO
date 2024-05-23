
from gestorLadrillo import GestorLadrillo
from gestorMateriales import GestorMateriales


if __name__ == '__main__':
    gl = GestorLadrillo()
    gm = GestorMateriales()
    gl.cargarLadrillos()
    gm.cargarMateriales()
    gl.añadirMaterial(1,2,gm)
    band = True
    while band:
        print ("[1] Detallar costo y característica del material solicitado.")
        print ("[2] Mostrar para cada ladrillo el costo total de fabricación del pedido.")
        print ("[3] Mostrar el informe detallado para cada ladrillo.")
        print ("[otro] Salir del sistema.")
        op = int (input ("Seleccione una opcion: "))
        if op == 1:
            xid = int(input("Ingrese el id del lote de ladrillos: "))
            pos = gl.buscarLote(xid)
            if  pos < 0:
                print("El lote no existe")
            else:
                print(f"LISTA DE MATERIALES DEL LOTE {xid}")
                gl.detalleMateriales(pos)
        elif op == 2:
            gl.mostrarCostos()
                
        elif op == 3:
            gl.mostrarDetalleLadrillos(gm)

        else:
            print("SALIENDO")
            band = False