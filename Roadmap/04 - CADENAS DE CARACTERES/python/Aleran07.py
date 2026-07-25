# 04
'''
Operaciones con cadenas de caracteres
'''

# Creacion y concatenacion
a = "Hola"
b = "Mundo"
c = a + " " + b        # Concatenación → 'Hola Mundo'
d = a * 3              # Repetición → 'HolaHolaHola'


# Indexación y segmentación (slicing)
texto = "Python"
texto[0]      # 'P' → primer carácter
texto[-1]     # 'n' → último carácter
texto[0:3]    # 'Pyt' → desde 0 hasta antes del 3
texto[2:]     # 'thon' → desde 2 hasta el final
texto[:4]     # 'Pyth' → desde el inicio hasta antes del 4
texto[::-1]   # 'nohtyP' → invertir cadena


#Búsqueda y verificación
texto = "programar en python"

"python" in texto       # True → verifica si existe
"java" not in texto     # True → verifica si no existe
texto.find("python")    # 13 → índice donde empieza
texto.rfind("n")        # última aparición de 'n'
texto.startswith("pro") # True
texto.endswith("on")    # True

# Modificación de contenido
texto = "hola mundo"

texto.upper()        # 'HOLA MUNDO'
texto.lower()        # 'hola mundo'
texto.title()        # 'Hola Mundo'
texto.capitalize()   # 'Hola mundo'
print(texto.swapcase())     # 'HOLA MUNDO' → 'hola mundo'
texto.replace("mundo", "Python")  # 'hola Python'

# Eliminación de espacios o caracteres
texto = "  hola mundo  "

texto.strip()        # 'hola mundo' → elimina espacios a ambos lados
texto.lstrip()       # 'hola mundo  ' → elimina solo a la izquierda
texto.rstrip()       # '  hola mundo' → elimina solo a la derecha
texto.strip("o")     # elimina las 'o' de los extremos → '  hola mund'


#División y unión
texto = "uno,dos,tres"

texto.split(",")     # ['uno', 'dos', 'tres'] → divide por comas
texto.split()        # divide por espacios
"-".join(["uno", "dos", "tres"])  # 'uno-dos-tres' → une con '-'

# Información de la cadena
texto = "Python"

len(texto)           # 6 → longitud
texto.count("t")     # 1 → cuántas veces aparece

# Comprobaciones de tipo
"abc".isalpha()      # True → solo letras
"123".isdigit()      # True → solo dígitos
"abc123".isalnum()   # True → letras y números
"hola mundo".isspace()  # False → solo espacios
"HOLA".isupper()     # True
"hola".islower()     # True
"Hola Mundo".istitle() # True

# Alineación y formato
texto = "Python"

texto.center(10, "-")  # '--Python--'
texto.ljust(10, ".")   # 'Python....'
texto.rjust(10, ".")   # '....Python'

# Formato de cadenas (interpolación)
nombre = "Brian"
edad = 24

# Forma moderna (f-string)
f"Hola {nombre}, tienes {edad} años"

# Método format
"Hola {}, tienes {} años".format(nombre, edad)

# Índices
"Hola {0}, tienes {1} años".format(nombre, edad)

# Diccionario
"Hola {n}, tienes {e} años".format(n=nombre, e=edad)

# Métodos útiles adicionales
texto = "Hola mundo"

texto.encode()         # convierte a bytes
texto.expandtabs()     # reemplaza tabulaciones con espacios
texto.partition(" ")   # ('Hola', ' ', 'mundo') → divide en 3 partes
texto.rpartition(" ")  # divide desde el final
texto.zfill(10)        # '000Hola mundo' → rellena con ceros
