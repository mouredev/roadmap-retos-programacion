# Implementación de una Pila (LIFO)
pila = []

# Apilar (push) elementos
pila.append("plato1")
pila.append("plato2")
pila.append("plato3")

print("Pila:", pila)  # ['plato1', 'plato2', 'plato3']

# Desapilar (pop) elementos
ultimo_plato = pila.pop()
print("Plato desapilado:", ultimo_plato)  # plato3
print("Pila después de desapilar:", pila)  # ['plato1', 'plato2']

# Implementación de una Cola (FIFO)
cola = []

# Encolar (enqueue) elementos
cola.append("tarea1")
cola.append("tarea2")
cola.append("tarea3")

print("\nCola:", cola)  # ['tarea1', 'tarea2', 'tarea3']

# Desencolar (dequeue) elementos
primera_tarea = cola.pop(0)  # pop(0) elimina el primer elemento
print("Tarea desencolada:", primera_tarea)  # tarea1
print("Cola después de desencolar:", cola)  # ['tarea2', 'tarea3']
