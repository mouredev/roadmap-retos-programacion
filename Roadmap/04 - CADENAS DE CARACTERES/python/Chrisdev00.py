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

# Creando una cadena

text = "P"
print(text)

multiline_string = """ 
Este es un ejemplo de una cadena
en varias lineas usando comillas dobles, tambien se puede
usar comillas simples.
"""
print(multiline_string)

# Concatenacion de cadenas

first_name = "Pepito"
last_name = "Perez"
space = " "

full_name = first_name + space +  last_name
print(full_name)


# Secuencia de escape en cadenas

"""
En Python y otros lenguajes de programación, \ seguido de un carácter es una secuencia de escape. 
Veamos los caracteres de escape más comunes:

\n: nueva línea
\t: Tabulador significa (8 espacios)
\\: barra invertida
\': Una frase (')
\": comillas dobles (")
"""

print('Este es un ejemplo de como usar una secuencia de escape.\nUsando barra invertida') # nueva linea
print('Dias\tTemas\tEjercicios')                                                # añadiendo tabulacion o 4 espacios 
print('Dia 4\t4\t4')
print('Dia 5\t5\t101')
print('Simbolo de barra invertida (\\)')                                        # Para escribir barra invertida
print('Usando comillas simples y comillas dobles \"Hola, Mundo!\"')


# Formateo de cadenas

a = 2
b = 6

print(f"{a} + {b} = {a+b}")
print(f'{a} / {b} = {a / b:.2f}')  #  formatea un número decimal(float) para que tenga dos lugares decimales después del punto decimal.


# Desempaquetando caracteres de una cadena

lenguaje = "Python"
a,b,c,d,e,f = lenguaje             # desempaquetando en secuencia los caracteres en las variables
print(a)            
print(b)            
print(c)            
print(d)            
print(e)            
print(f)    

# Accediendo a caracteres en cadenas por indice

lenguaje = "Python"
first_letter = lenguaje[0]
print(first_letter)
second_letter = lenguaje[1]
print(second_letter) 
last_index = len(lenguaje) - 1
last_letter = lenguaje[last_index]
print(last_letter)

last_letter = lenguaje[-1]           # Comenzando desde la derecha ultimo indice
print(last_letter)
second_last = lenguaje[-2]           # Comenzando desde la derecha penultimo indice
print(second_last)


# Separar o Cortar Cadenas en python

lenguaje = "JavaScript"
firts_three_char = lenguaje[0:3]     # Comienza en el indice 0 hasta el numero 3 pero sin incluir el numero 3
print(firts_three_char)
other_three = lenguaje[3:6]
print(other_three)
last_four = lenguaje[-4:]            # last_four = lenguaje[6:]  print(last_four)  Otra forma de escribir
print(last_four)


# Invertir una cadena 

my_string = "Hola mundo!"
print(my_string[::-1])

# Saltar caracteres mientras se corta   // slicing [start:end:step]

lenguaje = "Kotlin"
kti = lenguaje[0:6:2]
print(kti)


# Convertir caracteres de una cadena a mayusculas

my_string = "hola mundo"
print(my_string.capitalize())              # Convierte solo el primer caracter a mayuscula
print(my_string.upper())                   # Convierte todos los caracteres a mayusculas

# Convertir caracteres de una cadena a minusculas

my_other_string = "PYTHON"
print(my_other_string[0].lower() + my_other_string[1:])   # Convierte solo el primer caracter a minuscula
print(my_other_string.lower())                           # Convierte todos los caracteres a minusculas

variable = "Hola Mundo"
print(variable.swapcase())   # convierte todos los caracteres en mayúsculas a minúsculas y todos los caracteres en minúsculas a mayúsculas.     

# Contar cuantas veces aparece un caracter en una cadena   count(substring, start=..., end=...)

my_string = "Retos de programacion"
print(my_string.count("o"))              # 3
print(my_string.count("o",4, 15))        # 1
print(my_string.count("ro",4, 15))       # 1



# Comprobar si una cadena termina con un caracter especifico

