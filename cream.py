#Realizar un programa que solucione lo siguiente:
#problematica VENTA DE FRUTAS Y VERDURAS
#Ingrese por teclado la cantidad de ventas a realizar

#cada venta debe registrar
#Nombre del vendedor
#Apellido del vendedor
#Nombre del cliente
#Apellido del cliente
#Cantidad que va a comprar el usuario (en kgs)
#fruta quue va a comprar el usuario
#Precio de la fruta o verdura (en pesos chilenos, por kilo)
#Con cuanto pago el cliente
#Funcion: calcular total a pagar 
#funcion: calcular vuelto
#funcion: calcular nombre completo
def val_pago():
    while True:
        pago=float(input("Ingrese limite de pago del cliente: "))
        limpiar_pantalla()
        try:
            if pago>0:
                return pago
            else:
                print("Ingrese pago valido")
        except ValueError:
            print("Ingrese cantidad en numeros enteros")        
def limpiar_pantalla():
    from os import system
    system("cls")

def calcular_vuelto(pago, total):
    if total<pago:
        result=pago-total    
        return result
    elif pago-total==0:
        result="0"
        return result
    else:
        print("Dinero insuficiente")
    
def calcular_nombre_completo(nombre, apellido):
    return f"{nombre} {apellido}"

limpiar_pantalla()

