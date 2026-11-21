def crearTablero(filas, columnas):
    tablero = []
    for i in range(2 * filas - 1):
        fila = []
        for j in range(2 * columnas - 1):
            # Solo las posiciones (par, par) son puntos
            if i % 2 == 0 and j % 2 == 0:
                fila.append('+')
            else:
                fila.append(' ')
        tablero.append(fila)
    return tablero


def imprimirTablero(tablero):
    columnas = (len(tablero[0]) + 1) // 2
    print()
    print("    " + "".join(str(k + 1).ljust(4) for k in range(columnas)).rstrip())
    for i in range(len(tablero)):
        fila = tablero[i]
        if i % 2 == 0:
            etiqueta = str(i // 2 + 1).ljust(4)
        else:
            etiqueta = "    "
        print((etiqueta + " ".join(fila)).rstrip())
    print()

def mostrarMenu():
    print()
    print("Menu")
    print("1. Tablero de 4 x 4")
    print("2. Tablero de 6 x 8")
    print("3. Tablero de 10 x 10")
    print("4. Fin")


def pedirOpcion():
    while True:
        mostrarMenu()
        texto = input("Ingrese una opcion: ").strip()
        if texto.isdigit() and 1 <= int(texto) <= 4:
            return int(texto)
        print("Error: opcion no valida. Debe ingresar un numero del 1 al 4.")


def obtenerTamano(opcion):
    if opcion == 1:
        return 4, 4
    elif opcion == 2:
        return 6, 8
    else:
        return 10, 10


def convertirCoordenada(texto):
    texto = texto.replace(",", " ")
    partes = texto.split()
    if len(partes) != 2:
        return None
    if not (partes[0].isdigit() and partes[1].isdigit()):
        return None
    return int(partes[0]), int(partes[1])


def coordenadaValida(fila, columna, filas, columnas):
    return 1 <= fila <= filas and 1 <= columna <= columnas


def pedirCoordenada(mensaje, filas, columnas):
    while True:
        texto = input(mensaje)
        coord = convertirCoordenada(texto)
        if coord is None:
            print("Error: formato incorrecto. Ingrese fila y columna, por ejemplo: 7 3")
            continue
        fila, columna = coord
        if not coordenadaValida(fila, columna, filas, columnas):
            print("Error: coordenada fuera del tablero. Fila: 1-" + str(filas)
                  + ", Columna: 1-" + str(columnas))
            continue
        return fila, columna


def pedirJugada(filas, columnas):
    f1, c1 = pedirCoordenada("Ingrese origen: ", filas, columnas)
    f2, c2 = pedirCoordenada("Ingrese destino: ", filas, columnas)
    return f1, c1, f2, c2

def posicionLinea(f1, c1, f2, c2):
    if f1 == f2 and abs(c1 - c2) == 1:
        i = 2 * (f1 - 1)
        j = 2 * (min(c1, c2) - 1) + 1
        return i, j, '-'
    if c1 == c2 and abs(f1 - f2) == 1:
        i = 2 * (min(f1, f2) - 1) + 1
        j = 2 * (c1 - 1)
        return i, j, '|'
    return None


def validarLinea(tablero, f1, c1, f2, c2):
    filas = (len(tablero) + 1) // 2
    columnas = (len(tablero[0]) + 1) // 2
    if not coordenadaValida(f1, c1, filas, columnas):
        return False
    if not coordenadaValida(f2, c2, filas, columnas):
        return False
    posicion = posicionLinea(f1, c1, f2, c2)
    if posicion is None:
        return False
    i, j, simbolo = posicion
    if tablero[i][j] != ' ':
        return False

    return True


def colocarLinea(tablero, f1, c1, f2, c2):
    if not validarLinea(tablero, f1, c1, f2, c2):
        print("Movimiento invalido. Intente nuevamente.")
        return False
    i, j, simbolo = posicionLinea(f1, c1, f2, c2)
    tablero[i][j] = simbolo
    print("Linea colocada correctamente.")
    return True

def cerrarCajas(tablero, jugador):
    cerradas = 0
    for i in range(1, len(tablero), 2):
        for j in range(1, len(tablero[0]), 2):
            if tablero[i][j] == ' ':
                if (tablero[i - 1][j] != ' ' and tablero[i + 1][j] != ' '
                        and tablero[i][j - 1] != ' ' and tablero[i][j + 1] != ' '):
                    tablero[i][j] = jugador
                    cerradas += 1
    return cerradas


def cambiarJugador(jugador):
    if jugador == "A":
        return "B"
    return "A"


def procesarJugada(tablero, f1, c1, f2, c2, jugador, puntajes):
    if not colocarLinea(tablero, f1, c1, f2, c2):
        return jugador

    cajas = cerrarCajas(tablero, jugador)
    puntajes[jugador] += cajas

    if cajas == 0:
        jugador = cambiarJugador(jugador)
    else:
        print("Jugador " + jugador + " cerro " + str(cajas) + " caja(s) y juega otra vez.")

    return jugador


def juegoTerminado(tablero, puntajes):
    filas = (len(tablero) + 1) // 2
    columnas = (len(tablero[0]) + 1) // 2
    totalCajas = (filas - 1) * (columnas - 1)
    return puntajes["A"] + puntajes["B"] == totalCajas


def mostrarGanador(puntajes):
    print("Fin del juego")
    print("Puntaje final -> A: " + str(puntajes["A"]) + " | B: " + str(puntajes["B"]))
    if puntajes["A"] > puntajes["B"]:
        print("Gano el jugador A")
    elif puntajes["B"] > puntajes["A"]:
        print("Gano el jugador B")
    else:
        print("Empate")