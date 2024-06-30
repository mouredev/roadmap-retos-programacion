# Autor: Héctor Adán 
# GitHub: https://github.com/hectorio23 

import random
import sys

# Función que implementa el juego de adivinanzas
def mini_game():
    # Inicializar la semilla del generador de números aleatorios
    random.seed()

    print("Bienvenido al juego de adivinanzas!")
    print("Estoy pensando en un número entre 1 y 100. Adivina cuál es!")

    # Generar número aleatorio entre 1 y 100
    numero_aleatorio = random.randint(1, 100)
    intentos = 0
    intento_usuario = 0

    while intento_usuario != numero_aleatorio:
        try:
            intento_usuario = int(input("Ingresa tu intento: "))
            assert 1 <= intento_usuario <= 100, "El número debe estar entre 1 y 100"
            intentos += 1

            if intento_usuario < numero_aleatorio:
                print("El número que estoy pensando es mayor.")
            elif intento_usuario > numero_aleatorio:
                print("El número que estoy pensando es menor.")
            else:
                print(f"¡Felicidades! Has adivinado el número en {intentos} intentos.")

        except ValueError:
            print("Debes ingresar un número válido.")
        except AssertionError as e:
            print(e)

    continuar = input("¿Quieres jugar de nuevo? (s/n): ").lower()
    if continuar == 's':
        mini_game()
    else:
        print("Gracias por jugar. ¡Hasta luego!")

if __name__ == "__main__":
    # Ejemplos de aserciones en Python
    assert 2 + 2 == 4
    print("Checkpoint #1")

    assert 2 * 2 == 4, "Mensaje personalizado de aserción"
    print("Checkpoint #2")

    assert 0o10 + 0o10 == 16, "Otra forma de agregar un mensaje de aserción"
    print("Checkpoint #3")

    assert (2 + 2) % 3 == 1, "Success"
    print("Checkpoint #4")

    # Llamada a la función que implementa el juego de adivinanzas
    mini_game()

    assert (2 + 2) == 5, "Failed"
    print("La ejecución continúa después de la última aserción")

    sys.exit(0)  # Indicar que el programa finalizó correctamente