def ciclo_menu():
    print("*** Bienvenido a Supermercados Elver Galarga ***")
    print("")
    val_pago()
    carrito_de_compra = 0
    while True:
        print("""¿A que sección quiere ir? (Ingrese el numero de la seccion) \n
            1). Verduras y Frutas
            2). Lacteos
            3). Bebidas
            4). Higiene personal
            5). Salir""")
        
        print("")
        print(f"                         Carrito de compra actual: $ {carrito_de_compra}")
        print("")
        
        seccion = int(input(""))
        limpiar_pantalla()
        #Secciones 
        if seccion == 1:
            while True:
                print(f"""*** SECCION DE VERDURAS Y FRUTAS *** \n
                      Ingrese el numero de lo que desea agregar al carrito \n\n 
                      1). Papas (Kg)
                      2). Tomate (Kg)
                      3). Frutilla (Kg)
                      4). Uva (Kg)
                      5). Salir.
                      \n                         Carrito de compra: $ {carrito_de_compra}""")
                producto=int(input(""))
                if producto==1:
                    limpiar_pantalla()
                    
                    print(">>> Ingrese 0 para volver a la seccion 'Verduras y Frutas' <<<\n")

                    print("$ 1.000 x Kg")
                    cant=int(input("Ingrese cuantos Kg desea..."))
                    limpiar_pantalla()
                    if cant>0:
                        print(f"{cant} 'Papa(s)' ha sido añadida(s) al carrito")
                        multiplicacion = cant * 1000       
                        carrito_de_compra =+ multiplicacion   
                    else:
                        print("La cantidad no es válida, no se agregó ningún producto")
                        print("")
                        a = input("Presione ENTER para continuar...")
                        limpiar_pantalla()
                elif producto==2:
                    limpiar_pantalla()
                    
                    print(">>> Ingrese 0 para volver a la seccion 'Verduras y Frutas' <<<\n")
                    print("$ 1.000 x Kg")
                    cant=input("Ingrese cuantos Kg desea...")
                    limpiar_pantalla()
                    if cant>0:
                        print(f"{cant} 'Tomate' añadido(s) al carrito")
                        print("")
                        multiplicacion = cant * 1000 
                        carrito_de_compra =+ multiplicacion         
                    else:
                        print("La cantidad no es válida, por no se agregó ningún producto")
                        print("")
                        a = input("Presione ENTER para continuar...")       
                elif producto==3:
                    limpiar_pantalla("")
                    
                    print(">>> Ingrese 0 para volver a la seccion 'Verduras y Frutas' <<<\n")
                    print("$ 2.500 x Kg")
                    cant=input("Ingrese cuantos Kg desea...")
                    limpiar_pantalla()
                    if cant>0:
                        print(f"{cant} 'Frutilla' añadida(s) al carrito")
                        multiplicacion = cant * 2500    
                        carrito_de_compra =+ multiplicacion      
                    else:
                        print("La cantidad no es válida, no se agregó ningún producto")
                        print("")
                        a = input("Presione ENTER para continuar...")
                        limpiar_pantalla()     
                elif producto==4:
                    limpiar_pantalla("")
                    
                    print(">>> Ingrese 0 para volver a la seccion 'Verduras y Frutas' <<<\n")
                    print("$ 6.000 x Kg")
                    cant=input("Ingrese cuantos Kg desea...")
                    limpiar_pantalla()
                    if cant>0:
                        print("Uvas añadidas al carrito")
                        multiplicacion = cant * 6000 
                        carrito_de_compra =+ multiplicacion      
                    else:
                        print("La cantidad no es válida, no se agregó ningún producto")
                        print("")
                        a = input("Presione ENTER para continuar...")
                        limpiar_pantalla()
                elif producto==5:
                    break
                else:
                    print("Ingrese opcion valida")   
        elif seccion == 2:
            while True:
                print(f"""*** SECCION DE LACTEOS *** \n
                      Ingrese el numero de lo que desea agregar al carrito \n\n 
                      1). Leche Entera Colun 1L
                      2). Yogurt Batido Vainilla Soprole 165g
                      3). Yogurt Batido Frutilla Soprole 165g
                      4). Queso Gauda Soprole 15 Laminas
                      5). Salir.
                      \n                         Carrito de compra: $ {carrito_de_compra}""")
                producto=int(input(""))
                if producto==1:
                    limpiar_pantalla()
                    
                    print(">>> Ingrese 0 para volver a la seccion 'Lacteos' <<<\n")
                    print("$ 1.000 c/u")
                    cant=input("Ingrese cuanta cantidad desea...")
                    limpiar_pantalla()
                    if cant>0:
                        print(f"{cant} 'Leche Entera Colun 1L' ha sido añadido(s) al carrito")
                        print()
                        multiplicacion = cant * 1000
                        carrito_de_compra =+ multiplicacion   
                    else:
                        print("La cantidad no es válida, no se agregó ningún producto")
                        print("")
                        a = input("Presione ENTER para continuar...")
                elif producto==2:
                    limpiar_pantalla("")
                    
                    print(">>> Ingrese 0 para volver a la seccion 'Lacteos' <<<\n")
                    print("$ 490 c/u")
                    cant=input("Ingrese cuantos Kg desea...")
                    limpiar_pantalla()
                    if cant>0:
                        print(f"{cant} 'Yogurt Batido Vainilla 165g' añadido(s) al carrito")
                        multiplicacion = cant * 1000 
                        carrito_de_compra =+ multiplicacion         
                    else:
                        print("La cantidad no es válida, no se agregó ningún producto")
                        print("")
                        a = input("Presione ENTER para continuar...")       
                elif producto==3:
                    limpiar_pantalla("")
                    
                    print(">>> Ingrese 0 para volver a la seccion 'Lacteos' <<<\n")
                    print("$ 490 c/u")
                    cant=input("Ingrese cuantos Kg desea...")
                    limpiar_pantalla()
                    if cant>0:
                        print("frutillas añadidas al carrito")
                        multiplicacion = cant * 490    
                        carrito_de_compra =+ multiplicacion      
                    else:
                        print("La cantidad no es válida, no se agregó ningún producto")
                        print("")
                        a = input("Presione ENTER para continuar...")     
                elif producto==4:
                    limpiar_pantalla("")
                    
                    print(">>> Ingrese 0 para volver a la seccion 'Lacteos' <<<\n")
                    print("$ 2.890")
                    cant=input("Ingrese cuantos Kg desea...")
                    limpiar_pantalla()
                    if cant>0:
                        print("Uvas añadidas al carrito")
                        multiplicacion = cant * 2890 
                        carrito_de_compra =+ multiplicacion      
                    else:
                        print("La cantidad no es válida, no se agregó ningún producto")
                        print("")
                        a = input("Presione ENTER para continuar...")
                elif producto==5:
                    break
                else:
                    print("Ingrese opcion valida")   
        elif seccion == 3:
            while True:
                print(f"""*** SECCION DE VERDURAS Y FRUTAS *** \n
                      Ingrese el numero de lo que desea agregar al carrito \n\n 
                      1). Coca cola (2L)
                      2). Sprite (2L)
                      3). Monster (473ml)
                      4). Red Bull (250ml)
                      5). Salir.
                      \n                         Carrito de compra: $ {carrito_de_compra}""")
                producto=int(input(""))
                if producto==1:
                    limpiar_pantalla()
                    
                    print(">>> Ingrese 0 para volver a la seccion 'Verduras y Frutas' <<<\n")
                    print("$2.000 (c/u)")
                    cant=input("Ingrese la cantidad que desea...")
                    limpiar_pantalla()
                    if cant>0:
                        print(f"{cant} 'Coca Cola(s)' ha sido añadida(s) al carrito")
                        multiplicacion = cant * 2000       
                        carrito_de_compra =+ multiplicacion   
                    else:
                        print("La cantidad no es válida, no se agregó ningún producto")
                        print("")
                        a = input("Presione ENTER para continuar...")
                        limpiar_pantalla()
                elif producto==2:
                    limpiar_pantalla()
                    
                    print(">>> Ingrese 0 para volver a la seccion 'Verduras y Frutas' <<<\n")
                    print("$2.000 (c/u)")
                    cant=input("Ingrese la cantidad que desea...")
                    limpiar_pantalla()
                    if cant>0:
                        print(f"{cant} 'Sprite(s)' añadido(s) al carrito")
                        print("")
                        multiplicacion = cant * 2000 
                        carrito_de_compra =+ multiplicacion         
                    else:
                        print("La cantidad no es válida, por lno se agregó ningún producto")
                        print("")
                        a = input("Presione ENTER para continuar...")       
                elif producto==3:
                    limpiar_pantalla("")
                    
                    print(">>> Ingrese 0 para volver a la seccion 'Verduras y Frutas' <<<\n")
                    print("$1.800")
                    cant=input("Ingrese la cantidad que desea...")
                    limpiar_pantalla()
                    if cant>0:
                        print(f"{cant} 'Monster(s)' añadido(s) al carrito")
                        multiplicacion = cant * 1800    
                        carrito_de_compra =+ multiplicacion      
                    else:
                        print("La cantidad no es válida, no se agregó ningún producto")
                        print("")
                        a = input("Presione ENTER para continuar...")
                        limpiar_pantalla()     
                elif producto==4:
                    limpiar_pantalla("")
                    
                    print(">>> Ingrese 0 para volver a la seccion 'Verduras y Frutas' <<<\n")
                    print("1 Kg $1.600")
                    cant=input("Ingrese la cantidad que desea...")
                    limpiar_pantalla()
                    if cant>0:
                        print(f"{cant} 'Red Bull(s)' añadido(s) al carrito")
                        multiplicacion = cant * 1600 
                        carrito_de_compra =+ multiplicacion      
                    else:
                        print("La cantidad no es válida, no se agregó ningún producto")
                        print("")
                        a = input("Presione ENTER para continuar...")
                        limpiar_pantalla()
                elif producto==5:
                    break
                else:
                    print("Ingrese opcion valida")   
        elif seccion == 4:
            while True:
                print(f"""*** SECCION DE HIGIENE PERSONAL *** \n
                    Ingrese el numero de lo que desea agregar al carrito \n\n 
                    1). Toallas femeninas 'care up' 8 unidades
                    2). Paquete Confort 4 unidades
                    3). toallas humedas 'huggies' 48 unidades
                    4). Desodorante spray nivea man 150ml
                    5). Salir.
                    \n                         Carrito de compra: ${carrito_de_compra}""")
                producto=int(input(""))
                if producto==1:
                    limpiar_pantalla()
                    
                    print(">>> Ingrese 0 para volver a la seccion 'Verduras y Frutas' <<<\n")
                    print("$1.000 (c/u)")
                    cant=input("Ingrese la cantidad que desea...")
                    limpiar_pantalla()
                    if cant>0:
                        print(f"{cant} 'toallas femeninas' han sido añadidas al carrito")
                        multiplicacion = cant * 1000       
                        carrito_de_compra =+ multiplicacion   
                    else:
                        print("La cantidad no es válida, no se agregó ningún producto")
                        print("")
                        a = input("Presione ENTER para continuar...")
                        limpiar_pantalla()
                elif producto==2:
                    limpiar_pantalla()
                    
                    print(">>> Ingrese 0 para volver a la seccion 'Verduras y Frutas' <<<\n")
                    print("$1.000 (c/u)")
                    cant=input("Ingrese la cantidad que desea...")
                    limpiar_pantalla()
                    if cant>0:
                        print(f"{cant} Confort(s) añadido(s) al carrito")
                        print("")
                        multiplicacion = cant * 1000 
                        carrito_de_compra =+ multiplicacion         
                    else:
                        print("La cantidad no es válida, por lno se agregó ningún producto")
                        print("")
                        a = input("Presione ENTER para continuar...")       
                elif producto==3:
                    limpiar_pantalla("")
                    
                    print(">>> Ingrese 0 para volver a la seccion 'Verduras y Frutas' <<<\n")
                    print("$1.500 (c/u)")
                    cant=input("Ingrese la cantidad que desea...")
                    limpiar_pantalla()
                    if cant>0:
                        print(f"{cant} toallas humedas añadidas al carrito")
                        multiplicacion = cant * 1500    
                        carrito_de_compra =+ multiplicacion      
                    else:
                        print("La cantidad no es válida, no se agregó ningún producto")
                        print("")
                        a = input("Presione ENTER para continuar...")
                        limpiar_pantalla()     
                elif producto==4:
                    limpiar_pantalla("")
                    
                    print(">>> Ingrese 0 para volver a la seccion 'Verduras y Frutas' <<<\n")
                    print("$2.000 (c/u)")
                    cant=input("Ingrese la cantidad que desea...")
                    limpiar_pantalla()
                    if cant>0:
                        print(f" {cant} Desodorante(s) nivea man 150ml añadido(s) al carrito")
                        multiplicacion = cant * 2000
                        carrito_de_compra =+ multiplicacion      
                    else:
                        print("La cantidad no es válida, no se agregó ningún producto")
                        print("")
                        a = input("Presione ENTER para continuar...")
                        limpiar_pantalla()
                elif producto==5:
                    break
                else:
                    print("Ingrese opcion valida")   
        


productos=[]
ventas=[]

#datos:

v_name=input("Ingrese nombre del vendedor: ") 
limpiar_pantalla()
v_lastname=input("Ingrese apellido del vendedor: ") 
limpiar_pantalla()
client_name=input("Ingrese nombre del cliente: ") 
limpiar_pantalla()
client_lastname=input("Ingrese apellido del cliente: ") 
limpiar_pantalla()
pago=float(input("Ingrese limite de pago del cliente: "))
limpiar_pantalla()
pago=val_pago()
ciclo_menu()
limpiar_pantalla()
print("")

#mostrar datos

nombre_completo_cliente = calcular_nombre_completo(client_name, client_lastname)

print(f"Nombre del cliente: {nombre_completo_cliente}")
print(f"Total a pagar: {carrito_de_compra}")
