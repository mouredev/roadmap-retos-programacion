'''
Ejercicio mvidalb
'''

import random
import pprint

# Inicializo las distinas casas
houses = {
    "Frontend": 0,
    "Backend": 0,
    "Mobile": 0,
    "Data" : 0
    }

# Preguntas con sus respuestas y soluciones
questions = [
    {
        "pregunta": "¿Cuál de los siguientes lenguajes es más comúnmente utilizado para el desarrollo frontend?",
        "respuestas": {
            "a)": "Java",
            "b)": "Python",
            "c)": "JavaScript",
            "d)": "Kotlin"
        },
        "soluciones": {
            "a)": "Backend",
            "b)": "Data",
            "c)": "Frontend",
            "d)": "Mobile"
        }
    },
    {
        "pregunta": "En el contexto del desarrollo backend, ¿cuál es un framework popular para Node.js?",
        "respuestas": {
            "a)": "React",
            "b)": "Laravel",
            "c)": "Django",
            "d)": "Express"
        },
        "soluciones": {
            "a)": "Frontend",
            "b)": "Backend",
            "c)": "Data",
            "d)": "Mobile"
        }
    },
    {
        "pregunta": "¿Qué lenguaje es conocido por ser ampliamente utilizado en el desarrollo de aplicaciones móviles nativas para Android?",
        "respuestas": {
            "a)": "Swift",
            "b)": "Kotlin",
            "c)": "Flutter",
            "d)": "Objective-C"
        },
        "soluciones": {
            "a)": "Mobile",
            "b)": "Mobile",
            "c)": "Frontend",
            "d)": "Backend"
        }
    },
    {
        "pregunta": "En ciencia de datos, ¿qué biblioteca de Python es más conocida para trabajar con grandes volúmenes de datos?",
        "respuestas": {
            "a)": "Pandas",
            "b)": "TensorFlow",
            "c)": "NumPy",
            "d)": "Keras"
        },
        "soluciones": {
            "a)": "Data",
            "b)": "Mobile",
            "c)": "Frontend",
            "d)": "Backend"
        }
    },
    {
        "pregunta": "¿Cuál de estas tecnologías es comúnmente usada para la gestión del estado en aplicaciones frontend?",
        "respuestas": {
            "a)": "Redux",
            "b)": "Flask",
            "c)": "MongoDB",
            "d)": "Spring Boot"
        },
        "soluciones": {
            "a)": "Frontend",
            "b)": "Backend",
            "c)": "Data",
            "d)": "Mobile"
        }
    },
    {
        "pregunta": "En el desarrollo backend, ¿cuál de las siguientes bases de datos es relacional?",
        "respuestas": {
            "a)": "MongoDB",
            "b)": "Redis",
            "c)": "MySQL",
            "d)": "Cassandra"
        },
        "soluciones": {
            "a)": "Data",
            "b)": "Mobile",
            "c)": "Backend",
            "d)": "Frontend"
        }
    },
    {
        "pregunta": "¿Qué framework es comúnmente utilizado para desarrollar aplicaciones móviles multiplataforma?",
        "respuestas": {
            "a)": "Xamarin",
            "b)": "Swift",
            "c)": "Kotlin",
            "d)": "React Native"
        },
        "soluciones": {
            "a)": "Mobile",
            "b)": "Frontend",
            "c)": "Backend",
            "d)": "Data"
        }
    },
    {
        "pregunta": "¿Qué es un concepto clave de las bases de datos en el campo de los datos masivos (Big Data)?",
        "respuestas": {
            "a)": "DOM",
            "b)": "Cluster",
            "c)": "ORM",
            "d)": "CDN"
        },
        "soluciones": {
            "a)": "Frontend",
            "b)": "Data",
            "c)": "Backend",
            "d)": "Mobile"
        }
    },
    {
        "pregunta": "¿Cuál de las siguientes tecnologías es esencial para el diseño de interfaces de usuario en el desarrollo frontend?",
        "respuestas": {
            "a)": "CSS",
            "b)": "Flask",
            "c)": "Hadoop",
            "d)": "Redis"
        },
        "soluciones": {
            "a)": "Frontend",
            "b)": "Backend",
            "c)": "Data",
            "d)": "Mobile"
        }
    },
    {
        "pregunta": "¿Cuál de estos es un patrón de diseño común en la arquitectura backend?",
        "respuestas": {
            "a)": "MVC (Model-View-Controller)",
            "b)": "CSS Grid",
            "c)": "JWT (JSON Web Token)",
            "d)": "Kafka"
        },
        "soluciones": {
            "a)": "Backend",
            "b)": "Frontend",
            "c)": "Mobile",
            "d)": "Data"
        }
    }
]

# Método para calcular la puntuación de cada casa en función de la respuesta seleccionada
def add_score(houses, question, final_answer) -> dict:
    answer_selected = question["soluciones"][final_answer + ")"]
    for house in houses:
        if answer_selected == house:
            houses[answer_selected] += 2   # 2 puntos para una casa si seleccionas esta respuesta
   
    return houses

# Comienzo el programa
print("\nSOMBRERO SELECCIONADOR!")
name = input("¿Cuál es tu nombre, querido mago?: ")
print(f"\nGracias por hacerme saber tu nombre, {name}! Elige sabiamente para que el sombrero seleccionador escoja bien tu destino:")

# Recorro el diccionario de preguntas
for i, question in enumerate(questions):
    print(f"\n{i+1}. " +  question["pregunta"])
    for answers in question["respuestas"].items():
        print("  " + answers[0] + " " + answers[1])  # Opciones en cada pregunta mostradas por consola

    while True:  # Ejecutar hasta que se seleccione una respuesta correcta
        final_answer = input("\nSelecciona respuesta: ")
        if final_answer in ["a", "b", "c", "d"]:
            houses = add_score(houses, question, final_answer)  # Calculo la nueva puntuación de cada casa
            break
        else:
            print("Cáspitas! Ha ocurrido un error, selecciona una respuesta correcta.")
    
    print("\nPuntuación en tiempo real:")
    pprint.pprint(houses, width = 20)


# Compruebo qué casa ha obtenido mayor puntuación
winning_house = [key for key, value in houses.items() if value == max(houses.values())] # Máximo valor del dict houses
if len(winning_house) != 1:
    winning_house = [random.choice(winning_house)]
    print(f"\nENHORABUENA {name}! Ha sido una decisión muuuy difícil, pero eres nuevo integrante de la casa {winning_house[0].upper()}, buena suerte!\n")
else: 
    print(f"\nENHORABUENA {name}! Eres nuevo integrante de la casa {winning_house[0].upper()}, buena suerte!\n")


