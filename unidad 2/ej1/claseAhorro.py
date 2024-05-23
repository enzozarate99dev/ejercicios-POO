import io

class Caja_Ahorro:
    __nroCta: str
    __cuil: str
    __apellido: str
    __nombre: str
    __saldo: float

    def __init__(self, nroCta, cuil, apellido, nombre, saldo):
        self.__nroCta = nroCta
        self.__cuil = cuil
        self.__apellido = apellido
        self.__nombre = nombre
        self.__saldo = saldo

    def mostrarDatos(self):
        print("Apellido: ", self.__apellido)
        print("Nombre: ", self.__nombre)
        print("CUIL: ", self.__cuil)
        print("Numero de cuenta: ", self.__nroCta)
        print("Saldo: ", self.__saldo)

    def extraer(self, importe):
        importe = float(importe)
        if self.__saldo >= importe:
            self.__saldo -= importe
            print("Exitoso, nuevo saldo = ", self.__saldo)
            return 1
        else:
            print("Saldo insuficiente")
            return -1
    
    def depositar(self, importe):
        importe = float(importe)
        if importe > 0:
            self.__saldo += importe
        else:
            print("No puede ser negativo")
    
    def getCuil(self):
        return self.__cuil

    def validar(self):
        if len(self.__cuil) != 11:
            print("El CUIL debe tener 11 digitos")
            return False
        
        xy = self.__cuil[:2]
        suma = 0
        multip = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]

        for i in range(10):
            suma += int(self.__cuil[i]) * multip[i]
        
        cociente = suma // 11
        resto = suma - (cociente * 11)

        if resto == 0:
            z = 0
        elif resto == 1: 
            if xy == "20":
                z = 9
            elif  xy == "27":
                z = 4
        else:
            z = 11 - resto
        
        if z == int(self.getCuil()[-1]):
            return True
        else:
            return False
        

def test():
    cajas = []
    for i in range(2):
        while True:
            try:

                nroCta = int(input("Ingrese el Nro de cuenta: "))
                cuil = input("Ingrese el CUIL: ")
                apellido = input("Ingrese el apellido: ")
                nombre = input("Ingrese el nombre: ")
                saldo = 0
                c = Caja_Ahorro(nroCta, cuil, apellido, nombre, saldo)

                if c.validar():
                    cajas.append(c)
                    break
                else:
                    print("El CUIL/CUIT ingresado no es valido. Intentelo de nuevo")
            except ValueError:
                print("Error. Ingrese de nuevo  los datos")
    
    while True:
        flag = False
        cuilIngreso = input("Ingrese el cuil para acceder a la cuenta: ")
        for c in cajas:
            if c.getCuil() == cuilIngreso and flag == False:
                while True:
                    print("\033[;36m"+"\n1. Depositar")
                    print("\033[;36m"+"2. Extraer")
                    print("\033[;36m"+"3. Mostrar")
                    print("\033[;36m"+"4. Salir")
                    opcion = int(input("Ingrese una opcion: "))

                    if opcion == 1:
                        imp = input("Ingrese el deposito: ")
                        c.depositar(imp)
                    elif opcion == 2:
                        imp = input("Ingrese la extraccion: ")
                        c.extraer(imp)
                    elif opcion ==3:
                        c.mostrarDatos()
                    elif opcion == 4:
                        print("Saliendo de la app...")
                        flag = True
                        break

        if flag: break
        else: print("El Cuil/Cuit ingresado no esta en el sistema. Por favor, intentelo nuevamente")