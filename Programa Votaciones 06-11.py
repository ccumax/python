# Programa Votaciones
# Cre4ar un programa para una eleccion presidencial
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

def validar_genero():
    print("1 >>> HOMBRE")
    print("2 >>> MUJER")
    print("")
    sexo = input("Introduce tu sexo (hombre o mujer)")
    if sexo != "1" or "2":
        print("Sexo mal ingresado, ingrese 1 o 2")


sexo1 = validar_genero()