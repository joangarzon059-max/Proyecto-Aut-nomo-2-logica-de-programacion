import random

# Lista de palabras para el juego
palabras = [
    "python",
    "programacion",
    "ahorcado",
    "juego",
    "desarrollo",
    "uide",
    "profe",
    "lentes",
    "celular"
]

# Seleccionar una palabra aleatoria
palabra = random.choice(palabras)

# Guardar letras acertadas
letras_acertadas = []

# Número de intentos
intentos = 10


# Función para mostrar la palabra oculta
def mostrar_palabra():
    palabra_mostrada = ""

    for letra in palabra:
        if letra in letras_acertadas:
            palabra_mostrada += letra + " "
        else:
            palabra_mostrada += "_ "

    return palabra_mostrada.strip()


# Función para verificar si ganó
def verificar_ganador():
    for letra in palabra:
        if letra not in letras_acertadas:
            return False

    return True


# Inicio del juego
print("¡Bienvenido al juego del Ahorcado!")

while intentos > 0:

    print("\nPalabra:", mostrar_palabra())
    print("Intentos restantes:", intentos)

    entrada = input(
        "Ingresa una letra o la palabra completa: ").lower()

    # Si escribe la palabra completa
    if len(entrada) > 1:

        if entrada == palabra:

            # Agregar todas las letras a la lista
            for letra in palabra:
                if letra not in letras_acertadas:
                    letras_acertadas.append(letra)

            print("\nPalabra:", mostrar_palabra())
            print("\n¡Felicidades! Has ganado.")
            print("La palabra era:", palabra)
            break

        else:
            intentos -= 1
            print("¡Palabra incorrecta!")

    # Si escribe una sola letra
    else:

        letra = entrada

        if letra in letras_acertadas:
            print("Ya has acertado esa letra. Intenta con otra.")

        elif letra in palabra:
            letras_acertadas.append(letra)
            print("¡Correcto!")

            if verificar_ganador():
                print("\nPalabra:", mostrar_palabra())
                print("\n¡Felicidades! Has ganado.")
                print("La palabra era:", palabra)
                break

        else:
            intentos -= 1
            print("¡Incorrecto!")

# Si se quedó sin intentos
if intentos == 0:
    print("\n¡Has perdido!")
    print("La palabra era:", palabra)