""" /*
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 */ """

""" Ejemplo de clase: """


class Client:

    def __init__(self, id: int, name: str, surname: str, email: str) -> None:
        self.id = id
        self.name = name
        self.surname = surname
        self.email = email

    def __str__(self) -> str:
        return f"Id: {self.id} | Nombre: {self.name} | Apellido: {self.surname} | Email: {self.email}"


jose = Client(1, "Jose", "Lopez", "jose26@gmail.com")
maria = Client(2, "Maria", "Martinez", "mary@gmail.com")
rosa = Client(3, "Rosa", "Garcia", "ros@gmail.com")

# print(jose)
# print(maria)
# print(rosa)


""" * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 */ """


class Pila:

    def __init__(self, pila: list = []) -> None:
        self.pila = pila

    def show(self):
        for element in reversed(self.pila):
            print(f"--> {element}")

    def push(self, element):
        self.pila.append(element)

    def pop(self):
        if self.is_empty():
            return None
        return self.pila.pop()

    def is_empty(self):
        return len(self.pila) == 0


new_stack = Pila()

new_stack.push(5)
new_stack.push(4)
new_stack.push(3)
new_stack.push(8)
new_stack.push(7)

new_stack.show()

print(new_stack.pop())
print(new_stack.pop())
print(new_stack.pop())
print(new_stack.pop())
print(new_stack.pop())
print(new_stack.pop())
print(new_stack.pop())


class Cola:

    def __init__(self, cola: list = []) -> None:
        self.cola = cola

    def show(self):
        for element in self.cola:
            print(f"--> {element}")

    def enqueue(self, element):
        self.cola.append(element)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.cola.pop(0)

    def peek(self):
        return self.cola[0]

    def is_empty(self):
        return len(self.cola) == 0


new_queue = Cola()

new_queue.enqueue("Juan")
new_queue.enqueue("Pedro")
new_queue.enqueue("Pablo")

new_queue.show()


print(new_queue.dequeue())
print(new_queue.dequeue())
print(new_queue.dequeue())
print(new_queue.dequeue())
