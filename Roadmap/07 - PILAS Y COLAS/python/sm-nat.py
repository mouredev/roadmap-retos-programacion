#Pila (Stack - LIFO)
pila = []

pila.append(1)
pila.append(2)
pila.append(3)

print("Pila después de los push:", pila)  

ultimo_elemento = pila.pop()

print("Elemento eliminado (pop):", ultimo_elemento) 
print("Pila después del pop:", pila) 

#Cola (Queue - FIFO)
cola = []

cola.append(1)
cola.append(2)
cola.append(3)

print("Cola después de los enqueue:", cola) 

primer_elemento = cola.pop(0)

print("Elemento eliminado (dequeue):", primer_elemento)  
print("Cola después del dequeue:", cola)  
