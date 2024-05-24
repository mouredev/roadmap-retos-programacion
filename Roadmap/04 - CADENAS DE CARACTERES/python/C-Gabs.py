#Reto 04

'''EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 *   interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas'''

string = "Hola mundo"
string_2 = " Hola python"
string_3 = ""

#Concatenación
string_3 = string + string_2
print(string_3)
string_3 = "hola" + " Pandas"
print(string_3)

#indexacion
print(string[3])

print(string_3.join(["Hola","Mundo"," Hola ", "python"]))

#Repetición
print(string*3)

#Conversión a mayusculas o minusculas
string = string.upper()
print(string)
string = string.lower()
print(string)
string = string.capitalize()
print(string)
print(string.swapcase())
print(string.title())

#busqueda 
print(string.find("o"))
print(string.rfind("o",2,5)) #Devuelve -1 si no hay coincidencias
print(string.index("o",1,3))
#print(string.rindex("o",2,5)) genera un ValueError si no hay coincidencias
print("l" in string)
print(string.startswith("Hola"))
print(string.endswith("on"))
#conteo de coincidencias
string = "   hola python, hola swift, hola numpy  "
print(string.count("hola"))
print(string.count("py"))

#longitud
print(len(string))

#Recorrido
for char in string:
    print(char)

#Reemplazo

print(string.replace(" ", "#"))
print(string.rstrip()) #Remueve los espacios al final del texto
print(string.strip()) #Remueve los espacios al inicio del texto
string = string.removeprefix("   ")
print(string) 
string = string.removesuffix("  ")
print(string)
string = string.replace(",", "")

#División
print(string.split(" "))

#interpolación
print(f"string 1: {string} string 2: {string_2} estring 3: {string_3}")

#formateo
print("Hola {}, hola {}".format("brais","mundo"))

#rodajas
print(string[2:7])
print(string[::-1])

#conversion lista cadena y cadena a lista
print(list(string))
print("".join(["hola"," ","mundo"]))

#conversion a enteros
print(type(int("123")))

#comprobaciones
print(string.isalpha())
print("12w31j2d3h55rt42".isalnum())
print("1234565436".isdigit())
print("1234565436".isnumeric())
print("juan".islower())
print("JUAN".isupper())
print("Juan".istitle())
print("  ".isspace())
print(string.isascii())


# Reto Extra

def palindromo(string_1, string_2):
    if string_1.lower().replace(" ","") == string_1[::-1].lower().replace(" ",""):
        print(f"{string_1} Es palindromo")
    else:
        print(f"{string_1} No es palindromo")
    if string_1.lower().replace(" ","") == string_1[::-1].lower().replace(" ",""):
        print(f"{string_2} Es palindromo")
    else:
        print(f"{string_2} No es palindromo")
     
palindromo("dabale arroz a la zorra el abad","dabale arroz a la zorra el abad")


def anagrama(string_1,string_2):
    es_anagrama = "No es un anagrama"
    
    if string_1.lower() == string_2.lower():
        es_anagrama = "No es un anagrama"
    
    if sorted(string_1.lower().replace(" ","")) == sorted(string_2.lower().replace(" ","")):
        es_anagrama = "Es un anagrama"

    return es_anagrama 

print(anagrama("animales","milanesa"))


def isograma(string_1):
    string_dict = dict()
    for char in string_1:
        if char not in string_dict.keys():
            string_dict[char] = string_1.count(char)
    values = list(string_dict.values())
    repeticiones = values[0]
    for value in values:
        if repeticiones != values[value]:
            return "No es un isograma"
    return "Es un isograma"
print(isograma("hola"))


#otra forma de resolver el anagrama

def anagrama_2(string_1,string_2):
    sumaord_1 = 0
    sumaord_2 = 0
    for char in string_1.lower().replace(" ",""):
        sumaord_1 += ord(char)
    for char in string_2.lower().replace(" ",""):
        sumaord_2 += ord(char)
    if sumaord_1 == sumaord_2:
        return True
    else:
        return False
print(anagrama_2("ani MAles","mila nesa"))
