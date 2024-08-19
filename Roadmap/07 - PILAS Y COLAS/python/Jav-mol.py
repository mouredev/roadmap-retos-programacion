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
print()


# --- Extra ---

class NavegadorWeb():
    def __init__(self) -> None:
        self.web = ['https://github.com','/mouredev', '/roadmap-retos-programacion']
        self.index = 1

    def adelante(self):
        print(self.index)
        if self.index < len(self.web):
            self.index += 1
        print("".join(self.web[0:self.index]))
        cadena_guines()
        
    def atras(self):
        if self.index > 1:
            self.index -= 1
        print("".join(self.web[0:self.index]))
        cadena_guines()
    
    def agregar_web(self, web):
        self.web.append(web)
        print("".join(self.web))
        cadena_guines()
            
            
navegador = NavegadorWeb()

cadena_guines = lambda:print('-'*30)

menu = '''Adelate - Siguiente Pagina Web
Atras - Anterior Pagina Web
Exit/q - Salir del Programa
"Cualquier-Cadena" - Agrega una Nueva Pagina Web
=> '''

options = {
    'ad':navegador.adelante,
    'at':navegador.atras,
    'exit':False,
    'q':False
}

while True:
    cadena_guines()
    option = input(menu).lower()
    if not option in options.keys():
        navegador.agregar_web(option)
        continue
    
    x = options.get(option)

    if not x:
        break   
    x()
    print()
