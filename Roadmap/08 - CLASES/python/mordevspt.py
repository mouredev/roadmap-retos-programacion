"""
Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
atributos y una función que los imprima (teniendo en cuenta las posibilidades
de tu lenguaje).

Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
utilizando su función.
"""

# Clase única
class Alumno:
    # Inicializador - Constructor
    def __init__(self,nombre, curso):
        self.nombre = nombre
        self.clase = curso
    # Método para saludar a otro alumno por su nombre
    def saludar(self,nombre):
        print(f"Hola {nombre}")
    # Método donde nos identifica y muestra nuestro nombre como alumno
    def quienSoy(self):
        print(f"Soy {self.nombre}")
        
# Instanciación        
alumno1 = Alumno("Juan","Primaria")
print(f"Se ha instanciado un alumno con nombre {alumno1.nombre} en la clase de {alumno1.clase}.")

alumno2 = Alumno("Pablo","Secundaria")
print(f"Se ha instanciado un alumno con nombre {alumno2.nombre} en la clase de {alumno2.clase}.")

# Uso de sus métodos
alumno1.saludar(alumno2.nombre)
alumno1.quienSoy()
alumno2.saludar(alumno1.nombre)

# Clase con Herencia
class Area:
    # Método iniciador común para el cálculo de área
    def __init__(self,b,h):
        self.b = b
        self.h = h
# Cada tipo de polígono tiene una forma diferente de calcular su área
class Rectangulo(Area):
    # Cálculo de área concreto de un rectángulo
    def calcularArea(self):
        return self.b * self.h
    
class Triangulo(Area):
    # Cálculo de área concreto de un triángulo
    def calcularArea(self):
        return (self.b * self.h) / 2

# Instanciación
rectangulo = Rectangulo(30,80)
print(f"Se ha instanciado un Rectángulo de 30 de base * 80 de altura")
triangulo = Triangulo(75,90)
print(f"Se ha instanciado un Triángulo de 75 de base * 90 de altura")

# Uso de sus métodos
print(f"El área del rectángulo es de: {rectangulo.calcularArea()}")
print(f"El área del triángulo es de: {triangulo.calcularArea()}")

"""
DIFICULTAD EXTRA (opcional):
Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
en el ejercicio número 7 de la ruta de estudio)
- Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
  retornar el número de elementos e imprimir todo su contenido.
"""

# EJERCICIO 1 - REESCRITO
# LIFO
print("\nEJERCICIO 1 - REESCRITO\n")

class navegacionWeb():
    # INICIALIZADOR
    def __init__(self):
       self.mi_stack = [] # Iniciamos la pila
    # METODOS
    # Añadir elemento
    def nuevoElemento(self,respuesta):
        self.mi_stack.append(respuesta)
    # Eliminar elemento
    def eliminarElemento(self):
        self.mi_stack.pop()
    # Imprimir elementos
    def imprimirElementos(self):
        # Recorrido a la reversa
        for elemento in reversed(self.mi_stack):
            print(elemento)
    # Cantidad elementos
    def cantidadElementos(self):
        return len(self.mi_stack)
    # Pregunta inicial
    def preguntarAlUsuario(self):
        return input("Escribe una página, navega hacia adelante, atras, imprimir o salir: ")
    # Navegación
    def showWebSiteUser(self):
        print(f"Navegando por la web: {self.mi_stack[len(self.mi_stack)-1]}")
        
# Programa Inicial
def navegacion():
    # Instanciamos un objeto
    browser = navegacionWeb()
    respuesta = browser.preguntarAlUsuario()
    while True:
        match respuesta:
            case "atras":
                if browser.cantidadElementos() >= 1:
                    # Eliminamos el último registro
                    browser.eliminarElemento()
                # Para no provocar un problema en caso de no quedar elementos en la pila
                if (browser.cantidadElementos() > 0):
                    browser.showWebSiteUser()
                else:
                    print("Ha llegado al principio")
                # Pase lo que pase
                respuesta = browser.preguntarAlUsuario()
            case "adelante":
                print("No es posible")
                respuesta = browser.preguntarAlUsuario()
            case "salir":
                print("\n¡HASTA LUEGO!\n")
                break
            case "imprimir":
                if browser.cantidadElementos() >= 1:
                    print("\nELEMENTOS DE LA PILA\n")
                    print(f"Hay {browser.cantidadElementos()} elementos en la pila, los elementos son:\n")
                    browser.imprimirElementos()
                else:
                    print("No hay elementos en la pila")
                respuesta = browser.preguntarAlUsuario()
            case _:
                if len(respuesta) >= 1:
                    browser.nuevoElemento(respuesta)
                    browser.showWebSiteUser()
                # Pase lo que pase
                respuesta = browser.preguntarAlUsuario()

