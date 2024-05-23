class Departamento:
    __id: int
    __nya: str
    __nroPiso: int
    __nroDepto: int
    __cantHab: int
    __cantB: int
    __sup: float
    def __init__(self, idDepto, nya, nroPiso, nrodepto, canth, cantb, sup):
        self.__id = idDepto
        self.__nya = nya
        self.__nroPiso = nroPiso
        self.__nroDepto = nrodepto
        self.__cantHab = canth
        self.__cantB = cantb
        self.__sup = sup
    def getNyA(self):
        return self.__nya
    def getSup(self):
        return self.__sup
    def getNroPiso(self):
        return self.__nroPiso
    def getCantH(self):
        return self.__cantHab
    def getCantB(self):
        return self.__cantB
    