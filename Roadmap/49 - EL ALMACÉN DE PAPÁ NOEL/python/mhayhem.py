# @Author Daniel Grande (Mhayhem)

# EJERCICIO:
# Papá Noel tiene que comenzar a repartir los regalos...
# ¡Pero ha olvidado el código secreto de apertura del almacén!
#
# Crea un programa donde introducir códigos y obtener pistas.
# 
# Código:
# - El código es una combinación de letras y números aleatorios
#   de longitud 4. (Letras: de la A a la C, Números: del 1 al 3)
# - No hay repetidos.
# - Se genera de manera aleatoria al iniciar el programa.
# 
# Usuario:
# - Dispone de 10 intentos para acertarlo.
# - En cada turno deberá escribir un código de 4 caracteres, y 
#   el programa le indicará para cada uno lo siguiente:
#   - Correcto: Si el caracter está en la posición correcta.
#   - Presente: Si el caracter existe, pero esa no es su posición.
#   - Incorrecto: Si el caracter no existe en el código secreto.
# - Deben controlarse errores de longitud y caracteres soportados.
# 
# Finalización:
# - Papa Noel gana si descifra el código antes de 10 intentos.
# - Pierde si no lo logra, ya que no podría entregar los regalos.

import random

class SantaClausStore:
    def __init__(self):
        self.valid_chars = "ABC123"
        self.password = "".join(random.sample(self.valid_chars, 4))
    
    def check_length_and_valid_characters(self, code: str) -> bool:
        self.hints = []
        
        if len(code) != 4:
            return False
        for char in code:
            if char not in self.valid_chars:
                return False
        if len(set(code)) != 4:
            return False
        return True
    
    def check_position_char(self, code: str) -> bool:
        if code == self.password:
            correct_code = True
            return correct_code
        else:
            for index ,char in enumerate(code):
                if char == self.password[index]:
                    self.hints.append(f"Correcto - {char}")
                elif char in self.password:
                    self.hints.append(f"Presente - {char}")
                else:
                    self.hints.append(f"Incorrecto - {char}")
        return False
    
    def display_hints(self):
        print("\nPistas\n")
        for text in self.hints:
            print(text)
        self.hints.clear()
    
    def __str__(self) -> str:
        return self.password

def main():
    store = SantaClausStore()
    attempt = 10
    correct_code = False
    while attempt > 0 and correct_code != True:
        print(f"Intentos restantes: {attempt}\n")
        code = input("Introduzca un código de 4 dígitos y que tenga letas entre la A y la C y números entre el 1 y el 3: ").upper()
        valid = store.check_length_and_valid_characters(code)
        if valid:
            correct_code = store.check_position_char(code)
            store.display_hints()
        else:
            print("No cumple con los requisitos.")
        attempt -= 1
        print()
    if correct_code:
        print("Código correcto. Santa Clausesta abriendo almacén.")
    else:
        print("Santa Claus no pudo abrir el almacén")
        print(store.__str__())

if __name__=="__main__":
    main()