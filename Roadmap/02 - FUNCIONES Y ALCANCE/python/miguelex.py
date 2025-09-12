# Funcion simple

def saludar():
    print("Hola, soy una función simple")
    
saludar()

# Funcion con return
def suma(a,b):
    return a+b

print(suma(5,6))

# Funcion con parametro
def saludar(nombre):
    print(f"Hala, un {nombre} ha entrado en la sala")
    
saludar("Miguelex")

# Funcion con parametros por defecto
def saludar(nombre="Miguelex"):
    print(f"Hala, un {nombre} ha entrado en la sala")
    
saludar()
saludar("Juan")

# Funcion que devuelve varios valores
def varios():
    return "Pepi", "Lucy", "Boom"
x, y, z = varios()
print(x)
print(y)
print(z)

# Funcion con numero variable de parametros
def varios(*args):
    for arg in args:
        print(arg)
varios(2,4,6,8,10)

# Funcion lambda
suma = lambda a,b: a+b
print(suma(5,6))

# Funcion con funcion interior
def funcion_exterior():
    def funcion_interior():
        print("Soy una funcion interior")
    print("Soy una funcion exterior")
    funcion_interior()
    
funcion_exterior()

# Ejemplos de funciones del sistema
print(len("Miguelex"))
print(str(5))

# Ejercicio Extra

def extra(param1, param2) -> int:
    count = 0
    for number in range(1, 101):
        if number % 15 == 0:
            print(param1 + param2)
        elif number % 3 == 0:
            print(param1)
        elif number % 5 == 0:
            print(param2)
        else:
            print(number)
        count += 1
    return count

extra("Fizz", "Buzz")
