import os
import time
import unicodedata

clear = lambda: os.system('cls')
clear()

class Pila:
    def __init__(self):
        # Define elems list of the stack
        self.items = []
    
    def Add(self, elem):
        # Add elem to the stack
        if type(elem) == list:
            self.items += elem
        else:
            self.items.append(elem)
            
    def Take(self):
        # Return last elem from the stack
        return self.items.pop()

class Cola:
    def __init__(self):
        # Define elems list of the stack
        self.items = []
    
    def Add(self, elem):
        # Add elem to the stack
        if type(elem) == list:
            self.items += elem
        else:
            self.items.append(elem)
    
    def Take(self):
        # Return first elem from the queue
        return self.items.pop(0)
    
## EXTRA ##
    
def elimina_tildes(cadena):
    s = ''.join((c for c in unicodedata.normalize('NFD',cadena) if unicodedata.category(c) != 'Mn'))
    return s

def wait_and_clear(t):
    time.sleep(t)
    clear()

# Program 1 (Navegador)
def navegador():
    pila = Pila()

    while True:
        # Ask user what to do
        t = 2
        print("Estamos navegando ¿Qué desea hacer ahora?")
        userIn = input()

        if userIn.lower() == "end":
            break
        else:
            #Look for command
            command = [userIn.lower().find("adelante") > -1,elimina_tildes(userIn.lower()).find("atras") > -1]
        
        # Execution
        if all(command):
            # Both commands where sent, do nothing
            print("Error, no se puede ir adelante y atrás al mismo tiempo")

        elif command[0]:
            # ADELANTE
            pila.Add(userIn[len("adelante")+1:])
            print("Avanzamos a " + pila.items[-1])
            t = 1.5

        elif command[1]:
            # ATRÁS
            if not pila.items:
                # pila is empty
                print("No hay dirección anterior a la actual")
            else:
                # Return to previous adress
                print("Regresamos a " + pila.Take())

        else:
            # No commands where sent
            print('No hay comandos. Use adelante o atrás para navegar')
            
        wait_and_clear(t)

# Program 2 (Cola impresión)
def cola_impresion():
    cola = Cola()

    # Ask user what to do
    while True:
        t = 1
        print("INSTRUCCIONES PARA LA IMPRESORA. ESCRIBA IMPRIMIR O AÑADA UN ELEMENTO A LA COLA")
        userIn = input()

        # Execution
        if userIn.lower() == "end":
            break
        elif userIn.lower().find("imprimir") > -1:
            # Print
            print("Procedemos a imprimir " + str(cola.Take()) + ". Quedan " + str(len(cola.items)) + " elementos en la cola de impresión.")
            t = 2
        else:
            # Add elem to queue
            cola.Add(userIn)
            print(userIn + " ha sido añadido a la cola de impresión")
        
        wait_and_clear(t)

# navegador()
# cola_impresion()