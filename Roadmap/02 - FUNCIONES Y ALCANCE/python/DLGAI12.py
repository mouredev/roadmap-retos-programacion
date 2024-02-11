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
    */
 """

#Funcion sin parametros y sin retorno

def saludo():
    print("Hola Python")

#Funcion con un  parametro y sin retorno

def saludo1(parametro):
    print("Hola"+ parametro)


#Funcion con vcarios  parametros y sin retorno

def saludo2(parametro1,parametro2):
    print(parametro1+ parametro2)

#Funcion con retorno 

def saludo3(parametro1,parametro2):
    return parametro1+ parametro2


#Funcion con parametros determinados
 
def saludo4(parametro1,parametro2=" Python"):
    return parametro1+ parametro2

#Funcion dentro de funcion
def funcion_anidada():
    def funcion():
        print("Soy una funcion anidada")
    funcion()
"""Alcance Variables"""
def variables():
    variable_local = "¡Hola, soy una variable local!"
    print(variable_local)
    print(variable_global)

variable_global = "¡Hola, soy una variable global!"    
"""LLamado a tipos de funciones"""

saludo()
saludo1(" Python")
print(saludo3("Hola"," Adios"))
print(saludo4("Hola"," Como Estas"))
print(saludo4("Hola"))
funcion_anidada()


"""LLamado a alcance de tipos de variables"""
variables()
"""Ejercicio Extra"""
def extra(parametro1,parametro2):
    contador=0
    for i in range(1,101):
        if(i%15==0):
            print(f"{parametro1}  {parametro2}")
        elif(i%3==0):
            print(parametro1)
        elif(i%5==0):
            print(parametro2)
        else:
            print(i)
            contador+=1
    return contador

print(extra("Tres","Cinco"))