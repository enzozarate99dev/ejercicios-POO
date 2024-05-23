class Transaccion:
    __cbu: int
    __num: int
    __importe: float
    __tipo: str
    def __init__(self, cbu, num, importe, tipo):
        self.__cbu = cbu
        self.__num = num
        self.__importe = importe
        self.__tipo = tipo
    def getCbu(self):
        return self.__cbu
    def getNum(self):
        return self.__num
    def getImporte(self):
        return self.__importe
    def getTipo(self):
        return self.__tipo
    def mostrar(self):
        print("{},{},{},{}".format(self.__num, self.__cbu, self.__importe, self.__tipo))
    