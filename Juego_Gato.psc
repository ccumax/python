Algoritmo Juego_Gato
	
	Definir jugador,posicion,movimiento Como Entero;
	

	
Dimensionar posicion[9],movimiento[9];
	
Escribir "*** Bienvenido al juego GATO ***";
Escribir "";
Escribir "";
Repetir
	Escribir "Ingrese que jugador va a partir";
	Escribir "";
	Escribir "1 >>> JUGADOR 1";
	Escribir "2 >>> JUGADOR 2";
	Escribir "";
	Leer Jugador;
Hasta Que Jugador==1 o jugador==2
Si jugador==1 Entonces
	Escribir "Ingrese la posición que va a jugar el jugador ",jugador;
	Escribir "";
	Escribir "De 1 a 9";
	Repetir
		Leer movimiento[1];
	Hasta Que movimiento[1]==1 o movimiento[1]==2 o movimiento[1]==3 o movimiento[1]==4 o movimiento[1]==5 o movimiento[1]==6 o movimiento[1]==7 o movimiento[1]==8 o movimiento[1]==9
SiNo
	Escribir "Ingrese la posición que va a jugar el jugador ",jugador;
	Escribir "";
	Escribir "De 1 a 9";
	Repetir
		Leer movimiento[1];
	Hasta Que movimiento[1]==1 o movimiento[1]==2 o movimiento[1]==3 o movimiento[1]==4 o movimiento[1]==5 o movimiento[1]==6 o movimiento[1]==7 o movimiento[1]==8 o movimiento[1]==9
FinSi
Si movimiento[1]== 1 Entonces
	
FinSi


FinAlgoritmo
