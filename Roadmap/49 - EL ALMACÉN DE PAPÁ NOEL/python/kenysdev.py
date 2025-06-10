# _____________________________________
# https://github.com/kenysdev
# 2024 - Python
# _____________________________________
# #49 EL ALMACÉN DE PAPÁ NOEL
# ------------------------------------

"""
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
"""

# ____________________________________________________________________________
from random import sample

def verify_allowed_char(code_entry: str) -> bool:
    for ch in code_entry:
        if ch not in 'abc123':
            print("Uno de los caracteres no está entre los permitidos.\n")
            return False
    
    return True

def get_entry() -> str:
    while True:
        code_entry: str = input("Código: ")

        if len(code_entry) != 4:
            print("El código debe ser de 4 dígitos.\n")
            continue
        
        if verify_allowed_char(code_entry):
            return code_entry

def is_open(code: str) -> bool:
    code_entry: str = get_entry()
    if code_entry == code:
        return True
    print("Código inválido.\n")

    for i, ch in enumerate(code_entry):
        if ch == code[i]:
            print(f"'{ch}' está en la posición correcta.")

        elif ch in code:
            print(f"'{ch}' está en el código, pero en otra posición.")

        else:
            print(f"'{ch}' no está presente en el código.")
    
    return False

# ____________________________________________________________________________
print("""
* Papá Noel tiene que comenzar a repartir los regalos...
* ¡Pero ha olvidado el código secreto de apertura del almacén!

- Tienes 10 intentos para adivinar el código que abre el almacén.
- Código de 4 caracteres. Permitidos: a, b, c, 1, 2, 3.
- Nota: No hay dígitos repetidos.""")

code : str = ''.join(sample("abc123", 4))

for attempts in range(10):
    print(f"\n___________\nIntento #{attempts + 1}")

    if is_open(code):
        print("Código correcto, almacén abierto.")
        print("Papá Noel ahora podrá entregar los regalos.")
        break

    if attempts == 9:
        print("\n___________\nHas perdido.")
        print("Papá Noel ya no podrá entregar los regalos.")

