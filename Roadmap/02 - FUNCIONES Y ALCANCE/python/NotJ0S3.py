# /*
#  * EJERCICIO:
#  * - Crea ejemplos de funciones básicas que representen las diferentes
#  *   posibilidades del lenguaje:
#  *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
def sin_pr_rt():
    print("Funcion sin parametros ni retorno")
    
sin_pr_rt()

def varios_pr(a, b):
    print("Funcion con varios parametros")
    print(f'La suma de {a} y {b} es {a + b}')
    
varios_pr(5, 4)

def con_rt():
    return "Funcion con retorno"

print(con_rt())


#  * - Comprueba si puedes crear funciones dentro de funciones.

def funcion1():
    def funcion2():
        return "Saludos desde una funcion dentro de otra"
    return funcion2()

print(funcion1())

#  * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.

def contador_caracteres(cadena = str):
    return f'El total de caracteres en la palabra {cadena} es de {len(cadena)}'

print(contador_caracteres("Hola Mundo!"))

#  * - Pon a prueba el concepto de variable LOCAL y GLOBAL.

variable_global = "Es aquella la cual se puede acceder desde cualquier parte del codigo :)"

def funcion_var_local():
    variable_local = "Es aquella que solo se puede acceder dentro de una parte del codigo"
    return variable_local

print(variable_global)
print(funcion_var_local())
# print(variable_local) En este caso no podremos acceder a la variable local

#  * - Debes hacer print por consola del resultado de todos los ejemplos.
#  *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
#  * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
#  *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
#  *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
#  *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
#  *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
#  *
#  * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
#  * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
#  */

frase1 = input("Dame una frase: ")
frase2 = input("Dame otra más: ")

def ejercicio_extra(txt1 = str, txt2 = str):
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 != 0:
            print(txt1)
        elif i % 3 != 0 and i % 5 == 0:
            print(txt2)
        elif i % 3 == 0 and i % 5 == 0:
            print(txt1 + txt2)
        else:
            print(i)

ejercicio_extra(frase1, frase2)