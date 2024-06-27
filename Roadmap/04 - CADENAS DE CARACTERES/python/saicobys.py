""" Operaciones con cadenas en Python """

# Definir una cadena de texto
mensaje = "Hola, mundo!"

# Acceso a caracteres específicos (indexación)
print(mensaje[0]) # H (accede al primer caracter, el indice comienza en 0)
print(mensaje[4]) # a (accede al quinto carácter)
print(mensaje[-1])  # ! (accede al último carácter usando índice negativo)

# Subcadenas (slicing)
print(mensaje[0:4]) # Hola (desde el índice 0 hasta el 3, sin incluir el 4)
print(mensaje[7:]) # mundo! (desde el índice 7 hasta el final)
print(mensaje[2:9:2]) # l,m! (desde el índice 2 hasta el 8, saltando de 2 en 2)

# Longitud de la cadena
print(len(mensaje)) # 12 (número total de caracteres en la cadena)

# Concatenación (unir cadenas)
nombre = "Python"
nuevo_mensaje = mensaje + " " + nombre # 'Hola, mundo! Python'
print(nuevo_mensaje)

# Repetición
mensaje_repetido = mensaje * 3 # 'Hola, mundo!Hola, mundo!Hola, mundo!'
print(mensaje_repetido)

# Recorrido (iteración)
for letra in mensaje:
    print(letra) # Imprime cada carácter en una línea separada

# Conversión a mayúsculas y minúsculas
print(mensaje.upper()) # HOLA, MUNDO!
print(mensaje.lower()) # hola, mundo!

# Reemplazo de caracteres o subcadenas
nuevo_mensaje = mensaje.replace("mundo", "python") # "Hola, Python!"

# División (split) en una lista de subcadenas
palabras = mensaje.split(" ") # ['Hola,', 'mundo!']
print(palabras)

# Unión (join) de elementos de una lista en una cadena
nueva_cadena = "-".join(palabras) # 'Hola,-mundo!'
print(nueva_cadena)

# Interpolación de variables (f-strings)
edad = 30
print(f"Tengo {edad} años.") # 'Tengo 30 años.'

# Verificación de contenido
print("Hola" in mensaje)    # True (verifica si "Hola" está en la cadena)
print(mensaje.startswith("Hola"))  # True (verifica si comienza con "Hola")
print(mensaje.endswith("!"))   # True (verifica si termina con "!")
