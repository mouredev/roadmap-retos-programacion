from unicodedata import normalize

#Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
# *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
# *   interpolación, verificación...

## Acceso a caracteres especificos:
cadena = "Hola, Mundo!"
letra_a = cadena[3]
print(f"Este es un caracter perteneciente a la cadena 'Hola, Mundo!': {letra_a}")

## Subcadenas
### Se usa la tecnica llamada slicing:
otra_cadena = "Esta es una cadena que es tratada como ejemplo"
que_es = otra_cadena[:19]
print(f"Esta es una subcadena y pertenece a la cadena 'otra_cadena': {que_es}")

## logitud
longitud_otra_cadena = len(otra_cadena)
print(f"Esta es la cantidad de caracteres de 'otra_cadena', usamos la funcion integrada `len()`: {longitud_otra_cadena}")

## concatenacion
cadena_ejemplo1 = "Esta es la cadena 1"
cadena_ejemplo2 = "Esta es la cadena 2"
cadena_concatenada = cadena_ejemplo1 + " " + "y" + "" + cadena_ejemplo2
print(f"Usamos el operador de suma (+) para concatenar strings 'para unirlos': {cadena_concatenada}")

## repeticion
cadena_a_ser_repetida = "hola "
muchos_holas = cadena_a_ser_repetida * 8
print(f"Esta es una cadena repetida usando el operador (*) de multiplicacion: {muchos_holas}")

## recorrido
cadena_larga = "Esta es una cadena larga que sera recorrida, te quiero MoureDev ❤️"
for caracter in cadena_larga:
    print(caracter)

## conversion
mi_cadena = "Esta es una LinDa cadena"
### Convertir a uppercase
mi_cadena_upper = mi_cadena.upper()
print(f"Esta es la cadena declarada en su forma a uppercase: {mi_cadena_upper}")
### Convertir a lowercase
mi_cadena_lower = mi_cadena.lower()
print(f"Esta es la cadena declarada en su forma a lowercase: {mi_cadena_lower}")
### Convertir a capitalize
mi_cadena_capitalize = mi_cadena.capitalize()
print(f"Esta es la cadena declarada en su forma a capitalize: {mi_cadena_capitalize}")

## reemplazo
### Reemplazar una subcadena de la cadena principal por otra:
cadena_normal = "Esta es una cadena normal que se usa para un ejemplo"
cadena_cambiada = cadena_normal.replace("normal", "RARA")
print(f"Esta es una cadena que reemplaza una subcadena de la cadena principal: {cadena_cambiada}")

## division
### Dividir los caracteres o subcadenas de la cadena principal usando .split():
cadena_a_dividir = "Hola esta es una cadena que sera dividida."
cadena_dividida = cadena_a_dividir.split(" ")
print(f"Esta es una lista con todos las subcadenas que fueron divididas usando .split(): {cadena_dividida}")

## union
### Unir cadenas de una lista usando el metodo .join(): Cada caracter o elemento de la lista se concatenara junto a la cadena especificada
### como objeto que usa el metodo.
lista_de_cadenas = ["Python", "es", "un", "lenguaje", "de", "programacion"]
cadena_unida = " ".join(lista_de_cadenas)
print(f"Esta es la cadena unida usando el metodo .join(): {cadena_unida}")

## Interpolacion
### Haciendo iterpolacion de cadenas usando el metodo .format()
nombre = "Alvaro"
edad = 19
cadena_interpolada = "Hola mi nombre es {1} y tengo {0}".format(edad, nombre)
print(f"Esta es la cadena iterpolada resultante usando el metodo .format(): {cadena_interpolada}")

