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
 """

#Funciones sin parámetros ni retorno

def saludo():
    print(f"Hola mundo ¿que tal estais?")

saludo()

#Funciones con varios parametros y con retorno

#Calculadora se añade dos parametros y el tipo en el que se realiza

tipos_caluclo = ["suma","resta","multiplicacion","division","potencia"]

def calculadora(param1,param2,tipo):
    if(tipo == "suma"):
        return param1 + param2
    elif(tipo == "resta"):
        return param1 - param2
    elif(tipo == "multiplicacion"):
        return param1 * param2
    elif(tipo == "division"):
        return param1 / param2
    elif(tipo == "potencia"):
        return param1 ** param2

print(f"\nEsto es una calculadora. Elige una función, suma(0), resta(1), multiplicacion(2), division(3), potencia(4) de numeros.")
tipo_input = int(input("Introduce numero para la funcion: "))

print(f"Ahora introduce 2 numeros: ")
parametro1 = int(input("Parametro 1: "))
parametro2 = int(input("Parametro 2: "))

print(f"El resultado del calculo es {calculadora(parametro1,parametro2,tipos_caluclo[tipo_input])}")

def funcion_dentro_funcion():
    print("Llamada a una funcion dentro de la funcion")
    def saludo_interno():
        print("LLamada propia")

    print("Estoy llamando a la funcion ahora")
    saludo_interno()

    #Variable LOCALES y GLOBALES

    #Global: sería tipos_calculo dentro del propio script
    #Local: sería la variable 

"""
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
"""

def funcion_opcional(texto1,texto2):
    resultado = 0
    try:
        for i in range(1,101):

            if i%3 == 0 and i%5 == 0 :
                print(texto1+texto2)
            else:
                if(i%3 == 0):
                    print(texto1)
                elif(i%5 == 0):
                    print(texto2)
                else:
                    print(i)
                    resultado +=1
        
        return print("El numero de veces que se ha impreso el número en lugar de los textos "+ str (resultado))

    except TypeError as e:
        print(e)

text1 = "Esto es el texto 1"
text2 = "Esto es el texto 2"
#text2 = 2

funcion_opcional(text1,text2)