# Pilas y Colas

# --- PILAS --- 
array_pila = ['Python', 'Java', 'Rust', 'Go', 'Typescript']
print(array_pila)

# stacks - LIFO
push = lambda x: array_pila.append(x)
pop = lambda: array_pila.pop()

push('Javascript') # -> Agregando elemento
push('Php')
print(array_pila)

pop() # -> Eliminando elemento
print(array_pila)
print()

# --- COLAS ---
array_cola = ['Go', 'Java', 'Javascript', 'Python', 'Rust', 'Typescript']
print(array_cola)

# queue - FIFO
enqueue = lambda x: array_cola.insert(0, x)
dequeue = lambda: array_cola.pop()


enqueue('Dart') # -> Insertando elemento
enqueue('C#')
print(array_cola)

dequeue() # -> Eliminando elemento
print(array_cola)


