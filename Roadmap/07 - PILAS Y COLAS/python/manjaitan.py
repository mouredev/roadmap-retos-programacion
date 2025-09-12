'''
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 *
 '''

# añadimos elementos a una pila1.

pila1 = []
pila1.append(1)
print (pila1)
pila1.append(2)
print (pila1)
pila1.append(3)
print (pila1)

# retiramos elentos de la pila con el metodo pop

pila1.pop()
print (pila1)
pila1.pop()
print (pila1)
pila1.pop()

# Añadimos elementos de nuevo a la pila.,

pila1.append(4)
pila1.append(5)
pila1.append(6)

print (pila1)


# Sale el primero que entra, FIFO.

pila1.pop(0)
print (pila1) # Desaparece de la pila el 4.

### EXTRA ####

