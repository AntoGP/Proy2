# Grupo N: 8
# Integrantes:
# Antonio Garcia Palacios 2026PRECS01117
# Thiago Garrido RIvero 20261PREAD01035
# Adriano Mateo De Los Santos Díaz 20261PREAD01019
# Felipe Zapata Arias 20261PREAD01010
# Ralfh Alviery Pariona Reyes 2026PRECS01106
# Curso: CS6002 - Programacion I | Profesor: Maria Hilda Bermejos Rios
# Proyecto: Dot and Boxes

import Funciones

def jugarPartida(filas, columnas):
    tablero = Funciones.crearTablero(filas, columnas)
    puntajes = {"A": 0, "B": 0}
    jugador = "A"

    while not Funciones.juegoTerminado(tablero, puntajes):
        Funciones.imprimirTablero(tablero)
        print("Puntaje -> A: " + str(puntajes["A"]) + " | B: " + str(puntajes["B"]))
        print("Turno del jugador " + jugador)
        f1, c1, f2, c2 = Funciones.pedirJugada(filas, columnas)
        jugador = Funciones.procesarJugada(tablero, f1, c1, f2, c2, jugador, puntajes)

    Funciones.imprimirTablero(tablero)
    Funciones.mostrarGanador(puntajes)


opcion = Funciones.pedirOpcion()
while opcion != 4:
    filas, columnas = Funciones.obtenerTamano(opcion)
    jugarPartida(filas, columnas)
    opcion = Funciones.pedirOpcion()
print("Programa terminado.")
