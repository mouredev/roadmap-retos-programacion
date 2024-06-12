#String

my_str1 = "Hola Mundo"
my_str2 = "hEllo wOrld"
my_str3 = "hha bb sh hha ss"

#Longitud
print("*Longitud")
print(len(my_str1))

#Index del primer caracter encontrado
print("*Index del primer caracter encontrado")
print(my_str1.index("o"))

#Busqueda
print("*Busqueda")
print(my_str1.find("Mu"))

#Repeticiones
print("*Repeticiones")
print(my_str1.count("o"))
print(my_str3.count("ha"))
print(my_str3.count("ha",5))

#Subtring
print("*Subtring")
print(my_str1[2])
print(my_str1[1:3])
print(my_str1[-1])
print(my_str1[-2])


#rstrip y lstrip, ljust,rjust, center
print("*rstrip y lstrip, ljust,rjust, center")
my_str1 = "   Hola Mundo   "
print(my_str1)
print(my_str1.lstrip())
print(my_str1.rstrip())
my_str1 = "---Hola Mundo---"
print(my_str1)
print(my_str1.lstrip("-"))
print(my_str1.rstrip("-"))

print(my_str1.ljust(30,"*"))
print(my_str1.rjust(30))

print(my_str1.center(50,"_"))

#Uppercase, lowercase, capitalize,swapcase, tittle
print("*Uppercase, lowercase, capitalize,swapcase, tittle")
print(my_str2.upper())
print(my_str2.lower())
print(my_str2.capitalize())
print(my_str2.swapcase())
print(my_str2.title())

#Concatenacion
print("*Concatenacion")
my_oper = my_str1 + " " + my_str2
print(my_oper)
print(my_str2.join(["aa","bb"]))
print("-".join(["aa","bb","cc","dd"]))

#Replace
print("*Replace")
print(my_str1.replace("ola","ello"))

#Separar
print("*Separar")
print(my_str1.split(" "))
print(my_str1.partition("l"))

my_str_lines = "Hola mundo \n" + "testing splitlines \n" + "final test"
print(my_str_lines)
print(my_str_lines.splitlines())

#Verificaciones
print("*Verificaciones")

my_str_numeric = "11"
print(my_str_numeric)
print(f"Aphanumeric: {my_str_numeric.isalnum()}")
print(f"Alphabetic: {my_str_numeric.isalpha()}")
print(f"Decimal:{my_str_numeric.isdecimal()}")
print(f"Digito:{my_str_numeric.isdigit()}")
print(f"Numeric:{my_str_numeric.isnumeric()}")

print(my_str1)
print(f"Aphanumeric: {my_str1.isalnum()}")
print(f"Alphabetic: {my_str1.isalpha()}")
print(f"Decimal:{my_str1.isdecimal()}")
print(f"Digito:{my_str1.isdigit()}")
print(f"Numeric:{my_str1.isnumeric()}")

#Iteraciones
print("*Iteraciones")
my_str1 = "Hola"
for elem in my_str1:
    print(f"for character:{elem}")

i = 0
while i < len(my_str1):
    print(f"while character:{my_str1[i]}")
    i += 1


#Dificultad extra
print("***Dificultad extra")

def is_palindromo(my_str1):
    #Veridicamos si cada palabra es palindroma, se lee igual de izq a der que de der a izq
    palindromos = True
    i = 0
    while i < len(my_str1) // 2:
        if my_str1[i] == my_str1[0 - 1 - i]:
                i += 1
        else:
            palindromos = False
            break
    print(f"Palindromo palabra {my_str1}:{palindromos}")

def get_dict_word(my_str):
    my_dict1 = {}
    for elem in list(my_str):
        my_dict1[elem] = my_dict1.get(elem,0) + 1
    return my_dict1

def is_isograma(my_dict):
     for elem in my_dict.values():
          if elem > 1:
               return False
     return True
          
def is_anagrama(dict1,dict2):
     my_list1 = list(dict1.keys())
     my_list1.sort()
     my_list2 = list(dict2.keys())
     my_list2.sort()
     anagrama = False
     if len(my_list1) == len(my_list2):
          i = 0
          anagrama = True
          while i < len(my_list1):
               if my_list1[i] != my_list2[i] or my_dict1[my_list1[i]] != my_dict2[my_list2[i]]:
                    anagrama = False
                    break
               i += 1
     return anagrama


my_str1 = input("Insertar palabra_1 para verificar:")
my_str2 = input("Insertar palabra_2 para verificar:")
#Verificacion palindromo
is_palindromo(my_str1)
is_palindromo(my_str2)
#Verificacion isograma
my_dict1 = get_dict_word(my_str1)
my_dict2 = get_dict_word(my_str2)
print(f"Isograma palabra {my_str1}:{is_isograma(my_dict1)}")
print(f"Isograma palabra {my_str2}:{is_isograma(my_dict2)}")
#Verificacion de anagrama de las dos palabras
print(f"Son anagramas {my_str1} y {my_str2}: {is_anagrama(my_dict1,my_dict2)}")