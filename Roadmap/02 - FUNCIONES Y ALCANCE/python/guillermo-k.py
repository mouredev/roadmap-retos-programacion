from datetime import date
''' * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)'''


def saludo():
    print("FUNCIÓN SIN PARAMETROS")
    print("Hola, sea usted bienvenido")

def saludo_personalizado(nombre):
    print("FUNCIÓN CON UN PARAMETRO")
    print(f"Hola {nombre}, sea usted bienvenido")


def funcion_dentro_de_funcion():
    def dias_a_cumpleanios(dia,mes,nombre):
        saludo_personalizado(nombre)
        today = date.today()
        anio = today.year
        cumpleanios = int(date(anio,mes,dia).strftime("%y%j"))
        now = int(today.strftime("%y%j"))
        dias = cumpleanios - now
        if dias == 0:
            print("Felíz cumpleaños")
        elif dias > 0:
            print(f"Faltan {dias} días para su cumpleaños")
        elif dias < 0:
            print(f"Faltan {dias+365} días para su cumpleaños")
    

    print("Ingrese su fecha de cumpleaños('DD/MM')")
    entrada = input()
    print("Ingrese su nombre")
    nombre = input()

    if '/' in entrada:
        fecha = entrada.split('/')
        dias_a_cumpleanios(int(fecha[0]),int(fecha[1]),nombre)


def funcion_parametros_indeterminados(*args):
    for i in args:
        print(i)


saludo()
saludo_personalizado("Guillermo")
funcion_dentro_de_funcion()
funcion_parametros_indeterminados("Hola","Chau",23)
print("La funcion 'print' es una función propia del lenguaje, que es muy utilizada")
print(max("La función 'max' obtiene el maximo de una lista","AAA","BBB"))

variable_global = 'Esta es una variable global, ya que se encuentra declarada en el cuerpo principal, y no dentro de una estructura'
def tipos_de_variables():
    variable_local = 'Esta es una variable local, ya que se encuentra decalarada dentro de un bloque, en este caso, una función. A la misma, solo se podra acceder desde el bloque que la contiene'
    print(variable_global)
    print(variable_local)

tipos_de_variables()
print(variable_global)
try:
    print(variable_local)
except:
    print("no se pudo imprimir el contenido de 'variable_local' ya que esta fuera de alcance(scope)")

'''DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.'''


def extra(text1,text2):
    count = 0
    for i in range(1,101):
        cadena = ""
        if i%3 != 0 and i%5 != 0:
            cadena = i
            count += 1
        else:
            if i%3 == 0:
                cadena += text1
            if i%5 == 0:
                cadena += text2
        print(cadena)
    return count

cantidad_numeros = extra("Es divisible por 3.","Es divisible por 5")

print(f"Se ha escrito {cantidad_numeros} veces un número en lugar de los textos")