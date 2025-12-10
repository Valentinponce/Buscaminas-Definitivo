import time
import sys
import random

# Emojis del tablero
OCULTO = "⬜"
VACIO = "⬛"
MINA = "💣"

# Números con emojis
NUM_EMOJI = {
    0: VACIO,
    1: "1️⃣",
    2: "2️⃣",
    3: "3️⃣",
    4: "4️⃣",
    5: "5️⃣",
    6: "6️⃣",
    7: "7️⃣",
    8: "8️⃣",
}

# -------------------------------------------------------
def crear_tablero(filas, columnas):
    return [[OCULTO for _ in range(columnas)] for _ in range(filas)]

# -------------------------------------------------------
def colocar_minas(tablero, minas):
    filas = len(tablero)
    columnas = len(tablero[0])
    colocadas = 0

    while colocadas < minas:
        f = random.randint(0, filas - 1)
        c = random.randint(0, columnas - 1)
        if tablero[f][c] != "M":
            tablero[f][c] = "M"
            colocadas += 1

# -------------------------------------------------------
def contar_minas(tablero, fila, columna):
    filas = len(tablero)
    columnas = len(tablero[0])
    contador = 0

    for f in range(fila - 1, fila + 2):
        for c in range(columna - 1, columna + 2):
            if 0 <= f < filas and 0 <= c < columnas:
                if tablero[f][c] == "M":
                    contador += 1
    return contador

# -------------------------------------------------------
def mostrar(tablero):
    columnas = len(tablero[0])
    print("\n   " + " ".join(str(i) for i in range(columnas)))
    print("  " + "---" * columnas)
    
    for i, fila in enumerate(tablero):
        print(i, "|", " ".join(fila))
    print()
