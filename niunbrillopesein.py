from os import system
system("cls")

def promedio (a,b,c):
    prom = (a + b + c)/ 3
    return prom

def limp_pantalla (a):
    from os import system 
    system("cls")
    return limp_pantalla

print("Bienvenido Septiembre....TIKI TIKI TI")
print("")
pausa = input("Presione ENTER para continuar...")

from os import system
system("cls")

# Alumno 1
print("*** REGISTRO ALUMNO 1 ***")
nombre1 = input("Ingrese nombre del alumno 1...")
from os import system
system("cls")

edad1 = int(input("Ingrese la edad del alumno 1..."))
from os import system
system("cls")
while ((edad1 < 5) or (edad1 > 20)):
    if (edad1 < 5):
        print("Edad no valida, debe ser mayor de 4 años...")
    if (edad1 > 20):
        print("Edad no valida, debe ser menor de 21 años...")
    print("")
    edad1 = int(input("Ingrese la edad del alumno 1..."))
    limpiar_pantalla = limp_pantalla

nota1 = float(input("Ingrese la nota del alumno 1..."))
from os import system
system("cls")
while ((nota1 < 1.0) or (nota1 > 7.0)):
    if (nota1 < 1.0):
        print("Nota no valida, debe ser mayor de un 1.0...")
    if (nota1 > 7.0):
        print("Nota no valida, debe ser menor o igual que 7.0...")
    print("")
    nota1 = float(input("Ingrese la nota del alumno 1..."))
    from os import system
    system("cls")

mesada1 = int(input("Ingrese cuanta recibe de mesada el alumno 1..."))
from os import system
system("cls")
while (mesada1 < 0):
    mesada1 = int(input("No puedes recibir una mesada negativa, ingresa otra..."))
    from os import system
    system("cls")


# Alumno 2
print("*** REGISTRO ALUMNO 2 ***")
nombre2 = input("Ingrese nombre del alumno 2...")
from os import system
system("cls")

edad2 = int(input("Ingrese la edad del alumno 2..."))
from os import system
system("cls")
while ((edad2 < 5) or (edad2 > 20)):
    if (edad2 < 5):
        print("Edad no valida, debe ser mayor de 4 años...")
    if (edad2 > 20):
        print("Edad no valida, debe ser menor de 21 años...")
    print("")
    edad2 = int(input("Ingrese la edad del alumno 2..."))
    from os import system
    system("cls")

nota2 = float(input("Ingrese la nota del alumno 2..."))
from os import system
system("cls")
while ((nota2 < 1.0) or (nota2 > 7.0)):
    if (nota2 < 1.0):
        print("Nota no valida, debe ser mayor de un 1.0...")
    if (nota2 > 7.0):
        print("Nota no valida, debe ser menor o igual que 7.0...")
    print("")
    nota2 = int(input("Ingrese la nota del alumno 2..."))
    from os import system
    system("cls")

mesada2 = int(input("Ingrese cuanta recibe de mesada el alumno 2..."))
from os import system
system("cls")
while (mesada2 < 0):
    mesada2 = int(input("No puedes recibir una mesada negativa, ingresa otra..."))
    from os import system
    system("cls")


# Alumno 3
print("*** REGISTRO ALUMNO 3 ***")
nombre3 = input("Ingrese nombre del alumno 3...")
from os import system
system("cls")
edad3 = int(input("Ingrese la edad del alumno 3..."))
from os import system
system("cls")
while ((edad3 < 5) or (edad3 > 20)):
    if (edad3 < 5):
        print("Edad no valida, debe ser mayor de 4 años...")
    if (edad3 > 21):
        print("Edad no valida, debe ser menor de 21 años...")
    print("")
    edad3 = int(input("Ingrese la edad del alumno 3..."))
    from os import system
    system("cls")

nota3 = float(input("Ingrese la nota del alumno 3..."))
from os import system
system("cls")
while ((nota3 < 1.0) or (nota3 > 7.0)):
    if (nota3 < 1.0):
        print("Nota no valida, debe ser mayor de un 1.0...")
    if (nota3 > 7.0):
        print("Nota no valida, debe ser menor o igual que 7.0...")
    print("")
    nota3 = int(input("Ingrese la nota del alumno 3..."))
    from os import system
    system("cls")

mesada3 = int(input("Ingrese cuanta recibe de mesada el alumno 3..."))
from os import system
system("cls")
while (mesada3 < 0):
    mesada3 = int(input("No puedes recibir una mesada negativa, ingresa otra..."))
    from os import system
    system("cls")


promedad = promedio(edad1,edad2,edad3)
promnota = promedio(nota1,nota2,nota3)
prommesada = promedio(mesada1,mesada2,mesada3)

print("El promedio de edades entre los 3 alumnos es",promedad)
print("El promedio de notas entre los 3 alumnos es",promnota)
print("El promedio de mesadas que reciben los 3 alumnos es",prommesada)
print("")