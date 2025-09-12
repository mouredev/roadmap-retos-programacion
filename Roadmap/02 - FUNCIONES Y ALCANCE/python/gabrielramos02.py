# 02 Funciones y alcance


# Funcion sin parametros ni retorno
def imprimir_texto():
    print("Esto es un texto dentro de una funcion")


# Funcion con un solo parametro
def imprimir_numero(numero: int):
    print(numero)


# Funcion con varios parametros
def imprimir_suma(num1: int, num2: int):
    print(num1 + num2)


# Funcion con retorno
def devolver():
    return "Hola"


# Funcion con funcion dentro
def fun_externa():
    def fun_interna():
        print("Funcion anidada")

    fun_interna()


# Variables locales y globales
var1 = "Global"


def probando_variables():
    var1 = "Local"
    print(f"Esta variable tiene valor {var1}")


# Ejecucion de funciones
imprimir_texto()
imprimir_numero(3)
imprimir_suma(2, 3)
print(devolver())
fun_externa()
probando_variables()
print(f"Esta variable tiene valor {var1}")


# Funciones del lenguaje
print(float.is_integer(2.3))  # Funcion que permite preguntar si un float es entero

# Dificultad extra

def fun_principal(string1: str,string2: str):
    contador = 0
    for i in range(100):
        if (i+1) % 3 == 0 and (i+1) % 5 == 0:
            print(string1 + string2)
        elif (i+1) % 3 == 0:
            print(string1)
        elif (i+1) % 5 == 0:
            print(string2)
        else: 
            print(i+1)
            contador+=1
    
    return contador

print("Cantidad de iteraciones: ", fun_principal("Cadena 1","Cadena 2"))