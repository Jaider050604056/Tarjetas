import csv 
def activar_desactivar():
    encab=['nombre', 'direccion', 'codigo', 'saldo', 'estado']
    with open("compra.txt","r",encoding="UTF-8")as f:
      leer=csv.reader= csv.DictReader(f,delimiter=',')
      print("===========================================================================")
      print(encab)
      print("===========================================================================")
      for i in leer:
        a=({i['nombre']},{i['direccion']},{i['codigo']},{i['saldo']},{i['estado']})
        print(a)
        print("=========================================================================")
    print("quiere (1)--activar o (2)--desactivar?")
    ops=(input("-->"))
    



        

    return

activar_desactivar()