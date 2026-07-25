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
 * - Papa Noel gana si descifra el código antes de 10 intentos.
 * - Pierde si no lo logra, ya que no podría entregar los regalos.
"""

import random
import string

class Code:
    def __init__(self) -> None:
        self.chars = list(string.ascii_lowercase[:3]) + list(map(str, range(1,4)))
        self.target_code = random.sample(self.chars, 4)

    def get_code(self):
        return self.target_code

class CodeChecker:
    def __init__(self, code: Code) -> None:
        self.code = code
        
    def check_code(self, user_code: str) -> list:
        user_code_list = list(user_code)
        feedback =[]

        for index in range(4):
            if user_code_list[index] == self.code.target_code[index]:
                feedback.append("ok")
            elif user_code_list[index] in self.code.target_code:
                feedback.append("!")
            else:
                feedback.append("X")
        
        return feedback
    

class AcessController:
    def __init__(self, code: Code, code_checker: CodeChecker) -> None:
        self.code = code
        self.code_checker = code_checker

    def check_valid_input(self, user_code) -> bool:

        valid_chars = ["a", "b", "c", "1", "2", "3"]
        
        if len(user_code) != 4:
            print("El código debe tener 4 caracteres.")
            return False
        
        if len(set(user_code)) != 4:
            print("Todos los caracteres deben ser diferentes")
            return False
    
        if not all(char in valid_chars for char in user_code):
            print("Has introducido un caracter no válido.")
            return False
        
        return True


    def run(self):
        print("Introduce el código de acceso. Tienes 10 intentos para descubrirlo.")
        print("Debe tener 4 caracteres no repetidos y que esten entre (a, b, c, 1, 2, 3)")
        print("La respuesta de feedback funciona como sigue:")
        print("\tok -> caracter y posición correcta")
        print("\t ! -> caracter correcto pero posición incorrecta")
        print("\t X -> caracter incorrecto")

        round = 0
        while round < 10:
            round += 1
            print(f"ROUND {round}")

            valid = False
            while not valid:
                user_try = input("Introduce tu código:").lower()
                valid = self.check_valid_input(user_try)

            print(f"Tu codigo: {list(user_try)}")
            feedback = self.code_checker.check_code(user_try)
            print(f"Feedback : {feedback}")

            if len(set(feedback)) == 1 and feedback[1] == "ok":
                print(f"Correcto : {self.code.get_code()}")
                print(f"Has adivinado el código en {round} rondas.")
                break
        if round == 10:
            print(f"Correcto : {self.code.get_code()}")
            print("Has perdido. No has logrado descubrir el codigo en 10 intentos.")

new_code = Code()
code_checker = CodeChecker(new_code)
acces_controller = AcessController(new_code, code_checker)
acces_controller.run()
