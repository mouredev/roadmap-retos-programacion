import random

houses = {
    "Frontend": 0,
    "Backend": 0,
    "Mobile": 0,
    "Data": 0
}

questions = [
    {
        "question": "¿Qué tipo de proyectos te interesa más desarrollar?",
        "answers": [
            {
                "option": "Aplicaciones móviles nativas para múltiples plataformas.",
                "house": "Mobile"
            },
            {
                "option": "Interfaces visualmente atractivas y responsivas.",
                "house": "Frontend"
            },
            {
                "option": "Procesamiento y análisis de grandes volúmenes de datos.",
                "house": "Data"
            },
            {
                "option": "Sistemas robustos y optimización de rendimiento del servidor.",
                "house": "Backend"
            }
        ]
    },
    {
        "question": "¿Qué aspecto del desarrollo disfrutas más?",
        "answers": [
            {
                "option": "Resolver problemas complejos de lógica y escalabilidad.",
                "house": "Backend"
            },
            {
                "option": "Analizar datos para tomar decisiones basadas en estadísticas.",
                "house": "Data"
            },
            {
                "option": "Crear aplicaciones móviles eficientes y funcionales.",
                "house": "Mobile"
            },
            {
                "option": "Trabajar en el diseño y la experiencia de usuario.",
                "house": "Frontend"
            }
        ]
    },
    {
        "question": "¿Qué herramienta prefieres usar en tu día a día?",
        "answers": [
            {
                "option": "Kotlin o Swift para desarrollar apps móviles nativas.",
                "house": "Mobile"
            },
            {
                "option": "Python o R para análisis de datos.",
                "house": "Data"
            },
            {
                "option": "Frameworks como React o Angular.",
                "house": "Frontend"
            },
            {
                "option": "Lenguajes como Node.js o Python para la gestión de servidores.",
                "house": "Backend"
            }
        ]
    },
    {
        "question": "¿Cómo te ves en un equipo de desarrollo?",
        "answers": [
            {
                "option": "Modelando datos y construyendo dashboards de análisis.",
                "house": "Data"
            },
            {
                "option": "Encargado de la lógica del servidor y las APIs.",
                "house": "Backend"
            },
            {
                "option": "Desarrollando la interfaz y funcionalidad de una app móvil.",
                "house": "Mobile"
            },
            {
                "option": "Diseñando las interacciones y los componentes visuales.",
                "house": "Frontend"
            }
        ]
    },
    {
        "question": "¿Qué te motiva más al trabajar en un proyecto?",
        "answers": [
            {
                "option": "Ver cómo el diseño cobra vida en la pantalla.",
                "house": "Frontend"
            },
            {
                "option": "Descubrir insights a partir del análisis de datos.",
                "house": "Data"
            },
            {
                "option": "Optimizar el rendimiento y escalabilidad del sistema.",
                "house": "Backend"
            },
            {
                "option": "Lograr que una aplicación móvil funcione perfectamente en cualquier dispositivo.",
                "house": "Mobile"
            }
        ]
    },
    {
        "question": "¿Cuál es tu enfoque al aprender nuevas tecnologías?",
        "answers": [
            {
                "option": "Explorar técnicas avanzadas de análisis de datos y machine learning.",
                "house": "Data"
            },
            {
                "option": "Aprender sobre nuevas arquitecturas y lenguajes de servidor.",
                "house": "Backend"
            },
            {
                "option": "Probar nuevas plataformas y herramientas para desarrollo móvil.",
                "house": "Mobile"
            },
            {
                "option": "Experimentar con nuevas librerías y frameworks de interfaz de usuario.",
                "house": "Frontend"
            }
        ]
    },
    {
        "question": "¿Qué tipo de desafíos disfrutas más resolver?",
        "answers": [
            {
                "option": "Solución de problemas de concurrencia y carga en servidores.",
                "house": "Backend"
            },
            {
                "option": "Optimización de interfaces para que se vean bien en cualquier dispositivo.",
                "house": "Frontend"
            },
            {
                "option": "Análisis de grandes volúmenes de datos para detectar patrones ocultos.",
                "house": "Data"},
            {
                "option": "Creación de experiencias de usuario fluídas en dispositivos móviles.",
                "house": "Mobile"
            }
        ]
    },
    {
        "question": "¿Cómo te gusta medir el éxito de tu trabajo?",
        "answers": [
            {
                "option": "Por la estabilidad y rapidez del sistema bajo carga.",
                "house": "Backend"
            },
            {
                "option": "Mediante la satisfacción del usuario con la interfaz visual.",
                "house": "Frontend"
            },
            {
                "option": "Por la fluidez y buen rendimiento de la app móvil en diferentes dispositivos.",
                "house": "Mobile"},
            {
                "option": "Por la precisión y relevancia de los resultados obtenidos en el análisis de datos.",
                "house": "Data"
            }
        ]
    },
    {
        "question": "¿Qué te resulta más interesante al trabajar con tecnologías emergentes?",
        "answers": [
            {
                "option": "Trabajar con tecnologías de big data o inteligencia artificial.",
                "house": "Data"
            },
            {
                "option": "Explorar nuevas arquitecturas para mejorar el rendimiento del servidor.",
                "house": "Backend"
            },
            {
                "option": "Probar nuevas herramientas y metodologías para mejorar el diseño y la UX.",
                "house": "Frontend"
            },
            {
                "option": "Desarrollar apps móviles que aprovechen nuevas capacidades de hardware.",
                "house": "Mobile"
            }
        ]
    },
    {
        "question": "¿Cómo te enfrentas a un nuevo problema en un proyecto?",
        "answers": [
            {
                "option": "Buscando patrones y soluciones basadas en análisis de datos.",
                "house": "Data"
            },
            {
                "option": "Replanteando la estructura visual y funcional de la interfaz.",
                "house": "Frontend"
            },
            {
                "option": "Explorando cómo mejorar la experiencia del usuario en dispositivos móviles.",
                "house": "Mobile"
            },
            {
                "option": "Analizando la estructura de datos y la lógica del backend.",
                "house": "Backend"
            }
        ]
    }
]

print("\n¡Bienvenido a Hogwarts, la escuela de programación para magos y brujas del código!")
print("El sombrero seleccionador decidirá cuál es tu casa como programador.")

name = input("\n¿Cuál es tu nombre? ")

for index, question in enumerate(questions):

    print(f"\nPregunta {index + 1}: {question["question"]}\n")

    for i, answer in enumerate(question["answers"]):
        print(f"{i + 1}. {answer["option"]}")

    choice = int(input("\nSelecciona una respuesta entre 1 y 4: "))

    selected_answer = question["answers"][choice - 1]
    houses[selected_answer["house"]] += 1

assigned_house = max(houses, key=houses.get)
scores = list(houses.values())

if scores.count(max(scores)) > 1:
    possible_houses = [
        house for house,
        points in houses.items() if points == max(scores)
    ]
    assigned_house = random.choice(possible_houses)

    print(
        f"""\nHmmmm... Ha sido una decisión muy complicada, {
            name}.\n¡Pero finalmente tu casa será {assigned_house}!"""
    )
else:
    print(f"\nEnhorabuena, {name}.\n¡Tu casa será {assigned_house}!")
