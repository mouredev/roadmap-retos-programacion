# #04 - Python -> Jesus Antonio Escamilla

"""
EJERCIÓ
"""
#---STRING---
str = 'Hola Mundo'
print(f'String -> {str}')

#---SUB-CADENA---
sub_str = str[5:10]
print(f'Sub-Cadena -> {sub_str}')

#---LONGITUD---
length = len(str)
print(f'Longitud -> {length}')

#---CONCATENACIÓN---
str1 = 'Hola'
str2 = 'Mundo'
result = str1 + str2
print(f'Concatenación -> {result}')

#---REPETICIÓN---
repeated = str * 3
print(f'Repetición -> {repeated}')

#---MAYÚSCULAS Y MINÚSCULAS---
upper = str.upper()
lower = str.lower()
print(f'Mayúsculas -> {upper}')
print(f'Minúsculas -> {lower}')

#---REEMPLAZO---
replaced = str.replace("Mundo", "Python")
print(f'Reemplazo -> {replaced}')

#---DIVISION---
str_ = "Hola,Mundo,Python"
parts = str_.split(",")
print(f'Division -> {parts}')

#---UNION---
words = ["Hola", "Mundo", "Python"]
joined = " ".join(words)
print(f'Union -> {joined}')

#---INTERPOLACIÓN---
nombre = "Antonio"
str__ = "Hola {}".format(nombre)
print(f'Interpolación -> {str__}')

#---VERIFICACIÓN---
# --IGUALDAD--
str3 = "Hola Mundo"
is_equal = str == str3
print(f'Verificación-Igualdad (Hola Mundo == Hola Mundo) -> {is_equal}')

# --EMPIEZA--
starts_with = str.startswith("Hola")
print(f'Verificación-Empieza (Hola Mundo == Hola) -> {starts_with}')

# --TERMINA--
ends_with = str.endswith("Mundo")
print(f'Verificación-Termina (Hola Mundo == Mundo) -> {ends_with}')

# --CONTIENE--
contains = "Mundo" in str
print(f'Verificación-Contiene (Hola Mundo == Mundo) -> {contains}')



"""
EXTRA
"""
#Pendiente