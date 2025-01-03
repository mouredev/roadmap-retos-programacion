# 02 - Python

# Funcion sin parametros ni retorno
def saludar():
    print("Hola")
# Funcion con un parametro 
def saludar_n(nombre):
    print("Hola" + nombre)
# Funcion con vainos parametros 
def saludar_n2(nombre, apellido):
    print("Hola" + nombre + " " + apellido)
# Funcion con retorno
def saludar_r(nombre):
    return "Hola " + nombre

'''Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.'''

def funcion(texto1, texto2):
    contador = 0
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print(texto1 + " " + texto2)
        elif i % 3 == 0:
            print(texto1)
        elif i % 5 == 0:
            print(texto2)
        else:
            print(i)
            contador += 1
    return "Números: " + contador

# Probando
print(funcion("hola", "mundo"))