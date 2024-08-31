'''
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
 '''
 
 
#Función sin parámetros
def HolaMundo():
    print("Hola mundo")


print(HolaMundo())



#Con uno parámetro
def MostrarNumero(num1):
    print(num1)
    
print(MostrarNumero(7))



##Con varios parámetros
def sumarNumeros(num1, num2 , num3):
    print(num1 + num2+ num3)

print(sumarNumeros(3,5,7))



#Función con retorno
def Multiplicar(num1,num2,num3):
    return num1 * num2 * num3

print(Multiplicar(2,4,5))



#Funciones dentro de funciones
print("Funciónes anidadas")
def funcionAnidada(n1, n2):
    
    def Anidada():
        print("La multiplicación de ", n1, "y", n2, "es..", n1*n2)
        
    return n1 / n2

resultado = funcionAnidada(5,7)
print(resultado)


#Funciones propias de PYTHON 
#Usando la función Max():
def EncontrarMayor():
    numeros=[3,5,6,8,]
    return max(numeros)

print("numeros=[3,5,6,8,]")
print("El mayor numero de la lista es :", EncontrarMayor())


#Variables locales y Globales en python
"""
En Python las variables locales son las que se definen  
en una función y que solo permiten su acceso desde ella.  
Las globales se definen en el cuerpo principal 
del programa y permiten su acceso desde cualquier lugar.   
Las no locales son variables locales que se pueden modificar en funciones anidadas.
"""



#Dificultad Extra
def imprime(texto1 , texto2 ):
    
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print(texto1 + texto2)
        elif i % 3 == 0:
            print(texto1)
        elif i % 5 == 0:
            print(texto2)
        else:
            contador = 0
            contador += 1
    return print("Numero de veces que se imprime el numero y no el texto: ",contador)

#llamada a la función 
print(imprime("hello", "Python"))