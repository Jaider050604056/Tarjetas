import os, csv
from clear import limpiar_consola
from registro import registro
from recargar import recargar
from comprar import comprar
from activar_desactivar import activar_desactivar
from reportes import reportes

def existencia():
    if os.path.isfile("datos usuarios.txt"):
        if os.path.isfile("datos tarjeta.txt"):
            return True
        else:
            return False
    else:
        return False

def crear_archivos():
    fieldnames_user=["nombre","cedula","direccion","tarjetas"]
    try:
        with open("datos usuarios.txt","w",encoding="UTF-8",newline="") as title:
            csv_write = csv.DictWriter(title, fieldnames=fieldnames_user, quotechar='"')
            csv_write.writeheader()
    except FileNotFoundError:
        return False
    fieldnames_card=["nombre","cedula","tarjeta","codigo","estado","saldo"]
    try:
        with open("datos tarjeta.txt","w",encoding="UTF-8",newline="") as title:
            csv_write = csv.DictWriter(title, fieldnames=fieldnames_card, quotechar='"')
            csv_write.writeheader()
    except FileNotFoundError:
        return False
    return

def menu():
    validar = existencia()
    if validar == False:
        crear_archivos()
    while True:
        print("1. Recargar tarjeta")
        print("2. Registrarse")
        print("3. Comprar nueva tarjeta")
        print("4. Activar/Desactivar tarjeta")
        print("5. Reportar tarjeta")
        print("6. Salir"); print("")
        opcion=int(input("Ingrese un numero para continuar: "))
        if opcion == 1:
            recargar()
            pass
        elif opcion == 2:
            registro()
            pass
        elif opcion == 3:
            compar()
            pass
        elif opcion == 4:
            activar_desactivar()
            pass
        elif opcion == 5:
            reportes()
            pass
        elif opcion == 6:
            exit()
        else:
            print("Error")
            continue
    return