def funcion_print():
    print("Esto es una funcion")

funcion_print()

def funcion_return():
    return 'Esto es una funcion con return'

print(funcion_return())

def varios_returns():
    return "Hola", "que tal"

saludo, pregunta = varios_returns()
print(saludo)
print(pregunta)

def funcion_1_parametro(param):
    print(f'{param} con parametro')

funcion_1_parametro("funcion")

def funcion_2_parametros(param, param2):
    print(f'{param} {param2} 2 parametros')

funcion_2_parametros("funcion", "con")

def funcion_parametros_default(param='hola'):
    print(f'{param} funcion con valor default')

def returns_variables(*nombres):
    for nombre in nombres:
        print(f"Hola, {nombre}!")

returns_variables("Pepe", "hola", "tests")

# Funciones con dentro de funciones
def funcion_externa():
    def funcion_interna():
        print('Funcion interna')
    funcion_interna()

funcion_externa()


# Funciones de python
print(len("hola como estas"))

# variables locales y globales

var_global = 'Hola'

def funcion():
    var_local = 'Hola2'
    print(f'{var_local}, {var_global}')

# Extra 

def extra(num1, num2):
    count = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{num1}, {num2}")
        elif i % 3 == 0:
            print(num1)
        elif i % 5 == 0:
            print(num2)
        else:
            print(i)
            count +=1
    return i