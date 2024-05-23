class Matricula:
    __fecha: str
    __empleado: object
    __programa: object
    def __init__(self, fecha, empleado, programa):
        self.__fecha = fecha
        self.__empleado = empleado
        self.__programa = programa