text = "road map de programacion"
print(text.endswith("ion"))          # True
print(text.endswith("ción"))         # False, por el acento



# Reemplazar el carácter de tabulación con espacios, el tamaño de tabulación predeterminado es 8. 

my_string = "retos\tde\tprogramacion"
print(my_string)
print(my_string.expandtabs(10))
print(my_string.expandtabs(12))



# Buscar el índice de la primera y ultima aparición de un caracter, si no se encuentra devuelve -1

my_var = "Cadenas de caracteres"
print(my_var.find("e"))
print(my_var.find("de"))
print(my_var.find("f"))

print(my_var.rfind("e"))         # Imprime el indice de la ultima aparicion de un caracter
print(my_var.rfind("te"))        # Imprime el indice de la ultima aparicion de un caracter
print(my_var.rfind("f"))         # Sino lo encuentra retorna -1



# Devuelve el índice más bajo de una subcadena, los argumentos adicionales indican el índice inicial y final 
# los argumentos adicionales indican el índice inicial y final
# si no encuentra el valor da valueError 

my_other_string = "ejercicios de programacion"
sub_string = "de"
print(my_other_string.index(sub_string))          # 11
print(my_other_string.index(sub_string, 2, 13))       # error

print(my_other_string.rindex(sub_string))           # Devuelve el indice mas alto
print(my_other_string.rindex(sub_string, 2, 17))   


# Comprobar caracteres alfanumericos

my_text = "retosdeprogramacion2024"
print(my_text.isalnum())                        # True
my_text_two = "retos de programacion"
print(my_text_two.isalnum())                    # False,  los espacion no son caracteres alfanumericos


# Comprobar si los elementos de una cadena son caracteres alfabeticos

numeros = "123"
print(numeros.isalpha())                        # False

letters = "LogicaDeProgramacion"
print(letters.isalpha())                        # True

cadena = "Logica de Programacion"
print(cadena.isalpha())                         # False


# comprueba si todos los caracteres de una cadena son decimales (0-9)

my_string = "reto numero 4"
print(my_string.isdecimal())                    # False

num = "6574"
print(num.isdecimal())                          # True


# Devolver una cadena concatenada

lenguajes = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(lenguajes)
print(result)

# Reemplazar la subcadena con una cadena determinada

phrase = "road retos de programacion"
print(phrase.replace("retos", "ejercicios"))


#################      EXTRA      #############################


def is_Palindromo (text, text2):

    var_1 = text[::-1].lower().replace(" ", "")
    var_2 = text2[::-1].lower().replace(" ", "")
    if var_1 == text.replace(" ", "") and var_2 == text2.replace(" ", ""):
        print(f"Las palabras '{text}' y '{text2}' son palindromos")
    else:
        print(f"Las palabras '{text}' y '{text2}' no son palindromos")


def is_Anagrama (text , text2):

    var_1 = sorted(text.lower().replace(" ", ""))
    var_2 = sorted(text2.lower().replace(" ", ""))
    if var_1 == var_2:
        print(f"Las palabras '{text}' y '{text2}' son anagramas")
    else:
        print(f"Las palabras '{text}' y '{text2}' no son anagramas")


def is_Isograma (word):

    palabra = word.lower()
    caracteres_filtrados = []  
    
    for caracter in palabra:        
        if caracter.isalpha():            
            caracteres_filtrados.append(caracter)
    
    palabra = ''.join(caracteres_filtrados)
    return len(palabra) == len(set(palabra))

def comprobar_Isograma (text, text2):

    if is_Isograma(text) and is_Isograma(text2):
        print(f"Las palabras '{text}' y '{text2}' son Isogramas.")
    else:
        print(f"Las palabras '{text}' y '{text2}' no son isogramas.")


is_Palindromo("anita lava la tina", "reconocer")
is_Anagrama("anagrama", "amar gana")
comprobar_Isograma ("murcielago", "puerta")

is_Palindromo("zorra", "arroz")
is_Anagrama("Enrique", "quieren")
comprobar_Isograma ("python", "java")



