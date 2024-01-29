#String

my_string = "Esto es una cadena de caracteres"
print(my_string)

#Formateo de cadenas
number = 5
string_format = "El número es: " + str(number)
print(string_format)

string_format_1 = "Los números son {} y {}".format(5, 10)
print(string_format_1)

string_format_2 = "Los números son {n1} y {n2}".format(n1=15, n2=10)
print(string_format_2)

n1 = 30
n2 = 12
string_format_3 = f"El resultado de sumar {n1} + {n2} = {n1+n2}"
print(string_format_3)

#Concatenar cadenas
string1 = "Hola"
string2 = "Mundo"
print(string1+" "+ string2)

#Multiplicar string por un int
print(string1*3)

#Saber si una cadena contiene otra cadena
print("mola" in "Python mola")

#Longitud de una cadena
print(len(my_string))

#Acceder a una posición de la cadena
print(my_string[6])
print(my_string[-1]) #accede a la última posición
print(my_string[0:10])#accede desde la posición 0 a la 12 
print(my_string[10:])#accede desde la posición indicada hasta el final

#Métodos
#capitalize() Pone la primera letra en mayúscula
print(my_string.capitalize())

#lower() Convierte la cadena a minúsculas
string3 = "Hola MUNDO"
print(string3.lower())

#swapcase() Convierte los caracteres alfabéticos con mayúsculas en minúsculas y viceversa
print(string3.swapcase())

#upper Convierte la cadena a mayúsculas
print(string3.upper())

#count Cuenta las veces que la cadena indicada aparece en una cadena
print(my_string.count("ca"))

#isalnum() Devuelve True si la cadena esta formada únicamente por caracteres alfanuméricos y False al contrario
print(my_string.isalnum())

#strip() Elimina los espacios en blanco de izquierda y derecha
string4 = "           Aquí no hay espacios   "
print(string4)
print(string4.strip())

#join devuelve la primera cadena unida a cada uno de los elementos de la lista que se le pasa como parámetro
string5 = " y "
print(string5.join(["1","2","3"]))

#split() Divide una cadena en subcadenas y las devuelve almacenadas en una lista
languages = "Python, Java, C"
print(languages.split(","))

print("\n----------------------------")
print("EXTRA")

#EXTRA
def validate_word(word1, word2):
    word1_lower = word1.lower()
    word2_lower = word2.lower()

    #Palíndromo
    #Se ordena la palabra a la inversa
    word1_reverse = word1_lower[::-1]
    word2_reverse = word2_lower[::-1]
    
    #Comparamos si las palabras original y la inversa para ver si son iguales
    if word1_lower == word1_reverse and word2_lower == word2_reverse:
        print(f"Las palabras {word1} y {word2} son palíndromos\n")
    elif word1_lower == word1_reverse and word2_lower != word2_reverse:
        print(f"La palabra {word1} es un palíndromo\n")
    elif word1_lower != word1_reverse and word2_lower == word2_reverse:
        print(f"La palabra {word2} es un palíndromo\n")
    else:
        print(f"Las palabras {word1} y {word2} no son un palíndromo\n")
    
    #Anagrama
    #Con el método sorted() convertimos el string en una lista y la ordenamos, se comparan ambas lista para ver si son iguales
    if sorted(word1_lower) == sorted(word2_lower):
        print(f"La palabra {word1_lower} es un anagrama de la palabra {word2_lower}\n")
    else:
        print(f"La palabra {word1_lower} no es un anagrama de la palabra {word2_lower}\n")  
        
    #Isograma
    if len(word1_lower) == len(set(word1_lower)) and len(word2_lower) == len(set(word2_lower)):
        print(f"{word1_lower} y {word2_lower} son isogramas\n")
    elif len(word1_lower) == len(set(word1_lower)) and len(word2_lower) != len(set(word2_lower)):
        print(f"{word1_lower} es un isograma\n")
    elif len(word1_lower) != len(set(word1_lower)) and len(word2_lower) == len(set(word2_lower)):
        print(f"{word2_lower} es un isograma\n")
    else:
        print(print(f"{word1_lower} y {word2_lower}  no son isogramas\n"))

validate_word("Ana", "camion")
validate_word("frase", "fresa")