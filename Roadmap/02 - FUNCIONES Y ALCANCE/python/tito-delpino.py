""" EJERCICIO:
Crea ejemplos de funciones básicas que representen las diferentes
posibilidades del lenguaje:
Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
"""
# Sin parametros ni retorno
def bienvenida():
    print('Bienvenido!!')

bienvenida() # llamamos a la funcion

# Con uno o varios parametros
def area_cuadrado(lado):
    print(lado * lado)

def area_rectangulo(lado1, lado2):
    print(lado1 * lado2)
area_cuadrado(4)
area_rectangulo(3,4)

def saludar(nombre):
    return f'Hola {nombre}'

print(saludar("Pepe"))

def default_saludar(nombre="Usuario", password =1234):
    return f'Hola {nombre} tu contrasenia es {password}'

print(default_saludar('tito', 4567))

def multiples_args():
    return "Usuario", 1234

nombre, password = multiples_args()
print(nombre)
print(password)


# Comprueba si puedes crear funciones dentro de funciones.
def funcion_externa():
    def funcion_interna():
        print('A esta funcion interna la llamamos desde la funcion externa')
    funcion_interna()

funcion_externa() # llamamos a la funcion externa que llama a la interna


# Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
print(len('len va a printear el largo de este string'))
print(max(4,6,7,4,3)) # max printea el maximo de los valores
print(min(4,6,7,4,3)) # min printea el minimo de los valores
print(sum([4,5,6,7,8,6,4]))
print(type('string')) # devuelve el tipo de variable
print(sorted([9,6,8,4,7,5,7,3,6,2,5,1])) # devuelve una lista ordenada
print('tito'.upper())


# Pon a prueba el concepto de variable LOCAL y GLOBAL.
var_global ='Esta variable es accesible desde cualquier parte del codigo'

def funcion_con_variable_local():
    var_local = 'esta variable solo es accesible desde la funcion'
    print(f'print desde funcion de variable global - {var_global}')
    print(f'print desde funcion de variable local - {var_local}')


funcion_con_variable_local()
print(f'print desde fuera de la funcion de variable global - {var_global}')


""" DIFICULTAD EXTRA (opcional):
Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
* La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
    Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
    Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
    Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
    La función retorna el número de veces que se ha impreso el número en lugar de los textos.
"""

def funcion_prueba(string1, string2):
    contador = 0
    for num in range(1,101):
        if num % 3 == 0 and num % 5 == 0:
            print(string1 + string2)
        elif num % 3 == 0:
            print(string1)
        elif num % 5 == 0:
            print(string2)
        else:
            print(num)
            contador += 1
        
    return contador


resultado = funcion_prueba('Fizz', 'Buzz')
print(resultado)