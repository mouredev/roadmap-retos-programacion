#Reto 03

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
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.'''


#Función sin parametros ni retorno

def sin_par():
    print("Hola mundo")
    num = 12 + 5

sin_par()
print(sin_par())

#Función sin parametros y con retorno

def sin_par_con_retorno():
    print("Hola mundo")
    num = 12 + 5
    return num

sin_par_con_retorno()
retorno = sin_par_con_retorno()
print(sin_par_con_retorno())
print(f"Retorno", retorno)

#Con un parametro sin retorno

def con_un_par(parametro):
    print(f"hola", parametro)

con_un_par("Python")
print(con_un_par("Pypy"))

#Con un parametro con retorno

def con_un_par_con_retorno(parametro):
    print(f"Hola", parametro)
    return "hola mundo y hola " + parametro

con_un_par_con_retorno("Python")
retorno = con_un_par_con_retorno("Pypy")
print(retorno)

#Con varios parametros sin retorno

def con_varios_par(par_1,par_2,par_3 = "Parametro por defecto"):
    print(f"{par_1} {par_2}, {par_1} {par_3}")

con_varios_par("Hola","mundo")
con_varios_par("Hola","mundo","Python")
print(con_varios_par("Hola","mundo","Pypy"))

#Con varios parametros con retorno

def con_varios_par_con_retorno(par_1,par_2,par_3 = ", hola Parametro por defecto"):
    return par_1 + par_2 + par_3

retorno = con_varios_par_con_retorno("Hola ", "Mundo")
print(retorno)

retorno = con_varios_par_con_retorno("Hola ", "Mundo", ", Hola Brais")
print(retorno)

#Función con multiples parametros

'''Esto lo añadí luego de ver la solución
y notar que me faltó esta posibilidad de python'''

def multiples_parametros(*parametros):
    for parametro in parametros:
        print(parametro)

multiples_parametros("Python", "SQL", "Pandas", "Numpy")

def multiples_parametros_palabra_clave(**parametros):
    for valor,llave in parametros.items():
        print(f"{valor}: {llave}")

multiples_parametros_palabra_clave(nombre="Brais", apellido="Moure")

#Funciones dentro de funciones

def funcion_externa():
    def numeros():
        for n in range(0,11):
            print(n)
        return "Fin de la secuencia"
    print(numeros())

funcion_externa()

#Funciones integradas de python

#Función len()

print(len("Hola mundo"))

#Función enumerate()
resultado = list(enumerate(["Python", "C++", "C#", "Kotlin", "Swift", "Java"]))
print(resultado)

#Variable local y global

Global = "Soy una variable global"
def ejemplo():
    local = "soy una variable local"
    print(f"{Global} dentro de la función")
    print(f"{local} dentro de la función")

ejemplo()
'''Las variables locales solo existen dentro del contexto
donde son creadas'''
#Descomentar para probar
#print(f"{local} fuera de la función")


#Reto extra

print("Reto extra\n")

def reto(parametro_1 = "string por defecto 1", parametro_2 = "string por defecto 2"):
    contador = 0
    for num in range(1,101):
        if num % 3 == 0 and num % 5 == 0:
            print(f"{parametro_1} {parametro_2}")
        elif num % 3 == 0:
            print(parametro_1)
        elif num % 5 == 0:
            print(parametro_2)
        else: 
            print(num)
            contador += 1
    return contador

print(reto("Brais", "Moure"))