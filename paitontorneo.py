def validar_edad():
    edad = 0
    while ((edad < 8)or (edad > 50))
        try:
            edad=int(input("Ingrese edad del alumno: "))
            if edad < 18:
                print("La edad es menor de lo esperada, debe ser mayor o igual a 18... Inténtelo de nuevo.")
            if edad > 50:
                print("La edad es mayor de lo esperada, debe ser menor o igual a 50... Inténtelo de nuevo.")
        except ValueError:
            print("Debe escribir la edad como número entero")
        print("")
    return edad

    def validar_genero():
        generos_validos = ['masculino', 'femenino', 'no binario']
        while true:
            genero = input("Introduce tu género (masculino, femenino, no binario): ").strip(),
            lower()

            if genero in generos validos:
                print(f"Género '{genero}' validado correctamente.")
                return genero
            else
                print("Opción no válida, Por favor, intente de nuevo.")

nickname = [0,0,0,0,0,0,0,0,0,0]
nombre = [0,0,0,0,0,0,0,0,0,0]
edad = [0,0,0,0,0,0,0,0,0,0]
pais = [0,0,0,0,0,0,0,0,0,0]
genero = [0,0,0,0,0,0,0,0,0,0]
puntaje = [0,0,0,0,0,0,0,0,0,0]
ranking = [0,0,0,0,0,0,0,0,0,0]
local = []
visita = []
cont_match = 0

print("BIenvenido a Torneo de Cracks Insuco")
print("")

for i in range(10):
    nickname[i]=input("Ingrese nickname del usuario: ")
    nombre[i]=input("Ingrese nombre del usuario: ")
    edad[i]=validar_edad()
    genero[i]=validar_genero()
    pais[i]=input("Ingrese país del usuario: ")
    puntaje[i]= 0

while (puntaje[i]<30):
    print("Nuevo MATCH")
    print("")

    print("MENU PARTICIPANTES")
    print(f"Presione 1 para {nickname[0]}")
    print(f"Presione 2 para {nickname[1]}")
    print(f"Presione 3 para {nickname[2]}")
    print(f"Presione 4 para {nickname[3]}")
    print(f"Presione 5 para {nickname[4]}")
    print(f"Presione 6 para {nickname[5]}")
    print(f"Presione 7 para {nickname[6]}")
    print(f"Presione 8 para {nickname[7]}")
    print(f"Presione 9 para {nickname[8]}")
    print(f"Presione 10 para {nickname[9]}")
    local.append(input("Seleccione posición del participante LOCAL"))
    print("")
