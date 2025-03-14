import random  # Usaremos esta biblioteca para generar números aleatorios

jugador = {
    "saldo": 100,  # Monedas iniciales
    "apostado": 0,  # Total de monedas apostadas
    "ganado": 0,  # Total de monedas ganadas
    "ganadas": 0,  # Número de apuestas ganadas
    "perdidas": 0  # Número de apuestas perdidas
}

# Lista para guardar el historial de todas las apuestas
historial_apuestas = []

# Función para girar la ruleta
def girar_ruleta():
    numero = random.randint(1, 36)  # Número entre 1 y 36
    color = "rojo" if numero % 2 == 0 else "negro"  # Números pares son rojos, impares negros
    if numero <= 12:
        seccion = "1-12"
    elif numero <= 24:
        seccion = "13-24"
    else:
        seccion = "25-36"
    return numero, color, seccion

# Función para mostrar estadísticas básicas
def mostrar_estadisticas():
    print("\n--- Estadísticas ---")
    print("Saldo disponible:", jugador["saldo"])
    print("Total apostado:", jugador["apostado"])
    print("Total ganado:", jugador["ganado"])
    print("Apuestas ganadas:", jugador["ganadas"])
    print("Apuestas perdidas:", jugador["perdidas"])
    print("--------------------\n")

# Función para mostrar el historial de apuestas
def mostrar_historial():
    print("\n--- Historial de Apuestas ---")
    if len(historial_apuestas) == 0:
        print("Aún no has realizado ninguna apuesta.")
    else:
        for idx, apuesta in enumerate(historial_apuestas, start=1):
            print(f"{idx}. Tipo: {apuesta['tipo']}, Monto: {apuesta['monto']}, Resultado: {apuesta['resultado']}, Ganancia: {apuesta['ganancia']}")
    print("-----------------------------\n")

# Inicio del programa
print("¡Bienvenido al simulador de ruleta súper sencillo!")

while True:
    print("\nSaldo actual:", jugador["saldo"])
    print("1. Apostar a un número (gana 20 veces lo apostado)")
    print("2. Apostar a una sección (1-12, 13-24, 25-36, gana 5 veces lo apostado)")
    print("3. Apostar a un color (rojo o negro, duplica lo apostado)")
    print("4. Ver estadísticas")
    print("5. Ver historial de apuestas")
    print("6. Salir del juego")
    opcion = input("Elige una opción (1-6): ")

    if opcion == "1":  # Apuesta a un número
        numero_apuesta = int(input("Elige un número entre 1 y 36: "))
        monto = int(input("¿Cuánto deseas apostar?: "))
        if monto > jugador["saldo"]:
            print("No tienes suficiente saldo.")
            continue
        resultado = girar_ruleta()
        print("Resultado de la ruleta: Número", resultado[0], "y color", resultado[1])
        jugador["apostado"] += monto
        jugador["saldo"] -= monto
        if numero_apuesta == resultado[0]:
            ganancia = monto * 20
            jugador["ganado"] += ganancia
            jugador["saldo"] += ganancia
            jugador["ganadas"] += 1
            print("¡Ganaste!", ganancia, "coins")
        else:
            jugador["perdidas"] += 1
            print("Perdiste. ¡Suerte la próxima!")
        historial_apuestas.append({"tipo": "Número", "monto": monto, "resultado": f"{resultado[0]} ({resultado[1]})", "ganancia": ganancia if numero_apuesta == resultado[0] else 0})

    elif opcion == "2":  # Apuesta a una sección
        seccion_apuesta = input("Elige una sección (1-12, 13-24, 25-36): ")
        monto = int(input("¿Cuánto deseas apostar?: "))
        if monto > jugador["saldo"]:
            print("No tienes suficiente saldo.")
            continue
        resultado = girar_ruleta()
        print("Resultado de la ruleta: Número", resultado[0], "en la sección", resultado[2])
        jugador["apostado"] += monto
        jugador["saldo"] -= monto
        if seccion_apuesta == resultado[2]:
            ganancia = monto * 5
            jugador["ganado"] += ganancia
            jugador["saldo"] += ganancia
            jugador["ganadas"] += 1
            print("¡Ganaste!", ganancia, "coins")
        else:
            jugador["perdidas"] += 1
            print("Perdiste. ¡Suerte la próxima!")
        historial_apuestas.append({"tipo": "Sección", "monto": monto, "resultado": resultado[2], "ganancia": ganancia if seccion_apuesta == resultado[2] else 0})

    elif opcion == "3":  # Apuesta a un color
        color_apuesta = input("Elige un color (rojo/negro): ").lower()
        monto = int(input("¿Cuánto deseas apostar?: "))
        if monto > jugador["saldo"]:
            print("No tienes suficiente saldo.")
            continue
        resultado = girar_ruleta()
        print("Resultado de la ruleta: Color", resultado[1])
        jugador["apostado"] += monto
        jugador["saldo"] -= monto
        if color_apuesta == resultado[1]:
            ganancia = monto * 2
            jugador["ganado"] += ganancia
            jugador["saldo"] += ganancia
            jugador["ganadas"] += 1
            print("¡Ganaste!", ganancia, "coins")
        else:
            jugador["perdidas"] += 1
            print("Perdiste. ¡Suerte la próxima!")
        historial_apuestas.append({"tipo": "Color", "monto": monto, "resultado": resultado[1], "ganancia": ganancia if color_apuesta == resultado[1] else 0})

    elif opcion == "4":  # Ver estadísticas
        mostrar_estadisticas()

    elif opcion == "5":  # Ver historial
        mostrar_historial()

    elif opcion == "6":  # Salir del juego
        print("Gracias por jugar. ¡Hasta luego!")
        print(f"Fin del juego. Ganaste {jugador['ganadas']} veces y perdiste {jugador['perdidas']} veces.")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")

    # Fin del juego si el saldo llega a 0
    if jugador["saldo"] <= 0:
        print("Te quedaste sin saldo. Fin del juego.")
        print(f"Ganaste {jugador['ganadas']} veces y perdiste {jugador['perdidas']} veces.")
        break