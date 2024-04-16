### 04_Cadenas de Caracteres ###

#creating string
my_string = "Hello Python"
print(my_string)

multiline_string="""Hello Python Im mr David
Hello Python Im mr David
Hello Python Im mr David
"""
print(multiline_string)

#String Concatenation

name = "David"
last_name = "Parrado"
space = " "
full_name = name + space + last_name
print(full_name)

#separating strings 

print("Python es un buen lenguaje.\nNo crees?")
print("Python es un buen lenguaje.\tNo crees?")

#Strin formatting 
# strings and numbers
operation = "area"
radius = 10
pi = 3.14
area = pi * radius ** 2
#formated_string = 'The %s of circle with a radius %d is %.2f.' %(operation,radius, area)
#print(formated_string)

# f-strings

formated_fstring = f'The {operation} of circle with a radius {radius} is {area:.2f}.'
print(formated_fstring)

#python Strings as sequences of characters

lenguaje = "Python"
a,b,c,d,e,f = lenguaje
print(a)
print(b)
print(c)
print(d)
print(e)
print(f,"\n")

#accesing for index

first_letter = lenguaje[0]
print(first_letter)
second_letter = lenguaje[1]
print(second_letter)
last_index = len(lenguaje) - 1
last_letter = lenguaje[last_index]
print(last_letter,"\n")

#slicing python strings

first_three = lenguaje[0:3] #Del caracter en el indice 0 hasta el 3 pero no incluye este.
print(first_three)
last_three = lenguaje[3:6]
#print(last_three)

#otra forma
last_three = lenguaje[3:]
print(last_three,"\n")

#Reversing a string 

print(my_string[::-1],"\n")

#Skipping Characters While Slicing

ch = lenguaje[0:6:2]
print(ch,"\n")

#String Methods

other_string = "aprendiendo\tpython"
print(other_string.capitalize()) #coloca en mayuscula la primera letra del string
print(other_string.count("e")) #cuenta las veces que aparace la letra 
print(other_string.endswith("ion")) #verifica si el string finaliza con la cadena o letra especificada
print(other_string.expandtabs(10)) #reemplaza tabs por espacios
print(my_string.find("n")) # retorna el indice de la primera ocurrencia de una letra o cadena, retorna -1 si no hay ocurrencias
print(my_string.rfind("o")) # retorna el indice de la ultima ocurrencia de una letra o cadena, retorna -1 si no hay ocurrencias

print(other_string.isalnum()) #revisa si es un caracter alphanumerico
print(other_string.isalpha()) #revisa si es un caracter alfabetico (a-z A-Z)
print(other_string.isdecimal()) #revisa si es un caracter decimal (0-9)
print(other_string.islower()) #revisa si la cadena esta en minusculas
print(other_string.isupper()) #revisa si la cadena esta en mayusculas

languages = ["Html" , "CSS" , "JS", "React"]
res =" ".join(languages) #Retorna una cadena concatenada
print(res)

print(my_string.strip("He")) # elimina todos los caracteres especificados de la cadena

print(my_string.replace("Python","World")) #Reemplaza subcadenas por cadenas especificadas

print(multiline_string.split()) # Divide la cadena, separada por caracteres dados o por espacios

print(other_string.title())

print(other_string.swapcase()) #pone mayusculas en minusculas y visceversa


print(other_string.startswith("ap")) #valida si la cadena comienza con una letra o subcadena especificada

# EXTRA #

def my_string (cadena_1 :str, cadena_2:str):
    
    #Comprobacion Palindromo
    if  cadena_1.lower() == cadena_1.lower()[::-1] and cadena_2.lower() == cadena_2.lower()[::-1]  :
        print(f"la palabras {cadena_1} y {cadena_2} son palindromos")
    elif cadena_1.lower() ==  cadena_1.lower()[::-1] and cadena_2.lower() != cadena_2.lower()[::-1] :
        print(f"la palabra {cadena_1} es un palindromo pero {cadena_2} no lo es")
    elif cadena_1.lower() != cadena_1.lower()[::-1] and cadena_2.lower() == cadena_2.lower()[::-1]:
        print(f" la palabra {cadena_2} es un palindromo pero {cadena_1} no lo es")
    else:
        print(f" las palbras {cadena_1} y {cadena_2} no son palindromos" )

    #comprobacion anagrama
    if sorted(cadena_1.lower()) == sorted(cadena_2.lower()) and cadena_1.lower() != cadena_2.lower():
        print(f"Las palabras {cadena_1} y {cadena_2} son anagramas entre si")
    else:
        print(f"Las palabras {cadena_1} y {cadena_2}  no son anagramas entre si")
    
    #comprobacion isograma
    def isogram(word: str) -> bool:
        word_dict = dict()
        for ch in word:
            word_dict[ch] = word_dict.get(ch, 0) + 1
        
        isogram = True
        values = list(word_dict.values())
        isogram_len = values[0]
        for word_count in values :
            if word_count != isogram_len:
                isogram = False
                break
        return isogram
    print(f"La palabra {cadena_1} es un isograma?: {isogram(cadena_1)}")
    print(f"La palabra {cadena_2} es un isograma?: {isogram(cadena_2)}")

my_string("iman" , "mani")
