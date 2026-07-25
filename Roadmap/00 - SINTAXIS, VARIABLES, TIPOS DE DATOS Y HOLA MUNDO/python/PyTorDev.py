'''
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
'''
# La url con la documntación de Python es https://docs.python.org/es/3.13/

  #Comentario de una linea

'''
Comentario multilinea
Este tipo de comentario en Python, no es un comentario real, y ocupa meemoria en ejecución
'''

  #Declaración de variable

varianble1 = 1 #Asigna el valor 1 a variable1
variable_nombre= "Paco" #Asigna el valor Paco a variable_nombre
a, b, c = 1, 2, 3 #Asinga los valores 1, 2 y 3 a las variables a, b y c respectivamente

  #Declaración de constante

#En Python no existen las constantes, pero existe la conveción de que una variable en mayusculas, se considera constante,
#por tanto no deberia ser cambiada aunque el lenguje lo permite

URL_API = 'https:\\la-web-de-la-api.com'

  #Tipos de datos primitivos
#Enteros (int)
x = 1
num_int = 1234

#Flotantes/Decimales (float)
y = 1.12
num_float = 2345.1234

#Buleano (bool)
xBoolean = True
my_boolean = False

#Cadena de texto (String)
text = "Hola mundo"
text2 = 'Python es el lenguaje de la pitón'
texto_multilinea = '''
Este string esta dentro 
de texto_multilinea
'''


leng = 'Python'

print('Hola, el lenguaje es ' + leng)