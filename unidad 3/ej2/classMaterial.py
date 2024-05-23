class Material: 
    __idMat: int
    __caracteristicas: str
    __cantUsada: float
    __costoAdicional: float
    def __init__(self, idmat, caracteristicas, cantUsada, costoAdicional):
        self.__idMat = idmat
        self.__caracteristicas = caracteristicas
        self.__cantUsada = cantUsada
        self.__costoAdicional = costoAdicional
    def getMaterial(self):  
        return self.__idMat
    def getCantUsada(self):
        return self.__cantUsada
    def getCostoAdicional(self):
        return self.__costoAdicional
    def getCaracteristicas(self):
        return self.__caracteristicas