# #02 FUNCIONES Y ALCANCE
#### Dificultad: Fácil | Publicación: 08/01/24 | Corrección: 15/01/24

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
"""
#FUNCIONES SIN PARAMETROS NI RETORNO
def suma_():
    a=3
    b=5
    print(a + b)
    
def resta():
    a=5
    b=3
    print(a - b)               
    
def multiplicacion():
    a=4
    b=6
    print(a * b)   
    
    
#FUNCIONES CON UNO O VARIOS PARAMETROS
def suma_parametros(a,b):
    print(a + b) 
       
def resta_parametros(a,b):
    print(a - b)
 
def multiplicacion_parametros(a,b):
    print(a * b)

#FUNCIONES CON RETORNO / FUNCIONES DENTRO DE FUNCIONES
def calculadora():
    print("¿Que operacion quieres realzar?")
    print("1.- Suma")
    print("2.- Resta")
    print("3.- Multiplicacion")
    opcion = int(input("Opcion: "))
    
    print("Introduce los numeros")
    a = int(input("Numero 1: "))
    b = int(input("Numero 2: "))
    
    if opcion == 1:
        return suma_parametros(a,b)
    elif opcion == 2:
        return resta_parametros(a,b)
    elif opcion == 3:
        return multiplicacion_parametros(a,b)
    else:
        return "Opcion no valida"
#calculadora()

#DIFICULTAD EXTRA
def multiplos(a,b):
    for i in range(1,101): #bucle de 1 a 100 
        if i % 3 == 0 and i % 5 == 0:   #si el numero es multiplo de 3 y 5
            print(a + b)
        elif i % 3 == 0: #si el numero es multiplo de 3
            print(a)
        elif i % 5 == 0: #si el numero es multiplo de 5
            print(b)
        else:
            print(i)
    return i    #retorna el numero de veces que se ha impreso el numero en lugar de los textos

def app():
    a = input("Introduce el primer texto: ")
    b = input("Introduce el segundo texto: ")
    return multiplos(a,b)
app()
