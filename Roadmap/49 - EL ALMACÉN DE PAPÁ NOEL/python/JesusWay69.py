import os, platform, random, re

if (platform.platform().startswith("macOS") or platform.platform().startswith("Linux")):
    os.system('clear')
else:
    os.system('cls')

""" * EJERCICIO:
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
 * - Pierde si no lo logra, ya que no podría entregar los regalos."""

hidden_code = ["?","?","?","?"]
password = random.sample(("A", "B", "C", "1", "2", "3"), 4)
attempts = 10

print("Introduzca una clave de 4 caracteres que contenga A, B, C, 1, 2 0 3 sin repeticiones")

while attempts > 0:
    attempt = input("Introduzca la clave: ").upper()
    if re.match("[A-C1-3]{4}", attempt):
        for index, (item1, item2) in enumerate(zip(password, attempt)):
            if item1 == item2:
                print(f"El caracter '{item1}' está en la contraseña en su posición ")
                hidden_code[index] = password[index]
            elif item2 in password:
                print(f"El caracter '{item2}' está en la contraseña pero no lo has puesto en su posición")
            else:
                print(f"El caracter '{item2}' no está en la contraseña")
                
        print("Contraseña:", end=" ")
        [print("\b", char, end=' ') for char in hidden_code]
        if hidden_code.count("?") == 1: print("\n¡ANIMO! YA CASI LO  TIENES") 
        if "".join(hidden_code) == attempt:
            print("\n\n¡¡ENHORABUENA, HAS ADIVINADO LA CONTRASEÑA!!")
            print("\n      *****FELIZ NAVIDAD*****")
            break
    else:
        print("\nEl código introducido tiene una longitud diferente a 4 o tiene algún caracter no válido.")
        print("Pierdes un intento.")
    
    attempts -= 1
    if attempts > 0: print(f"\n\nTe {f"quedan {attempts} intentos" if attempts > 1 else f"queda 1 intento"} para adivinar la contraseña")
    if attempts == 0:
        print("\n\nSe te han acabado los intentos, Papá Noel no podrá entregar los regalos 😔")
        print(f"La contraseña es: {"".join(password)} , era muy sencilla.. ")
        
    
