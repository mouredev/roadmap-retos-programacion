'''
 * EJERCICIO:
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
 * - Isogramas
'''

## CONCATENATION ##

string:str = "[+] Hello" + " " + "World!"   # Use the + operator to join two or morw strings

print (string)


## REPETITION ##

string = "Hello World\t" * 3 # Use the * operator to repeat a string a specified number of times

print (string)


## INDEXES AND SLICES ##

string = "Hello Python"

print(string[0], string[-1])    # Indexes: You can access a character using its index
print(string[0:3])  # Slicing: To extract parts of a string


## LENGTH ##

len_str = len(string)   # Get the length of the strings: With the len() function

print(len_str)  

## TRANSFORMATIONS METHODS ##

upper_str = string.upper()  # HELLO PYTHON
print(upper_str)

lower_str = string.lower()  # hello python
print(lower_str)

cap_str = string.capitalize()   # Hello python
print(cap_str)

title_str = string.title()  # Hello Python
print(title_str)

title_swap = string.swapcase()  # hELLO pYTHON
print(title_swap)

## SEARCH AND REPLACE ##

print(string.find('Python'))    # 6  Returns the index of the first occurrence of a substring, or -1 if not found.

print(string.index('Python'))   # 6  the same that find but raises an error if the substring is not found.

print(string.replace("Python","Hello")) # replace all the ocurrences of a substring with another.

print(string.count("Hello"))    # 2 Counts how many times a substring appears in the string.

## COMPARISON ##


print("a" < "b")    # Strings can be compared using comparison operators.

print("HELLO" == "HELLO")

## VALIDATION METHODS ##

print(string.startswith("Hello"))   # Checks if the string starts with a substring.

print(string.endswith("Python"))    # Checks if the string ends with a substring. 

print(string.isalpha())     # Checks if all characters are letters. 

print(string.isdigit())     # Checks if all characters are digits.

print(string.isspace())     # Checks if the string contains only whitespace.

print(string.isalnum())     # Checks if the string is alphanumeric ( contains letters and/or digits ).

## SPLIT AND JOIN ##

print(string.split())       # Splits the string into a list of  substrings based on a delimeter ( by default, spaces ).

print(string.join(" !!!!")) # Joins the elements of a list into a string, using a separator.

## TRIM WHITESPACE ##

print('   string '.strip())     # Removes leading and trailing whitespace.

print('    string'.lstrip())    # Removes leading whitespace.

print('string    '.rstrip())    # Removes trailing whitespace.

## STRING FORMATTING ##

print("[+] {}".format(string))  # Used to format a string with values.

print(f"[+] {string}")          # f-strigns: A simplified syntax for string formatting.

## REVERSING ##

print(string[::-1])     # There isn't a direct method to reverse a string, but you can use slicing.



## EXTRA ##


text1 = input("\n[+] Write the first word without accents, character specials:\t")
text2 = input("\n[+] Write the second word without accents, character specials:\t")

def get_text(text1, text2) -> str:


    if (sorted(set(text1)) == sorted(set(text2))):
        print("\n[+] Son anagramas\n")
    elif (text1.strip() == (text1.strip()[::-1]) and text2.strip() == (text2.strip()[::-1])):
        print("\n[+] Son Palindromos\n")
    elif (sorted(set(text1)) == sorted(text1) and sorted(set(text2)) == sorted(text2)):

        for i in text1:
            if i in text2:
                break
            else:
                print("\n[+] Son Isogramas\n")
                break
    else:
        print("\n[!] Hubo algun error\n")


get_text(text1, text2)

