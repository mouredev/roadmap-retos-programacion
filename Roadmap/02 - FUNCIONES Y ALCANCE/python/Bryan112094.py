"""
/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 */
"""
#Función sin parametro ni retorno
def hola():
    print("Hola soy Bryan")

#Función con parametro pero sin retorno
def mi_edad(edad: int):
    print(f"Soy Bryan y tengo {edad} años")

#Funcion con parametro con retorno
def sumar(*num):
    return sum(num)

#Comprobar si una funcion puede estar dentro de otra funcion
def fun_principal(numero):
    def fun_secundaria(doble_numero):
        return doble_numero * 2

    numero_doble = fun_secundaria(numero)
    return numero_doble

#Funciones ya creadas
lista = [1, 4, 5, 9, 3]
#->cantidad de elementos
cant = len(lista)
#->elemento mayor
mayor = max(lista)
#->Agregar elemento
lista.append(34)

#Variables locales -> solo dan dentro de la funcion mas no fuera de ella
saludar = "hello"
def cambiar_saludar():
    saludar = "hola"

#Variables globales -> para que reconozca la variable se tiene que anteponer la palabra "global"
nombre = "Cristhian"
def segundo_nombre():
    global nombre
    nombre = "Bryan"

print("IMPRIMIR FUNCIONES DECLARADAS\n")

print("Función sin variable ni retorno: hola()")
hola()
print("\nFunción con variable ni retorno: mi_edad(29)")
mi_edad(29)
print("\nFunción con variable y con retorno: sumar(20, 30)")
rpta = sumar(20, 30)
print(rpta)

print("\nVerificar si se puede poner una funcion dentro de otra: fun_principal(80)")
verificar = fun_principal(80)
print(verificar)

print("\nImprimir funciones ya creadas de la lista [1, 4, 5, 9, 3]")
print(f"Cantidad de elementos: {cant}")
print(f"Elemento mayor de la lista: {mayor}")
print(f"Lista con un elemento nuevo: {lista}")

print("\nVariable local: la variable dentro la función no cambiara el valor de la variable fuera de ella asi tenga el mismo nombre")
print(f"Antes de la función: {saludar}")
cambiar_saludar()
print(f"Después de la función: {saludar}")

print("\nVariable Global: la variable dentro la función cambiara el valor de la variable fuera de ella si se le antepone la palabra global")
print(f"Antes de la función: {nombre}")
segundo_nombre()
print(f"Después de la función: {nombre}")

"""
/*
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 */
"""

print("\n\nDIFICULTAD EXTRA\n")

def exer_extra(texto01: str, texto02: str):
    cantidad_num = 0
    for i in range(1, 101):
        if i % 5 == 0 and i % 3 == 0:
            print(texto01 + texto02)
        elif i % 5 == 0:
            print(texto02)
        elif i % 3 == 0:
            print(texto01)
        else:
            cantidad_num += 1
            print(i)
    return cantidad_num

final_func = exer_extra("hola ", "mundo")
print(f"Cantidad de números impresos: {final_func}")