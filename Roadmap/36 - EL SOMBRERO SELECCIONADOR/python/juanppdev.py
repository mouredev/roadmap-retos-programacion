"""
 * EJERCICIO:
 * Cada 1 de septiembre, el Hogwarts Express parte hacia la escuela
 * de programación de Hogwarts para magos y brujas del código.
 * En ella, su famoso sombrero seleccionador ayuda a los programadores
 * a encontrar su camino...
 * Desarrolla un programa que simule el comportamiento del sombrero.
 * Requisitos:
 * 1. El sombrero realizará 10 preguntas para determinar la casa del alumno.
 * 2. Deben existir 4 casas. Por ejemplo: Frontend, Backend, Mobile y Data.
 *    (Puedes elegir las que quieras)
 * Acciones:
 * 1. Crea un programa que solicite el nombre del alumno y realice 10
 *    preguntas random, con cuatro posibles respuestas cada una.
 * 2. Cada respuesta asigna puntos a cada una de las casas (a tu elección).
 * 3. Una vez finalizado, el sombrero indica el nombre del alumno 
 *    y a qué casa pertenecerá (resuelve el posible empate de manera aleatoria,
 *    pero indicándole al alumno que la decisión ha sido complicada).
"""

import random

# Definimos las casas
casas = ["Frontend", "Backend", "Mobile", "Data"]

# Definimos las preguntas y las respuestas
preguntas = [
    ("¿Qué prefieres hacer en tu tiempo libre?", ["Leer documentación", "Desarrollar una app", "Analizar datos", "Diseñar interfaces"]),
    ("¿Qué lenguaje de programación te gusta más?", ["JavaScript", "Python", "Swift", "SQL"]),
    ("¿Qué tipo de proyectos te interesan más?", ["Web", "Backend", "Móvil", "Big Data"]),
    ("¿Qué herramienta prefieres usar?", ["React", "Django", "Flutter", "Pandas"]),
    ("¿Qué tipo de problemas te gusta resolver?", ["Interfaz de usuario", "Lógica de negocio", "Optimización de rendimiento", "Análisis de datos"]),
    ("¿Qué tipo de empresa te gustaría trabajar?", ["Startup", "Corporación", "Freelance", "Investigación"]),
    ("¿Qué tipo de tareas disfrutas más?", ["Diseño", "Programación", "Pruebas", "Análisis"]),
    ("¿Qué prefieres aprender?", ["CSS", "Docker", "Kotlin", "Machine Learning"]),
    ("¿Qué tipo de equipo prefieres?", ["Diseñadores", "Desarrolladores", "Ingenieros de software", "Científicos de datos"]),
    ("¿Qué tipo de retos te motivan?", ["Creativos", "Técnicos", "Innovadores", "Analíticos"])
]

# Función para asignar puntos a las casas
def asignar_puntos(respuesta):
    if respuesta == 0:
        return [1, 0, 0, 0]
    elif respuesta == 1:
        return [0, 1, 0, 0]
    elif respuesta == 2:
        return [0, 0, 1, 0]
    elif respuesta == 3:
        return [0, 0, 0, 1]

# Función principal
def sombrero_seleccionador():
    nombre = input("¿Cuál es tu nombre? ")
    puntos = [0, 0, 0, 0]
    
    for i in range(10):
        pregunta, respuestas = random.choice(preguntas)
        print(f"\nPregunta {i+1}: {pregunta}")
        for j, respuesta in enumerate(respuestas):
            print(f"{j+1}. {respuesta}")
        eleccion = int(input("Elige una opción (1-4): ")) - 1
        puntos = [x + y for x, y in zip(puntos, asignar_puntos(eleccion))]
    
    max_puntos = max(puntos)
    posibles_casas = [casas[i] for i, p in enumerate(puntos) if p == max_puntos]
    
    if len(posibles_casas) > 1:
        casa_final = random.choice(posibles_casas)
        print(f"\n{nombre}, la decisión ha sido complicada, pero finalmente perteneces a la casa {casa_final}!")
    else:
        casa_final = posibles_casas[0]
        print(f"\n{nombre}, perteneces a la casa {casa_final}!")

# Ejecutar el programa
sombrero_seleccionador()
