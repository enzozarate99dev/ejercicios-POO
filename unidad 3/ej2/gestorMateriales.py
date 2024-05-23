import csv

from classMaterial import Material


class GestorMateriales:
    __listMateriales: list
    def __init__(self):
        self.__listMateriales = []
    def cargarMateriales(self):
        archi = open("materiales.csv")
        reader = csv.reader(archi)
        band = False
        for fila in reader:
            if band == False: 
                band = True
            else:
                idmat = int(fila[0])
                car = fila[1]
                kg = float(fila[2])
                costoAd = float(fila[3])
                self.__listMateriales.append(Material(idmat, car, kg, costoAd))
        archi.close()
    def buscarMaterial(self, xid):
        ret = None
        i = 0
        while i < len(self.__listMateriales) and self.__listMateriales[i].getMaterial() != xid:
            i += 1
            if i == len(self.__listMateriales):
                ret = -1
            else:
                ret = i
        return ret
    def getMaterialPorPosicion(self, pos):
        return self.__listMateriales[pos]