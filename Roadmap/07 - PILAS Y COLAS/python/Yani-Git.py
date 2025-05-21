"""
1. Pila (Stack)
Una pila es una estructura de datos que sigue el principio de LIFO ("Last In, First Out" o "Último en entrar, primero en salir").
 Esto significa que el último elemento agregado a la pila será el primero en ser retirado.

🔹 Operaciones principales:

push: Agregar un elemento a la pila.

pop: Eliminar y devolver el último elemento agregado.

peek o top: Ver el último elemento sin eliminarlo.

isEmpty: Verificar si la pila está vacía.

Ejemplo de una pila:
Imagina que tienes una pila de platos, y solo puedes tomar el plato superior.
 Si agregas un nuevo plato, ese plato estará encima de los demás, y para tomar un plato, tienes que tomar el de arriba.

Implementación en Python:
python
Copiar
Editar
# Usamos una lista como pila
pila = []

# Agregar elementos a la pila (push)
pila.append(10)
pila.append(20)
pila.append(30)

print(pila)  # [10, 20, 30]

# Eliminar el último elemento agregado (pop)
ultimo = pila.pop()
print(ultimo)  # 30
print(pila)    # [10, 20]

# Ver el último elemento sin eliminarlo (peek)
top = pila[-1]
print(top)    # 20

2. Cola (Queue)
Una cola sigue el principio de FIFO ("First In, First Out" o "Primero en entrar, primero en salir").
 Es como una fila en una tienda: la primera persona que entra es la primera en ser atendida.

🔹 Operaciones principales:

enqueue: Agregar un elemento a la cola.

dequeue: Eliminar y devolver el primer elemento agregado.

front: Ver el primer elemento sin eliminarlo.

isEmpty: Verificar si la cola está vacía.

Ejemplo de una cola:
Imagina una fila en el banco: la primera persona en llegar es la primera en ser atendida, 
y siempre se agregan nuevas personas al final de la fila.

Implementación en Python:
Aunque las listas pueden usarse para implementar una cola, 
es más eficiente usar la clase deque de la librería collections, 
ya que las listas no son muy eficientes para eliminar elementos al principio.

python
Copiar
Editar
from collections import deque

# Usamos deque como cola
cola = deque()

# Agregar elementos a la cola (enqueue)
cola.append(10)
cola.append(20)
cola.append(30)

print(cola)  # deque([10, 20, 30])

# Eliminar el primer elemento agregado (dequeue)
primer = cola.popleft()
print(primer)  # 10
print(cola)    # deque([20, 30])

# Ver el primer elemento sin eliminarlo (front)
front = cola[0]
print(front)   # 20

"""


"""
🔧 ¿Cuándo usar pilas y colas?
Pilas: Útiles cuando necesitas recordar el orden de las últimas acciones (por ejemplo, navegadores web,
 recursión, deshacer/rehacer).

Colas: Útiles cuando necesitas procesar elementos en el orden en que llegaron (por ejemplo, en sistemas de impresión,
 tareas en segundo plano, procesamiento de datos en orden).

"""


#Pila/Stack (LIFO)


"""
Ejercicio  MoureDev

"""




stack = []


#Push
stack.append(1) 
stack.append(2) 
stack.append(3) 
print (stack)


#pop 

stack_item = stack[len(stack) -1]
del stack [len(stack)- 1]
print (stack_item)
print(stack.pop())
print (stack)


#Cola /Queue  (FIFO)

queue = []


#enqueue 

queue.append (1)
queue.append (2)
queue.append (3)

print (queue)

#dequeue

queue_item = queue [0]
del queue [0]
print(queue_item)

print (queue.pop(0))

print (queue)

"""

Extra

"""


#Web


def web_navigation ():

    stack = []

    while True: 
        action = input("Agrega un URL o escribe: adelante / atras / salir: ").strip().lower() 
        if action == "salir":
            print("Saliendo del navegador web.")
            break
        elif action == "adelante":
            pass
        elif action == "atras":
            if len(stack) > 0:
                stack.pop ()
        else: 
                stack.append(action)

        if len(stack) > 0:
            print(f"Has navegado a la web: {stack [len(stack)-1]}.")
        else: 
            print ("Estas en la pagina de inicio.")

        

web_navigation ()


def shared_printend (): 

    queue = []

    while True: 
    
        action = input("Añade un documento o selecciona imprimir / salir: ")

        if action == "salir":
            break
        elif action == "imprimir":
            if len(stack) > 0:
                print(f"Imprimiendo: {queue.pop (0)}")
        else:
            queue.append(action)

        print(f"Cola de impresión: {queue}")

shared_printend ()

