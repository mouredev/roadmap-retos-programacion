def suma(a, b):
    return a + b    

print(suma(5, 3))  # Output: 8

def potencia(base, exponente):
    print(base ** exponente)

potencia(3, 3)  # Output: 9

def resta(a=10, b=5):
    return a - b

print(resta())  # Output: 5
print(resta(15, 7))  # Output: 8

def escribe_mensaje(mensaje):
    print(f"Mensaje: {mensaje}")

escribe_mensaje("Hola, este es un mensaje de prueba.")

def escribe_mensaje_con_repeticion(mensaje, repeticiones=10):
    for i in range(repeticiones):
        print(f"Mensaje: {mensaje}")
escribe_mensaje_con_repeticion("Este mensaje se repetirá 10 veces.")

def varios_parametros(**args):
    for clave, value in args.items():
        print(f"Argumento: {clave}, {value}")
varios_parametros(nombre="Juan", edad=30, ciudad="Madrid")

# Funcion de tipado débil comentada
def funcion (a: int, b: int) -> int:
    """
    Esta función toma dos parámetros a y b, y devuelve su suma.Se demuestra el débil tipado de Python
    """
    print(f"a = {a}, b = {b}, a + b = {a + b}")
    return "funcion comentada"

help(funcion)
print(funcion.__doc__)

funcion("Hola", "Mundo") # Output: HolaMundo
funcion(5, 10)  # Output: a + b = 15
funcion(3.5, 2.5)  # Output: a + b = 6.0
funcion(True, False)
funcion("1", "2")

# Ahora los ejemplos de alcance de variables y funciones anidadas
def funcion_externa(x, y):
    def funcion_interna():
        return x + y
    return funcion_interna

funcion_interna = funcion_externa(5, 10)
print(funcion_interna())  # Output: 15

def funcion_externa_con_parametros(x, y):
    def funcion_interna(a=8, b=9):
        return a + b + x + y
    return funcion_interna

#No se puede llamar a la funcion_interna directamente, ya que está definida dentro de funcion_externa_con_parametros.
#Tampoco se le pueden asignar valores a los parámetros a y b de la función interna, ya que no se puede acceder a ellos desde fuera de la función externa.
funcion_interna = funcion_externa_con_parametros(5, 10)
print(funcion_interna())  # Output: 32


#Ahora vamos a ver el alcance de las variables globales y locales
global_variable = "Soy una variable global"
global_variable_efimera = "Soy una variable global efimera en la funcion, después me mantengo"
def funcion_con_variable_global():
    global global_variable
    local_variable = "Soy una variable local"
    global_variable = "He sido modificada dentro de la función"
    global_variable_efimera = "He sido modificada dentro de la función, pero no me mantengo fuera de la función"    
    print(global_variable)
    print(global_variable_efimera)

funcion_con_variable_global()  # Output: He sido modificada dentro de la función

print(global_variable)  # Output: He sido modificada dentro de la función, la modificación de la variable global se mantiene fuera de la función
# por la sentncia global!!!
print(global_variable_efimera)

try:
    print(local_variable)  # Output: NameError: name 'local_variable' is not defined
except NameError:
    print(f"Error has llamado a una variable local que no está definida fuera de la función")

#Extra

def parametros (cadena1, cadena2):
    cuenta = 0
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print(f"Número: {cadena1} {cadena2}") 
        elif num % 3 == 0:
            print(f"Número: {cadena1}")
        elif num % 5 == 0:
            print(f"Número: {cadena2}")    
        else:
            cuenta += 1
            print(f"Número: {num} {cuenta}")


parametros("fizz", "buzz")  # Output: Números del 1 al 100