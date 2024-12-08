"""
 EJERCICIO:
 Cada 1 de septiembre, el Hogwarts Express parte hacia la escuela
 de programación de Hogwarts para magos y brujas del código.
 En ella, su famoso sombrero seleccionador ayuda a los programadores
 a encontrar su camino...
 Desarrolla un programa que simule el comportamiento del sombrero.
 Requisitos:
 1. El sombrero realizará 10 preguntas para determinar la casa del alumno.
 2. Deben existir 4 casas. Por ejemplo: Frontend, Backend, Mobile y Data.
    (Puedes elegir las que quieras)
 Acciones:
 1. Crea un programa que solicite el nombre del alumno y realice 10
    preguntas, con cuatro posibles respuestas cada una.
 2. Cada respuesta asigna puntos a cada una de las casas (a tu elección).
 3. Una vez finalizado, el sombrero indica el nombre del alumno 
    y a qué casa pertenecerá (resuelve el posible empate de manera aleatoria,
    pero indicándole al alumno que la decisión ha sido complicada).
"""

preguntas = {
    "pregunta_1": {
        "pregunta": "¿Qué es lo que más disfrutas al programar?",
        "opciones": {
            "a": {"respuesta": "Diseñar interfaces atractivas", "casa": "Frontend"},
            "b": {"respuesta": "Optimizar el rendimiento del servidor", "casa": "Backend"},
            "c": {"respuesta": "Crear aplicaciones móviles útiles", "casa": "Mobile"},
            "d": {"respuesta": "Analizar grandes conjuntos de datos", "casa": "Data"}
        }
    },
    "pregunta_2": {
        "pregunta": "¿Qué tipo de proyecto te atrae más?",
        "opciones": {
            "a": {"respuesta": "Aplicaciones web con mucho estilo", "casa": "Frontend"},
            "b": {"respuesta": "Sistemas que manejen grandes volúmenes de datos", "casa": "Backend"},
            "c": {"respuesta": "Aplicaciones para teléfonos inteligentes", "casa": "Mobile"},
            "d": {"respuesta": "Dashboards para visualizar información", "casa": "Data"}
        }
    },
    "pregunta_3": {
        "pregunta": "¿Qué herramienta te resulta más interesante?",
        "opciones": {
            "a": {"respuesta": "HTML, CSS y JavaScript", "casa": "Frontend"},
            "b": {"respuesta": "Node.js o Python", "casa": "Backend"},
            "c": {"respuesta": "React Native o Swift", "casa": "Mobile"},
            "d": {"respuesta": "SQL o Python con Pandas", "casa": "Data"}
        }
    },
    "pregunta_4": {
        "pregunta": "¿Cuál es tu mayor fortaleza como programador?",
        "opciones": {
            "a": {"respuesta": "Crear interfaces amigables", "casa": "Frontend"},
            "b": {"respuesta": "Solucionar problemas complejos en el servidor", "casa": "Backend"},
            "c": {"respuesta": "Desarrollar apps funcionales", "casa": "Mobile"},
            "d": {"respuesta": "Encontrar patrones en los datos", "casa": "Data"}
        }
    },
    "pregunta_5": {
        "pregunta": "¿Qué prefieres en un equipo de desarrollo?",
        "opciones": {
            "a": {"respuesta": "Ser quien diseña el look y feel", "casa": "Frontend"},
            "b": {"respuesta": "Ser quien gestiona la arquitectura de la aplicación", "casa": "Backend"},
            "c": {"respuesta": "Ser quien se encarga de la versión móvil", "casa": "Mobile"},
            "d": {"respuesta": "Ser quien analiza el rendimiento del sistema", "casa": "Data"}
        }
    },
    "pregunta_6": {
        "pregunta": "¿En qué te enfocas más cuando trabajas en un proyecto?",
        "opciones": {
            "a": {"respuesta": "En el diseño visual y la experiencia de usuario", "casa": "Frontend"},
            "b": {"respuesta": "En la estabilidad y escalabilidad del sistema", "casa": "Backend"},
            "c": {"respuesta": "En hacer que la app funcione en dispositivos móviles", "casa": "Mobile"},
            "d": {"respuesta": "En el análisis y visualización de los datos", "casa": "Data"}
        }
    },
    "pregunta_7": {
        "pregunta": "¿Cuál es tu mayor motivación como desarrollador?",
        "opciones": {
            "a": {"respuesta": "Crear experiencias de usuario memorables", "casa": "Frontend"},
            "b": {"respuesta": "Resolver problemas complejos con eficiencia", "casa": "Backend"},
            "c": {"respuesta": "Desarrollar aplicaciones que la gente use todos los días", "casa": "Mobile"},
            "d": {"respuesta": "Descubrir patrones ocultos en los datos", "casa": "Data"}
        }
    },
    "pregunta_8": {
        "pregunta": "¿Qué aspecto prefieres de un nuevo proyecto?",
        "opciones": {
            "a": {"respuesta": "Hacer que se vea genial y sea fácil de usar", "casa": "Frontend"},
            "b": {"respuesta": "Asegurarme de que el servidor funcione sin problemas", "casa": "Backend"},
            "c": {"respuesta": "Hacer que funcione bien en dispositivos móviles", "casa": "Mobile"},
            "d": {"respuesta": "Organizar y visualizar los datos de forma eficiente", "casa": "Data"}
        }
    },
    "pregunta_9": {
        "pregunta": "¿Qué tecnología te emociona más aprender?",
        "opciones": {
            "a": {"respuesta": "Frameworks de JavaScript como React o Angular", "casa": "Frontend"},
            "b": {"respuesta": "Microservicios o arquitectura en la nube", "casa": "Backend"},
            "c": {"respuesta": "Desarrollo de aplicaciones móviles", "casa": "Mobile"},
            "d": {"respuesta": "Big Data o inteligencia artificial", "casa": "Data"}
        }
    },
    "pregunta_10": {
        "pregunta": "Si pudieras elegir un área de especialización, ¿cuál sería?",
        "opciones": {
            "a": {"respuesta": "Interfaz y experiencia de usuario", "casa": "Frontend"},
            "b": {"respuesta": "Desarrollo y mantenimiento del servidor", "casa": "Backend"},
            "c": {"respuesta": "Aplicaciones móviles", "casa": "Mobile"},
            "d": {"respuesta": "Ciencia de datos y análisis", "casa": "Data"}
        }
    }
}

def print_quiz():
    # Ejemplo para acceder a las preguntas
    answers = []
    for clave, contenido in preguntas.items():
        print(contenido["pregunta"])
        for opcion, detalle in contenido["opciones"].items():
            print(f"{opcion}: {detalle['respuesta']}")
        answer = input("Selecciona una de las opciones: ")
        answers.append(answer)
    return answers

def select_house(answers):
    # Contar las respuestas para cada casa
    countFront = answers.count('a')
    countBackend = answers.count('b')
    countMobile = answers.count('c')
    countData = answers.count('d')

    casas = {
        "Frontend": countFront,
        "Backend": countBackend,
        "Mobile": countMobile,
        "Data": countData
    }

    max_count = max(casas.values())

    posibles_casas = [casa for casa, count in casas.items() if count == max_count]

    if len(posibles_casas) > 1:
        print("¡Ha sido una decisión complicada!")
        return random.choice(posibles_casas)
    
    return posibles_casas[0]

def main():
    name = input("Introduce tu nombre: ")
    answers = print_quiz()
    house = select_house(answers)
    print(f"{name } la casa seleccionada es: {house}")

if __name__ == "__main__":
    main()