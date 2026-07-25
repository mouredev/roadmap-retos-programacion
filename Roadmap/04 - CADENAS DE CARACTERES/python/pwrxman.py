

"""
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 *   interpolación, verificación...
 """

# Creating a string
letter="P"
string="My string"
hello="Hello World!!"
print(letter)
print(string)
print(hello)


multiline_string="""this is an example of a string divided in several lines.
The power of you is coming from inside of you.
The life is great, enjoy it!!"""
print(multiline_string)


# To get the length of a string, use the len() function.

a = "Hello, World!"
print(len(a))


# To check if a certain phrase or character is present in a string, we can use the keyword in.
# Check if "free" is present in the following text:
txt = "The best things in life are free!"
print("free" in txt)

# string concatenation
name="Andrei"
last_name=("Med")
full_name=name+" "+last_name

# Strings only
first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formated_string)

# string interpolation
a = 4
b = 3
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')

# Sequence of characters
language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n

# String index normal from 0 to the end
language = 'Python'
first_letter = language[0]
print(first_letter) # P
second_letter = language[1]
print(second_letter) # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter)

# String index inverse order the end to -len
language = 'Python'
last_letter = language[-1]
print(f"\n{last_letter}") # n
second_last = language[-2]
print(second_last) # o
print(language[-len(language)])

# Reversing a String
hello = 'Hello, World!'
print("\nreversing the string  --> ", hello[::-1]) 

# substrings
language = 'Python'
pto = language[0:6:2] #
print(pto) # Pto

# Methods
phrase="the world is ours, enjoy it!"

# Convert first character Upper
print(phrase.capitalize(), "\n")

# count(substring, start=.., end=..). 
# Returns the number of times a specified value occurs in a string. 
# The start is a starting indexing for counting and end is the last index to count.
# return 0 if not found
print("COUNT")
print(phrase.count('w')) 
print(phrase.count('o')) 
print(phrase.count('ld', 7, 14)) 
print(phrase.count('x'))

# find(): Returns the index of the first occurrence of a substring, if not found returns -1
print("FIND")
print("\n", phrase.find('ours'))
print(phrase.find('the'))
print(phrase.find('xx'))

# format(): formats string into a nicer output
print("FORMAT")
radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'The area of a circle with radius {} is {}'.format(str(radius), str(area))
print("\n", result) # The area of a circle with radius 10 is 314

# isalnum()	Returns True if all characters in the string are alphanumeric
print("ISALNUM")
phrase="No pain no gain"
print("\n", phrase.isalnum())
phrase="Pele won 5 futbol wold championships"
print("\n", phrase.isalnum())

# isalpha()	Returns True if all characters in the string are in the alphabet
print("ISALPHA")

phrase = 'Las clases de Moure'
print(phrase.isalpha()) # False, space is excluded
phrase = 'LasclasesdeMoure'
print(phrase.isalpha()) 
num = '85478'
print(num.isalpha()) 

# isdecimal()	Returns True if all characters in the string are decimals '0123456789'
print("DECIMAL")

phrase = 'thirty'
print(phrase.isdecimal())
phrase = '69587'
print(phrase.isdecimal()) 
phrase = '3.1416'
print(phrase.isdecimal())

# isdigit()	Returns True if all characters in the string are digits 0123456789 other unicode characters for numbers) 
print("ISDIGIT")

phrase = 'Thirty'
print(phrase.isdigit())
phrase = '53489'
print(phrase.isdigit())
phrase = '\u00B2'
print(phrase.isdigit())

# islower()	Returns True if all characters in the string are lower case
print("ISLOWER")

phrase = 'Los cursos de Moure'
print(phrase.islower()) 
phrase = 'las clases de python'
print(phrase.islower())

# isupper()	Returns True if all characters in the string are upper case
print("ISUPPER")

phrase = 'Los cursos de Moure'
print(phrase.isupper()) 
phrase = 'THE COURSE OF PYTHON'
print(phrase.isupper()) 


# strip()	Returns a trimmed version of the string
print("STRIP")

phrase = 'thirty days of vacationnn'
print("\n", phrase.strip('nothdv')) 


# upper()	Converts a string into upper case
print("UPPER")

print(phrase.upper())

print("\n\n< < < < < < < < < < < < < < < < <   INICIA LA DIFICULTAD EXTRA   > > > > > > > > > > > > > > > > >\n\n")

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos    Palabra o frase que se lee identicamente en ambos sentidos
                    Ejemplos:  "Dábale arroz a la zorra el abad", "reconocer", "radar", "sanas", "amor a roma",
                    "Somos o no somos", "Isaac no ronca así", "Sé verlas al revés", "Amó la paloma", 
                    "Anita lava la tina", "Luz azul", "Yo hago yoga hoy", "Ana lava lana"

 * - Anagramas      Palabra o frase con las mismas letras pero con distinto significado. Ejemplos:
                    "Sergio – riesgo", "ramo – armo", "delira – lidera", "anagrama – amar gana",
                    "Istmo de Panama – Tío Sam me da pan", "Valiente – Ni te vale", "Llave sorda > El Salvador.",
                    "Llenaba > Ballena", "Botines > Bisonte", "Cara - arca"                    
                    "Lácteo - coleta", "Retener - enterré", "Castor - castro", "Seto - esto",
                    "Nido - Odín", "Lobo - bolo", "Toledo - El todo"

 * - Isogramas      Palabra o frase en la que ninguna letra del alfabeto aparece más de una vez,
                    es decir, no tiene letras repetidas. ​ 
                    Si cada letra aparece solo una vez será un isograma, Ejemplos:
                    "lumberjacks", "background", "downstream", "six-year-old", "yuxtaponer",
                    "centrifugado", "luteranismo", "adulteros", "hiperblandos"
 """

def is_palindromo():
    str1 = input("Ingrese la palabra a Analizar: ")
    str11 = str1
    rts1 = str1[::-1]
    lstrts1 = rts1.split()
    lststr1 = str1.split()
    str1 = ""  
    rts1 = ""
    for x in lststr1:
        str1 = str1 + x
    
    for x in lstrts1:
        rts1 = rts1 + x

    if str1 == rts1:
        print(f"<{str11}>  es un Palindromo! ")
    else:
        print(f"{str11} NO es un Palindromo")
      
    print(f"str1 despues del split {lststr1}\nrts1 ya invertida y sin blanco {lstrts1}")
    
    return


def is_anagram():
    str1 = input("Ingrese la palabra 1 a Analizar: ")
    str2 = input("Ingrese la palabra 2 a Analizar: ")
    
    for x in str1:
        if str2.find(x) < 0:
            return print(f"{str1} NO es anagrama de {str2}")
            
    return print(f"{str1} SI es anagrama de {str2}")

def is_isograma():
    str1 = input("Ingrese la palabra a Analizar: ")
    str2=""
    esisogram=True
    for i in range(len(str1)):
        if str2.find(str1[i]) < 0:
            str2=str2 + str1[i]
        else:
            esisogram=False
    siono = "SI" if esisogram else "NO"
    return print(f"la palabra o frase {str1} -> {siono} es Isograma")

while True:
    action = input("Ingrese el Análisis a Realizar: \n(P) Pal´ndromo\n(A) Anagrama\n(i) Isograma\n(q) Terminar : ")

    match action:
        case "p":
            is_palindromo()

        case "a":
            is_anagram()

        case "i":
            is_isograma()

        case "q":
            break


