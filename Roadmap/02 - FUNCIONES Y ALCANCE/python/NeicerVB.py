"""
Crea ejemplos de funciones básicas que representen
las diferentes posibilidades del lenguaje
"""

# Funcion sin argumentos ni retornos
def bio():
    print("Soy Autodidacta y me gusta aprender sobre programación.\n \
          - Aprendo sobre IA y Machine Learning en Platzi.\n \
          - Aprendo sobre Python con Mouredev")
    
bio()

# Funcion con argumento de posición y por defecto, y sin retorno
def birthday(nombre, fecha="23 de Diciembre"):
    print(f"Me llamo {nombre} y cumplo el {fecha}")
    
birthday("Neicer Vásquez")

# Funcion con argumentos por nombres y con retorno
def specialty(universidad, especialidad, pais):
    return f"Soy de {pais} y estudio en la Universidad {universidad} en la especialidad {especialidad}"

print(specialty(pais="Ecuador", universidad="ESPOL", especialidad="Ciencia de datos e Inteligencia Artificial"))


# Usando Funciones nativas del lenguaje
notas = [9,9,9,9,9,10,8,8,1,1,1,1,1,1,1]
promedio = sum(notas)/len(notas)
print(promedio)


# Aplicando paso por valor y paso por referencia
### Paso por valor
"""Intentar cambiar un objeto inmutable (int, string, tuple)"""
actualidad = 76
def battery(actualidad):
    actualidad = 0
    
print(actualidad)

### Paso por referencia
"""Intentar cambiar un objeto mutable (list, dict)"""
calificaciones = [8,9,10,8,9,10]
def add(nota):
    nota.append(10)

add(calificaciones)
print(calificaciones)

calificaciones_2 = [8,9,10,8,9,10]
def add(nota_2):
    nota_2 = []

add(calificaciones_2)
print(calificaciones_2)
