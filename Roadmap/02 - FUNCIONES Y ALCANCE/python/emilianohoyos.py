"""
 EJERCICIO:
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
"""Sin parámetros ni retorno"""
def saludo():
    print("hola");

saludo()

""" con uno o varios parámetros"""
def saludoConNombre(name):
    print("Hello "+name+"!")

saludoConNombre('emiliano')

""" con retorno"""    
def producto(val1,val2):
    return val1*val2

print(producto(3,2))

"""Comprueba si puedes crear funciones dentro de funciones"""
def usuario():
    def nombre():
        print("carlos")
    nombre()
usuario()

"""Utiliza algún ejemplo de funciones ya creadas en el lenguaje."""
def argumentoMasGrande(val1,val2,val3):
    valor=max(val1,val2,val3)
    print(valor)
argumentoMasGrande(3,2,1)


#con un argumento por defecto
def default_saludo(name="carlos"):
    print(f"Hola, {name}!")

default_saludo()

#multiple return 
def multiple_return_saludo():
    return "Hola", "python"

greet,name=multiple_return_saludo()
print(greet)
print(name)

#con un numero variable de argumentos
def variable_arg_saludo(*names):
    for name in names:
        print(f"Hola,{name}!")

variable_arg_saludo("php", "python","emiliano", "carlos")

#con un numero variable de argumentos con palabras claves
def variable_key_arg_saludo(**names):
    for key,name in names.items():
        print(f"Hola,{name} ({key})!")

variable_key_arg_saludo( language="python",nombre="emiliano",alias="carlos",edad=30)

"""Pon a prueba el concepto de variable LOCAL y GLOBAL."""
nombre="emiliano"

def saludo2():
    nombre="Maria"
    print("Hola "+ nombre)
# Llamamos a la función
saludo2()

# Imprimimos la variable global
print("La variable global es " + nombre)
 

"""DIFICULTAD EXTRA (opcional):""" 
def imprimir(var1,var2)->int:
    contador=0
    for number in range(0,101):
        if number%3==0 and number%5==0:
           print(str(var1)+str(var2))
        elif number%3==0:
           print(str(var1))
        
        elif number%5==0:
            print(str(var2))
        else:
           contador+=1
           print(number)

    return contador

print(imprimir("uno","dos"))   
