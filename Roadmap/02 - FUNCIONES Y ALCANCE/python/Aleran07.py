# 02
# Primero que son funciones basicas que representen las diferentes posibilidades de


# funcion con parametro
def mi_funcion(x): # Funcion con parametro
    #codigo
    print("what's up bro?")
    return

mi_funcion(1) # si o si toca enviarle un parametro para que se ejecute asi no haga nada con ese parametro

# funcion sin parametro
def mi_funcion_sin_parametro():
    print("Aqui no se usa parametro")
    return

mi_funcion_sin_parametro()

# funcion sin parametro pero con retorno
def funcion_sin_parametro_pero_con_retorno(): # las funciones puedes nombrarse de forma larga
    return "que pedo"

x = funcion_sin_parametro_pero_con_retorno() # aqui la funcion se crea para que retorne algo
print(x)

# funcion con parametro y retorno
def sumar(a, b):
    return a + b

print(sumar(2, 5))

# funciones con parametros por defecto
def saludar(name="invitado"):
    print(f"Hola, {name}")

saludar()
saludar("boludo")

# funciones con parametros variables
def mostrar_args(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

mostrar_args(1, 2, 3, name="Brian", age=24)

"""
Por lo tanto los parametros son datos que la funcion necesita.
Mientras que el retorno es el resultado que entrega la funcion
"""

# funciones anidadas
def funcion_externa():
    print("Soy la función externa")

    def funcion_interna():
        print("Soy la función interna")

    # Llamamos a la interna dentro de la externa
    funcion_interna()

# Ejecuto la externa
funcion_externa()
# funcion_interna() son puede ser llamada fuera de la funcion mas grande

# funcion interna con retorno
def externa(x):
    def interna(y):
        return y * 2
    return interna(x)

print(externa(5))  # 10

# funcion closure
def multiplicador(n):
    def multiplicar(x):
        return x * n
    return multiplicar

doble = multiplicador(2)
triple = multiplicador(3)

print(doble(5))   # 10
print(triple(5))  # 15
print(doble(2))   # 4

# Ejemplo random
def caluladora_simple(x, tipo):
    def suma(y):
        return x + y
    def restar(y):
        return x - y
    def multiplicar(y):
        return x * y
    def dividir(y):
        return x / y
    # return {"sumar": suma, "restar": restar, "multiplicar": multiplicar, "dividir": dividir}
    if tipo == "suma":
        return suma
    elif tipo == "restar":
        return restar
    elif tipo == "multiplicar":
        return multiplicar
    elif tipo == "dividir":
        return dividir

x = caluladora_simple(2, "suma")
y = x(3)
print(y)

x = caluladora_simple(2, "restar")
y = x(3)
print(y)

x = caluladora_simple(2, "multiplicar")
y = x(3)
print(y)

x = caluladora_simple(2, "dividir")
y = x(3)
print(y)



def calculadora(n):
    def sumar(x):
        return x + n
    def multiplicar(x):
        return x * n
    def restar(x):
        return x - n

    # Retorno un diccionario con varias funciones
    return {"sumar": sumar, "multiplicar": multiplicar, "restar": restar}

ops = calculadora(10)

print(ops )        # 15
print(ops )  # 50
print(ops )       # -5



x = 10  # variable global

def mostrar():
    print(x)  # puede acceder a la global

mostrar()      # 10
print(x)       # 10

###
def funcion():
    y = 5  # variable local
    print(y)

funcion()   # 5
# print(y)    # ❌ Error: NameError (no existe fuera de la función)



# Crear una funcion que que reciba 2 para metros de texto y retorne los numeros del 1 al 100
def cadena_num(a, b):
    x = 0
    y = 0
    for i in range (1, 101):
        if i % 3 == 0:
            x += 1
            print(a)
        elif i % 5 == 0:
            x += 1
            print(b)
        else:
            y += 1
            print(i)
    return print(f"Numero de numeros impresos: {y}\nNumero de Textos impresos: {x}")

cadena_num("tres", "cinco")