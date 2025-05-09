'''EJERCICIO:
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
 */'''

def extra(texto_1,texto_2):
    contador=0
    for i in range(1,101):
        if i%3==0 and i%5==0:
            print(texto_1+texto_2)
        elif i%3==0:
            print(texto_1)
        elif i%5==0:
            print(texto_2)
        else:
            contador+=1
            print(i)
    return f'{contador}, se ha impreso el número en lugar de los textos'
print(extra('mi ejercicio ','está terminado.'))

print('_____________________________Separador___________________________________')
#Ahora ejemplos de fuciones

resultado=0 #variable global

def sin_argumentos():
    print('Fin del ejercicio')

def con_argumentos(a,b):
    return a+b

def con_variable_local(n1,n2):
    resultado=n1*n2
    return resultado

def funciones_con_funciones(n):
    m=int(input('Introduce un numero: '))
    resultado=n
    print(con_argumentos(resultado,m))

'''He creado resultado como variable global y dentro de una función como local para ver la diferencia
, he creado funcines con argumentos y sin ellos, también utilizo una de ellas dentro de otra y a su vez
utilizando la variable golobal para que se vea claramente como funciona cada una de ellas'''

sin_argumentos()
print(con_argumentos(3,5))
print(con_variable_local(7,3))
funciones_con_funciones(3)