#### PATRONES DE DISEÑO: DECORADORES

'''
El Patrón Decorador es un patrón estructural que permite añadir funcionalidades a un objeto dinámicamente sin modificar su estructura original. 
Es especialmente útil cuando necesitas extender las capacidades de una clase de manera flexible y reutilizable.

En Python, este concepto también está integrado en el lenguaje a través de la sintaxis de decoradores, 
que simplifica el uso del patrón.
'''

# Ejemplo básico con una función decoradora
def decorador(funcion):
    def wrapper(*args, **kwargs):
        print("Antes de ejecutar la función")
        result = funcion(*args, **kwargs)
        print("Después de ejecutar la función")
        
        return result
    
    return wrapper

@decorador
def saludo(name):
    print(f'Hola {name}, estás siendo saludado desde un decorador')
    
saludo("Manuel")

# En lugar de funciones también se pueden usar decoradores con Clases
class DecoradorClase():
    def __init__(self, function):
        self.function = function
    
    def __call__(self, *args, **kwargs):
        print("Antes de ejecutar la función")
        result = self.function(*args, **kwargs)
        print("Después de ejecutar la función")
        
        return result

@DecoradorClase
def saludo(name: str):
    print(f'Hola {name}, ahora el decorador es de clase')

saludo("Otra vez Manuel")

### EJERCICIO EXTRA
class DecoradorContador():
    
    count = 0
    
    def __init__(self, function):
        self.function = function
        
    def __call__(self, *args, **kwds):
        result = self.function(*args, **kwds)
        self.count += 1
        print(f'La función se ha ejecutado {self.count} veces')
        return result

@DecoradorContador    
def saludo(name: str):
    print(f'Hola {name}')

names = ['Antonio', 'Rita', 'Gabriel']

for name in names:
    saludo(name)


### FIN EJERCICIO EXTRA
#### FIN PATRONES DE DISEÑO: DECORADORES
