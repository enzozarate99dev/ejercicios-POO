import numpy as np

class gestorVentas:
    __cantDias: int
    __ventas: int
    __cantSuc: int

    def __init__(self):
        self.__cantDias = 7
        self.__cantSuc = 5
        self.__ventas = []

        for i in range(self.__cantSuc):
            self.__ventas.append([0] * self.__cantDias) #va "apilando" filas de 7 elementos

    
    def acumular(self, dia, suc, imp):
        self.__ventas[suc-1][dia-1] += imp

    
    def calcularTotalSuc(self, suc):
        total = sum(self.__ventas[suc - 1])
        return total
    
    def masFacturo(self, dia):
        max = 0
        sucMax = 0
        for i in range(self.__cantSuc):
            if self.__ventas[i][dia-1] > max:
                max = self.__ventas[i][dia-1]
                sucMax = i + 1
        return sucMax
    
    def calcularTotal(self):
        total = 0
        for i in range(self.__cantSuc):
            for j in range(self.__cantDias):
                total += self.__ventas[i][j]
        return total

def menu():
    venta = gestorVentas()
    while True:
        print("\n1. Cargar venta")
        print("\n2. Calcular el total de una sucursal")
        print("\n3. Obtener la sucursalr que mas facturo")
        print("\n4. Calcular Total de todas las sucursales")
        print("\n0. Salir")
        op= int(input("\nIngrese una opcion: "))
        if op == 1:
            dia = int(input("\nIngrese el dia: ")) 
            suc = int(input("\nIngrese el nro de la sucursal: "))
            imp = float(input("\nIngrese el importe de la venta: "))
            venta.acumular(dia, suc, imp)
        elif op == 2:
            s = int(input("\nIngrese una sucursal: "))
            print(f"El total de la semana para la sucursal {s} es: {venta.calcularTotalSuc(s)}")
            
        elif op == 3:
            d = int(input("\nIngrese una dia de la semana (1-7): "))
            print(f"La sucursal que mas facturo es: {venta.masFacturo(d)}")
            
        elif op == 4: 
            print(f"El total recaudado de la semana es: {venta.calcularTotal()}")
            
        elif op == 0:
            print("SALIENDO...")
            break

