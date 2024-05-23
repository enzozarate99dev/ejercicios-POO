import csv

from classLadrillo import Ladrillo
from gestorMateriales import GestorMateriales


class GestorLadrillo:
    __listLadrillos: list
    def __init__(self):
        self.__listLadrillos = []
    def cargarLadrillos(self):
        archi = open("ladrillos.csv")
        reader = csv.reader(archi)
        band = False
        for fila in reader:
            if band == False:
                band = True
            else:
                id = int(fila[0]) 
                cantidad = int(fila[1])
                kgMat = float(fila[2])
                costo = float(fila[3])
                self.__listLadrillos.append(Ladrillo(id, cantidad, kgMat, costo))
        archi.close()
    def añadirMaterial(self, xid, xmat, gm: GestorMateriales):
        for ladrillo in self.__listLadrillos:
            if ladrillo.getId() == xid:
                pos = gm.buscarMaterial(xmat)
                if pos > 0:
                    ladrillo.addMaterial(gm.getMaterialPorPosicion(pos))
                    ladrillo.actualizarCosto()
    def buscarLote(self, xid):
        ret = 0
        i = 0
        while i < len(self.__listLadrillos) and self.__listLadrillos[i].getId() != xid:
            i += 1
            if i == len(self.__listLadrillos):
                ret = -1
            else:
                ret = i
        return ret
    def detalleMateriales(self, pos):
        self.__listLadrillos[pos].listarMateriales()
    def mostrarCostos(self):
        for lad in self.__listLadrillos:
            print(f"Lote: {lad.getId()} - Costo Total: {lad.getCostoTotal()}")

    
    def mostrarDetalleLadrillos(self, gm: GestorMateriales):
        print("{:<20} {:<20} {:<20}".format("N° ladrillo", "Material", "Costo asociado del material"))
        for lad in self.__listLadrillos:
            id = lad.getId()
            mat = lad.getMateriales()
            if mat != "":
                costo = lad.getCostosAdicionales()
                print("{:<20} {:<20} {:<20}".format(id, mat, costo))

    
    
    
