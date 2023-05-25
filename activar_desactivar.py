from clear import limpiar_consola

def activar_desactivar(repositorio):
    print("Activar/Desactivar tarjeta"); print("")
    nombre = input("Escriba su nombre: ")
    limpiar_consola()
    tarjetas = list(repositorio[nombre][2].keys)
    for i in range (len(tarjetas)):
        print(tarjetas[i])
    opcion = input("Escriba su tarjeta: ")
    limpiar_consola()
    for i in range (len(tarjetas)):
        if opcion == tarjetas[i]:
            codigo = int(input("Escriba el codigo de su tarjeta: "))
            limpiar_consola()
            if codigo  == repositorio[nombre][2][tarjetas[i]][0]:
                if repositorio[nombre][2][tarjetas[i]][1] == "activa":
                    print("Su tarjeta está activa")
                    print("Desea desactivarla?"); print("")
                    print("1. Si")
                    print("2. No"); print("")
                    opcion = int(input("Escriba un numero para continuar: "))
                    if opcion == 1:
                        repositorio[nombre][2][tarjetas[i]][1] = "no activa"
                    else:
                        pass
                else:
                    print("Su tarjeta no está activa")
                    print("Desea activarla?"); print("")
                    print("1. Si")
                    print("2. No"); print("")
                    opcion = int(input("Escriba un numero para continuar: "))
                    if opcion == 1:
                        repositorio[nombre][2][tarjetas[i]][1] = "activa"
                    else:
                        pass
                print("------------------- Estado de tarjeta modificado con exito -------------------"); print("")
                input("Pulsa enter para continuar")
            else:
                print("Error, intentalo de nuevo")
                input("Pulse enter para continuar")
                activar_desactivar(repositorio)
        else:
            print("Error, intentalo de nuevo")
            input("Pulse enter para continuar")
            activar_desactivar(repositorio)
    return