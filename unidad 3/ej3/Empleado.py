class Empleado:
    __nya: str
    __idEmp: int
    __puesto: str
    __matriculas: list
    def __init__(self, nya, id, puesto):
        self.__nya = nya
        self.__idEmp = id
        self.__puesto = puesto
        self.__matriculas = []