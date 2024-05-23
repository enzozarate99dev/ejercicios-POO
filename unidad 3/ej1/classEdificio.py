# actua como un gestor de deptos
from classDepto import Departamento


class Edificio:
    __id: int
    __nombre: str
    __direccion: str
    __empresa: str
    __cantPisos: int
    __departamentos: list
    def __init__(self, id, nombre, dir, empresa, cantP):
        self.__id = id
        self.__nombre = nombre
        self.__direccion = dir
        self.__empresa = empresa
        self.__cantPisos = cantP
        self.__departamentos = []
    def cargarDepto(self, idDepto, nya, nroPiso, nroDpto, canth, cantb, sup):
        unDepto = Departamento(idDepto, nya, nroPiso, nroDpto, canth, cantb, sup)
        self.__departamentos.append(unDepto)
    def getId(self):
        return self.__id
    def getNombre(self):
        return self.__nombre
    def getInquilinos(self):
        for depa in self.__departamentos:
            print(depa.getNyA())
    def calcSup(self):
        supT = 0
        for depa in self.__departamentos:
            supT = supT + depa.getSup()
        return supT
    def existeProp(self, xnom):
        encontrado = False
        i = 0
        while i < len(self.__departamentos) and encontrado is False:
            if self.__departamentos[i].getNyA() == xnom:
                encontrado = True
            else:
                i += 1
        return encontrado
    def calcSupProp(self, xnom):
        s = 0
        for depa in self.__departamentos:
            if depa.getNyA() == xnom:
                s = s + depa.getSup()
        return s
    def existePiso(self, xp):
        encontrado = False
        i = 0
        while i < len(self.__departamentos) and encontrado is False:
            if self.__departamentos[i].getNroPiso() == xp:
                encontrado = True
            else:
                i += 1
        return encontrado
    def contarSuit(self, xp):
        cont = 0
        for depto in self.__departamentos:
            if depto.getNroPiso() == xp:
                if depto.getCantH() == 3 and depto.getCantB() > 1:
                    cont += 1
        return cont

    def getDeptos(self):
        return self.__departamentos
    # def mostrarInquilinos(self):
    #     for unDepto in self.__departamento:
    #         unDepto.getNyA()
    