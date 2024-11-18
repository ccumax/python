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

def calcular_total_a_pagar(cant, precio):
    return cant * precio

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


carrito_de_compra = 0

def ciclo_menu():
    print("*** Bienvenido a Supermercados Elver Galarga ***")
    print("")
    while True:
        print("""¿A que sección quiere ir? (Ingrese el numero de la seccion) \n
            1). Verduras y Frutas \n
            2). Lacteos \n
            3). Bebidas \n
            4). Higiene personal \n
            5). Salir""")
        
        print("")
        print(f"Carrito de compra actual: ${carrito_de_compra}")
        
        seccion = int(input(""))
        #Secciones 
        if seccion == 1:
            while True:
                print(f"*** SECCION DE VERDURAS Y FRUTAS *** \n\n Ingrese el numero de lo que desea agregar al carrito \n\n 1). Papas \n 2). Tomate $1.000 el kg \n 3). Frutilla \n4). Uva \n5). Salir.\n\n Carrito de compra: ${carrito_de_compra}")
                producto=int(input(""))
                if producto==1:
                    limpiar_pantalla("")
                    
                    print("Ingrese 0 para volver a la seccion 'Verduras\n'")
                    print("1 Kg $1.000")
                    cant=input("Ingrese cuantos Kg desea...")
                    limpiar_pantalla()
                    if cant>0:
                        print("Producto añadido al carrito")
                        multiplicacion = cant * 1000       
                        carrito_de_compra =+ multiplicacion   
                    else:
                        print("La cantidad no es válida, no se agregó ningún producto")
                        print("")
                        a = input("Presione ENTER para continuar...")
                elif producto==2:
                    limpiar_pantalla("")
                    
                    print("Ingrese 0 para volver a la seccion 'Verduras y frutas'")
                    print("1 Kg $1.000")
                    cant=input("Ingrese cuantos Kg desea...")
                    limpiar_pantalla()
                    if cant>0:
                        print("Producto añadido al carrito")
                        multiplicacion = cant * 1000 
                        carrito_de_compra =+ multiplicacion         
                    else:
                        print("La cantidad no es válida, no se agregó ningún producto")
                        print("")
                        a = input("Presione ENTER para continuar...")       
                elif producto==3:
                    limpiar_pantalla("")
                    
                    print("Ingrese 0 para volver a la seccion 'Verduras y frutas'")
                    print("1 Kg $2.500")
                    cant=input("Ingrese cuantos Kg desea...")
                    limpiar_pantalla()
                    if cant>0:
                        print("Producto añadido al carrito")
                        multiplicacion = cant * 1000    
                        carrito_de_compra =+ multiplicacion      
                    else:
                        print("La cantidad no es válida, no se agregó ningún producto")
                        print("")
                        a = input("Presione ENTER para continuar...")     
                elif producto==4:
                    limpiar_pantalla("")
                    
                    print("Ingrese 0 para volver a la seccion 'Verduras y frutas'")
                    print("1 Kg $6.000")
                    cant=input("Ingrese cuantos Kg desea...")
                    limpiar_pantalla()
                    if cant>0:
                        print("Producto añadido al carrito")
                        multiplicacion = cant * 1000 
                        carrito_de_compra =+ multiplicacion      
                    else:
                        print("La cantidad no es válida, no se agregó ningún producto")
                        print("")
                        a = input("Presione ENTER para continuar...")
        
        elif seccion==2:
            print("*** SECCIÓN DE LACTEOS *** \n\n Ingrese el numero de lo que desea agregar al carrito ")

        






productos=[]
ventas=[]

print("Bienvenido a distribuidora  x")
print("")

#datos:

n=int(input("Ingrese cuantas ventas realizara: "))
print("")



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

ciclo_menu()


venta = {
    "client_name": client_name,
    "client_lastname": client_lastname,
}
ventas.append(venta)
print("")

#mostrar datos :3
for i, venta in enumerate(ventas):
    nombre_completo_cliente = calcular_nombre_completo(venta["client_name"], venta["client_lastname"])
    
    print(f"Venta {i + 1}:")
    print(f"Nombre del vendedor: {nombre_completo_cliente}")
