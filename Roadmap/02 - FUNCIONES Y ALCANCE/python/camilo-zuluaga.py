# #02 FUNCIONES Y ALCANCE

print("-Funciones-\n")


# Sin parametros ni retorno
def saludar():
    print("Hola Mundo!")


saludar()


# Con uno o varios parametros
def saludar_usuario(nombre, apellido):
    print(f"Hola {nombre} {apellido}!")


saludar_usuario("Camilo", "Zuluaga")


# Con retorno
def suma(a, b):
    return a + b


resultado = suma(1, 2)
print(resultado)


# Funciones dentro de funciones
print("-Funciones dentro de funciones-\n")


def function1():
    print("Hola desde la funcion 1")

    def function2():
        print("Hola desde la funcion 2 (Anidada)")

    function2()


function1()

# Funciones lambda
x = lambda a, b: a * b  # Función lambda que multiplica dos números
print(x(5, 6))

# Funciones creadas por el lenjuage
print("-Funciones creadas por el lenjuage-\n")
# Ejemplo de sum(), max(), min()

# Sumar numeros de una lista, encontrar el mayor y el menor
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# sum() suma los números de una lista
# max() retorna el número mayor de una lista
# min() retorna el número menor de una lista
print(
    f"""
Suma de los números: {sum(arr)}
Número mayor del array: {max(arr)}
Número menor del array {min(arr)}
    """
)

# Variables locales y globales en funciones
# Variables locales: Son aquellas que se declaran dentro de una función y solo son accesibles dentro de la misma.
# Variables globales: Son aquellas que se declaran fuera de una función y son accesibles desde cualquier parte del código.
print("-Variables locales y globales en funciones-\n")


def foo():
    # Variable local
    s = "Hola Mundo!"
    print(s)


foo()

# print(s) nos daria -> Error, la variable s no existe fuera de la función foo()

a = "Soy una variable global"


def func():
    print(a)


func()


# Palabra reservada global
def myfunc():
    global x  # Si utiliza la palabra clave global, la variable pertenece al ámbito global
    x = "genial!"


myfunc()

print("Python is " + x)


# DIFICULTAD EXTRA
def exercise(a, b):
    contador = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{a}{b}")
        elif i % 3 == 0:
            print(a)
        elif i % 5 == 0:
            print(b)
        else:
            print(i)
            contador += 1
    return contador


resultado = exercise("Python", "Numpy")
print(
    f"Número de veces que se ha impreso el número en lugar de los textos: {resultado}"
)
