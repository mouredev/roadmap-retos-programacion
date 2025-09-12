'''
EJERCICIO:
- Crea ejemplos de funciones básicas que representen las diferentes
posibilidades del lenguaje:
Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
- Comprueba si puedes crear funciones dentro de funciones.
- Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
- Pon a prueba el concepto de variable LOCAL y GLOBAL.
- Debes hacer print por consola del resultado de todos los ejemplos.
(y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)

DIFICULTAD EXTRA (opcional):
Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
- La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
- Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
- Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
- Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
- La función retorna el número de veces que se ha impreso el número en lugar de los textos.

Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
'''

#------------------FUNCIOINES SIN PARAMETROS, NI RETORNO-----------------

def func():
    print("Función básica")

func()

#Función con parámetros
def suma(a,b):
    print(a+b)

suma(2,3)

#------------------FUNCIONES CON RETORNO---------------------------------

def suma(a,b):
    return(a+b)
resultado = suma(4,3)
print(resultado)

#------------------FUNCIONES DENTRO DE FUNCIONES GLOBAL------------------

def resta_suma(a,b):
    def resta(a):
        return(a-1)
    resultado = resta(a)+b
    return resultado

print(resta_suma(5,7))

#------------------FUNCIONES DEL SISTEMA---------------------------------

texto = "esto es una cadena de texto"

print(texto.title())
print(texto.upper())
print(texto.capitalize())
print(len(texto))

#------------------VARIABLE LOCAL----------------------------------------

def resta():
    num1 = 6
    num2 = 2
    resultado = num1 - num2
    print(resultado)
    
resta()

#Esto daria error puesto que la variable num1 solo tiene validez dentro del #ambito de la función.
#print(num1)

#------------------VARIABLE GLOBAL----------------------------------------

num4 = 2
def multipl():
    global num3
    num3 = 7
    resultado = num3 * num4
    print(resultado)
    
multipl()

#En este caso la variable declarada como global es accesible desde el exterior de la funcion
print(num3)

#Las variables declaradas fuera de funciones también se consideran globales puesto que son accesibles fuera y dentro de las funciones.
print(num4)

#------------------DIFICULTAD EXTRA----------------------------------------

def imprime_num(text1,text2):
    num_veces = 0
    for x in range(1,102):
        if x % 3 == 0 and x % 5 == 0:
            print(f"número:{x} - {text1} {text2}")
        elif x % 5 == 0:
            print(f"número:{x} - {text2}")
        elif x % 3 == 0:
            print(f"número:{x} - {text1}")
        else:
            print(f"número:{x}")
            num_veces += 1
    print(f"número de veces que se imprime solo el número: {num_veces}")
    
imprime_num("hola","adios")