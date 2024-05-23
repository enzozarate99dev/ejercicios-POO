from gestorCliente import GestorCliente
from gestorReparacion import GestorReparacion




if __name__ == "__main__":
    gc = GestorCliente()
    gr = GestorReparacion()
    gc.cargarClientes()
    gr.cargarRep()
    band = True
    while band:
        print("1. Informar datos de un cliente")
        print("2. Informar datos de un cliente terminado")
        print("3. Informar datos de cliente/s que le hace/n servicio a mas de un vehiculo")
        print("\n0. Salir")
        op= int(input("Ingrese una opcion: "))    

        if op == 1:
            dni=int(input("Ingrese el DNI: "))
            indice_cliente = gc.buscarCliente(dni)
            if indice_cliente == None:
                print("No se encontro el cliente ")
            else:
                cliente = gc.getCliente(indice_cliente)
                print("DNI: {}, Apellido y nombre: {} {},".format(dni, cliente.getApellido(), cliente.getNombre()))
                print("Patente: {}, Vehiculo: {},".format(cliente.getPatente(), cliente.getVehiculo()))
                xpat = cliente.getPatente()
                indices_rep = gr.buscarReparaciones(xpat)
                if not indices_rep:
                    print("No coinciden las patentes")
                else:
                    print("{:<20} {:<20} {:<20} {:<20}".format("Reparacion", "Precio Repuesto", "Mano de obra", "Subtotal"))
                    total = 0
                    for i in indices_rep:
                        reparacion = gr.getReparacionPorIndice(i)
                        subtotal = reparacion.calcularSubTotal()
                        total += subtotal
                        print("{:<20} {:<20} {:<20} {:<20}".format(reparacion.getReparacion(), reparacion.getPrecioR(), reparacion.getPrecioMO(), subtotal))
                    print("TOTAL A PAGAR: {:>20}".format(total))

        elif op == 2:
            pat = input("Ingrese la patente: ")
            indices_rep = gr.buscarReparaciones(pat)
            if not indices_rep:
                print("Patente no encontrada")
            else:
                count = 0
                for i in indices_rep:
                    reparacion = gr.getReparacionPorIndice(i)
                    if reparacion.getEstado() == "T":
                        count += 1
            
                        

            
        elif op == 0:
            print("SALIENDO...")
            band = False
    
    
