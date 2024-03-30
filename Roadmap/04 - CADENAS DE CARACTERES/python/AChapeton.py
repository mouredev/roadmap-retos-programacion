# Declarar strings
myString = 'Este es un string'
multipleString = 'Este es un string \n de multiples \n lineas'
emptyString = ''

print(myString)
print(multipleString)
print(emptyString)

# Metodos

# capitalize() - Convierte la primera letra en mayuscula
myString.capitalize()
print(myString)

# lower() - Convierte todos los caracteres en minusculas
myString.lower()
print(myString)

# swapcase() - Conviertes todos los caracteres de mayusculas a minusculas y viceversa
multipleString.swapcase()
print(multipleString)

# upper() - Convierte todos los caracteres a mayusculas
multipleString.upper()
print(multipleString)

# isalmun - Devuelve True si todos los caracteres son alfanumericos
print(myString.isalnum())

# isalpha() - Devuelve True si todos los caracteres son alfabeticos
print(myString.isalpha())

# strip() - Elimina espacios en blanco
whiteSpace = '    mucho espacio        '
print(whiteSpace.strip())

# join() - Devuelve una cadena unida por el elemento del primer parametro
numbers = ["1", "2", "3"]
newNumbers = " - ".join(numbers)
print(newNumbers)

# split() - Divide una cadena en subcadenas y las devuelve en una lista. Se dividen segun el elemento del primer parametro
names = "Python,JavaScript,C"
newNames = names.split(",")
print(newNames)


# DIFICULTAD EXTRA

def esPalindroma(string1):
  if(string1 == string1[::-1]):
    print('Es palindroma')
  else:
    print('No es palindroma')

esPalindroma('level')

def esAnagrama(string1, string2):
  if(string1 == string2[::-1]):
    print('{string1} es anagrama de {string2}')
  else:
    print('No son anagramas')

def esIsograma(string1):
  letrasArray = string1.split()
  letrasSet = set(letrasArray)
  if(len(letrasArray) == len(letrasSet)):
    print("Es anagrama")
  else:
    print("No es anagrama")