""" 

* EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 
 """
cadena:str="" # cadena vacía
print(cadena)
cadena = "Estoy creando cadenas" #cadena con comillas dobles
print(cadena)
cadena = 'Estoy creando cadenas' #cadena con comillas simples
print(cadena)
cadena="las cadenas no tienen limite de tamaño solamente el espacio en memoria que abarquen en el ordenador"
print(cadena)
cadena=" Esto es una comilla doble \" de ejemplo dentro de una cadena"
print(cadena)
cadena ="se puede incluir salto de linea utilizando el caracter \n llevando el textro a otra linea (\ n sin espacios)"
print(cadena)
cadena="al escribir la barra invertida \ seguida de un numero se imprime el caracter correspondiente ejemple \110 (\ 110 sin espacios) es la 'H'"
print(cadena)
cadena = """ tambien se pueden
escribir cadenas
de varias lineas
utilizando las triples comillas
"""
print(cadena)

#formateo de cadenas
a="Python "
b="es "
c="un lenguaje de programación de: "
d=10
e=a+b+c+str(d) 
print(e)
f="Python es un lenguaje de programacion de: %a" %d
print(f)
s = "Los números son %d y %d." % (5, 10)
print(s) #Los números son 5 y 10.
s = "Los números son {} y {}".format(5, 10)
print(s) #Los números son {} y {}".format(5, 10)
s = "Los números son {a} y {b}".format(a=5, b=10)
print(s) #Los números son 5 y 10
a = 5; b = 10
s = f"Los números son {a} y {b}"
print(s) #Los números son 5 y 10
a = 5; b = 10
s = f"a + b = {a+b}"
print(s) #a + b = 15
def funcion():
    return 20
s = f"El resultado de la función es {funcion()}"
print(s) #El resultado de la funcion es 20

#multiplicar string por un int
s = "Hola " * 3
print(s) #HolaHolaHola
#verificar si exite una string dentro de otra con in
print("mola" in "Python mola") #True
print("Hola" in "Python mola") #False

#longitud
cadena = " esta es una cadena de texto con cierta longitud y muchos espacios, de manera que podamos ver su longitud de caracteres y buscar en valores altos o bajos"
longitud=len(cadena)
print(longitud)

#indexado de cadenas
print(cadena[0],cadena[-5])

#Porcionando cadenas
print(cadena[:10])
print(cadena[::2])
print(cadena[1:2])
print(cadena[0:30:3])

#capitalize
print(cadena.capitalize())

#lower
print(cadena.lower())

#Swapcase
cadena= "HolA ComO EsTaS"
print(cadena.swapcase())

#upper
print(cadena.upper())

#contar fragmentos de cadenas
cadena = " esta es una cadena de texto con cierta longitud y muchos espacios, de manera que podamos ver su longitud de caracteres y buscar en valores altos o bajos"
print(cadena.count("al"))

#Reconocer caracteres alfanumericos, alfabeticos
string="abcdefghijklmnopqrstuvwxyz"
print(string.isalpha())
string=("1231456789abcdefghijklmnopqrstuvwxyz")
print(string.isalnum())

#Reconocer espacios
print(cadena.isspace())

print("EXTRA\n\n\n")
"""
EXTRA
"""
def es_isograma(palabra):
    return len(set(palabra)) == len(palabra)

def evaluador_de_palabras():
    palabra1=input("Escribe la primera palabra: ").lower()
    palabra2=input("Escribe la segunda palabra: ").lower()
    inverted1=palabra1[::-1]
    inverted2=palabra2[::-1]
    sorted1=sorted(palabra1)
    sorted2=sorted(palabra2)

    if palabra1==inverted1:
        print(f"La palabra {palabra1} es un palindromo")
    else :
        print(f"La palabra {palabra1} no es un palindromo")
    if palabra2==inverted2:
        print(f"La palabra {palabra2} es un palindromo")
    else :
        print(f"La palabra {palabra1} no es un palindromo")
    if sorted1==sorted2:
        print(f"Las palabras {palabra1} y {palabra2} son anagramas")
    else :
        print(f"Las palabras {palabra1} y {palabra2} no son anagramas")
    if es_isograma(palabra1):
        print(f"{palabra1} es un isograma.")
    else:
        print(f"{palabra1} no es un isograma.")

    if es_isograma(palabra2):
        print(f"{palabra2} es un isograma.")
    else:
        print(f"{palabra2} no es un isograma.")

evaluador_de_palabras()
    
