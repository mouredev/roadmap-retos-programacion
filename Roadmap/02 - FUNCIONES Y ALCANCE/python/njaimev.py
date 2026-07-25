# Los parametros son las variables que se definen entre () en la declaracion de una funcion.
# Return es una instruccion que se usa dentro de una funcion para devolver un valor
# o resultado al lugar donde fue llamada.

# Como no comprendo muy bien lo de return, pondre un ejemplo:
def sumar(a, b):
    resultado = a + b
    return resultado

# Llamada a la función y uso del valor de retorno
suma = sumar(5, 3)
print(suma)  # Salida: 8
# return resultado FINALIZA la funcion sumar.
# resulado es el valor devuelto al codigo que llamó a la funcion.
# la variable suma almacena el valor devuelto (8).

# 1. Funcion sin parámetros ni retorno
# esta no recibe ningún parámetro y no devuelve nada, solo ejecuta su tarea y termina
def saludar():
    print("Hola, bienvenido!")

saludar()

# 2. Función con parámetro pero sin retorno
# recibe parámetros para realizar una operación, pero no devuelve ningun valor
def saludar(nombre):
    print(f"Hola, {nombre}!")

saludar("Ana")

# 3. Función sin parámetros pero con retorno
# no recibe parámetros, pero devuelve un valor
def obtener_mensaje():
    return "Este es un mensaje de prueba."

mensaje = obtener_mensaje()
print(mensaje)

# 4. Funcion con parámetros y retorno 
# recibe parametros y devuelve un valor, se usa para calculos o transformaciones
def sumar(a, b, c):
    return a + b + c

resultado = sumar(3, 5, 4)
print(resultado)

# 5. Funcion con parametros predeterminados
# si no se pasa un valor, usa el predeterminado 
def saludar(nombre="invitado"):
    print(f"Hola, {nombre}!")

# Llamada a la función sin y con un argumento
saludar()         # Salida: Hola, invitado!
saludar("Carlos") # Salida: Hola, Carlos!

# 6. Funcion con un numero variable de parámetros
# usa *args o **kwargs, aceptando un numero arbitrario de argumentos
def sumar_varios(*numeros):
    return sum(numeros)

# Llamada a la función con múltiples argumentos
resultado = sumar_varios(1, 2, 3, 4, 5)
print(resultado) # Salida: 15

# *args recibe un numero indeterminado de argumentos en forma de tupla (que no puede cambiarse 
# el orden)
def sumar(*numeros):
    total = sum(numeros)
    return total

print(sumar(1, 2, 3, 4))  # Salida: 10

# **kwargs recibe un numero indeterminado de argumentos nombrados tipo clave-valor en forma 
# de diccionario
def mostrar_informacion(**info):
    for clave, valor in info.items():
        print(f"{clave}: {valor}")

mostrar_informacion(nombre="Ana", edad=25, ciudad="Madrid")
# Salida:
# nombre: Ana
# edad: 25
# ciudad: Madrid


# Una función dentro de otra función se llama función anidada
# esta función interna solo puede usarse dentro de la función externa, no se puede acceder 
# a ella fuera de esta.
def calcular_total_pedido(pedido):
    # Función interna para verificar condiciones
    def verificar_pedido():
        if not pedido:  # Verifica si el pedido está vacío
            print("El pedido está vacío.")
            return False
        if sum(pedido.values()) <= 0:  # Verifica que el total sea positivo
            print("El total del pedido no puede ser cero o negativo.")
            return False
        return True
    
    # Si las condiciones se cumplen, calcula el total
    if verificar_pedido():
        total = sum(pedido.values())
        print(f"El total del pedido es: {total}")
    else:
        print("No se pudo calcular el total.")

# Ejemplos de uso
pedido_valido = {"item1": 15, "item2": 30}
pedido_vacio = {}
pedido_invalido = {"item1": -10, "item2": -20}

calcular_total_pedido(pedido_valido)    # Salida: El total del pedido es: 45
calcular_total_pedido(pedido_vacio)     # Salida: El pedido está vacío.
calcular_total_pedido(pedido_invalido)  # Salida: El total del pedido no puede ser cero o negativo.


# variables globales: se definen fuera de cualquier función y son accesibles de cualquier parte
# del programa (incluidas funciones)

x = 10  # Variable global

def imprimir_valor():
    print(x)  # Puede acceder a la variable global

imprimir_valor()  # Salida: 10

# Variable local: se definen dentrode una función y solo es accesible dentro de esta.

def calcular_suma():
    y = 5  # Variable local
    return y + 10

print(calcular_suma())  # Salida: 15



# Si se quiere modificar una variable global dentro de una función se debe usar la 
# palabra global 

z = 20  # Variable global

def modificar_variable():
    global z
    z = 30  # Modifica la variable global

modificar_variable()
print(z)  # Salida: 30

# DIFICULTAD EXTRA (opcional):
 # Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 # - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 #   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 #   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 #   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 #   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.

def print_num(str_1, str_2) -> int:
    count = 0
    for num in range (1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print(str_1 + str_2)
        elif num % 3 == 0:
            print(str_1)
        elif num % 5 == 0:
            print(str_2)
        else:
            print(num)
            count += 1
    return count

print(print_num("Mult3", "Mult5"))

# Se imprime al final el resultado del return que sería cuantas veces se imprimieron numeros.