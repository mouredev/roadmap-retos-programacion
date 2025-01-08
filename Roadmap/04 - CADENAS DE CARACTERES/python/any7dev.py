""" /*
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
 */ """

cadena1 = "mi cadena"
cadena2 = "Mi Cadena"
cadena3 = "micadena"
cadena4 = " micadena "
cadena0 = "otra cadena"
cadena7 = "mi cadena"
cadena8 = "012345"
numeros = 123

# Formateo de cadena, interpolación
print(f"Esta es {cadena1}, {cadena0} y una cadena de números {cadena8}")
print("Esta es %s, %s y una cadena de números %s" %(cadena1, cadena0, cadena8))
print("Esta es {0}, {1} y una cadena de números {2}".format(cadena1, cadena0, cadena8))
print(f"Esta es {cadena1} y estos unos números {numeros}")
print("Esta es %s y estos unos números %d" %(cadena1, numeros))
print("Esta es {0} y estos unos números {1}" .format(cadena1, numeros))

# Concatenar cadenas
print(cadena1 + " " + cadena0)
cadena7 += cadena0
print(cadena7)

# Multiplicar cadena, repetición
print(cadena1*5)

# Invertir cadena
print(cadena1[::-1])

# Saber si una cadena está en otra cadena
print(cadena1 in cadena0)
print("mi" in cadena1)

# Contar las veces que aparece una cadena en otra
print(cadena1.count("ca"))

# Devolver la posición en la que se encuentra
print(cadena1.find("de"))

# Accede al caracter que te interesa
print(cadena1[3])
print(cadena1[-1])

# Se puede mostrar la subcadena que quieras, división
print(cadena1[0:5])
print(cadena1[2:5])
print(cadena1[2:])
print(cadena1[0:5:2])
print(cadena1[0::2])

# Pone la primera letra en mayúsculas
print(cadena1.capitalize())

# Todo en mayúsculas
print(cadena1.upper())

# Todo en minúsculas
print(cadena1.lower())

# Te dice si la cadena está en minúsculas
print(cadena1.islower())

# Te dice si la cadena está en mayúsculas
print(cadena1.isupper())

# Cambia las mayúsculas por minúsculas y viceversa
print(cadena2.swapcase())

# Reemplazar
print(cadena1.replace("a", "4"))

# Te dice si la cadena es alfanumérica
print(cadena1.isalnum())

# Te dice si todos los caracteres son alfabéticos
print(cadena3.isalpha())

# Te dice si es una cadena numérica
print(cadena8.isnumeric())

# Te dice si son dígitos
print(cadena8.isdigit())

# Te dice la longitud de la cadena
print(len(cadena1))

# Elimina los espacios que tenga la cadena a la izquierda y/o derecha
print(cadena4.strip())

#Divide cadena en subcadenas en forma de lista
print(cadena1.split(" "))

# De una lista devuelve una cadena
cadena5 = " ".join(["Esto", "es", "otra", "cadena"])
print(cadena5)


#DIFICULTAD EXTRA (Me he ceñido a lo que pone tal cuál, no me he querido complicar con tema acentos y mayúsculas)

def extra(pal1, pal2):
    if pal1 == pal1[::-1]:
        print(f"{pal1} es un palíndromo")
    else:
        print(f"{pal1} no es un palíndromo")
    if pal2 == pal2[::-1]:
        print(f"{pal2} es un palíndromo")
    else:
        print(f"{pal2} no es un palíndromo")

    print("-------------")

    if pal1 == pal2[::-1]:
        print(f"{pal1} y {pal2} son anagramas")
    else:
        print(f"{pal1} y {pal2} no son anagramas")

    print("-------------")

    contador = 0
    for caracter in pal1:
        if pal1.count(caracter) == 1:
            contador += 1
            continue
        else:
            print(f"{pal1} no es isograma") 
            break
    if contador == len(pal1):
        print(f"{pal1} es isograma")
    contador = 0
    for caracter in pal2:
        if pal2.count(caracter) == 1:
            contador += 1
            continue
        else:
            print(f"{pal2} no es isograma") 
            break
    if contador == len(pal2):
        print(f"{pal2} es isograma")               

    print("-------------")    

if __name__ == '__main__':
    extra("radar", "oyo")
    extra("amor", "roma")
    extra("aba", "dermatoglyphics")

