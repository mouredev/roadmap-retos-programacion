# 49 - El almacén de papá noel
import random

class WorkshopAccess:
    def __init__(self):
        self.letters = "abc"
        self.numbers = "123"
        self.valid_characters = self.letters + self.numbers
        self.access_code = self.generate_code(self.valid_characters)

    def generate_code(self,text):
        caracters = list(text.lower())
        code = "".join(random.sample(caracters,k=4))
        return code
    
    def valid_text(self, text):
        if len(text) != 4:
            print("Numero de caracteres incorrecto.")
            return False
        for char in text:
            if char not in list(self.valid_characters):
                print("Caracter no soportado encontrado.")
                return False
        return True

    def try_code(self, text):
        if text == self.access_code:
            print("Codigo correcto. Acceso concedido.")
            print("Bienvenido Santa!")
            return True
        for index, char in enumerate(text):
            if char == self.access_code[index]:
                print(f"Caracter '{char}' (posición: {index+1}) es correcto.")
            elif char in self.access_code:
                print(f"Caracter '{char}' esta presente, pero no en la posición: {index+1}.")
            else:
                print(f"Caracter '{char}' incorrecto: no existe en el codigo secreto.")
        return False
    
    def entry_acceess(self):
        print("Bienvenido")
        for i in range(10):
            print(f"Ingrese el codigo de acceso (caracteres disponibles {self.valid_characters} y longitud 4): ")
            code = input(f"Intento {i+1}: ").lower()
            if santa_workshop_access.valid_text(code):
                status = santa_workshop_access.try_code(code)
                if status:
                    break
        if not status:
            print("Ha fallado en los 10 intentos, bloque permanente activado!")
            print("No habra regalos en esta navidad! :(")

santa_workshop_access = WorkshopAccess()
santa_workshop_access.entry_acceess()    
