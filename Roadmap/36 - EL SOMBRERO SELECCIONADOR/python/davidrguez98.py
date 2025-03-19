""" /*
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
 */ """

#EJERCICIO

import random

houses = {
    "Frontend": 0,
    "Backend": 0,
    "Mobile": 0,
    "Data": 0
}

questions = [
    {
        "question": "¿Qué tipo de desarrollo disfrutas más?",
        "answers": [
            {"option": "Analizar y procesar grandes volúmenes de datos", "house": "Data"},
            {"option": "Construir la lógica y la estructura detrás de una aplicación", "house": "Backend"},
            {"option": "Crear interfaces atractivas y dinámicas", "house": "Frontend"},
            {"option": "Desarrollar aplicaciones para dispositivos móviles", "house": "Mobile"}
        ]
    },
    {
        "question": "¿Qué lenguaje de programación prefieres?",
        "answers": [
            {"option": "Swift/Kotlin", "house": "Mobile"},
            {"option": "JavaScript/TypeScript", "house": "Frontend"},
            {"option": "SQL/Python (Pandas, NumPy)", "house": "Data"},
            {"option": "Python/Java", "house": "Backend"}
        ]
    },
    {
        "question": "¿Qué parte de un proyecto disfrutas más?",
        "answers": [
            {"option": "Trabajar en la integración con hardware y sensores", "house": "Mobile"},
            {"option": "Realizar análisis de datos y crear reportes", "house": "Data"},
            {"option": "Construir la API y manejar bases de datos", "house": "Backend"},
            {"option": "Diseñar y optimizar la experiencia del usuario", "house": "Frontend"}
        ]
    },
    {
        "question": "¿Qué herramienta te resulta más interesante?",
        "answers": [
            {"option": "Node.js/Django", "house": "Backend"},
            {"option": "Flutter/React Native", "house": "Mobile"},
            {"option": "React/Vue.js", "house": "Frontend"},
            {"option": "BigQuery/Tableau", "house": "Data"}
        ]
    },
    {
        "question": "¿Qué tipo de desafíos te gustan más?",
        "answers": [
            {"option": "Crear aplicaciones que funcionen bien en distintos dispositivos", "house": "Mobile"},
            {"option": "Optimizar la velocidad y la accesibilidad de una web", "house": "Frontend"},
            {"option": "Encontrar patrones en conjuntos de datos complejos", "house": "Data"},
            {"option": "Mejorar la eficiencia de las consultas en una base de datos", "house": "Backend"}
        ]
    },
    {
        "question": "¿Dónde te gustaría trabajar?",
        "answers": [
            {"option": "En una compañía de tecnología desarrollando apps móviles", "house": "Mobile"},
            {"option": "En una startup creando experiencias visuales innovadoras", "house": "Frontend"},
            {"option": "En una empresa analizando datos para la toma de decisiones", "house": "Data"},
            {"option": "En una gran empresa optimizando servidores y APIs", "house": "Backend"}
        ]
    },
    {
        "question": "¿Cómo te gusta resolver problemas?",
        "answers": [
            {"option": "Estructurando datos y optimizando procesos", "house": "Backend"},
            {"option": "Diseñando interfaces intuitivas", "house": "Frontend"},
            {"option": "Asegurando compatibilidad en distintas plataformas", "house": "Mobile"},
            {"option": "Utilizando modelos estadísticos y machine learning", "house": "Data"}
        ]
    },
    {
        "question": "¿Cuál consideras tu mayor fortaleza como programador?",
        "answers": [
            {"option": "Adaptabilidad y optimización", "house": "Mobile"},
            {"option": "Creatividad y diseño", "house": "Frontend"},
            {"option": "Lógica y estructura", "house": "Backend"},
            {"option": "Análisis y resolución de problemas", "house": "Data"}
        ]
    },
    {
        "question": "¿Qué tecnología te gustaría dominar?",
        "answers": [
            {"option": "GraphQL y microservicios", "house": "Backend"},
            {"option": "WebAssembly y animaciones avanzadas", "house": "Frontend"},
            {"option": "Desarrollo de apps con IA", "house": "Mobile"},
            {"option": "Deep Learning y análisis predictivo", "house": "Data"}
        ]
    },
    {
        "question": "¿Cuál sería tu proyecto ideal?",
        "answers": [
            {"option": "Un sistema escalable con alta concurrencia", "house": "Backend"},
            {"option": "Un modelo de machine learning con predicciones precisas", "house": "Data"},
            {"option": "Un sitio web con interacciones innovadoras", "house": "Frontend"},
            {"option": "Una aplicación móvil con funciones avanzadas", "house": "Mobile"}
        ]
    }
]

print("¿Bienvenido a la escuela de programación para magos y brujas del código!")
name = input("\n¿Cuál es tu nombre?: ")

for index, question in enumerate(questions):

    print(f"Pregunta {index + 1}: {question["question"]}")

    for i, answer in enumerate(question["answers"]):
        print(f"{i + 1}. {answer["option"]}")

    choice = int(input("\nSelecciona una respuesta entre 1 y 4. "))

    selected_asnwer = question["answers"][choice - 1]
    houses[selected_asnwer["house"]] += 1


assigned_house = max(houses, key=houses.get)
scores = list(houses.values())

if scores.count(max(scores)) > 1:
    possible_houses = [
        house for house, points in houses.items() if points == max(scores)
    ]

    assigned_house = random.choice(possible_houses)

    print(f"Tras una difícil decisión el alumno {name} ha sido seleccionado por el sombrero para la casa {assigned_house}")
else:
    print(f"El alumno/a {name} ha sido seleccionado por el sombrero para la casa {assigned_house}.")