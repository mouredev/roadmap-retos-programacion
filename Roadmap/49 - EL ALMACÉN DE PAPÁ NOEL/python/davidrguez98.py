""" /*
 * EJERCICIO:
 * Papá Noel tiene que comenzar a repartir los regalos...
 * ¡Pero ha olvidado el código secreto de apertura del almacén!
 *
 * Crea un programa donde introducir códigos y obtener pistas.
 * 
 * Código:
 * - El código es una combinación de letras y números aleatorios
 *   de longitud 4. (Letras: de la A a la C, Números: del 1 al 3)
 * - No hay repetidos.
 * - Se genera de manera aleatoria al iniciar el programa.
 * 
 * Usuario:
 * - Dispone de 10 intentos para acertarlo.
 * - En cada turno deberá escribir un código de 4 caracteres, y 
 *   el programa le indicará para cada uno lo siguiente:
 *   - Correcto: Si el caracter está en la posición correcta.
 *   - Presente: Si el caracter existe, pero esa no es su posición.
 *   - Incorrecto: Si el caracter no existe en el código secreto.
 * - Deben controlarse errores de longitud y caracteres soportados.
 * 
 * Finalización:
 * - Papa Noel gana si descrifra el código antes de 10 intentos.
 * - Pierde si no lo logra, ya que no podría entregar los regalos.
 */ """

import random

letters = ["A", "B", "C"]
numbers = ["1", "2", "3"]
password_elements = letters + numbers

def generate_password() -> str:
    return "".join(random.sample(password_elements, 4))

secret_password = generate_password()
attemps = 1

while attemps <= 10:
    
    print(f"Intento {attemps}")

    password = input("Introduce la contraseña: ").upper()

    if len(password) != 4:
        print("La contraseña debe de tener 4 caracteres.")
        continue
    if not all(character in password_elements for character in password):
        print(f"Solo se permiten los caracteres {password_elements}")
        continue

    if password == secret_password:
        print("¡Contraseña correcta! Has descifrado el código del almacén.")
        break
    
    attemps += 1

    if attemps > 10:
        print("Los 10 intentos para descrifrar el código han finalizado.")
    else:
        for index, character in enumerate(password):
            if character == secret_password[index]:
                print(f"{character}: Correcto.")
            elif character in secret_password:
                print(f"{character}: Presente")
            else:
                print(f"{character}: Incorrecto")