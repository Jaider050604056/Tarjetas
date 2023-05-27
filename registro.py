import random, csv
from clear import limpiar_consola

def registro():
    datos_usuario = {}
    datos_tarjeta = {}
    print("Create Account"); print("")
    nombre=input("Escriba su nombre completo: ").lower()
    cedula=int(input("Escriba su numero de cedula: "))
    direccion=input("Escriba su dirección: ").lower()
    limpiar_consola()
    datos_usuario["nombre"] = nombre
    datos_usuario["cedula"] = cedula
    datos_usuario["direccion"] = direccion
    datos_usuario["tarjetas"] = "1 tarjeta(s)"
    datos_tarjeta["nombre"] = nombre
    datos_tarjeta["cedula"] = cedula
    datos_tarjeta["direccion"] = direccion
    datos_tarjeta["tarjeta"] = "tarjeta 1"
    def random_codigo(datos_tarjetas):
        with open("datos tarjeta.txt","r",encoding="UTF-8") as leer_codigo:
            reading = csv.reader = csv.DictReader(leer_codigo,delimiter=",")
            codigos = [row["codigo"] for row in reading]
            while True:
                codigo_generador = random.randint(1000,9999)
                if codigos != str(codigo_generador):
                    datos_tarjetas["codigo"] = codigo_generador
                    break
    random_codigo(datos_tarjeta)
    datos_tarjeta["estado"] = "activa"
    datos_tarjeta["saldo"] = 0
    print("Su tarjeta ha sido creada exitosamente"); print("")
    option=input("Dese activar su tarjeta? (si/no): ").lower(); limpiar_consola()
    if option == "si":
        pass
    elif option == "no":
        datos_tarjeta["estado"] = "no activa"
    else:
        print("Error, se tomará como un sí")
    print("")
    datos_usuario["nombre"] = nombre
    datos_usuario["cedula"] = cedula
    datos_usuario["direccion"] = direccion
    datos_usuario["tarjetas"] = "1 tarjeta"
    datos_tarjeta["nombre"] = nombre
    datos_tarjeta["cedula"] = cedula
    datos_tarjeta["tarjeta"] = "tarjeta 1"
    print("Nombre:",datos_usuario["nombre"])
    print("Cedula:",datos_usuario["cedula"])
    print("Direccion:",datos_usuario["direccion"])
    print("Numero de tarjetas: 1 tarjeta")
    print("Codigo:", datos_tarjeta["codigo"])
    print("Estado:",datos_tarjeta["estado"])
    print("Saldo: 0$"); print("")
    input("Press enter to continue")
    with open("datos usuarios.txt", "a", encoding="UTF-8", newline="") as agregar_usuario:
        fieldnames = datos_usuario.keys()
        writer = csv.DictWriter(agregar_usuario, fieldnames=fieldnames, quotechar='"')
        writer.writerow(datos_usuario)
    with open("datos tarjeta.txt", "a", encoding="UTF-8", newline="") as agregar_tarjeta:
        fieldnames2 = datos_tarjeta.keys()
        writer = csv.DictWriter(agregar_tarjeta, fieldnames=fieldnames2, quotechar='"')
        writer.writerow(datos_tarjeta)
    limpiar_consola()
    return
