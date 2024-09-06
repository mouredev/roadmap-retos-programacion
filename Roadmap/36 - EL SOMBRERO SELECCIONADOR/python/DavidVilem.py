
import random

# Definimos las casas
casas = ["Frontend", "Backend", "Mobile", "Data"]

# Definimos un diccionario para almacenar los puntos de cada casa
puntos = {casa: 0 for casa in casas}

# Preguntas y opciones 
preguntas = [
    {
        "pregunta": "¿Cuál es tu lenguaje de programación favorito?",
        "opciones": {
            "a": ("JavaScript", "Frontend"),
            "b": ("Python", "Backend"),
            "c": ("Swift", "Mobile"),
            "d": ("R", "Data")
        }
    },
    {
        "pregunta": "¿Qué tipo de proyectos te gusta más desarrollar?",
        "opciones": {
            "a": ("Aplicaciones web", "Frontend"),
            "b": ("Sistemas distribuidos", "Backend"),
            "c": ("Aplicaciones móviles", "Mobile"),
            "d": ("Análisis de datos", "Data")
        }
    },
    {
        "pregunta": "¿Cuál es tu herramienta preferida para desarrollo?",
        "opciones": {
            "a": ("React", "Frontend"),
            "b": ("Django", "Backend"),
            "c": ("Flutter", "Mobile"),
            "d": ("Pandas", "Data")
        }
    },
    {
        "pregunta": "¿Qué es lo que más valoras en un proyecto?",
        "opciones": {
            "a": ("Interfaz de usuario", "Frontend"),
            "b": ("Rendimiento y escalabilidad", "Backend"),
            "c": ("Compatibilidad en dispositivos", "Mobile"),
            "d": ("Información y análisis", "Data")
        }
    },
    {
        "pregunta": "¿Cuál es tu entorno de trabajo favorito?",
        "opciones": {
            "a": ("Navegador", "Frontend"),
            "b": ("Servidor", "Backend"),
            "c": ("Dispositivo móvil", "Mobile"),
            "d": ("Ambiente de análisis", "Data")
        }
    },
    {
        "pregunta": "¿Qué prefieres aprender en tu tiempo libre?",
        "opciones": {
            "a": ("Nuevas tecnologías web", "Frontend"),
            "b": ("Arquitectura de software", "Backend"),
            "c": ("Desarrollo de apps", "Mobile"),
            "d": ("Machine learning", "Data")
        }
    },
    {
        "pregunta": "¿En qué tipo de equipo te gustaría trabajar?",
        "opciones": {
            "a": ("Equipo de UX/UI", "Frontend"),
            "b": ("Equipo de DevOps", "Backend"),
            "c": ("Equipo de desarrollo móvil", "Mobile"),
            "d": ("Equipo de ciencia de datos", "Data")
        }
    },
    {
        "pregunta": "¿Qué consideras más desafiante?",
        "opciones": {
            "a": ("Diseño responsivo", "Frontend"),
            "b": ("Optimización de consultas", "Backend"),
            "c": ("Compatibilidad multiplataforma", "Mobile"),
            "d": ("Limpieza de datos", "Data")
        }
    },
    {
        "pregunta": "¿Cuál es tu prioridad en un proyecto?",
        "opciones": {
            "a": ("Experiencia de usuario", "Frontend"),
            "b": ("Seguridad", "Backend"),
            "c": ("Accesibilidad", "Mobile"),
            "d": ("Precisión de los resultados", "Data")
        }
    },
    {
        "pregunta": "¿Qué te motiva más?",
        "opciones": {
            "a": ("Crear interfaces atractivas", "Frontend"),
            "b": ("Resolver problemas complejos", "Backend"),
            "c": ("Desarrollar apps innovadoras", "Mobile"),
            "d": ("Descubrir patrones en datos", "Data")
        }
    }
]

# Solicitar el nombre del alumno
nombre_alumno = input("¡Bienvenido al sombrero seleccionador! ¿Cuál es tu nombre? ")

# Realizar las preguntas
for idx, pregunta in enumerate(preguntas):
    print(f"\nPregunta {idx + 1}: {pregunta['pregunta']}")
    for opcion, (respuesta, casa) in pregunta["opciones"].items():
        print(f"  {opcion}. {respuesta}")
    
    eleccion = input("Elige una opción (a, b, c, d): ").lower()
    
    while eleccion not in pregunta["opciones"]:
        eleccion = input("Opción inválida. Por favor, elige entre a, b, c, d: ").lower()
    
    # Asignar puntos a la casa correspondiente
    casa_asignada = pregunta["opciones"][eleccion][1]
    puntos[casa_asignada] += 1

# Determinar la casa con mayor puntaje
max_puntos = max(puntos.values())
casas_ganadoras = [casa for casa, puntaje in puntos.items() if puntaje == max_puntos]

# Resolver empates si es necesario
if len(casas_ganadoras) > 1:
    casa_final = random.choice(casas_ganadoras)
    print(f"\n¡Vaya, {nombre_alumno}! El sombrero ha tenido una decisión difícil...")
else:
    casa_final = casas_ganadoras[0]

# Mostrar el resultado final
print(f"\n{nombre_alumno}, has sido seleccionado para la casa de {casa_final}!")