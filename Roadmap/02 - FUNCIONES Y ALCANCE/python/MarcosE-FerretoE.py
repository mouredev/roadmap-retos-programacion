# Funciones ya creadas en el lenguaje
print(len("Hola mundo"))
print(type("Hola"))
print("Python".upper())


# Funciones


def funcion_hola():
    print("Hola mundo")


def funcion_pass():
    # Función sin parámetros y sin retorno
    pass


def suma(a, b):
    # Función con parámetros y retorna una suma
    return a + b


def funcion_dentro_funcion(a):
    # Función dentro de una función
    def suma(b):
        return a + b
    return suma


funcion_hola()

print(funcion_pass())

a = 10
b = 14

# F-string para imprimir el resultado de la función suma
print(f"Este es el resultado de una función que suma dos números: {
      suma(a, b)}")

a = 34
b = 54

sumar = funcion_dentro_funcion(a)

# F-string para imprimir el resultado de la función dentro de otra función
print(f"Este es el resultado de una suma que tiene una función dentro de otra función: {
      sumar(b)}")

# Variable global
numero_uno_global = 45


def variable_local_global():
    # Variable local
    numero_dos_local = 32

    print(f"El valor de la variable local es: {numero_uno_global}")
    print(f"El valor de la variable global es: {numero_dos_local}")


variable_local_global()


def numeros_textos(cadena_uno, cadena_dos):
    contador = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(cadena_uno + cadena_dos)
        elif i % 3 == 0:
            print(cadena_uno)
        elif i % 5 == 0:
            print(cadena_dos)
        else:
            print(i)
            contador += 1

    return contador


print(numeros_textos("Helado", "Ice Cream"))
