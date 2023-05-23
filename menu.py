from clear import limpiar_consola
# from recargar import recargar
from registro import registro
# from comprar import comprar
# from activar_desactivar import activar_desactivar
# from reportes import reportes

def menu(repositorio):
    while True:
        print("1. Recargar tarjeta")
        print("2. Registrarse")
        print("3. Comprar nueva tarjeta")
        print("4. Activar/Desactivar tarjeta")
        print("5. Reportar tarjeta")
        print("6. Salir"); print("")
        opcion=int(input("Ingrese un numero para continuar: "))
        if opcion == 1:
            #recargar()
            pass
        elif opcion == 2:
            registro(repositorio)
            pass
        elif opcion == 3:
            #compar()
            pass
        elif opcion == 4:
            #activar_desactivar()
            pass
        elif opcion == 5:
            #reportes()
            pass
        elif opcion == 6:
            exit()
        else:
            print("Error")
            continue
    return