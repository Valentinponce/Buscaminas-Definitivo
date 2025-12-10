def abrir_automatico(real, visible, fila, columna, visitado):
    if (fila, columna) in visitado:
        return
    visitado.add((fila, columna))

    numero = contar_minas(real, fila, columna)
    visible[fila][columna] = NUM_EMOJI[numero]

    if numero == 0:
        filas = len(real)
        columnas = len(real[0])

        for f in range(fila - 1, fila + 2):
            for c in range(columna - 1, columna + 2):
                if 0 <= f < filas and 0 <= c < columnas:
                    if visible[f][c] == OCULTO:
                        abrir_automatico(real, visible, f, c, visitado)

# -------------------------------------------------------
def jugar(filas, columnas, minas):
    real = crear_tablero(filas, columnas)
    visible = crear_tablero(filas, columnas)

    colocar_minas(real, minas)

    casillas_sin_minas = filas * columnas - minas
    visitado = set()

    print("\n=== BUSCAMINAS EMOJI ===")
    mostrar(visible)

    while True:
        try:
            fila, columna = map(int, input("Elige casilla (fila columna): ").split())
        except:
            print("Ingresa coordenadas válidas.")
            continue

        if not (0 <= fila < filas and 0 <= columna < columnas):
            print("Coordenadas fuera del tablero.")
            continue

        if real[fila][columna] == "M":
            print("\n💥 ¡Pisaste una mina! 💥")

            for f in range(filas):
                for c in range(columnas):
                    if real[f][c] == "M":
                        visible[f][c] = MINA

            mostrar(visible)
            break


        abrir_automatico(real, visible, fila, columna, visitado)

        mostrar(visible)

        descubiertas = sum(1 for f in visible for c in f if c != OCULTO)

        if descubiertas >= casillas_sin_minas:
            print("🎉 ¡GANASTE! Todas las casillas seguras fueron descubiertas.")
            break

# -------------------------------------------------------
def menu():

    time.sleep(0.5)
    
    barras = [
        "[░░░░░░░░░]",
        "[█░░░░░░░░]",
        "[██░░░░░░░]",
        "[███░░░░░░]",
        "[████░░░░░]",
        "[█████░░░░]",
        "[██████░░░]",
        "[███████░░]",
        "[████████░]",
        "[█████████]"
    ]

    for barra in barras:
          sys.stdout.write("\r" + barra)
          sys.stdout.flush()
          time.sleep(0.25)

    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Fácil  (6x6, 5 minas)")
        print("2. Normal (8x8, 10 minas)")
        print("3. Difícil (10x10, 20 minas)")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            jugar(6, 6, 5)
        elif opcion == "2":
            jugar(8, 8, 10)
        elif opcion == "3":
            jugar(10, 10, 20)
        elif opcion == "4":
            print("Saliendo del juego...")
            break
        else:
            print("Opción inválida.")

menu()