#CADENAS

mi_cadena = "Hola soy una cadena de caracteres"
mi_cadena_vacia = ''

print(type(mi_cadena))
print(len(mi_cadena))  #Longitud de caracteres de una cadena
print(mi_cadena_vacia)

#SECUENCIAS DE ESCAPE

sec_esc = "Esta es una cadena con comillas simples dentro \"HOLA\" "
print(sec_esc)

#SALTO DE LINEA

salt_linea = "Esta es una cadena\n con saltos de linea"
print(salt_linea)

#FORMATEO DE CADENAS E INTERPOLACIÓN

numero_a_cadena = 12345
print("El numero es " + str(numero_a_cadena))

#ESTILO PRINTF

n1 = 5
resultado_formateo = "El numero formateado es %d" % n1
print(resultado_formateo)

resultado_formateo = "Los numeros formateados son {} y {}".format(4, 3)
print(resultado_formateo)

#INTERPOLACION O F-STRINGS

n1 = 20
n2 = 30
suma = n1 + n2
suma_formateada = str(n1) + str(n2)  #FORMATEO A CADENAS

print(f'La suma de {n1} + {n2} = {suma}')
print(f'La suma formateada de {n1} + {n2} = {suma_formateada}'
      )  #NO SE REALIZA LA SUMA, SE CONCATENAN LOS VALORES FORMATEADOS

#SUMA DE CADENAS

cadena_1 = "Hola soy la primera parte..."
cadena_2 = "y yo soy la segunda parte!"

print(cadena_1 + " " + cadena_2)

#REPETIR UNA CADENA n VECES

cadena_repetida = "Hola soy una cadena repetida \n"
print(cadena_repetida * 5)

#SABER SI UNA CADENA ESTA CONTENIDA EN OTRA

cadena = "Python es clave"

print("thon" in cadena)  #True

#ACCEDER A LOS VALORES DE UNA CADENA COMO EN UNA LISTA

mi_cadena = "Hola"
print(mi_cadena[0])  #ACCEDER AL PRIMER CARACTER

#CORTAR CADENAS O SLICING

print(mi_cadena[0:2])  #EMPIEZA DESDE EL INDICE 0 AL 2
print(mi_cadena[2:])  #EMPIEZA DEL INDICE 2 HASTA EL FINAL
print(mi_cadena[0::2])  #CORTA LA CADENA DE 2 en 2
print(mi_cadena[::-1])  #INVIERTE LA CADENA

#METODOS DE CADENA

cadena = "hola soy una cadena que sera modificada"
print(
    cadena.capitalize())  #PONE LA PRIMERA LETRA DE TODA LA CADENA EN MAYUSCULA
print(cadena.upper())  #CONVIERTE A MAYUSCULA TODA LA CADENA
print(cadena.lower())  #CONVIERTE A MINUSCULA TODA LA CADENA
print(cadena.swapcase())  #VARIACION ENTRE MAYUSCULAS Y MINUSCULAS
print(cadena.title())  #CONVIERTE LA PRIMERA LETRA DE CADA PALABRA EN MAYUSCULA
print(
    cadena.count("ca")
)  #EVALUA CUANTAS VECES SE REPITE SE REPITE UN FRAGMENTO DE CADENA EN OTRA
print(cadena.replace("hola", "Hey"))

mi_cadena = "correo@gmail.com"
print(mi_cadena.isalnum())  #EVALUA SI LA CADENA ESTA FORMADA POR CARACTERES ALFANUMERICOS
mi_cadena = "soy una cadena normal"
print(mi_cadena.isalpha())  #EVALUA SI LA CADENA ESTA FORMADA POR CARACTERES ALFABETICOS

cadena = " Hola soy una cadena que tenia espacios al inicio y al final "
print(cadena.strip())  #ELIMINA ESPACIOS AL INICIO Y FINAL DE LA CADENA

numero = 345
print(str(numero).zfill(
    7))  #RELLENA CON 0 HASTA LLEGAR AL NUMERO PASADO COMO PARAMETRO

cadena = " y ".join(["1", "2", "3", "4", "5"])  #UNIR UNA CADENA A UNA LISTA
print(cadena)

cadena_a_lista = "Python, Java, C++, Typescritp"
print(
    cadena_a_lista.split(",")
)  #DIVIDE Y CONVIERTE LA CADENA EN UN ARRAY DEPENDIENDO EL PARAMETRO PASADO

#RECORRER UNA CADENA
for cadena in mi_cadena:
    print(cadena)

#EJERCICIO ---------------------------------------------------------------------

salir = False

#FUNCIONES PARA EVALUAR LAS PALABRAS


def esPalindromo():
    palabra = input('Ingresa la palabra a evaluar: ')

    palabra_invertida = palabra[::-1]

    if palabra.lower() == palabra_invertida.lower():
        print(f'La palabra {palabra} es palindroma')
    else:
        print(f'La palabra {palabra} no es palindroma')


def esAnagrama():
    palabra_1 = input("Ingrese palabra 1: ")
    palabra_2 = input("Ingrese palabra 2: ")

    if sorted(palabra_1) == sorted(palabra_2):
        print("Las palabras ingresadas son anagramas")
    else:
        print("Las palabras ingresadas no son anagramas")


def esIsograma(palabra):
    letras = set()
    palabra = palabra.lower()

    for letra in palabra:
        if letra.isalpha():
            if letra in letras:
                return False
            letras.add(letra)
    return True


def evaluarIsograma():

    palabra_1 = input("Ingrese palabra 1: ").strip()
    palabra_2 = input("Ingrese palabra 2: ").strip()

    isograma_1 = esIsograma(palabra_1)
    isograma_2 = esIsograma(palabra_2)

    if isograma_1 and isograma_2:
        print(f"Ambas palabras '{palabra_1}' y '{palabra_2}' son isogramas.")
    elif isograma_1 and not isograma_2:
        print(
            f"La palabra '{palabra_1}' es un isograma, pero '{palabra_2}' no lo es."
        )
    elif not isograma_1 and isograma_2:
        print(
            f"La palabra '{palabra_2}' es un isograma, pero '{palabra_1}' no lo es."
        )
    else:
        print(
            f"Ninguna de las dos palabras ('{palabra_1}' y '{palabra_2}') es un isograma."
        )


while not salir:

    #MENU INTERACTIVO

    print('''---BIENVENIDO AL EVALUADOR DE PALABRAS---\n
            1. Evaluar palindromos
            2. Evaluar Anagramas
            3. Evaluar Isogramas
            4. Salir''')

    opcion = input('Ingresa una opción: ').strip()

    match opcion:
        case '1':
            esPalindromo()
        case '2':
            esAnagrama()
        case '3':
            evaluarIsograma()
        case '4':
            print('Saliendo del programa...')
            salir = True
