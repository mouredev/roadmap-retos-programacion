"""
/*
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
 */

"""

import random
houses = {"Frontend": 0, "Backend": 0, "Data": 0, "Mobile": 0}

questions = [
    {
        "question" :"¿Cuál es tu lenguaje de programación favorito?",
        "answer" : [{
            "option": "JavaScript",
            "house": "Frontend"
        },
        {
            "option": "Python",
            "house": "Data"
        },
        {
            "option": "Swift",
            "house": "Mobile"
        },
        {
            "option": "SQL",
            "house": "Backend"
        }
        
        ]
    },
    {
        "question": "¿Qué tipo de tareas disfrutas más en un proyecto de desarrollo?",
        "answer": [
        {
            "option": "Analizar información y extraer conocimientos a partir de datos",
            "house": "Data"
        },
        {
            "option" : "Diseñar la estructura lógica y gestionar la base del sistema",
            "house": "Backend"
        },
        {
            "option": "Desarrollar soluciones optimizadas para dispositivos móviles",
            "house": "Mobile"
        },
        {
            "option" : "Crear experiencias visuales y mejorar la interacción del usuario", 
            "house" : "Frontend"
        }
        ]
    },
    {
        "question": "¿Qué disfrutas más en un proyecto de software?",
        "answer": [
            {
                "option": "Implementar sistemas eficientes",
                "house": "Backend"
            },
            {
                "option": "Diseñar interfaces atractivas",
                "house": "Frontend"
            },
            {
                "option": "Trabajar con grandes volúmenes de datos",
                "house": "Data"
            },
            {
                "option": "Crear apps móviles innovadoras",
                "house": "Mobile"
            }
        ]
    },
    {
        "question": "¿Qué tipo de problemas prefieres resolver?",
        "answer": [
            {
                "option": "Estéticos y de diseño",
                "house": "Frontend"
            },
            {
                "option": "Funcionalidad en dispositivos móviles",
                "house": "Mobile"
            },
            {
                "option": "Escalabilidad y rendimiento",
                "house": "Backend"
            },
            {
                "option": "Predicción y análisis de datos",
                "house": "Data"
            }
        ]
    },
    {
        "question": "¿Qué entorno de desarrollo prefieres?",
        "answer": [
            {
                "option": "Un dispositivo móvil",
                "house": "Mobile"
            },
            {
                "option": "Un clúster de datos",
                "house": "Data"
            },
            {
                "option": "Un navegador",
                "house": "Frontend"
            },
            {
                "option": "Un servidor",
                "house": "Backend"
            }
        ]
    },
    {
        "question": "¿Cómo prefieres aprender nuevas tecnologías? ",
        "answer": [
            {
                "option": "Diseñando interfaces",
                "house": "Frontend"
            },
            {
                "option": "Creando APIs",
                "house": "Backend"
            },
            {
                "option": "Programando apps móviles",
                "house": "Mobile"
            },
            {
                "option": "Explorando datasets",
                "house": "Data"
            }
        ]
    },
    {
        "question": "¿Qué herramienta te es más cómoda usar?",
        "answer": [
            {
                "option": "HTML/CSS",
                "house": "Frontend"
            },
            {
                "option": "Xcode",
                "house": "Mobile"
            },
            {
                "option": "Node.js",
                "house": "Backend"
            },
            {
                "option": "Jupyter Notebook",
                "house": "Data"
            }
        ]
    },
    {
        "question": "¿Qué es más importante para ti en un proyecto?",
        "answer": [
            {
                "option": "La experiencia del usuario",
                "house": "Frontend"
            },
            {
                "option": "La arquitectura del sistema",
                "house": "Backend"
            },
            {
                "option": "La compatibilidad con múltiples plataformas móviles",
                "house": "Mobile"
            },
            {
                "option": "El manejo eficiente de datos",
                "house": "Data"
            }
        ]
    },
    {
        "question": "¿En qué parte de un equipo de desarrollo te sientes más cómodo? ",
        "answer": [
            {
                "option": "Diseñando y desarrollando interfaces",
                "house": "Frontend"
            },
            {
                "option": "Implementando la lógica del sistema",
                "house": "Backend"
            },
            {
                "option": "Creando apps móviles",
                "house": "Mobile"
            },
            {
                "option": "Analizando datos y creando modelos",
                "house": "Data"
            }
        ]
    },
    {
        "question": "¿Qué crees que dominará el futuro de la programación?",
        "answer": [
            {
                "option": "Inteligencia artificial y big data",
                "house": "Data"
            }, 
            {
                "option": "Aplicaciones web dinámicas",
                "house": "Frontend"
            },
            {
                "option": "Aplicaciones móviles",
                "house": "Mobile"
            },
            {
                "option": "Computación en la nube",
                "house": "Backend"
            }
        ]
    },

]



for index, text in enumerate(questions):
    print(f"\n{index+1}-", text["question"]+"\n")
    for num, op in enumerate(text["answer"]):
        print(f"{num+1}.", op["option"])
    user_option = int(input("Elige una de las cuatro opciones: "))
    house = text["answer"][user_option-1]["house"]
    houses[house] += 1
    print(houses)
    
result_house = max(houses, key= lambda x: houses[x])

scores = list(houses.values())

if scores.count(max(scores)) > 1: 
    print("Se ha producido un empate...")
    print("Dificil decisión.....")
    possible_houses = [house for house, point in houses.items() if point == max(scores) ]
    print(f"Tu casa será... {random.choice(possible_houses)}")
else: 
    print(f"La casa ganadora es {result_house}")
    
sorted_houses = sorted(houses, key= lambda x: houses[x], reverse=True)
print("Resultados: ")
print("\n".join(i for i in sorted_houses))

