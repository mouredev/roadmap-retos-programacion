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
 */
""" 
from datetime import datetime
import calendar

#funcion sin retorno
def impresion():
    print("Hola mundo")

#funcion con retorno
def suma():
    suma = 5 + 5
    return suma

#funcion con un parametro
def nombre(palabra):
    message = 'Hola, ' + palabra.capitalize() 
    return message

#funcion con varios parametros
def cumple(date, now):
    if date < now:
        date = date.replace(year=date.year + 1) #funcion dentro de otra funcion ejecutada
    diff = date - now
    hours, seconds = divmod(diff.seconds, 60*60)
    minutes, seconds = divmod(seconds, 60)

    return (diff.days, hours, minutes, seconds)

print(impresion())
print(suma())
print(nombre(input("escriba una su nombre: ")))
now = datetime.now()
try:
    mes = int(input("Digite el mes: "))
    dia = int(input("Digite el dia: "))
    nextcumple = cumple(datetime(now.year, mes, dia), now)
    print(f"Tu siguiente cumpleaños sera en: {nextcumple[0]} dias, {nextcumple[1]} horas, {nextcumple[2]} minutos, {nextcumple[3]} segundos")
except Exception as e:
    print(f'error: {e}')

#numero variable de argumentos
def meses(*args):
    for i in args:
        mes = calendar.month_name[i]
        print(f"En el año tenemos a: {mes}")


meses(1,2,3,4,5,6,7,8,9,10,11,12)

#argumentos variables con palabras clave
def info(**args):
    for param, i in args.items():
        print(f"info relevante: ({param}): {i}")

info(
    nombre = "juan",
    edad = 25,
    ciudad = "cartagena",
    pais = "colombia"
)

def funcionOut():
    def funcionIn():
        print("Holaaaaaaaaaaaaa")
    funcionIn()

funcionOut()

#Funcion built-in
numero = 1
print(numero.to_bytes())

#Variable global
numero1 = 1
print(numero1)

nombre = 'Diego'

def imp_nombre():
    global frase
    frase = 'El nombre es: '
    print(f"{frase} {nombre}")

imp_nombre()

#EXTRA
def cadenas(param1, param2):
    cuenta = 0
    for i in range (1,101):
        if i % 3 == 0 and i % 5 == 0 :
            print(param1 + param2)
        elif i % 3 == 0:
            print(param1)
        elif i % 5 == 0:
            print(param2)
        else:
            print(i)
            cuenta += 1
    return cuenta

cadena1 = str(input("Digite una cadena de texto que se digite cuando el valor sea múltiplo de 3: "))
cadena2 = str(input("Digite una cadena de texto que se digite cuando el valor sea múltiplo de 5: "))

print(f"La cantidad de veces que apareció un numero en vez de texto fueron: {cadenas(cadena1,cadena2)}")