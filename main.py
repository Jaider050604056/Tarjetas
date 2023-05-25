from menu import menu
from clear import limpiar_consola
limpiar_consola()

repositorio={"jaider sanchez" : [1065869921, "cra 31 a", {"tarjeta 1" : [123456, "activa", 10000], "tarjeta 2" : [654321, "activa", 20000]}]}

datos_recargas = {}
datos_tarjetas = {
                "nombre" : "jaider stiveen sanchez arciniegas",
                "cedula" : 1065869921,
                "tarjetas" : ["tarjeta 1", "tarjeta 2"],
                "codigos" : [123456,654321],
                "estado" : [True,True],
                "saldo": [0,0]
                }

datos_usuarios = {
                "nombre" : "jaider stiveen sanchez arciniegas",
                "cedula" : 1065869921,
                "direccion" : "cra 31a",
                "tarjetas" : ["2 tarjetas"],
                }


if __name__ == "__main__":
    menu(repositorio)