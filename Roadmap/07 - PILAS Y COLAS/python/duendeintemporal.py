#7 { Retos para Programadores }  PILAS Y COLAS
"""
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 *
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
"""

# The list structure in Python can be useful to simulate stacks and queues.

# A stack is a linear data structure that follows the Last In, First Out (LIFO) principle.
# This means that the last element added to the stack is the first one to be removed.
# You can think of it like a stack of plates: you add plates to the top and also remove them from the top.
# Key Operations:
# - Push: Add an element to the top of the stack.
# - Pop: Remove the element from the top of the stack.
# - Peek/Top: Retrieve the top element without removing it.
# - IsEmpty: Check if the stack is empty.

log = print

# Stack implementation using a list
stack = [1, 2, 3, 4]

# View the contents of a stack
log('View stack:', stack)  # View stack: [1, 2, 3, 4]

# Add an element to the stack
stack.append(5)
log('Add an element:', stack)  # Add an element: [1, 2, 3, 4, 5]

# Get the size of the stack
log('Size:', len(stack))  # Size: 5

# Get the last value of the stack
log('Last value of the stack:', stack[-1])  # Last value of the stack: 5

# Remove the last value from the stack and print its value
log('Delete and return the last value:', stack.pop())  # Delete and return the last value: 5

# Empty the stack
stack = []
log('Empty the stack:', stack)  # Empty the stack: []

# We can also enclose the stack operations in a class for better organization and reusability
class Stack:
    def __init__(self, initial_items=None):
        # Initialize the stack with an optional list of items
        self.items = initial_items if isinstance(initial_items, list) else []

    def push(self, element):
        # Add an element to the top of the stack
        self.items.append(element)

    def pop(self):
        # Remove the element from the top of the stack
        if self.is_empty():
            log("Stack is empty. Cannot pop an element.")
            return None
        return self.items.pop()

    def peek(self):
        # Retrieve the top element without removing it
        if self.is_empty():
            log("Stack is empty. Cannot peek.")
            return None
        return self.items[-1]

    def empty(self):
        # Empty the stack
        self.items = []

    def is_empty(self):
        # Check if the stack is empty
        return len(self.items) == 0

    def size(self):
        # Get the size of the stack
        return len(self.items)

# Create a new stack instance
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
log('Pop from empty stack2:', stack2.pop())  # Stack is empty. 
# Cannot pop an element. & None

# Queue implementation
# A queue is a linear data structure that follows the First In, First Out (FIFO) principle.
# This means that the first element added to the queue is the first one to be removed.
# You can think of it like a line of people waiting for service: the first person in line is the first to be served.
# Key Operations:
# - Enqueue: Add an element to the end of the queue.
# - Dequeue: Remove the element from the front of the queue.
# - Front/Peek: Retrieve the front element without removing it.
# - IsEmpty: Check if the queue is empty.

# Queue implementation using a list
queue = [8, 5, 4, 2, 1]

# View the contents of a queue
log('View queue:', queue)  # View queue: [8, 5, 4, 2, 1]

# Add elements to the queue
# Add elements to the queue
queue.append(7)
log('Add an element:', queue)  # Add an element: [8, 5, 4, 2, 1, 7]

# Get the size of the queue
log('Size:', len(queue))  # Size: 6

# Get the first value of the queue
log('First value:', queue[0])  # First value: 8

# Remove the first value from the queue and log its value
log('Delete and return the first value:', queue.pop(0))  # Delete and return the first value: 8

# Empty the queue
queue = []
log('Empty the queue:', queue)  # Empty the queue: []

# We can also enclose the queue operations in a class for better organization and reusability
class Queue:
    def __init__(self, initial_items=None):
        # Initialize the queue with an optional list of items
        self.items = initial_items if isinstance(initial_items, list) else []

    def enqueue(self, element):
        # Add an element to the end of the queue
        self.items.append(element)

    def dequeue(self):
        # Remove the element from the front of the queue
        if self.is_empty():
            log("Queue is empty. Cannot dequeue an element.")
            return None
        return self.items.pop(0)

    def front(self):
        # Retrieve the front element without removing it
        if self.is_empty():
            log("Queue is empty. Cannot peek.")
            return None
        return self.items[0]

    def empty(self):
        # Empty the queue
        self.items = []

    def is_empty(self):
        # Check if the queue is empty
        return len(self.items) == 0

    def size(self):
        # Get the size of the queue
        return len(self.items)

