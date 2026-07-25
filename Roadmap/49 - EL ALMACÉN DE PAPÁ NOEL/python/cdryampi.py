# /*
#  * EJERCICIO:
#  * Papá Noel tiene que comenzar a repartir los regalos...
#  * ¡Pero ha olvidado el código secreto de apertura del almacén!
#  *
#  * Crea un programa donde introducir códigos y obtener pistas.
#  * 
#  * Código:
#  * - El código es una combinación de letras y números aleatorios
#  *   de longitud 4. (Letras: de la A a la C, Números: del 1 al 3)
#  * - No hay repetidos.
#  * - Se genera de manera aleatoria al iniciar el programa.
#  * 
#  * Usuario:
#  * - Dispone de 10 intentos para acertarlo.
#  * - En cada turno deberá escribir un código de 4 caracteres, y 
#  *   el programa le indicará para cada uno lo siguiente:
#  *   - Correcto: Si el caracter está en la posición correcta.
#  *   - Presente: Si el caracter existe, pero esa no es su posición.
#  *   - Incorrecto: Si el caracter no existe en el código secreto.
#  * - Deben controlarse errores de longitud y caracteres soportados.
#  * 
#  * Finalización:
#  * - Papa Noel gana si descrifra el código antes de 10 intentos.
#  * - Pierde si no lo logra, ya que no podría entregar los regalos.
#  */

import random

class Codigo:
    BASE = ['A', 'B', 'C', '1', '2', '3']
    CORRECTO = 'Correcto'
    PRESENTE = 'Presente'
    INCORRECTO = 'Incorrecto'

    def __init__(self):
        self.code = random.sample(self.BASE, 4)
    def check_character_valid(self, character: str) -> bool:
        return character in self.BASE

    def check_character_status(self, value: str, pos: int) -> str:
        if value == self.code[pos]:
            return self.CORRECTO
        if value in self.code:
            return self.PRESENTE
        return self.INCORRECTO

    def __str__(self) -> str:
        return "".join(self.code)


class UserControl:
    MAX_INTENTOS = 10

    def __init__(self):
        self.codigo = Codigo()
        self.intentos = self.MAX_INTENTOS
        print("Bienvenido al Almacén de Papá Noel.\nUtiliza letras de la A a la C y números del 1 al 3.")
        self.run_game()

    def run_game(self):
        while self.intentos > 0:
            if self.new_code():
                break
            print(f"Te quedan {self.intentos} intentos.")

    def new_code(self) -> bool:
        if self.intentos <= 0:
            print("Has perdido el juego. Has superado los 10 intentos.")
            return False

        self.__NEW_CODE = input("Introduce un código de 4 dígitos:\n").strip().upper()
        self.intentos -= 1

        if len(self.__NEW_CODE) != 4 or not all(self.codigo.check_character_valid(c) for c in self.__NEW_CODE):
            print("El código que has introducido no es válido.\nPor favor, introduce un código de 4 dígitos.\nLos dígitos válidos son letras de la A a la C y números del 1 al 3.")
            return False

        if self.check_code():
            return True
        return False

    def check_code(self) -> bool:
        status = [self.codigo.check_character_status(c, i) for i, c in enumerate(self.__NEW_CODE)]
        if all(s == Codigo.CORRECTO for s in status):
            print("¡El código que has introducido es correcto!\nHas descifrado el código del Almacén.")
            return True
        else:
            result = [f"{c} - {s} " for c,s in zip(self.__NEW_CODE, status)]
            print(" ".join(result))

        return False


if __name__ == "__main__":
    control = UserControl()