# *** TORNEO VIDEOJUEGOS ***

# Crear un programa en Python que de solución a la siguiente problematica:

# Ingresar 10 usuarios o participantes
# Cada usuario tiene:
# Nombre, nickname, edad, ranking, género, país y puntaje

# Nombre participante local
# Nombre participante visita
# Elegir videojuego
# (Rocket League, League of Legends o Valorant)
# Al ganador se le entrega 5 puntos
# Match hasta que un usuario llegue a los 30 ptos.

# Mostrar PODIUM del torneo (ranking, nickname y puntos)

def validar_edad():
    a




nickname = [0,0,0,0,0,0,0,0,0,0]
nombre = [0,0,0,0,0,0,0,0,0,0]
edad =  [0,0,0,0,0,0,0,0,0,0]
ranking = [0,0,0,0,0,0,0,0,0,0]
género = [0,0,0,0,0,0,0,0,0,0]
país = [0,0,0,0,0,0,0,0,0,0]
puntaje = [0,0,0,0,0,0,0,0,0,0]

print("Bienvenido al Torneo de Papulandia VideoGames")
print("")
for i in range(10):
    nombre[i]=input("Ingrese nickname del usuario")
    nickname[i]=input("Ingrese el nickname del usuario")
    edad[i]=input("Ingrese la edad del usuario")
    género[i]=input("Ingrese el género del usuario")
    país[i]=input("Ingrese el país del usuario")
    ranking[i]=input("Ingrese el ranking del usuario")
    puntaje[i]= 0