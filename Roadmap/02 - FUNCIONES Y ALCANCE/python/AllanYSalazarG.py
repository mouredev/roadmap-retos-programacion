"""#02 FUNCIONES Y ALCANCE"""


saludoVar = "Hola global"  # Variable global


def saludo():
    print("Hola Mundo")


def saludoUsuario(usuario):
    saludoVar = "Hola"  # Variable local, no es igual a la variable saludo en la L4
    # son variables diferentes almacenadas en distinto lugar de memoria
    print(f"{saludoVar} {usuario}")


def saludoUsuarioValidado(usuario, validado):
    if validado == 1:
        print(f"Hola {usuario}, haz sido validado")
        return validado
    else:
        print(f"El usuario {usuario} no existe")


saludo()
saludoUsuario("AllanYSalazarG")
confirmado = saludoUsuarioValidado("allansalazar", 0)
print(confirmado)


# verificando si se puede agregar una función dentro de otra
# al parecer no se puede, cuando intentas llamar a hola() fuera de la funcion saludoAdicional,
# Las funciones trabajan igual que variables globales y locales
# sale error de variable no definida siendo que es función
def saludoAdicional():
    def hola():
        print("Como estás, soy una funcion dentro de otra\n\n")
    hola()


saludoAdicional()
# hola()

""" El código de bloque anterior ⬆️ se lo agradezco a alexdevrep, miré su código y entendí
el funcionamiento de una función dentro de otra, yo creía que no se podría porque 
la intentaba llamar fuera de saludoAdicional() (Comprendiendo más sobre el alcance en python)"""

# Funciones de python

""" # print, muestra en consola lo que esté dentro de los parentesis
print("Hola otra vez")
# range, el valor dentro indica cuando debe parar, devuelve una lista
for numero in range(10):
    print(numero, end="-")
# input, espera que el usuario ingresa algun dato
numeroIngresado = input("\nIngresa un numero: ")
# int, transforma a enteros los valores ingresados por input
numeroIngresado = int(numeroIngresado)
if numeroIngresado.is_integer:
    print("Es entero") """


# Ejercicio extra

print("EJERCICIO ADICIONAL: \n")


def palabra(primera, segunda):
    contador = 0
    for numero in range(1, 101):
        if numero % 3 == 0 and numero % 5 == 0:
            print(f"{primera}, {segunda}", end=" | ")
        elif numero % 5 == 0:
            print(f"{segunda}", end=" | ")
        elif numero % 3 == 0:
            print(f"{primera}", end=" | ")
        else:
            print(numero, end=" | ")
            contador += 1
    return contador


contadorFinal = palabra("Hola", "Mundo")
print(f"\n\nNúmeros impresos en lugar de textos: {contadorFinal}")
