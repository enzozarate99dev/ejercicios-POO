class Cuenta:
    __apellido: str
    __nombre: str
    __dni: int
    __telefono: int
    __saldo: float
    __cbu: int
    # Variable de clase
    porcAnual=68

    def __init__(self, apellido, nombre, dni, telefono, saldo, cbu):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        self.__telefono = telefono
        self.__cbu = cbu
        self.__saldo = saldo
    
    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido
    
    def getDNI(self):
        return self.__dni
    
    def getTelefono(self):
        return self.__telefono
    
    def getCbu(self):
        return self.__cbu
    
    def getSaldo(self):
        return self.__saldo
    def setSaldo(self, monto):
        self.__saldo = self.__saldo + monto
    
    def mostrar(self):
        print("{}, {}, {}, {}, {}, {}".format(self.__apellido, self.__nombre, self.__dni, self.__telefono, self.__saldo, self.__cbu))
    
    @classmethod
    def getPorcAnual(cls):
        return cls.porcAnual
    
    @classmethod
    def setPorcAnual(cls, porc):
        cls.porcAnual = porc
    @classmethod
    def getPorcAnual(cls):
        return cls.porcAnual