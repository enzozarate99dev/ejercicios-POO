class ProgramaCap:
    __nombre: str
    __cod: int
    __duracion: int
    __matriculas: list
    def __init__(self, nom, cod, duracion):
        self.__nombre = nom
        self.__cod = cod
        self.__duracion = duracion
        self.__matriculas = []