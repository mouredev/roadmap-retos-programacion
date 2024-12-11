r"""
 EJERCICIO:
 Papá Noel tiene que comenzar a repartir los regalos...
 ¡Pero ha olvidado el código secreto de apertura del almacén!

 Crea un programa donde introducir códigos y obtener pistas.
 
 Código:
 - El código es una combinación de letras y números aleatorios
   de longitud 4. (Letras: de la A a la C, Números: del 1 al 3)
 - No hay repetidos.
 - Se genera de manera aleatoria al iniciar el programa.
 
 Usuario:
 - Dispone de 10 intentos para acertarlo.
 - En cada turno deberá escribir un código de 4 caracteres, y 
   el programa le indicará para cada uno lo siguiente:
   - Correcto: Si el caracter está en la posición correcta.
   - Presente: Si el caracter existe, pero esa no es su posición.
   - Incorrecto: Si el caracter no existe en el código secreto.
 - Deben controlarse errores de longitud y caracteres soportados.
 
 Finalización:
 - Papa Noel gana si descrifra el código antes de 10 intentos.
 - Pierde si no lo logra, ya que no podría entregar los regalos.
"""
from random import randint
characters = ["a", "1", "b", "2", "c", "3"]
tries = 10
access_granted = False


def create_passkey() -> str:
    pass_characters = characters.copy()
    passkey = ""
    while passkey.__len__() < 4:
        character = pass_characters.pop(randint(0, pass_characters.__len__() - 1))
        passkey += character

    return passkey


def validate_entry(word: str, passkey: str) -> bool:
    if word == passkey:
        print("Acceso Permitido.")
        return True
    if word.__len__() != 4:
        print("Error: la longitud DEBE ser igual a cuatro caracteres.")
        return False
    if [x for x in word if x in characters].__len__() != 4:
        print("Error: solo son válidos los carateres a, b, c, 1, 2, 3")
        return False
    for x, y in zip(word, passkey):
        if x not in passkey:
            print(f"{x} no es parte de la clave")
        elif x == y:
            print(f"{x} está en la posioción CORRECTA")
        else:
            print(f"{x} está en la posioción INCORRECTA")
    print("Acceso DENEGADO")
    return False


passkey = create_passkey()
# print(passkey)
while tries > 0 and not access_granted:
    word = input(f"Ingrese la palabra clave (intento# {11 - tries}): ")
    access_granted = validate_entry(word, passkey)
    tries -= 1
