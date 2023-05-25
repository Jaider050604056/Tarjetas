from clear import limpiar_consola

def activar_desactivar(repositorio):
    print("Activar/Desactivar tarjeta"); print("")
    nombre = input("Escriba su nombre: ")
    tarjetas = list(repositorio[nombre][2].keys)
    for i in range (len(tarjetas)):
        print(tarjetas[i])
    opcion = input("Escriba su tarjeta: ")
    for l in range (len(tarjetas)):
        if opcion == tarjetas
    codigo = int(input("Escriba el codigo de su tarjeta: "))
    if codigo  == repositorio[nombre][2]["tarjeta 1"][0]:
        pass
    else:
        pass


    print("Desea activarla?"); print("")
    print("1. Activar")
    print("2. Desactivar"); print("")
    opcion = int(input("Escriba un numero para continuar: "))
    limpiar_consola()
    if opcion == 1:
        pass
    elif opcion == 2:
        repositorio[nombre][2]["tarjeta 1"][1] = "no activa"
    else:
        pass
    print("------------------- Usuario registrado con exito -------------------"); print("")
    print(f"Nombre: {nombre}")
    print("Cedula: {}")
    print("Dirección: {}"); print("")
    print("Tarjeta 1"); print("")
    print(f"Código: {codigo}")
    print("Saldo: 0")
    print(repositorio[nombre][2]["tarjeta 1"][1]); print("")
    input("Pulsa enter para continuar")
    return