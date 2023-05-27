import random, csv, os
     
def comprar():
    datos={}
    ntarj=100
    while True:
        print("para comprar tarjeta ingrese los siguientes datos")
        while True:
            nom=input("nombre--->")
            datos['nombre'] = nom
            if nom.isnumeric():
                print("caracter invalido")
            else:
                ntarj=ntarj+1
                ident=random.randint(100000,999999)
                saldo=0
                act=input("quieres activarla?[si/no]")
                if act =="si":
                    estado="activa"
                elif act =="no":
                     estado="desactivada"
                
                datos["codigo"]=ident
                datos["saldo"]=saldo
                datos["estado"]= estado
                break
            

        print("=====================================================")
        print("====================TU TARJETA=======================")
        print("=====================================================")
        print("Número de tarjeta" , "Código" , "Estado" , "Saldo" , "Nombres completos")
        print("=====================================================")
        print(ntarj,"         ",ident,"       ",estado,"     ",saldo,"     ",nom)
        print("=====================================================")

                    
                        
        if not os.path.exists("estado_programa.txt"):
            fieldnames=["Número de tarjeta", "Código", "Estado", "Saldo", "Nombres completos"]
            with open("compra.txt", "w", encoding="UTF-8", newline="") as f:
                    csv_write = csv.DictWriter(f, fieldnames=fieldnames, quotechar='"')
                    csv_write.writeheader()
            
            with open("estado_programa.txt", "w") as estado:
             estado.write("Ejecutado")
                    
                        
            
        lista=["nombre","direccion","codigo","saldo","estado"]
        with open("compra.txt","a",encoding="UTF-8",newline="")as f:
                escribir=csv.DictWriter(f,fieldnames = lista,quotechar='"')
                escribir.writerow(datos)
        
        opc=input("deseas crear otra tarjeta [si/no]")
        if opc=="si":
             os.system("cls")
        elif opc == "no":
             break
