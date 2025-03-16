"""
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */"""

# Funcion sin parametros
def sin_parametros():
    print("la funcion no recibi parametros y no tiene retorno")

# Funcion con parametros y retorno
def con_parametros(parametro1,parametro2):
    print(f"la funcion imprime el parametro 1:{parametro1} y el parametro 2:{parametro2 }")
    print("retorno la concatenacion con un espacio de parametro 1 y parametro 2")
    return parametro1 + " " + parametro2

# funcion dentro de una funcion
def imprimir_suma(num1,num2):
    def suma(num1,num2):
        return num1+num2
    
    print(suma(num1,num2))

def extra(param1="fizz",param2="buzz"):

    for i in range(1,101):
        if i % 3 == 0:
            if i % 5 == 0:
                print(i,param1+param2)
            else:
                print(i,param1)
        elif i % 5 == 0:
            print(i,param2)
        else:
            print(i,"____") 




if __name__ == "__main__":
    
    sin_parametros()

    retorno = con_parametros("hola","mundo")
    print(retorno)

    imprimir_suma(4,3)

    extra()


