#### Funciones
def saludar():
    print("Hola Mundo!")

saludar()
    
def saludar2(nombre):
    print("Hola", nombre)
    
saludar2("Hernan")

def suma(a, b):
    return a + b

print(suma(2, 3))

def funcion_anidada():
    print("Esto es una funcion anidada")
    
    def funcion_anidada2():
        print("Esto es una funcion anidada 2")
        
    funcion_anidada2()
    
funcion_anidada()

## Variables locales y globales en funciones

def variable_local():
    variable_local = "Valor variable local"
    print(variable_local)
    
variable_local()

variable_global = "Valor variable global"

def variable_global():
    global variable_global
    variable_global = "Nuevo valor variable global"
    print(variable_global)
    
variable_global()

## Ejercicio Extra
def extra(texto1, texto2):
    contador = 0
    
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{texto1}{texto2}")
        elif i % 3 == 0:
            print(texto1)
        elif i % 5 == 0:
            print(texto2)
        else:
            print(i)
            contador += 1
            
    return contador

print(extra("Python", "Django"))