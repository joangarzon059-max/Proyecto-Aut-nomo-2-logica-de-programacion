import random
#lista de palabras para el juego
palabras = ["python", "programacion", "ahorcado", "juego", "desarrollo","uide","profe","lentes","celular"]
#selecciona una palabra aleatoria de la lista
palabra = random.choice(palabras)
#guardar las letras acertadas
letras_acertadas = []
#numero de intentos
intentos = 10
#funcion para mostrar la palabra secreta
def mostrar_palabra():
    palabra_mostrada = ""
    for letra in palabra:
        if letra in letras_acertadas:
            palabra_mostrada += letra + " "
        else:
            palabra_mostrada += "_ "
    return palabra_mostrada.strip()
#funcion para validar si el jugador gano
def verificar_ganador():
    for letra in palabra:
        if letra not in letras_acertadas:
            return False
    return True
#Inicio del juego
print("¡Bienvenido al juego del Ahorcado!")
while intentos > 0:
    print("\nPalabra: " + mostrar_palabra())
    print("Intentos restantes: " + str(intentos))
    letra = input("Ingresa una letra: ").lower()
    if letra in letras_acertadas:
        print("Ya has acertado esa letra. Intenta con otra.")
    elif letra in palabra:
        letras_acertadas.append(letra)
        print("¡Correcto!")
        if verificar_ganador():
            print("\n¡Felicidades! Has ganado. La palabra era: " + palabra)
            break
    else:
        intentos -= 1
        print("¡Incorrecto!")
if intentos == 0:
    print("\n¡Has perdido! La palabra era: " + palabra)
    