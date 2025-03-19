# ╔══════════════════════════════════════╗
# ║ Autor: Kenys Alvarado                ║
# ║ GitHub: https://github.com/Kenysdev  ║
# ║ 2024 - Python                        ║
# ╚══════════════════════════════════════╝

# 1. Funciones:
# *************
# Definir función:
def function_name():
    print("1. Funciones:")

function_name()
#_________________________
# Con Parámetro:
def imprimir(parametro):
    print(parametro)
    
# Con retorno:
def saludo(nombre):
    return (f"¡Hola, nombre!")

imprimir(saludo("Ken"))
#_________________________
# Con parametros:
def resta(a, b):
    return (a-b)

imprimir(resta(4, 2))
#_________________________
# Con parámetro predeterminado.
def suma(a, b=5):
    return (a + b)

imprimir(suma(5))
#_________________________
# Número Variable de Argumentos:
def sumar_numeros(*numeros):
    return sum(numeros)

imprimir(sumar_numeros(1, 2, 3))
#_________________________
# Argumentos de palabra clave.
def usuario(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

usuario(nombre="Ben", edad="21")
#_________________________
# Con recursividad:
def recursivo(n):
    if n == 0:
        print("Completado")
    else:
        print(n)
        n -=1
        recursivo(n)

recursivo(3)
#_________________________
# 2. Función anidada:
# *******************
def principal(a):
    def interna(b):
        return (b + a)
    b = a * 2
    return interna(b)

imprimir(principal(10))
#_________________________
# 3. Ejemplo de funciones incorporadas:
# *************************************
# Solicitar una entrada.
#entrada = input("Escribe:")
#print(f"Loro: {entrada}")

print(len("123"))   # total char
print("ABC".lower()) # minusculas
print("abc".upper()) # mayusculas
a, b = "a b".split() # divide una cadena
print(b)

# conversión de tipo(int, float, str, list, bool)
un_bool = True
print(type(un_bool))
a_str = str(un_bool)
print(type(a_str))

#_________________________
# 4. Variable LOCAL y GLOBAL.
# *************************************
Variable_global = "Variable_global"
def var():
    variable_local = 21 
    return Variable_global

imprimir(var)
# Variable local no accesible fuera de la función.
#print(variable_local)
#print(Variable_global)

#_________________________
# 5. Ejercicio:
# *************
'''
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 * - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 * - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 * - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 * - La función retorna el número de veces que se ha impreso el número en lugar de los textos.""")
'''
def ejercicio(str_1, str_2):
    n_veces = 0
    for num in range(1, 101):
        if num % 3 == 0 and num % 5  == 0: print(str_1 + str_2)
        elif num % 3 == 0: print(str_1)
        elif num % 5 == 0: print(str_2)
        else: n_veces +=1; print(num)
    return(n_veces)

imprimir(ejercicio("  múltiplo de 3", "  múltiplo de 5"))
