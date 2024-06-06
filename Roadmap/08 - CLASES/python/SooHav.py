# 08 Clases

# Ejercicio

'''Las clases en Python proporcionan una forma de empaquetar datos y funcionalidad juntos. 
Al crear una nueva clase, estamos creando un nuevo tipo de objeto, lo que nos permite crear 
nuevas instancias de ese tipo. Cada instancia de clase puede tener atributos adjuntos 
para mantener su estado, y también puede tener métodos definidos por su clase para modificar ese estado.

En la definición de una clase, los atributos se definen como variables que se inicializan en el 
método especial init. Por ejemplo, en la clase Mascota, los atributos son nombre, edad y animal.

Los métodos son funciones que se definen dentro de una clase y se utilizan para realizar operaciones 
en los objetos creados a partir de esa clase. Siempre tienen como primer parámetro el objeto al que se 
aplicará el método, por convención llamado self.

Para utilizar un método de una clase, primero debemos crear un objeto a partir de esa clase, como perro 
o gato, y luego llamar al método sobre ese objeto. Por ejemplo, para hacer que un perro 
ladre: perro.hacer_sonido('Guau').'''


from collections import deque


class Mascota:
    def __init__(self, nombre, edad, animal):
        self.nombre = nombre
        self.edad = edad
        self.animal = animal

    def hacer_sonido(self, sonido):
        print(f"{self.nombre} dice {sonido}")

    def comer(self, comida):
        print(f"{self.nombre} está comiendo {comida}")

    def dormir(self):
        print(f"{self.nombre} está durmiendo")

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Mascota: {self.animal}"


# Implementacion
perro = Mascota("Fido", 5, "Perro")
print(perro)
perro.comer("croquetas")
perro.hacer_sonido("Guauu")
perro.dormir()
gato = Mascota("Kiti", 2, "Gato")
print(gato)
gato.comer("pescado")
gato.hacer_sonido("Miuauu")
gato.dormir()


'''La herencia es un proceso mediante el cual se puede crear una clase hija que hereda 
de una clase padre, compartiendo sus métodos y atributos.'''


class Cuidado(Mascota):
    def __init__(self, nombre, edad, animal, cuidador):
        super().__init__(nombre, edad, animal)
        self.cuidador = cuidador

    def bañar(self, numero_veces):
        print(f"{self.cuidador} baña a {self.nombre} {numero_veces} veces al mes.")

    def entrenar(self,  juego):
        print(f"{self.cuidador} {juego} a {self.nombre}.")


# Implementaciòn
gato = Cuidado("Kiti", 2, "gato", "Sofi")
gato.bañar(2)
gato.entrenar("pasea")

# Ejercicio extra

# Colas


class HacerFila:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.cola = []

    def primer_elemento(self):
        return self.primero

    def ultimo_elemento(self):
        return self.ultimo

    def agrega_elemento(self, elemento):
        self.cola.append(elemento)
        self.ultimo = elemento
        return self.ultimo

    def saca_elemento(self):
        self.cola.pop(0)
        self.primero = self.cola[0]
        return self.primero

    def __str__(self):
        return str(self.cola)

    def __len__(self):
        return len(self.cola)


# Implementacion
en_fila = HacerFila()
en_fila.agrega_elemento(1)
en_fila.agrega_elemento(2)
en_fila.agrega_elemento(3)
en_fila.agrega_elemento(4)
print(en_fila)
en_fila.saca_elemento()
en_fila.saca_elemento()
print(en_fila)
print(len(en_fila))

# Navegador web


class NavegadorWeb:
    def __init__(self):
        self.historial = deque()
        self.actual = ""

    def atras(self):
        if self.historial:
            self.actual = self.historial.pop()
            print("Retrocediendo a la pagina anterior")
        else:
            print("No hay páginas para retroceder")

    def adelante(self, url):
        if self.actual:
            self.historial.append(self.actual)
        else:
            print("No hay página adelante")
        self.actual = url

    def ver_historial(self):
        print("Historial:")
        for pagina in self.historial:
            print(pagina)
        print(f"Página actual: {self.actual}")

    def __str__(self):
        return f"Página actual: {self.actual}"


# Implementacion
navegador = NavegadorWeb()
navegador.adelante("https://www.ejemplo.com/pagina-1")
print(navegador)
navegador.adelante("https://www.ejemplo.com/pagina-2")
print(navegador)
navegador.adelante("https://www.ejemplo.com/pagina-3")
print(navegador)
navegador.atras()
print(navegador)
navegador.ver_historial()
