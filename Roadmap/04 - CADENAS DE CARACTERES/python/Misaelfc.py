# Operaciones
mensaje = "Aprendiendo Python"
# Concatenación
mensaje2 = mensaje + " con Misael"
print(mensaje2)

# Repetición
mensaje3 = mensaje * 2
print(mensaje3)

#Indexación
print(mensaje[0]) # A

# Longitud
print(len(mensaje)) # 17

#Slicing (porción)
print(mensaje[0:11]) # Aprendiendo
print(mensaje[12:18]) # Python

# Busqueda
print("P" in mensaje) # True
print("z" in mensaje) # False

# Reemplazo
mensaje4 = mensaje.replace("Python", "Java")
print(mensaje4) # Aprendiendo Java

#División
mensaje5 = mensaje.split(" ")
print(mensaje5) # ['Aprendiendo', 'Python']

# Mayusculas y minúsculas
print(mensaje.upper()) # APRENDIENDO PYTHON
print(mensaje.lower()) # aprendiendo python

# Eliminación de espacios al principio y al final
mensaje6 = "   Aprendiendo Python   "
print(mensaje6.strip()) # Aprendiendo Python

# Busqueda al principio y al final
print(mensaje.startswith("Aprendiendo")) # True
print(mensaje.endswith("Python")) # True

# Busqueda de posición
print(mensaje.find("Python")) # 12

# Busqueda de ocurrencias
print(mensaje.count("a")) # 0
print(mensaje.count("e")) # 2
print(mensaje.lower().count("a")) # 1

#Formateo de cadenas
nombre = "Misael"
edad = 25
mensaje7 = "Hola, mi nombre es {} y tengo {} años".format(nombre, edad)
print(mensaje7) # Hola, mi nombre es Misael y tengo 25 años

# Interpolación de cadenas (f-strings)
mensaje8 = f"Hola, mi nombre es {nombre} y tengo {edad} años"
print(mensaje8) # Hola, mi nombre es Misael y tengo 25 años

# Tranformación de cadenas a listas y viceversa
mensaje9 = "Aprendiendo Python"
lista_mensaje = list(mensaje9)
print(lista_mensaje) # ['A', 'p', 'r', 'e', 'n', 'd', 'i', 'e', 'n', 'd', 'o', ' ', 'P', 'y', 't', 'h', 'o', 'n']
print("".join(lista_mensaje)) # Aprendiendo Python

# Transformaciones numericas a cadenas y viceversa
numero = 123
cadena_numero = str(numero)
print(cadena_numero) # '123'
cadena_numero2 = "456"
numero2 = int(cadena_numero2)
print(numero2) # 456

# Comprobaciones varias
print(mensaje.isalpha()) # False (porque contiene un espacio)
print(mensaje.isdigit()) # False
print(mensaje.islower()) # False
print(mensaje.isupper()) # False
print(mensaje.isnumeric()) # False

"""
    Extra
"""

def check(palabra1: str, palabra2: str):
    
    #Palindromos
    print(f"¿{palabra1} es un palíndromo? {palabra1 == palabra1[::-1]}")
    print(f"¿{palabra2} es un palíndromo? {palabra2 == palabra2[::-1]}")
    
    # Anagramas
    print(f"¿{palabra1} y {palabra2} son anagramas? {sorted(palabra1) == sorted(palabra2)}")
    
    #Isogramas
    print(f"¿{palabra1} es un isograma? {len(palabra1) == len(set(palabra1))}")
    print(f"¿{palabra2} es un isograma? {len(palabra2) == len(set(palabra2))}")
    
    palabra_dict = dict()
    for letra in palabra2:
        palabra_dict[letra] = palabra_dict.get(letra, 0) + 1
    
    isograma = True   
    values = list(palabra_dict.values())
    print(values)
    isograma_len = values[0]
    for letra_count in values:
        if letra_count != isograma_len:
            isograma = False
            break
        
    print(isograma)
        
    print(palabra_dict)
    
check("radar", "python")
#check("amor", "roma")



    