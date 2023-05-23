import random
from clear import limpiar_consola

datos_tarjetas = {}
datos_usuario = {}

def registro(repositorio):
    print("Registrar usuario"); print("")
    nombre = input("Ingrese primer nombre y primer apellido: ")
    cedula = int(input("Ingrese numero de cedula: "))
    direccion = input("Ingrese su dirección: ")
    codigo = random.randint(100000,999999)
    datos_tarjetas["nombre"] = nombre
    datos_tarjetas["cedula"] = cedula
    datos_tarjetas["direccion"] = direccion
    repositorio[nombre] = [cedula,direccion,{"tarjeta 1" : [codigo, "activa", 0]}]
    limpiar_consola()
    print("Se ha creado una tarjeta de regalo")
    print(f"Codigo de la tarjeta: {codigo}"); print("")
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
    print(f"Cedula: {cedula}")
    print(f"Dirección: {direccion}"); print("")
    print("Tarjeta 1"); print("")
    print(f"Código: {codigo}")
    print("Saldo: 0")
    print(repositorio[nombre][2]["tarjeta 1"][1]); print("")
    input("Pulsa enter para continuar")
    return
