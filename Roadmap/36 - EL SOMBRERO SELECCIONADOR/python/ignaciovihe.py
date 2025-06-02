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
 *    preguntas, con cuatro posibles respuestas cada una.
 * 2. Cada respuesta asigna puntos a cada una de las casas (a tu elección).
 * 3. Una vez finalizado, el sombrero indica el nombre del alumno 
 *    y a qué casa pertenecerá (resuelve el posible empate de manera aleatoria,
 *    pero indicándole al alumno que la decisión ha sido complicada).
"""

import os
import time
import random

seconds = 1

houses = {
    "Frontend": 0,
    "Backend": 0,
    "Mobile": 0,
    "Data": 0
}

questions = {
    "1. ¿Qué parte de un proyecto te entusiasma más?":
    {
        "a) Diseñar interfaces atractivas y accesibles": "Frontend",
        "b) Crear la lógica del servidor y manejar bases de datos": "Backend",
        "c) Desarrollar aplicaciones que funcionen en cualquier dispositivo": "Mobile",
        "d) Analizar grandes volúmenes de datos para tomar decisiones": "Data"
    },
    "2. ¿Qué editor o herramienta prefieres usar?":
    {
        "a) Jupyter Notebook o herramientas de visualización": "Data",
        "b) Postman, SQL clients, terminal": "Backend",
        "c) Figma o herramientas de diseño UI/UX": "Frontend",
        "d) Android Studio o Xcode": "Mobile"
    },
    "3. ¿Cuál sería tu proyecto ideal?":
    {
        "a) Construir una API robusta para un sistema financiero": "Backend",
        "b) Predecir el clima con aprendizaje automático": "Data",
        "c) Diseñar una app para gestionar tareas diarias": "Mobile",
        "d) Crear una web interactiva y moderna": "Frontend"
    },
    "4. ¿Qué te resulta más satisfactorio al programar?":
    {
        "a) Ver algo visual funcionando perfectamente": "Frontend",
        "b) Probar tu app en diferentes móviles y ver que todo funcione": "Mobile",
        "c) Limpiar y visualizar datos complejos con claridad": "Data",
        "d) Hacer que todo se comunique sin errores entre servicios": "Backend"
    },
    "5. ¿Qué lenguaje te atrae más?":
    {
        "a) Kotlin o Swift": "Mobile",
        "b) Java o Go": "Backend",
        "c) JavaScript o TypeScript": "Frontend",
        "d) Python o R": "Data"
    },
    "6. ¿Cuál de estas habilidades te gustaría perfeccionar?":
    {
        "a) Modelado estadístico y análisis predictivo": "Data",
        "b) Uso de sensores y funciones nativas del dispositivo": "Mobile",
        "c) Seguridad web y eficiencia de APIs": "Backend",
        "d) Animaciones CSS y frameworks como React": "Frontend"
    },
    "7. ¿Qué superpoder de programación querrías tener?":
    {
        "a) Optimizar cualquier algoritmo": "Backend",
        "b) Encontrar patrones ocultos en cualquier conjunto de datos": "Data",
        "c) Crear experiencias que atrapen al usuario": "Frontend",
        "d) Hacer que tu app se adapte a cualquier pantalla sin errores": "Mobile"
    },
    "8. ¿Qué parte del proceso de desarrollo disfrutas más?":
    {
        "a) Transformar datos crudos en información útil": "Data",
        "b) Resolver problemas complejos del sistema": "Backend",
        "c) La creatividad del diseño y la usabilidad": "Frontend",
        "d) Asegurarme de que todo funcione bien en el móvil": "Mobile"
    },
    "9. ¿Con qué tipo de proyecto grupal te identificas más?":
    {
        "a) Diseñar la arquitectura de un sistema completo": "Backend",
        "b) Coordinar la apariencia y estilo de una plataforma": "Frontend",
        "c) Realizar dashboards y análisis para el equipo": "Data",
        "d) Integrar funciones móviles con el resto del equipo": "Mobile"
    },
    "10. ¿Qué frase te representa mejor?":
    {
        "a) 'Los datos hablan por sí solos'": "Data",
        "b) 'La base lo es todo'": "Backend",
        "c) 'La primera impresión lo es todo'": "Frontend",
        "d) 'Todo en la palma de tu mano'": "Mobile"
    }

}

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_results():
    for question, answers in questions.items():
        print(question)
        for answer in answers:
            print("\t" + answer)
        while True:
            try:
                selected = input("Selecciona tu respuesta: ")
                if selected not in("a", "b", "c", "d"):
                    raise ValueError("Elige una opcion correcta.")
                break
            except ValueError as e:
                print(e)
        for answer in answers:
            if answer.startswith(selected):
                houses[answers[answer]] += 5
        limpiar_consola()

def get_house() -> list:
    max_points = max(houses.values())
    return [house for house, points in houses.items() if points == max_points]


def sorting_hat():
    limpiar_consola()
    print("Bienvenido a la escuela para programadores de Hogwarts!")
    time.sleep(seconds)
    limpiar_consola()
    print("Vamos a asignarte una de las casas.")
    time.sleep(seconds)
    limpiar_consola()
    print("Es un proceso complicado así que contesta con sinceridad.")
    time.sleep(seconds)
    limpiar_consola()
    name = input("Lo primero de todo necesito tu nombre: ")
    limpiar_consola()
    print(f"De acuerdo, {name}. Vamos allá.")
    time.sleep(seconds)
    limpiar_consola()
    get_results()
    print("De acuerdo...")
    time.sleep(seconds)
    limpiar_consola()
    print("mmm....")
    time.sleep(seconds)
    limpiar_consola()
    print("Interesante...")
    time.sleep(seconds)
    limpiar_consola()
    result = get_house()
    if len(result) > 1:
        print("Lo tengo! No ha sido una decisión fácil.")
        time.sleep(seconds)
        limpiar_consola()
        numero = random.randint(0, len(result) - 1)
        final_house = result[numero]
    else:
        print("Lo tengo! Lo tengo muy claro.")
        time.sleep(seconds)
        limpiar_consola()
        final_house = result[0]
    print(f"{name}, tu casa es... {final_house}")

sorting_hat()