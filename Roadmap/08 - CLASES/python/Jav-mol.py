### Clases ###

class MiClasePersona:
    def __init__(self, nombre:str, apellido:str) -> None:
        self.nombre = nombre
        self.apellido = apellido
    
    def imprimir_atributos(self) -> None:
        print(f'Atributos de la clase: \n[{self.nombre} - {self.apellido}]')
    
    def __str__(self) -> str:
        return f'Nombre: {self.nombre} - Apellido: {self.apellido}'
    
# Inicializando la clase

mi_clase_persona = MiClasePersona('Javier', 'Molina')

mi_clase_persona.imprimir_atributos() # Llamando una funcion
print(mi_clase_persona) # Por defecto se llama la funcion __str__ al imprimir el objeto


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
