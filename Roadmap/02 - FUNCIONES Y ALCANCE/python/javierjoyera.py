#Función sin parámetros	ni retorno
print("-----------------------------------------")
print("Función sin parámetros ni retorno")
print("-----------------------------------------")
def function_sin_parametro():
    print("Esta es una función sin parametros")

#Llamada a la función
function_sin_parametro()

#Función con parámetros
print("-----------------------------------------")
print("Función con parámetros y retorno")
print("-----------------------------------------")
def suma(a, b):
    resultado = a + b
    return resultado
    

#Llamada a la función
resultado_suma = suma(2, 8)
print("El resultado de la suma es: %d" % resultado_suma)

#Función con parámetros
print("-----------------------------------------")
print("Función con parámetros")
print("-----------------------------------------")
def function_con_parametro(parametro):
    print("Este es el parametro a imprimir: %s" % parametro)

#Llamada a la función
function_con_parametro("Jdelarubia - Dev")

#Función dentro de una función
print("-----------------------------------------")
print("Función dentro de una función")
print("-----------------------------------------")

def function_dentro_de_function():
    print("Esta es la función principal")
    def function_dentro():
        print("Esta es la función dentro de la función principal")
    function_dentro()

#Llamada a la función
function_dentro_de_function()

#Variable global y local
print("-----------------------------------------")
print("Variable global y local")
print("-----------------------------------------")
variable_global = "1999"

def function_variable_local():
    variable_local = "2999"
    print(variable_local)
    print(variable_global)

#Llamada a la función
function_variable_local()

print("La variable global es: %s" % variable_global)

#Funciones del lenguaje
print("-----------------------------------------")
print("Funciones del lenguaje")
print("-----------------------------------------")

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#Función len
print("La longitud de la lista es: %d" % len(lista))

#Función type
print("El tipo de la variable lista es: %s" % type(lista))

#Función range
print("La lista generada con la función range es: %s" % list(range(14)))

cadena_texto = "Jdelarubia - Dev"
#Función upper
print("La cadena de texto en mayúsculas es: %s" % cadena_texto.upper())

#Función lower
print("La cadena de texto en minúsculas es: %s" % cadena_texto.lower())

#Función capitalize
print("La cadena de texto con la primera letra en mayúsculas es: %s" % cadena_texto.capitalize())

#Función count
print("La cadena de texto tiene %d letras 'a'" % cadena_texto.count("a"))




#EJERCICIO EXTRA 
def imprimir_numeros_con_condiciones(cadena1, cadena2):
    contador = 0

    for numero in range(1, 101):
        mensaje = ""

        if numero % 3 == 0:
            mensaje += cadena1

        if numero % 5 == 0:
            mensaje += cadena2

        if mensaje == "":
            mensaje = numero  # Si no es múltiplo de 3 ni de 5, muestra el número

        print(mensaje)
        contador += 1

    return contador


veces_impreso = imprimir_numeros_con_condiciones("cadena_1", "cadena_2")
print("Número de veces impreso: %d" % veces_impreso)