# Funciones sin argumentos
def saludar():
    print("Hola, ¿como estas?")


saludar()


# Funciones con argumentos
def saludar(nombre):
    print(f"Hola, {nombre} ¿como estas?")


saludar("Christian")


# Funciones con argumentos posicionales
def saludar(nombre, apellido):
    print(f"Hola, {nombre} {apellido} ¿como estas?")


saludar("Christian", "Siles")


# Funciones con argumentos de palabra clave
def saludar(apellido, nombre, saludo="Hola"):
    print(f"{saludo}, {nombre} {apellido} ¿como estas?")


saludar("Siles", "Christian")


# Funciones con argumentos predeterminados
def saludar(saludo="Hola", nombre="Christian", apellido="Siles"):
    print(f"{saludo}, {nombre} {apellido} ¿como estas?")


saludar()


# Funciones con retorno
def saludar():
    return "Hola, ¿como estas?"


print(saludar())


# Funciones recursivas
def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)


print(factorial(5))

# Funciones lambda
suma = lambda x, y: x + y
print(suma(2, 3))


# Funciones dentro de funciones
def saludar_(nombre):
    print(f"Hola, {nombre}")

    def ayuda():
        print("Por favor, ponte en contacto conmigo")

    ayuda()


saludar_("Christian")

# Extra

def retorna_numero(cadena_1, cadena_2):
    contador = 0
    for numero in range(1, 101):
        if numero % 3 == 0 and numero % 5 == 0:
            print(cadena_1 + " y " + cadena_2)
        elif numero % 3 == 0:
            print(cadena_1)
        elif numero % 5 == 0:
            print(cadena_2)
        else:
            print(numero)
            contador += 1
    return print(f"Los mumeros han sido impreso {contador} veces")

retorna_numero("hola", "chau")
