import csv

from classEdificio import Edificio


class GestorEdificio:
    __lista_edificios: list
    def __init__(self):
        self.__lista_edificios = []
    
    def cargarEdificios(self):
        archi = open("EdificioNorte.csv")
        reader = csv.reader(archi, delimiter=";")
        edif = None
        for fila in reader:
            if len(fila) == 6:
                id = int(fila[0])
                nomb = fila[1]
                dir = fila[2]
                empresa = fila[3]
                cantPisos = int(fila[4])
                edif = Edificio(id, nomb, dir, empresa, cantPisos)
                self.__lista_edificios.append(edif)
            else:
                idDepto = int(fila[1])
                nya = fila[2]
                nroPiso = int(fila[3])
                nroDpto = int(fila[4])
                canth = int(fila[5])
                cantb = int(fila[6])
                sup = float(fila[7])
                edif.cargarDepto(idDepto, nya, nroPiso, nroDpto, canth, cantb, sup)
        archi.close()
    
    def buscarEdificio(self, xnom):
        i = 0
        ret = 0
        while i < len(self.__lista_edificios) and self.__lista_edificios[i].getNombre() != xnom:
            i += 1
            if i == len(self.__lista_edificios):
                ret = -1
            else:
                ret = i
        return ret

    def mostrarInquilinosEdif(self, pos):
        self.__lista_edificios[pos].getInquilinos()
    def calcularSupEdificio(self, pos):
        return self.__lista_edificios[pos].calcSup()
    
    def mostrarSupProp(self,xnom):
        band = False
        for edif in self.__lista_edificios:
            if edif.existeProp(xnom):
                print(f"{xnom} tiene depto/s en el {edif.getNombre()}")
                supProp = edif.calcSupProp(xnom)
                print(f"La superficie total de su/s propiedad/es es de {supProp}m2")
                p = supProp * 100 / edif.calcSup()
                print(f"Ocupan un {p}% de la superficie total del edificio")
                band = True
        return band
            

    def mostrarCantSuits(self, xpiso):
        band = False
        for edif in self.__lista_edificios:
            if edif.existePiso(xpiso):
                c = edif.contarSuit(xpiso)
                print(f"El piso {xpiso} del {edif.getNombre()} tiene {c} suits")
                band = True
            else:
                band = False
        return band

              

        

        