# Create a new queue instance
queue2 = Queue([8, 5, 4, 2, 1])
log('Initial queue2:', queue2.items)  # [8, 5, 4, 2, 1]

queue2.enqueue(7)
log('After enqueueing 7:', queue2.items)  # [8, 5, 4, 2, 1, 7]

log('Front:', queue2.front())  # 8

log('Dequeue:', queue2.dequeue())  # 8
log('After dequeueing:', queue2.items)  # [5, 4, 2, 1, 7]

log('Dequeue all elements:')
while not queue2.is_empty():
    log('Dequeued:', queue2.dequeue())
# or we can just empty the queue
# queue2.empty()

log('Final queue2:', queue2.items)  # []
log('Dequeue from empty queue2:', queue2.dequeue())  # Dequeue from empty queue2:. 
# Cannot dequeue an element. & None

 # Additional exercises:

 # Simulate the behavior of the back and forward buttons in a browser.

# List of documents to print
documents_queue = [
    {'name': 'Tratado de Tantra.txt', 'content': 'Here comes the content of Tratado de Tantra.'},
    {'name': 'Nada Sagrado.doc', 'content': 'Here comes the content of Nada Sagrado.'},
    {'name': 'El Blanco Invisible.pdf', 'content': 'Here comes the content of El Blanco Invisible.'}
]

def print_queue(arr):
    if len(arr) == 0:
        log('There are no elements to print in the queue!')
        return
    while len(arr) > 0:
        document = arr.pop(0)  # Get the first document
        log('Printing document:', document['name'])
        log('Content:', document['content'])
    log('There are no more elements to print in the queue!')

print_queue(documents_queue)
# Output:
# Printing document: Tratado de Tantra.txt
# Content: Here comes the content of Tratado de Tantra.
# Printing document: Nada Sagrado.doc
# Content: Here comes the content of Nada Sagrado.
# Printing document: El Blanco Invisible.pdf
# Content: Here comes the content of El Blanco Invisible.
# There are no more elements to print in the queue!

# Simulate the behavior of the back and forward buttons in a browser.

# List of documents to print
documents_queue = [
    {'name': 'Tratado de Tantra.txt', 'content': 'Here comes the content of Tratado de Tantra.'},
    {'name': 'Nada Sagrado.doc', 'content': 'Here comes the content of Nada Sagrado.'},
    {'name': 'El Blanco Invisible.pdf', 'content': 'Here comes the content of El Blanco Invisible.'}
]

def print_queue(arr):
    if len(arr) == 0:
        log('There are no elements to print in the queue!')
        return
    while len(arr) > 0:
        document = arr.pop(0)  # Get the first document
        log('Printing document:', document['name'])
        log('Content:', document['content'])
    log('There are no more elements to print in the queue!')

print_queue(documents_queue)
# Output:
# Printing document: Tratado de Tantra.txt
# Content: Here comes the content of Tratado de Tantra.
# Printing document: Nada Sagrado.doc
# Content: Here comes the content of Nada Sagrado.
# Printing document: El Blanco Invisible.pdf
# Content: Here comes the content of El Blanco Invisible.
# There are no more elements to print in the queue!

# Simulating browser navigation
url_stack = []
current_index = -1  # To keep track of the current position.

def browse_web(url):
    global current_index, url_stack  # Declare these variables as global

    def back():
        global current_index  # Declare current_index as global
        if current_index > 0:
            current_index -= 1
            previous_url = url_stack[current_index]
            log('Location:', previous_url)
        else:
            log("There are no more pages back..")

    def forward():
        global current_index  # Declare current_index as global
        if current_index < len(url_stack) - 1:
            current_index += 1
            next_url = url_stack[current_index]
            log('Location:', next_url)
        else:
            log("There are no more pages forward.")

    if url != 'back' and url != 'forward':
        if current_index < len(url_stack) - 1:
            url_stack = url_stack[:current_index + 1]  # Clear forward if navigation has occurred.
        url_stack.append(url)
        current_index += 1
        log('Location:', url)
    elif url == 'back':
        back()
    elif url == 'forward':
        forward()

# Simulating browsing
browse_web('www.lectura_prospectiva.net')  # Location: www.lectura_prospectiva.net
browse_web('www.test.web')  # Location: www.test.web
browse_web('back')  # Location: www.lectura_prospectiva.net
browse_web('forward')  # Location: www.test.web

# Simulating a simple UI setup (console-based)
def setup_ui():
    log('Retosparaprogramadores #7.')

# Call the UI setup function
setup_ui()

