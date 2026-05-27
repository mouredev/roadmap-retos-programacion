
def mensaje ():
    print("Archivo cargado correctamente")

mensaje()

def suma (num1, num2):
    print(num1 + num2)

suma(4, 10)

def resta (num1, num2):
    return (num1 - num2)

print(resta(15, 10))

def funcion1 ():
    def funcion2 ():
        print("Hola, buenas tardes")
    funcion2()

funcion1()

# Funciones del lenguaje
print("Hola")
print(type("Sergio"))
#nombre = input("Cual es tu nombre: ")
#print("Hola " + nombre)


variable_global = "Hola"
def saludo():
    variable_local = "Sergio"
    print(f"{variable_global}, {variable_local}")

saludo()


# DIFICULTAD EXTRA

def numeros(cadena1, cadena2):
    contador = 0
    for i in range (1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{cadena1} y {cadena2}")
        elif i % 3 == 0:
            print(f"{cadena1}")
        elif i % 5 == 0:
            print(f"{cadena2}")
        else:
            print(i)
            contador += 1
    return contador

print(numeros("Es multiplo de 3", "es multiplo de 5"))