import random

#Definicion casas
Casas = {
    "Frontend": 0,
    "Backend": 0,
    "Mobile": 0,
    "Data": 0
}

#Definicion preguntas
Preguntas = [
    {
        "Pregunta": "Si no fueras quisieras ser programador, ¿Cual seria tu profesión favorita?",
        "Opciones": {
            "a": ("Pintor", "Frontend"),
            "b": ("Arquitecto", "Backend"),
            "c": ("Influencer", "Mobile"),
            "d": ("Estadista", "Data")
        }

    },

    {
        "Pregunta": "¿Cual es tu lenguaje de programacion favorito?",
        "Opciones": {
            "a": ("JavaScript", "Frontend"),
            "b": ("C#", "Backend"),
            "c": ("Java", "Mobile"),
            "d": ("Python", "Data")
        }

    },

    {
        "Pregunta": "¿Donde te sientes mas comodo?",
        "Opciones": {
            "a": ("Navegadores web", "Frontend"),
            "b": ("Sistemas distribuidos", "Backend"),
            "c": ("Plataformas móviles", "Mobile"),
            "d": ("Entornos de big data", "Data")
        }

    },

    {
        "Pregunta": "¿Cual seria tu rol ideal en un equipo de desarrollo?",
        "Opciones": {
            "a": ("Diseñador de interfaces de usuario", "Frontend"),
            "b": ("Ingeniero de sistemas", "Backend"),
            "c": ("Desarrollador de aplicaciones móviles", "Mobile"),
            "d": ("Científico de datos", "Data")
        }
    },

    {
        "Pregunta": "¿Que herramienta te resulta mas interesante?",
        "Opciones": {
            "a": ("Figma", "Frontend"),
            "b": ("Docker", "Backend"),
            "c": ("Android Studio", "Mobile"),
            "d": ("Jupyter Notebook", "Data")
        }
    },

    {
        "Pregunta": "¿Que consideras más importante en un producto tecnologico?",
        "Opciones": {
            "a": ("La usabilidad y el diseño", "Frontend"),
            "b": ("La robustez y escalabilidad", "Backend"),
            "c": ("La accesibilidad en cualquier dispositivo", "Mobile"),
            "d": ("La capacidad de extraer informacion valiosa", "Data")
        }
    },

    {
        "Pregunta": "¿Como definirias el exito en un proyecto?",
        "Opciones": {
            "a": ("Una interfaz atractiva y funcional", "Frontend"),
            "b": ("Un sistema eficiente y seguro", "Backend"),
            "c": ("Una aplicacion que funcione sin problemas en cualquier dispositivo", "Mobile"),
            "d": ("Tomar decisiones basadas en datos solidos", "Data")
        }
    },

{
        "Pregunta": "¿Que te motiva mas al iniciar un nuevo proyecto?",
        "Opciones": {
            "a": ("Crear una experiencia visual impresionante", "Frontend"),
            "b": ("Resolver problemas complejos con codigo eficiente", "Backend"),
            "c": ("Innovar con funciones mobiles nunca vistas", "Mobile"),
            "d": ("Descubrir nuevas tendencias a base del estudio de datos", "Data")
        }
    },

    {
        "Pregunta": "¿Que aspectos consideras mas desafiantes en el desarrollo de software?",
        "Opciones": {
            "a": ("Hacer una interfaz sencilla y atractiva", "Frontend"),
            "b": ("Hacer un sistema escalable", "Backend"),
            "c": ("Adaptar la app a diferentes sistemas operativos", "Mobile"),
            "d": ("Gestionar grandes volumenes de informacion con precision", "Data")
        }
    },

    {
        "Pregunta": "¿Si tuvieras que especializarte en una tecnología ¿Cual elegirias?",
        "Opciones": {
            "a": ("React o Vue.js para interfaces dinamicas", "Frontend"),
            "b": ("Node.js o Django para desarrollo backend", "Backend"),
            "c": ("Swift o Kotlin para aplicaciones moviles", "Mobile"),
            "d": ("SQL o Hadoop para manejo de grandes datos", "Data")
        }
    }
]

#Funcion Principal
def SombreroMagico():
    nombre = input("Cual es tu nombre? ")
    print(f"\nHola {nombre}! Vamos a ver a que casa perteneces...\n")
          
    for Pregunta in Preguntas:
        print(Pregunta["Pregunta"])
        for key, value in Pregunta["Opciones"].items():
            print(f"{key}) {value[0]}")
        respuesta = input("\nSelecciona una opción (a/b/c/d): ").lower()

        while respuesta not in Pregunta["Opciones"]:
            print("Respuesta no válida. Intenta nuevamente.")
            respuesta = input("Selecciona una opción (a/b/c/d): ").lower()

            # Asignar el punto
            casa_elegida = Pregunta["Opciones"][respuesta][1]
            Casas[casa_elegida] += 1

    # Decidir  casa con más puntos
    casa_ganadora = max(Casas, key = Casas.get)
    max_puntos = max(Casas.values())
    
    # Si hay empate, elegimos una al azar
    casas_empate = [Casa for Casa, puntos in Casas.items() if puntos == max_puntos]

    if len(casas_empate) > 1:
        casa_ganadora = random.choice(casas_empate)
        print(f"\n¡Decisión difícil! {nombre}, el sombrero ha decidido finalmente colocarte en... ¡{casa_ganadora}!\n")
    else:
        print(f"\n¡Felicidades {nombre}! El sombrero te ha colocado en... ¡{casa_ganadora}!\n")

# Ejecutar el programa
SombreroMagico()