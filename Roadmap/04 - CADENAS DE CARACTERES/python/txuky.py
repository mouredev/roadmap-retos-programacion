### Nuevo reto

print('Hola')

# strings con comillas dentro del string
print("Hola 'Txuky'")
print('Hola "Txuky"')

#asignar strings a variables 
my_name = 'Francesc'
print(my_name)

#acceso a elementos del string
a = "Hola, Python!"
print(a[-1])

#repeticion 
print((a + ' ') * 3)

# crear bucles con los elementos de l string
for a in 'Hola, Txuky':
    print(a)

# usar el tamaño del string
print(len(my_name))

# chekear si un caracter o grupo de ellos esta presente en el string devolviendo true folse
my_frase = 'El placer más noble es el júbilo de comprender'
print('placer' in my_frase)
print('Placer' in my_frase)

#podemos usarlo deintro de un condicional
if 'Noble' in my_frase:
    print('"noble" esta incluido en la frase')
else:
    print('"noble" NO esta incluido en la frase')

#concatenar strings
print(my_name + ' siempre dice ' + my_frase)

#concatenar  con cambio de linea strings
print(my_name + ' siempre dice \n' + my_frase)

#concatenar  con tabulacion con cambio de linea strings
print('\t' + my_name + ' siempre dice \n' + my_frase)

#formato f-string
name, surname, age = "Francesc", "More", 35 
print(" mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print(" mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print(f" mi nombre es {name} {surname} y mi edad es {age}")

# Desempaquetado de caracteres
language = "python" 
a, b, c, d, e, f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# Porciones
language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[:3]
print(language_slice)

language_slice = language[-3]
print(language_slice)

#Reverse
reversed_language = language [::-1] 
print(reversed_language)

# Reemplazo
print(language.replace("o", "a"))

# División
print(language.split("t"))

#mayusculas y minusculas
print(language.capitalize())
print(language.upper())
print(language.lower())
print(language.title())

# Búsqueda de ocurrencias
print(language.count("t"))

# Búsqueda de posición
print(language.find('p'))
print(language.find('o'))
print(language.find('O'))

# comptovaciones 
print(language.isnumeric())
print("1".isnumeric())
print(language.upper().isupper())
print(language.lower().isupper())
s4 = "123456"
print(language.isalnum())
print(language.isalpha())
print(s4.isalpha())
print(s4.isnumeric())


#busquedas al final i principio
print(language.startswith("py"))
print(language.startswith("Py"))
print(language.endswith("on"))
print(language.endswith("ON"))


# Eliminación de espacios al principio y al final
print(' francesc txuky '.strip())

#transformacion en lista de caracteres
print(list(language))

###extra

titulo='ejercicio'

print(titulo.capitalize().upper())

palab_1 = input('\nEscribe la primera palabra: ')
palab_2 = input('Escribe la segunda palabra: ')


#Anagramas dos palabras con las mismas letras en diferente orden y diferente significado Amor Roma

palab_1 = palab_1.lower()
palab_2 = palab_2.lower()

iso_1 = 'No'
iso_2 = 'No'
palin_1 = 'No'
palin_2 = 'No'
anagram = 'No'

#comprobar Isograma que es cuando si  repite alguna ej.isograma acacia
for x in palab_1:
    repet = palab_1.count(x)
    if repet >= 2:
        iso_1 = 'Si'
for x in palab_2:
    repet = palab_2.count(x)
    if repet >= 2:
        iso_2 = 'Si'   

#comprobar Palindromos que es cuando la palabra se puede leer de delante atras o al reves y se lee lo mismo ej.rotor
if palab_1 == palab_1[::-1]:
    palin_1 = 'Si'
if palab_2 == palab_2[::-1]:
    palin_2 = 'Si'
    
#Anagramas dos palabras con las mismas letras en diferente orden y diferente significado Amor Roma
palab_1_lst = list(palab_1)
palab_2_lst = list(palab_2)
palab_1_lst.sort()
palab_2_lst.sort()

if len(palab_1) == len(palab_2):
    for elem1, elem2 in zip(palab_1_lst, palab_2_lst):
        if elem1 == elem2:
            anagram = 'Si'
        else:
            anagram = 'No'
            break

    
print(f'\nLa palabra {palab_1} {iso_1} es un Isograma\ny {palin_1} es un Palindromo\n' )
print(f'La palabra {palab_2} {iso_2} es un Isograma\ny {palin_2} es un Palindromo\n' )
print(f'\tLas palabras {palab_1} y {palab_2} {anagram} son un Anagrama')
