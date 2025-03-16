
# Funciones básicas que representen las diferentes posibilidades
# Función sin argumentos
def saludo_simple():
    print("Hola!")

print("\nSaludo Simple:")
saludo_simple()


# Función con argumentos
def saludar_persona(nombre):
    print(f"Hola {nombre}!")

print("\nSaludo con argumentos:")
saludar_persona("Dani")


# Función con retorno
def saludar_a_persona(nombre):
    return f"Hola {nombre}"

print("\nSaludo con retorno:")
mensaje = saludar_a_persona("Dani")
print(mensaje)


# Función con argumentos definidos por defecto
def saludo_definido(nombre="Invitado", saludo="Saludos"):
    return f"{saludo}, {nombre}"

print("\nSaludo con valores por defecto:")
mensaje = saludo_definido()
print(mensaje)
print(saludo_definido(nombre="Dani", saludo="Buenos días"))


# *Args
def saludos_varios(*args, saludo="Hola"):
    for arg in args:
        print(f"{saludo}, {arg}")

print("\nSaludo con *args:")
saludos_varios("Pepe", "Maria", "Dani", "Jesus", "Cristobal")


# **kwargs
def saludos_diccionario(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}:{valor}")

print("\nFunción con *kwargs:")
saludos_diccionario(nombre="dani", edad=34, sexo="Hombre")


# Función dentro de otra función
def funcion_exterior(x):
    def funcion_interior(y):
        return y * 2
    resultado = x + funcion_interior(x)
    return resultado

print("\nFunción dentro de otra función:")
print(funcion_exterior(4))   


# Variables LOCAL y variable GLOBAL
variable_global = 5

def variables():
    global variable_global
    variable_local = 10
    print(variable_local + variable_global)

print("\nVariable local + Variable global:")
variables()


# Dificultad Extra:

def prueba_extra(string1, string2) -> int:
    count = 0
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(f"{number} {string1} y {string2}")
        elif number % 3 == 0:
            print(string1)
        elif number % 5 == 0:
            print(string2)
        else:
            print(number)
            count += 1
    return count

print("\nEjercicio (dificultad extra):")
prueba = prueba_extra("Es multiplo de 3", "Es multiplo de 5")
print(f"Se imprimió {prueba} veces el número en vez de el texto")
