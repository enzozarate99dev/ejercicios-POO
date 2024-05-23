class Cliente:
    __dni: int
    __apellido: str
    __nombre: str
    __telefono: int
    __patente: str
    __vehiculo: str
    __estado: str
    def __init__(self, dni, apellido, nombre, telefono, patente, vehiculo, estado):
        self.__dni = dni
        self.__apellido = apellido
        self.__nombre = nombre
        self.__telefono = telefono
        self.__patente = patente
        self.__vehiculo = vehiculo
        self.__estado = estado
    
    def __str__(self):
        return "%s %s %s %s %s %s %s" % (self.__dni, self.__apellido, self.__nombre, self.__telefono, self.__patente, self.__vehiculo, self.__estado)
    def getDni(self):
        return self.__dni
    def getApellido(self):
        return self.__apellido
    def getNombre(self):
        return self.__nombre
    def getTelefono(self):
        return self.__telefono
    def getPatente(self):
        return self.__patente
    def getVehiculo(self):
        return self.__vehiculo
    def getEstado(self):
        return self.__estado
