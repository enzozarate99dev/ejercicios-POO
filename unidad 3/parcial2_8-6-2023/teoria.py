class Noticia:
    __fecha: str
    __autor: str
    __componenteN: object

    def __init__(self, fecha, autor, tit, cop, cue):
        self.__fecha = fecha
        self.__autor = autor
        self.__componenteN = ComponenteNoticia(tit, cop, cue)

    def __str__(self):
        return f"{self.__componenteN.getTitulo()}\n{self.__componenteN.getCopete()}\n{self.__componenteN.getCuerpo()}\n{self.__fecha}\n{self.__autor}\n"

class ComponenteNoticia:
    __titulo: str
    __copete: str
    __cuerpo: str

    def __init__(self, tit, cop, cue):
        self.__titulo = tit
        self.__copete = cop
        self.__cuerpo = cue

    def __str__(self):
        return f"{self.__titulo}\n{self.__copete}\n{self.__cuerpo}\n"

    def getTitulo(self):
        return self.__titulo

    def getCopete(self):
        return self.__copete

    def getCuerpo(self):
        return self.__cuerpo

def test():
    comp = ComponenteNoticia("Y ELLA", "asd", "asdasdasdasdasdasdasd")
    noti = Noticia("12/12/2020", "elvio lado", comp.getTitulo(), comp.getCopete(), comp.getCuerpo())
    print(noti)

test()
