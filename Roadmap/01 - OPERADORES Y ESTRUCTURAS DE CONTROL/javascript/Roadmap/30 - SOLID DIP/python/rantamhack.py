
# ESTE PRINCIPIO ESTABLECE DOS COSAS:
# 1ª LOS MODULOS DE ALTO NIVEL NO PUEDEN DEPENDER DE LOS MODULOS DE BAJO NIVEL, LOS DOS DEBEN DEPENDER DE LAS ABSTRACCIONES
# 2ª LAS ABSTRACCIONES NO PUEDEN DEPENDER DE LOS DETALLES SINO LOS DETALLES DE LAS ABSTRACCIONES



print("\n\n=======================================EJERCICIO=======================================\n\n")

'''
 * EJERCICIO:
 * Explora el "Principio SOLID de Inversión de Dependencias (Dependency Inversion
 * Principle, DIP)" y crea un ejemplo simple donde se muestre su funcionamiento 
 * de forma correcta e incorrecta.
'''

# SIN DIP

# class Dictionary():
#     def chek_word(self, word, dictionary):
#         if word in dictionary:
#             return f"La palabra {palabra} estÃ¡ en el diccionario"
            
             
# class SpellCorrect:
#     def __init__(self, dictionary):
#         self.dictionary = Dictionary()
        
#     def correct_text(self, text):
#          #Tenemos que usar el diccionario para corregir el texto o cambiar toda la logica
#          pass



# CON DIP

from abc import ABC, abstractmethod

class SpellChecker(ABC):
    @abstractmethod
    def check_word(self):
        pass
 
    
class Dictionary(SpellChecker):
    def check_word(self, word, dictionary):
        # Logica para verificar la palabra en el diccionario
        pass
 
    
class OnlineService(SpellChecker):
    def check_word(self, word, url):
        # Logica para verificar palabras desde el servicio web
        pass
    
class SpellCorrect:
    def __init__(self, checker):
        self.cheker = checker
        
    def correct_text(self, text):
        # Usamos el verificador para corregir el texto da igual si usamos un servicio local o web, solo hay que indicar desde donde lo queremos hacer
        pass




print("\n\n=======================================DIFICULTAD EXTRA=======================================\n\n")

'''
 * DIFICULTAD EXTRA (opcional):
 * Crea un sistema de notificaciones.
 * Requisitos:
 * 1. El sistema puede enviar Email, PUSH y SMS (implementaciones específicas).
 * 2. El sistema de notificaciones no puede depender de las implementaciones específicas.
 * Instrucciones:
 * 1. Crea la interfaz o clase abstracta.
 * 2. Desarrolla las implementaciones específicas.
 * 3. Crea el sistema de notificaciones usando el DIP.
 * 4. Desarrolla un código que compruebe que se cumple el principio.
'''

from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def send(self, message):
        pass
    
    
class EmailNotification(Notifier):
    def send(self, message):
        print(f"Enviando por email el mensaje: {message}")
        
        
        
class PUSHNotification(Notifier):
    def send(self, message):
        print(f"Enviando por PUSH el mensaje: {message}")
        
        
class SMSNotification(Notifier):
    def send(self, message):
        print(f"Enviando por SMS el mensaje: {message}")
        
        
class Notification:
    def __init__(self, notifier: Notifier):
        self.notifier = notifier
        
    def notify(self, message):
        self.notifier.send(message)
        
        
        
notice1 = Notification(EmailNotification())
notice1.notify("Felices vacaciones!!!")

notice2 = Notification(PUSHNotification())
notice2.notify("Felices vacaciones!!!")

notice3 = Notification(SMSNotification())
notice3.notify("Felices vacaciones!!!")

    
    
    