# Ejecución programa 1
navegacion()

# EJERCICIO 1 - CLASE STACK
# LIFO
print("\nEJERCICIO 1 - CLASE STACK\n")

class stack:
    # INICIALIZADOR
    def __init__(self):
       self.mi_stack = [] # Iniciamos la pila
    # METODOS
    # Añadir elemento
    def push(self,item):
        self.mi_stack.append(item)
    # Eliminar elemento
    def pop(self):
        if self.count() >= 1:
            self.mi_stack.pop()
    # Contar elementos
    def count(self):
        return len(self.mi_stack)
    # IMprimir elementos
    def print(self):
        for item in reversed(self.mi_stack):
            print(item)

# Ejemplo de uso
alcalina = stack()
alcalina.push("Duracel")
alcalina.push("Varta")
alcalina.push("Panasonic")
print("----------")
alcalina.print()
print(alcalina.count())
print("----------")
alcalina.pop()
alcalina.pop()
alcalina.print()
print(alcalina.count())
print("----------")

# EJERCICIO 2 - REESCRITO
# FIFO
print("\nEJERCICIO 2 - REESCRITO\n")

class poolPrinter:
    # INICIALIZADOR
    def __init__(self):
       self.pool = [] # Iniciamos la pila
    # METODOS
    # Añadir elemento
    def nuevoElemento(self,respuesta):
        self.pool.append(respuesta)
        print(f"Agregamos el documento {respuesta} a la cola de impresión")
    # Imprimer elemento y eliminarlo
    def imprimirElemento(self):
        print(f"Imprimimos el documento {self.pool[0]}")
        self.pool.pop(0)
    # Imprimir elementos
    def imprimirElementos(self):
        for elemento in self.pool:
            print(elemento)
    # Cantidad elementos
    def cantidadElementos(self):
        return len(self.pool)
    # Pregunta inicial
    def preguntarAlUsuarioPool(self):
        return input("Escribe si deseas imprimir, agregar un nuevo documento, mostrar o salir: ")
    # Navegación
    def showWebSiteUser(self):
        print(f"Navegando por la web: {self.pool[len(self.pool)-1]}")

# Programa inicial
def printer():
    # Instanciamos un objeto
    poolPrinterUser = poolPrinter()
    respuestaUsuario = poolPrinterUser.preguntarAlUsuarioPool()
    while True:
        match respuestaUsuario:
            case "imprimir":
                # Comprobamos
                if poolPrinterUser.cantidadElementos() == 0:
                    print("No hay documentos en la cola de impresión, agregue uno antes")
                    respuestaUsuario = poolPrinterUser.preguntarAlUsuarioPool()
                else:
                    poolPrinterUser.imprimirElemento()
                    respuestaUsuario = poolPrinterUser.preguntarAlUsuarioPool()
            case "salir":
                print("\n¡HASTA LUEGO!\n")
                break
            case "mostrar":
                if poolPrinterUser.cantidadElementos() >= 1:
                    poolPrinterUser.imprimirElementos()
                else:
                  print("Escriba el nombre de un documento o si desea imprimir")
                # Pase lo que pase
                respuestaUsuario = poolPrinterUser.preguntarAlUsuarioPool()
            case _:
                if len(respuestaUsuario) >= 1:
                    poolPrinterUser.nuevoElemento(respuestaUsuario)
                else:
                  print("Escriba el nombre de un documento o si desea imprimir")
                # Pase lo que pase
                respuestaUsuario = poolPrinterUser.preguntarAlUsuarioPool()

# Ejecución programa 2
printer()

# EJERCICIO 2 - CLASE QUEUE
# LIFO
print("\nEJERCICIO 2 - CLASE QUEUE\n")

class queue:
    # INICIALIZADOR
    def __init__(self):
       self.mi_queue = [] # Iniciamos la pila
    # METODOS
    # Añadir elemento
    def equeue(self,item):
        self.mi_queue.append(item)
    # Eliminar elemento
    def deequeue(self):
        if self.count() >= 1:
            self.mi_queue.pop(0)
    # Contar elementos
    def count(self):
        return len(self.mi_queue)
    # IMprimir elementos
    def print(self):
        for item in self.mi_queue:
            print(item)

# Ejemplo de uso
tail = queue()
tail.equeue("Zorro")
tail.equeue("Lagarto")
tail.equeue("Puma")
print("----------")
tail.print()
print(tail.count())
print("----------")
tail.deequeue()
tail.deequeue()
tail.print()
print(tail.count())
print("----------")