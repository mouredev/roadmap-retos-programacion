 # EJERCICIO:
 # Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 # en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 # - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 #   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 #   interpolación, verificación...

 # Operaciones con strings en Python

my_str = "Hola python"
sec_str = "Soy Aitor López"
name, surname, job, age = "Aitor", "López", "Software Developer", 27

# Devolver numero de caracteres
print(len(my_str))

# Concatenar strings
print(my_str + ". " + sec_str)

# Formateo de un string. Diferentes metodos ordenados de mas recomendado a menos recomendado
print(f"Hola, soy {name} {surname}, soy un {job} junior, y tengo {age} años") # Forma mas moderna y legible
print("Hola, soy {} {}, soy un {} junior, y tengo {} años".format(name, surname, job, age)) # Forma algo mas antigua, pero aun legible
print("Hola, soy %s %s, soy un %s junior, y tengo %d años" % (name, surname, job, age)) # Esta forma es hereadada de versiones antiguas de Python
print("Hola, soy " + name + " " + surname + ", soy un " + job + " junior, y tengo " + str(age) + " años") # Totalmente desaconsejable, pero legibilidad y propenso a errore

# Desempaquetado de caracteres
a, b, c, d, e = name
print(a)
print(b)

# Division (slice)
name_slice = name[1:3]
print(name_slice)

name_slice = name[1:]
print(name_slice)

name_slice = name[-2]
print(name_slice)

name_slice = name[0:3:2]
print(name_slice)

# Revertir string
name_slice = name[::-1] #Lee de principio a fin pero en intervalos de -1
print(name_slice)

# Funciones del sistema para strings
print(surname.capitalize()) # Pone la primera letra en mayuscula
print(surname.upper()) # Pone todas las letras en mayusculas
print(surname.lower()) # Pone todas las letras en minusculas
print(surname.isupper()) # Comprueba si todas las letras son mayusculas
print(surname.count("ó")) # Cuenta cuantas veces aparece un caracter
print(surname.isnumeric()) # Comprueba si el string es numerico (es decir, si se podria pasar a un int)
print(surname.startswith("Ló")) # Comprueba si un string comienza con cierto prefijo
print(surname == name) # Compara dos strings

 # DIFICULTAD EXTRA (opcional):
 # Crea un programa que analice dos palabras diferentes y realice comprobaciones
 # para descubrir si son:
 # - Palíndromos
 # - Anagramas
 # - Isogramas

def str_analycer(str1, str2):
  clean1 = str1.replace(" ", "").lower()
  reverse1 = clean1[::-1]
  caracters1 = set()
  clean2 = str2.replace(" ", "").lower()
  reverse2 = clean2[::-1]
  caracters2 = set()
  result = []
  
  # Comprovar Palíndormos 
  result.append("si" if clean1 == reverse1 else "no") # result[0]
  result.append("si" if clean2 == reverse2 else "no") # result[1]

  # Comprobar anagramas 
  result.append("si" if sorted(clean1) == sorted(clean2) else "no") #result[2]

  #Comprobar isogramas
  # result[3]
  for letra in clean1:
    if letra in caracters1:
      result.append("no")
      break
    else:
      caracters1.add(letra)
  else:
    result.append("si")

  # result[4]
  for letra in clean2:
    if letra in caracters2:
      result.append("no")
      break
    else:
      caracters2.add(letra)
  else:
    result.append("si")

  #Imprimir el resultado
  print("-----------------------------------------------------")
  print(f"La palabra {str1} {result[0]} es un palindormo.\nLa palabra {str2} {result[1]} es un palindormo. \nLas palabras {str1} y {str2}, {result[2]} son un anagrama. \nLa palabra {str1} {result[3]} es un isograma. \nLa palabra {str2} {result[4]} es un isograma.")
  print("-----------------------------------------------------")

str_analycer("Reconocer", "Anilina") # Palindromos, no isogramas, no anagramas
str_analycer("Amor", "Roma") #Anagramas, no palindormos, si isogramas
str_analycer("Murcielago", "Centavo") # Isogramas, no palindormos ni anagramas
str_analycer("Oso", "oso") #Palindromos, anagramas, no isogramas
str_analycer("Luz", "zul") # Anagramas, isogramas, no palindromos
str_analycer("Hola", "Adios") # Todo no
str_analycer("carro", "rocar") # anagramas, no isogramas, no palindormos
str_analycer("dabale arroz a la zorra el abad", "la zorra el abad dabale arroz") # palindromos y anagramas

