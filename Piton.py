def limpiar_pantalla():
    from os import system
    system("cls")

def validar_cant_artist():
    while True:
        try:
            cant_artist = int(input("Ingrese la cantidad de artistas que se presentarán en la Pampilla... "))
            limpiar_pantalla()
            if cant_artist <= 0:
                print("La cantidad de artistas debe ser un número entero positivo.")
                print("")
            else:
                return cant_artist
        except ValueError:
            limpiar_pantalla()
            print("Tiene que ingresar un número entero.")
            print("")

def validar_nombre(i):
    nom_artista = input(f"Ingrese el nombre del artista {i + 1}... ")
    print("")
    apellido_artista = input(f"Ingrese el apellido del artista {i + 1}... ")
    limpiar_pantalla()
    nomcompleto_artista = nom_artista + " " + apellido_artista
    return nomcompleto_artista

def validar_sueldo(i):
    while True:
        try:
            sueldo_artista = int(input(f"Ingrese el sueldo del artista {i + 1}... "))
            limpiar_pantalla()
            if sueldo_artista < 1000000 or sueldo_artista > 17000000:
                print("El sueldo ingresado no está dentro del rango requerido")
                print("$1.000.000 min y $17.000.000 max")
            else:
                return sueldo_artista
        except ValueError:
            limpiar_pantalla()
            print("Tiene que ingresar números enteros")
            print("")

def validar_dia(i):
    while True:
        try:
            dia_artista = int(input(f"Ingrese el día al que se presentará el artista {i + 1} (17-20)... "))
            limpiar_pantalla()
            if dia_artista < 17 or dia_artista > 20:
                print("Los días disponibles son el 17-18-19-20 de Septiembre")
                print("")
            else:
                return dia_artista
        except ValueError:
            limpiar_pantalla()
            print("Tiene que ingresar números enteros")
            print("")


def control_presupuesto(a, b):
    pres_actual = 0
    pres_actual = a - b
    return pres_actual


def calcular_prom(total_sueldo, cant_artist):
    return total_sueldo / cant_artist if cant_artist > 0 else 0

pres = 1700000
max_sueldo = 0
total_sueldo = 0
max_sueldo_nom = ""

limpiar_pantalla()

print("Bienvenido al registro de la Pampilla de Coquimbo")
print("")
cant_artist = validar_cant_artist()
limpiar_pantalla()

for i in range(cant_artist):
    nomcompleto_artista = validar_nombre(i)
    apodo_artista = input(f"Ingrese el apodo del artista {i + 1}... ")
    limpiar_pantalla()
    print(f"Presupuesto actual: $ {pres}")
    print("")
    sueldo_artista = validar_sueldo(i)
    dia_artista = validar_dia(i)
    p = control_presupuesto(pres,sueldo_artista)
    pres = p

    total_sueldo += sueldo_artista

    if sueldo_artista > max_sueldo:
        max_sueldo = sueldo_artista
        max_sueldo_nom = nomcompleto_artista

    print(f"""Artista {i + 1}
    Nombre Completo: {nomcompleto_artista}
    Apodo: {apodo_artista}
    Fecha: {dia_artista} de Septiembre
    Sueldo: {sueldo_artista}
    """)
    input("Presione ENTER para continuar...")
    limpiar_pantalla()

prom_sueldo = calcular_prom(total_sueldo, cant_artist)

print(f"El promedio de sueldos en la Pampilla de Coquimbo es de $ {prom_sueldo:.2f} pesos.")
print(f"El artista más pagado es {max_sueldo_nom} con un sueldo de $ {max_sueldo} pesos.")