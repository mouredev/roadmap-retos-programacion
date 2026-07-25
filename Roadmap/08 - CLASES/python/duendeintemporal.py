#8 { Retos para Programadores } CLASES 
""" 
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

"""

# Bibliography reference
# Secrets of the JavaScript Ninja (John Resig, Bear Bibeault, Josip Maras)
# Professional JavaScript for web developers by Matt Frisbie
# Python para todos (Raúl Gonzáles Duque)
# GPT

# Classes and Objects

# To understand this paradigm, we first need to comprehend what a class is and what an object is.
# An object is an entity that groups related state and functionality. The state of the object is defined
# through variables called attributes, while the functionality is modeled through functions known as the object's methods.

# An example of an object could be a car, which would have attributes such as the brand, the number of doors,
# or the type of fuel, and methods such as start and stop. Alternatively, it could be any other combination
# of attributes and methods relevant to our program.

# A class, on the other hand, is a generic template from which to instantiate objects; a template that defines
# what attributes and methods the objects of that class will have.

# The fundamental part of most classes is its constructor, which sets up each instance's initial state
# and handles any parameters that were passed when calling the class.

# In Python, we define a class using the 'class' keyword.

log = print

class User:
    def __init__(self, name, nickname, email):
        self.name = name
        self.nickname = nickname
        self.email = email

    def greeting(self):
        log(f"Hi {self.nickname}. Welcome to this Roadmap for Developers!")

    def get_email(self):
        if self.email is not None:
            return self.email
        else:
            log('No email set yet!')
            return None

    def get_name(self):
        if self.name is not None:
            return self.name
        else:
            log('No name set yet!')
            return None

    def get_nickname(self):
        if self.nickname is not None:
            return self.nickname
        else:
            log('No nickname set yet!')
            return None

    def set_name(self, name):
        if name:
            self.name = name

    def set_email(self, email):
        if email:
            self.email = email

    def set_nickname(self, nickname):
        if nickname:
            self.nickname = nickname

    def user_info(self):
        log(f"User name: {self.name or 'not set'}, User nickname: {self.nickname or 'not set'}, User email: {self.email or 'not set'}")


# Creating an instance of User
user1 = User('Niko Zen', 'duendeintemporal', 'duendeintemporal@hotmail.com')
user1.greeting()  # Hi duendeintemporal. Welcome to this Roadmap for Developers!

user1.user_info()  # User name: Niko Zen, User nickname: duendeintemporal, User email: duendeintemporal@hotmail.com

user1.set_nickname('psicotrogato')
log(user1.get_nickname())  # psicotrogato

# In Python, we can check the type of a class using the type() function.
log(type(User))  # <class 'type'>

# We can use isinstance() to check if an instance is of a certain class.
log(isinstance(user1, User))  # True

# Class Inheritance
# Inheritance works just like it does in other object-oriented languages: methods defined on the superclass
# are accessible in the extending subclass.

class Log:
    def __init__(self):
        self.logger = log
        self.error_log = log

    def log(self, msg):
        if msg:
            self.logger(msg)
        else:
            self.error_log('You should provide a message')


# When you extend a class in Python, you must call the superclass constructor using super().
class Greeting(Log):
    def __init__(self, msg):
        super().__init__()
        self.msg = msg


say_hi_people = Greeting('Hi everybody. Welcome to the most weird and lonely place in cyberspace...')
say_hi_people.log(say_hi_people.msg)  # Hi everybody. Welcome to the most weird and lonely place in cyberspace...

# Static Methods
# Static methods and properties are defined on the class itself, not on instance objects.
# These are specified in a class definition using the @staticmethod decorator.

class ElectroCat:
    @staticmethod
    def cat_say():
        return 'Miauu'

    @property
    def cat_think(self):
        return "Let's see if there's some lovely gircat over there"


log(ElectroCat.cat_say())  # Miauu
log(ElectroCat().cat_think)  # Let's see if there's some lovely gircat over there

# We can see that static properties are not defined on object instances:
mishu = ElectroCat()
# The following lines would raise an AttributeError if uncommented, as static methods are not available on instances.
# log(mishu.cat_say())  # Raises AttributeError
# log(mishu.cat_think)  # Raises AttributeError

# However, they are defined on subclasses:
class PoetCat(ElectroCat):
    pass

log(PoetCat.cat_say())  # Miauu
log(PoetCat().cat_think)  # Let's see if there's some lovely gircat over there

# Getters and setters allow you to define custom behavior for reading and writing a given property on your class.
# In Python, we can use the @property decorator for getters and the @<property_name>.setter decorator for setters.

class Cat:
    def __init__(self, name):
        self._name = name  # Using a private variable

    @property
    def name(self):
        """Getter for the name property."""
        return self._name

    @name.setter
    def name(self, new_name):
        """Setter for the name property."""
        if new_name:
            self._name = new_name
        else:
            log("Name cannot be empty!")

# Example usage of the Cat class with getters and setters
my_cat = Cat("Whiskers")
log(my_cat.name)  # Whiskers

