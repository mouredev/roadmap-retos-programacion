def saludar():
    print("¡Hola, mundo!")


saludar()


def saludar_persona(nombre):
    print("¡Hola,", nombre, "!")


saludar_persona("Juan")


def suma(a, b):
    return a + b


resultado = suma(3, 5)
print("La suma es:", resultado)


def exterior():
    def interior():
        print("¡Función interior!")

    print("¡Función exterior!")
    interior()


exterior()
nombre = "Juan"
longitud = len(nombre)
print("La longitud del nombre es:", longitud)

x = 10  # Variable global


def funcion():
    x = 5  # Variable local
    print("Dentro de la función, x es:", x)


funcion()
print("Fuera de la función, x es:", x)


def imprimir_numeros(texto1, texto2):
    contador = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(texto1 + texto2)
        elif i % 3 == 0:
            print(texto1)
        elif i % 5 == 0:
            print(texto2)
        else:
            print(i)
        contador += 1
    return contador


num_impresiones = imprimir_numeros("Fizz", "Buzz")
print("Número de impresiones:", num_impresiones)
