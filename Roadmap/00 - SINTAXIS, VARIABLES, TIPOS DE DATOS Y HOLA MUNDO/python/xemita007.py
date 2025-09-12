'''
# #00 SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO
> #### Dificultad: Fácil | Publicación: 26/12/23 | Corrección: 02/01/24

Author: Alfredo Aburto Alcudia: https://github.com/alabacw74

## Ejercicio

```
/*
 * ¿Preparad@ para aprender o repasar el lenguaje de programación que tú quieras?
 * - Recuerda que todas las instrucciones de participación están en el
 *   repositorio de GitHub.
 *
 * Lo primero... ¿Ya has elegido un lenguaje?
 * - No todos son iguales, pero sus fundamentos suelen ser comunes.
 * - Este primer reto te servirá para familiarizarte con la forma de participar
 *   enviando tus propias soluciones.
 *
 * EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 *
 * ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
 * debemos comenzar por el principio.
 */
```
'''


#https://www.python.org/

""""
Este comentario 
es 
de varias lineas 
"""


'''
Esta es otra manera de comentar 

entre lineas

'''

my_variable="hola mundo"
CONSTANTE=" mi variable constante"

#my_variable=5 si lo desconmentamos no da error 

try:
    
    print(int(my_variable))
    print(type(my_variable))

except ValueError:

    print("da error por que no se puede convertir una cadena a int salvo que sea un numero")

#var primitivos
    
my_variable="mi cadena de texto"

my_variable=5 #entero
print(type(my_variable))
my_variable=1.5 #float
print(type(my_variable))
my_variable=True # boleano
print(type(my_variable))
    
print("¡Hola, [python]!")