## Verificacion
cadena_numerica = "21948190248102931"
es_numerica = cadena_numerica.isnumeric()
print(f"Usando el metodo .isnumeric() podemos verificar si todos los elementos de la cadena son numeros. Devuelve un valor booleano: {es_numerica}")
cadena_con_digitos = "123131439"
tiene_digitos = cadena_con_digitos.isdigit()
print(f"Usando el metodo .isdigit() podemos verificar si todos los elementos de la cadena son digitos. Devuelve un valor booleano: {tiene_digitos}")
cadena_de_letras = "HOLA ESTA ES UNA CADENA UPPERCASE"
es_alfabetico = cadena_de_letras.isalpha()
print(f"Verifica si todos los caracteres de la cadena son alfabeticos, devuelve valor booleano: {es_alfabetico}")
es_alfanumerico = cadena_de_letras.isalnum()
print(f"Verifica si todos los caracteres de la cadena son alfanumericos, devuelve valor booleano: {es_alfanumerico}")
empieza_con_H = cadena_de_letras.startswith("H")
print(f"Verifica si la cadena termina con 'H', devuelve valor booleano: {empieza_con_H}")
termina_con_E = cadena_de_letras.endswith("E")
print(f"Verifica si la cadena termina con 'E', devuelve valor booleano: {termina_con_E}")
es_uppercase = cadena_de_letras.isupper()
print(f"Verifica si la cadena es uppercase: {es_uppercase}")
es_lowercase = cadena_de_letras.islower()
print(f"Verifica si la cadena es lowercase: {es_lowercase}")
tiene_espacios = cadena_de_letras.isspace()
print(f"Verifica si la cadena contiene solo espacios en blanco, devuelve valor booleano: {tiene_espacios}")

## Busqueda:
my_string = "Mi cadena de caracteres de Python"
encontrar_cadena = my_string.find("cadena")
print(f"Devuelve el primer numero de indice que coincide con la cadena pasada al metodo .find(): {encontrar_cadena}")
dame_index = my_string.rfind("caracteres")
print(f"Devuelve la primera posicion de la coincidencia pasada: {dame_index}")
mi_indice = my_string.index("c")
print(f"Devuelve el indice de la primera coincidencia encontrada: {mi_indice}")
contar_letras_e = my_string.count("e")
print(f"Contar las coincidencias encontradas en la cadena: {contar_letras_e}")

# DIFICULTAD EXTRA (opcional):
def anagrama(string1: str, string2 : str):
    anagrama1 = string1.replace(" ", "").lower()
    anagrama2 = string2.replace(" ", "").lower()
    return sorted(anagrama1) == sorted(anagrama2)

def palindroma(string1 : str):
    trans_tab = dict.fromkeys(map(ord, u'\u0301\u0308'), None)
    string1 = normalize('NFKC', normalize('NFKD', string1).translate(trans_tab))
    palindroma1 = string1.replace(" ", "").lower()
    return palindroma1 == palindroma1[::-1]

def isograma(string1 : str, string2 : str):
    for char in string1:
        if string1.count(char) == 1:
            pass
        else:
            return False
    for char in string2:
        if string2.count(char) == 1:
            pass
        else:
            return False
    return True

def verificar_palabras():
    string1 = input("Primera palabra a verificar: ")
    string2 = input("Segunda palabra a verificar: ")

    while True:
        comprobacion = input("Que quieres comprobar con estas palabras? Si son: (anagramas, palindromas o isogramas) o escribe 'cancelar' si deseas cerrar la ejecucion, escribe: ")
        if comprobacion.lower() == 'cancelar':
            break
        elif comprobacion.lower() == 'anagramas':
            resultado = anagrama(string1, string2)
            if resultado:
                print(f"Las dos palabras que me proporcionaste son anagramas")
            else:
                print("No son anagramas")
        elif comprobacion.lower() == 'palindromas':
            resultado1 = palindroma(string1)
            resultado2 = palindroma(string2)
            if resultado1:
                print(f"La primera palabra es palindroma")
            else:
                print(f"La primera palabra no es palindroma")
            if resultado2:
                print(f"La segunda palabra es palindroma")
            else:
                print(f"La segunda palabra no es palindroma")
        elif comprobacion.lower() == 'isogramas':
            resultado = isograma(string1, string2)
            if resultado:
                print(f"Las dos palabras son isogramas")
            else:
                print(f"No son isogramas")

verificar_palabras()