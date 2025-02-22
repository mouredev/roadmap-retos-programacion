# Funciones 

# Funcion Basica
"""
def nombre_de_la_funcion(parametros):
    # Cuerpo de la funcion
    return valor
"""


"""
    def: Palabra clave que define la funcion
    nombre_de_la_funcion: Nombre que se le da a la funcion
    parametros: Argumentos que la funcion puede recibir (opcional)
    return: Devuelve un valor al finalizar la funcion (opcional)
""" 

def saludar():
    print('¡Hola, mundo!')

saludar()


# Funcion con parametros
def sumar(a, b):
    resultado = a + b
    return resultado

resultado = sumar(3, 2)
print(resultado)

# Funciones con valores por defecto
def saludar(nombre='Usuario'):
    print(f'¡Hola, {nombre}!')

saludar()
saludar('Diego')

# Funciones con retorno
def multiplicar(a, b):
    return a * b

resultado = multiplicar(4, 5)
print(resultado)

# Funciones con multiples valores de retorno
def operaciones(a, b):
    suma = a +b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return suma, resta, multiplicacion, division

resultados = operaciones(10, 2)
print(resultados)

# Desempaquetar los valores
s, r, m, d = operaciones(10, 2)
print(r)


# Funciones con argumentos variables
# *args -> Lista de argumentos
def sumar_todo(*args):
    return sum(args)

print(sumar_todo(1,2,3,4))

# **kwargs -> Diccionario de argumentos
def mostrar_info(**kwargs):
    for clave, valor in kwargs.items():
        print(f'{clave}: {valor}')

mostrar_info(nombre='Juan', edad=25, ciudad='Madrid')


# Funciones dentro de funciones
def exterior():
    print('Estoy en la funcion exterior')

    def interior():
        print('Estoy en la funcion interior')

    interior()

exterior()


# Funcion lambda
multiplicar = lambda a, b: a * b
print(multiplicar(3, 4))


# Extra
def imprimir_numeros(text1, text2) -> int:
    contador = 0
    for numero in range(1, 101):
        if numero % 3 == 0 and numero % 5 == 0:
            print(text1 + text2)
        elif numero % 3 == 0:
            print(text1)
        elif numero % 5 == 0:
            print(text2)
        else:
            print(numero)
            contador += 1
    return contador

print(imprimir_numeros('Fizz', 'Buzz'))