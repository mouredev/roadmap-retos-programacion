# funciones sin parametro ni retorno:


def saludo():
    print("¡Hola, mundo!")


saludo()

# funciones con un parametro:


def cuadrado(n):
    return n ** 2


print(cuadrado(5))

# funciones con varios parametros:


def suma(a, b, c):
    return a + b + c


print(suma(1, 2, 3))

# funciones con retorno:


def multiplicar(x, y):
    return x * y


resultado = multiplicar(4, 5)
print(resultado)


# funciones con funciones anidadas:

def funcion_externa(a, b):
    def funcion_interna(c, d):
        return c + d
    resultado = funcion_interna(a, b)
    return resultado


print(funcion_externa(5, 10))

#### Ejemplos de funciones ya creadas en python (existen mas...!!) #####

#len
def longitud_lista(lista):
    return len(lista)

mi_lista = [1, 2, 3, 4, 5]

print(longitud_lista(mi_lista))

#abs(x) devuelve el valor absoluto 
def funcion_abs(x):
    return abs(x)

mi_abs = -7
print(funcion_abs(mi_abs))

#max(iterable) o max(arg1, arg2, *args) devuelve el mayor de dos o mas Args.
def funcion_iterable(x):
    return max(x)

mi_max = [1, 2, 3, 4, 5]
print(funcion_iterable(mi_max))


#### Ejemplos de variables locales y variables globales #####

#Variables locales
"""
En Python, las variables se pueden clasificar en dos tipos principales: 
variables locales y variables globales, dependiendo de su alcance.

Variables Locales: Una variable definida dentro de una función se conoce como variable local. 
El alcance de estas variables está limitado 
a la función en la que se definen. 
No se pueden acceder fuera de esa función. 
Por ejemplo:
"""

def mi_vlocal():
    variable_local = "¡Hola, soy una variable local!"
    print(variable_local)

mi_vlocal()

#Variables Globales
"""
Variables Globales: Una variable que se define fuera de todas las funciones 
se conoce como variable global. 
Estas variables pueden ser accedidas desde cualquier parte del código, 
tanto dentro como fuera de las funciones 
(a menos que se sobrescriban en el ámbito local). 
Por ejemplo:
"""
variable_global = "¡Hola, soy una variable global!"

def mi_vglobal():
    print(variable_global)

mi_vglobal()


#funcion contador hecha por mi

def  funcion_contar1(texto1 , texto2):
        for numero in range(101):
            if numero % 3 == 0 and numero % 5 == 0:
                print (texto1 + " " + texto2)
            elif numero % 3 == 0: 
                print (texto1)
            elif numero % 5 == 0:
                print (texto2)
            else:
                print (numero)


hola = "Hola"
mundo = "mundo!"

print(funcion_contar1(hola, mundo))

#funcion mejorada con chatgpt y creando funciones extras
def contador():
    for numero in range(101):
        yield numero

def es_multiplos5(contador):
    for num5 in contador:
        if(num5 % 5 == 0):
            yield True, num5
        else:
            yield False, num5

def es_multiplos3(contador):
    for num3 in contador:
        if(num3 % 3 == 0):
            yield True, num3
        else:
            yield False, num3

def funcion_contar2(texto1 , texto2):
    contador_gen1 = contador()
    contador_gen2 = contador()
    for (resultado5, num5), (resultado3, num3) in zip(es_multiplos5(contador_gen1), es_multiplos3(contador_gen2)):
        if resultado5 and resultado3:
            print(f"{texto1} {texto2} {num5} es múltiplo de 5 y 3")
        elif resultado3:
            print(f"{texto1} {num3} es múltiplo de 3")
        elif resultado5:
            print(f"{texto2} {num5} es múltiplo de 5")
        else:
            print(num5)

hola = "Hola"
mundo = "mundo!"

print(funcion_contar2(hola, mundo))