my_cat.name = "Fluffy"  # Using the setter
log(my_cat.name)  # Fluffy

my_cat.name = ""  # Attempting to set an empty name
# Output: Name cannot be empty!

# Hidden methods can be indicated by prefixing the method name with an underscore.
class HiddenMethodExample:
    def __init__(self):
        self._hidden_method = "This is a hidden method"

    def _hidden_method_function(self):
        return self._hidden_method

hidden_example = HiddenMethodExample()
log(hidden_example._hidden_method_function())  # This is a hidden method
# Note: The method is not truly private, but it's a convention to indicate that it should not be accessed directly.

# Summary
# This code demonstrates the use of classes, inheritance, static methods, and property decorators in Python.
# It also illustrates how to define and use getters and setters, as well as the concept of hidden methods.

# We use private properties in Python classes to avoid infinite recursion in getters and setters
# by referencing the private property instead of the public property.

class GopiElectronica:
    def __init__(self, name):
        self._name = name  # Using a private variable

    @property
    def name(self):
        """Getter for the name property."""
        return self._name

    @name.setter
    def name(self, new_name):
        """Setter for the name property."""
        self._name = new_name

    def hidden_method(self):
        return 'I will hack you boy'

# Example usage of GopiElectronica
Nicky = GopiElectronica('Nicky')
log(Nicky.name)  # Nicky
Nicky.name = 'Samantha'
log(Nicky.name)  # Samantha
log(f"{Nicky.name} says: {Nicky.hidden_method()}!")  # Samantha says: I will hack you boy!

# Note: In Python, we don't have a direct equivalent to JavaScript's Symbol for hiding methods.
# However, we can use naming conventions (like prefixing with an underscore) to indicate that a method is intended to be private.

# Tips: (relevant info)
# Classes are first-class citizens in Python, meaning they can be passed around as you would any other object or function reference.

# Classes may be defined anywhere a function would, such as inside a list:
class_list = [
    type('DynamicClass', (object,), {
        '__init__': lambda self, id_: log(f'instance {id_}')
    })
]

def create_instance(class_definition, id_):
    return class_definition(id_)

foo = create_instance(class_list[0], 3141)  # instance 3141

# Similar to an immediately invoked function expression, a class can also be immediately instantiated.
# Because it is a class expression, the class name is optional.
# Create a class dynamically and instantiate it immediately
# Create a class dynamically using type with a different name
bar = type('Bar', (object,), {
    '__init__': lambda self, x: log(x)  # This lambda will log the value of x
})

# Now create an instance of Bar
p = bar('bar')  # This will log 'bar'

# log the instance
log(p)  # This will log something like <__main__.Bar object at 0x000002108065EF90>

# Additional Exercises

# QUEUE
class Queue:
    def __init__(self, initial_items=None):
        self.items = initial_items if isinstance(initial_items, list) else []

    def enqueue(self, element):
        self.items.append(element)

    def dequeue(self):
        if self.is_empty():
            log("Queue is empty. Cannot dequeue an element.")
            return None
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            log("Queue is empty. Cannot peek.")
            return None
        return self.items[0]

    def empty(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Example usage of Queue
queue2 = Queue([45, 32, 16])
log('Initial queue2:', queue2.items)  # [45, 32, 16]

queue2.enqueue(77)
log('After enqueueing 77:', queue2.items)  # [45, 32, 16, 77]

log('Peek:', queue2.peek())  # 45

log('Dequeue:', queue2.dequeue())  # 45
log('After dequeueing:', queue2.items)  # [32, 16, 77]

log('Dequeue all elements:')
while not queue2.is_empty():
    log('Dequeued:', queue2.dequeue())
# or we can just empty the queue
# queue2.empty()

log('Final queue2:', queue2.items)  # []
log('Dequeue from empty queue2:', queue2.dequeue())  # Logs error: Queue is empty. Cannot dequeue an element. & Dequeue from empty queue2: None

# STACK
class Stack:
    def __init__(self, initial_items=None):
        self.items = initial_items if isinstance(initial_items, list) else []

    def push(self, element):
        self.items.append(element)

    def pop(self):
        if self.is_empty():
            log("Stack is empty. Cannot pop an element.")
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            log("Stack is empty. Cannot peek.")
            return None
        return self.items[-1]

    def empty(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Example usage of Stack
stack2 = Stack([55, 76, 98, 100])
log('Initial stack2:', stack2.items)  # [55, 76, 98, 100]

stack2.push(32)
log('After pushing 32:', stack2.items)  # [55, 76, 98, 100, 32]

log('Peek:', stack2.peek())  # 32

log('Pop:', stack2.pop())  # 32
log('After popping:', stack2.items)  # [55, 76, 98, 100]

log('Pop all elements:')
while not stack2.is_empty():
    log('Popped:', stack2.pop())
# or we can just empty the stack
# stack2.empty()

log('Final stack2:', stack2.items)  # []
log('Pop from empty stack2:', stack2.pop())  # Logs error: Stack is empty. Cannot pop an element. & Pop from empty stack2: None


