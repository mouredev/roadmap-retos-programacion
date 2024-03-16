#07 PILAS Y COLAS
"""/*
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 *
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás  de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web. Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se interpretan como nombres de documentos.
 */
https://stackabuse.com/stacks-and-queues-in-python/
 """

#Stacks - LIFO (PILA)

letters = []
# Add letters into the list PUSH
letters.append('c')
letters.append('a')
letters.append('t')
letters.append('g')
print(letters)

# POP letters, the last one 'g' exits first POP
last_item = letters.pop()
print(last_item)

# Another way to delete the last one:
last_item = letters[len(letters) - 1]
del letters[len(letters) - 1]
print(last_item)

# 'c' and 'a' remain
print(letters) # ['c', 'a']

#Queue - FIFO (COLA)

# enqueue. Add elements
animals = []
animals.append('cat')
animals.append('dog')
animals.append('tuna')
animals.append('horse')
print(animals)

# dequeue
first_item = (animals.pop(0))
print(first_item)
print(animals)

# Another way to delete the first position:
first_item = animals[0]
del animals[0]
print(first_item)
print(animals)

#EXTRA I

def runWebMovement():
    listOfWebs = ["abc.es", "facebook.com", "youtube.com", "google.com"]
    #popped = []

    while True:
        movement = input('You can enter the webpage or enter the movement command ("back"/"forward") or "exit": ').lower()
        if movement == "exit":
            print("You are exiting from the web browser.")
            break
        elif movement == "back":
            if len(listOfWebs) > 0:
                listOfWebs.pop()
            else:
                print("You can't go back anymore.")
        elif movement == "forward":
            print("You can't go to the next one.")
        else:
            listOfWebs.append(movement)
    
        print(f"You are in web: {listOfWebs[len(listOfWebs) - 1]}.")

runWebMovement()

#EXTRA II

def printUsingQueues():
    listToPrint = ["toprint01","toprint02","toprint03","toprint04","toprint05","toprint06","toprint07","toprint08","toprint09","toprint10","toprint11"]

    while True:
        instruction = input("Add a new document or print from the queu. (You can exit using: 'Exit'): ").lower()
        if instruction == "print":
            if len(listToPrint) > 0:
                toPrintNow = listToPrint.pop(0)
                print(f"Printing... {toPrintNow}")
            else:
                print("Nothing to print.")
        elif instruction == "exit":
            break
        else:
            listToPrint.append(instruction)
            print(f'"{instruction}" file added to the printer queu.')
        
        print(f"Current files in the queu: {listToPrint}")


printUsingQueues()


