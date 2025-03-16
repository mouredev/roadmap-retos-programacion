"""
# 22 Funciones de Orden Superior
"""

# Son aquellas que pueden aceptar otras funciones como argumentos y/o como resultado.
# En python las funciones son objetos de primera clase, son tratadas como otro tipo de dato.
# Pueden ser asignadas a variables, pasadas como parametros o retornadas

"""
Como funciona?
"""
# Imaginemos que tenemos una caja de herramientas.
# Una funcion de orden superior seria como un ahheramienta que puede usar varias herramientas  o incluso crear otra herramienta para realizar el trabajo

"""
1. Pasar una funcion como argumento
"""
# Usamos la funcion map(funcion, iterable)
# Devuelve 

def doblar(x):
    return x * 2

datos = [1, 2, 3, 4, 5]
resultado = map(doblar, datos)
print(list(resultado))

"""
2. Devolver una funcion como resultado
"""
# Una funcion crea y devuelve otra funcion

def saludar(idioma: str):

    def saludo_en_es():
        return 'Hola...'
    
    def saludo_en_en():
        return 'Hello...'
    
    if idioma == 'es':
        return saludo_en_es
    else:
        return saludo_en_en


saludo_es = saludar('es')
saludo_en = saludar('en') 
print(saludo_es())
print(saludo_en())


"""
Funciones comunes en Python
"""
# filter(): Filtra elementos de una lista. Devuelve True o False
# sorted(): Ordena elementos y se puede personalizar con el parametro "key"
# map(): Aplica una funcion a cada elemento

def es_par(x):
    return x % 2 == 0

numeros = [1, 2, 3, 4, 5, 6]
pares = filter(es_par, numeros)
print(list(pares))


"""
Extra
"""
from datetime import datetime

estudiantes =[
    {"name": "Diego", "birthdate": "29-04-1987", "grades": [5, 8.5, 3, 10]},
    {"name": "Andres", "birthdate": "04-08-2005", "grades": [1, 9.5, 2, 4]},
    {"name": "Pedro", "birthdate": "15-12-2000", "grades": [4, 6.5, 5, 2]},
    {"name": "Maria", "birthdate": "25-01-1980", "grades": [10, 9, 9.7, 9.9]}
]

def promedio(grades):
    return sum(grades) / len(grades)
print('------------')

# Promedio por estudiante
print('Promedio por estudiante: ')
print(list(map(lambda estudiantes: {'name': estudiantes['name'], 'promedio': promedio(estudiantes['grades'])}, estudiantes)))
print('------------')

# Mejor estudiante
print('Mejor estudiante: ')
print(list(map(lambda estudiantes: estudiantes['name'], filter(lambda estudiantes: promedio(estudiantes['grades']) >= 9, estudiantes))))
print('------------')

# Fecha nacimiento ordenada
print('Fecha ordenada por estudiante: ')
print(sorted(estudiantes, key=lambda estudiantes: datetime.strptime(estudiantes['birthdate'], '%d-%m-%Y'), reverse=True))
print('------------')

# Calificacion mas alta
print('Calificacion mas lata de cada estudiante: ')
print((list(map(lambda estudiantes: {'name': estudiantes['name'], 'max': max(estudiantes['grades'])}, estudiantes))))