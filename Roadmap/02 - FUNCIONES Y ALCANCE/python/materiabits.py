#FUNCIONES Y ALCANCE DE LA FUNCION
"""Funciones definidas por el usuario"""

#Simple
def saludo():
    print("Hola, bienvenido a la clase de Python")  

saludo()
#saludo()

#Funciones con retorno
def retorna_saludo():
    return "Hola, bienvenido a la clase de Python RETORNADO"

greet = retorna_saludo()
print(greet)

#Funciones con parametros
def saludo_parametros(nombre):
    print(f"Hola {nombre}, bienvenido a la clase de Python")

saludo_parametros("Leandro")

def saludo_parametros_retorno(saludo,nombre):
    return f"{saludo} {nombre}, bienvenido a la clase de Python"

print(saludo_parametros_retorno("Bon giorno","Nany"))

#fUNCION con retorno de varios valores
def operaciones_matematicas(a,b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return suma, resta, multiplicacion, division

operaciones = operaciones_matematicas(10,5)
print(f"Operaciones matematicas: {operaciones}")


#FUncionaes CON PARAMETROS VARIABLES
def suma_numeros(*args):
    suma = 0
    for numero in args:
        suma += numero
    return suma

print(f"Suma de numeros: {suma_numeros(1,2,3,4,5)}")

#funciones con parametros y asociados a claves
def saludo_claves(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

saludo_claves(nombre="Leandro", edad=30, ciudad="Buenos Aires")

#funcion dentro de otra funcion
def funcion_externa():
    print("Esta es la funcion externa")
    
    def funcion_interna():
        print("Esta es la funcion interna")
    
    funcion_interna()

funcion_externa()