my_string = 'Hola mundo'
my_other_string = 'soy Cristian'
my_long_string = 'Hola soy Cristian y soy Developer'
# Acceso a caracteres especificos

print(my_string[1])

# Subcadenas

rango = slice(1,6)

subcadena1 = my_string[rango]
print(subcadena1)

print(my_other_string[1:6])

# Longitud

print(len(my_long_string))

# Concatenacion

Subcadena2 = my_string + ' ' + my_other_string

print(Subcadena2)

# Busqueda

print('Cristian' in my_long_string)

# Repeticion

print(my_string * 3)

# Recorido

for a in my_string:
    print(a)

# Conversion a Mayúsculas y minúsculas y letras en mayusculas

print(my_other_string.upper())
print(my_long_string.lower())
print(my_long_string.capitalize())
print(my_long_string.title())

# Remplazo

print(my_long_string.replace('Cristian', 'Juan'))

# Division

print(my_long_string.split(' ', 3))

# Interpolacion

print(f'Hola mundo {my_other_string}')

# Verificacion

print(my_long_string.count('a'))
print(my_long_string.find('C'))


# Ejercicio extra

def verificaciones():
 

        def palindormo(palabra1):
            palabra1 = palabra1.lower()
            if palabra1 == palabra1[::-1]:
                return 'Es un palindromo'
            else:
                return 'No es un palindromo'
            

        def anagrama(palabra1, palabra2):
            palabra1 = palabra1.lower()
            palabra2 = palabra2.lower()
            comprovacion = sorted(palabra1) == sorted(palabra2)
            if comprovacion == False:
                return 'No es un anagrama'
            else:
                return 'Es un anagrama'

        def isograma(palabra1):
            palabra1 = palabra1.lower()
            for letra in palabra1:
                if palabra1.count(letra) > 1:
                    return 'No es un isogrma'
            return 'Es un isograma'
    
        palabra1 = input('Ingrese una palabra: ')
        palabra2 = input('Ingrese una palabra: ')
        print(palindormo(palabra1))
        print(anagrama(palabra1, palabra2))
        print(isograma(palabra1))

verificaciones()











