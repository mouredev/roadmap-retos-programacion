###############################################################################
### EJERCICIO
###############################################################################
### FORMA INCORRECTA

class Notifier:
    """
    Clase base abstracta para notificaciones. 
    Define el método send_message que debe ser implementado por las subclases.
    """

    def send_message(self):
        """
        Método abstracto que debe ser implementado por las subclases.
        Lanza una excepción NotImplementedError si no se implementa.
        """
        raise NotImplementedError("Este método debe ser anulado")


class Mobile(Notifier):
    """
    Clase derivada que implementa el método send_message para enviar un mensaje al móvil.
    """

    def send_message(self):
        """
        Implementa el método send_message para enviar un mensaje al móvil.
        """
        return "Enviando mensaje al móvil"


class Phone(Notifier):
    """
    Clase derivada que intenta implementar el método send_message.
    Sin embargo, no puede enviar mensajes de texto y por lo tanto viola el 
    principio de sustitución de Liskov (LSP).
    """

    def send_message(self):
        """
        Implementa el método send_message pero no puede enviar mensajes de texto.
        Esta implementación viola el principio LSP porque Phone no puede 
        ser sustituido por Notifier sin alterar la funcionalidad esperada.
        """
        return "Phone can't send messages"



### FORMA CORRECTA

class Notifier:
    """
    Define un método notify que debe ser implementado por las clases derivadas. 
    Este método se asegura de que cualquier subclase implemente la 
    funcionalidad de notificación.
    """
    def notify(self):
        raise NotImplementedError("Este método debe ser anulado")

class Mobile(Notifier):
    """
    Hereda de Notifier e implementa el método notify para enviar mensajes.
    """
    def notify(self):
        return "Enviando mensaje al móvil"

class Phone(Notifier):
    """
    Hereda de Notifier e implementa el método notify para hacer llamadas
    """
    def notify(self):
        return "Haciendo llamada con un robot"

"""
El principio LSP establece que una subclase debe poder ser sustituida por su 
clase base sin alterar el funcionamiento del programa. En este caso, tanto 
Mobile como Phone pueden ser tratadas como instancias de Notifier y llamadas 
al método notify se comportarán de manera esperada sin errores. 
"""





###############################################################################
### DIFICULTAD EXTRA
###############################################################################
"""
*** Principio de Sustitución de Liskov (LSP):
Para seguir el principio LSP, las subclases (Car, Motorbike, Bicycle) deben poder 
sustituir a la clase base (Vehicle) sin alterar la funcionalidad esperada del 
programa. Cada subclase debe implementar los métodos de la clase base de manera 
coherente.
"""


class Vehicle:
    """
    Clase base para vehículos que define métodos para acelerar y detener.
    """

    def accelerate(self):
        """
        Método para acelerar el vehículo.
        """
        return "The vehicle is accelerating"
    
    def stop(self):
        """
        Método para detener el vehículo.
        """
        return "The vehicle is stopped"


class Car(Vehicle):
    """
    Clase derivada que representa un coche, hereda de Vehicle.
    """

    def accelerate(self):
        """
        Método para acelerar el coche.
        """
        return "The car is accelerating"
    
    def stop(self):
        """
        Método para detener el coche.
        """
        return "The car is stopped"


class Motorbike(Vehicle):
    """
    Clase derivada que representa una motocicleta, hereda de Vehicle.
    """

    def accelerate(self):
        """
        Método para acelerar la motocicleta.
        """
        return "The motorbike is accelerating"
    
    def stop(self):
        """
        Método para detener la motocicleta.
        """
        return "The motorbike is stopped"


class Bicycle(Vehicle):
    """
    Clase derivada que representa una bicicleta, hereda de Vehicle.
    """

    def accelerate(self):
        """
        Método para acelerar la bicicleta.
        """
        return "The bicycle is accelerating"
    
    def stop(self):
        """
        Método para detener la bicicleta.
        """
        return "The bicycle is stopped"



# USO:
vehicles = [Car(), Motorbike(), Bicycle()]

for vehicle in vehicles:
    print(vehicle.accelerate())
    print(vehicle.stop())
    


