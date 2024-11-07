# Programa Votaciones
# Crear un programa para una eleccion presidencial
# Tiene 2 candidatos (candidato AZUL, candidato ROJO)
# Se ingresan votantes hasta ingresar el nombre X

# Para cada votante se debe ingresar:
# NOMBRE 
# APELLIDO
# SEXO (validar sexo)
# EDAD (Validar edad mayor 18 años)
# CIUDAD DE SEDE DE VOTACIÓN
# LUGAR (COLEGIO O ESTADIO)

# Indicar quén ganó las elecciones
# y fue elegido presidente

# Calcular los votos obtenidos por AZUL
# Calcular los votos obtenidos por ROJO

import os

def limpiar_pantalla():
    os.system('cls')

def val_edad():
    while True:
        try:
            edad = int(input("Ingrese edad del trabajador (500.000-2.000.000): "))
            if 18 < edad < 120:
                return edad
            else:
                print("Ingrese edad mayor a 18 años")
        except ValueError:
            print("Ingrese edad en números enteros.")


def val_gen():
    genes_validas = {'masculino', 'femenino', 'no binario'}
    while True:
        gen = input("Introduce tu género (Masculino/Femenino/No Binario): ").lower()
        if gen in genes_validas:
            print(f"Género {gen} validado correctamente.")
            return gen
        else: 
            print("Opción no válida, ingrese otra vez.")


def val_voto():
    votos_validas = {'alan', 'sebastian', 'blanco', 'nulo'}
    while True:
        voto = input("Introduce tu voto (Alan/Seba/Blanco/Nulo): ").lower()
        if voto in votos_validas:
            print(f"Voto {voto} validado correctamente.")
            return voto
        else: 
            print("Voto no válido, ingrese otra vez.")


print("Bienvenido a elecciones presidenciales")
print("")
print("CANDIDATO 1: ALAN ")
print("CANDIDATO 2: SEBA ")

print("")

while True:
    nombre = input("Ingrese nombre del votante: ")
    if nombre != "x":
        break
    apellido = input("Ingrese apellido del candidato: ")
    print("")
    edad = val_edad()
    print("")
    genero = val_gen 
    print("")
    ciudad = input("Ingrese ciudad donde votara: ")
    print("")
    sede = input("Ingrese sede de votacion (colegio/estadio)")
    print("")
    voto = val_voto()
    print("")

    if(voto=='alan'):
        cont_rojo += 1
    elif(voto=='seba')
        cont_azul += 1
    elif(voto=='blanco')
        cont_blanco += 1
    else
        cont_nulo =+ 1

    



    nombre = input("Ingrese nombre del votante: ")
    print("")