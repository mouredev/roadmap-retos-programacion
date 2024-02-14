
# Comprobar si empieza por una secuancia de caracteres
string = "Hola mundo"

booleano = string.startswith("hola")

print(booleano)

# Convierte en mayúsculas
print(string.capitalize())

# Reemplaza caracteres
print(string.replace("mundo", "España!!"))

# Centraliza el texto a partir de un ancho acordado
print(string.center(20))

# Cuanta el número de veces que aparece la secuencia de caracteres
print(string.count("o"))

# Devuelve el indice menor donde se encuentra esta secuencia
print(string.find("mun"))

# Convierte en minúsculas
print(string.lower())

# Separa la cadena en dos si encuentra la cadena proporcionada
print(string.split(" "))

# Devuelve la longitud de la cadena
print(len(string))

# Cambia las mayúsculas por minúsculas y viceversa
print(string.swapcase())