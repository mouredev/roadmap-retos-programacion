'''
Ejercicio:
Desarrolla un programa que simule el comportamiento del sombrero.

Requisitos:
    1. El sombrero realizara 10 preguntas para determinar la casa del alumno.
    2. Deben existir 4 casas. Por ejemplo: Frontend, Backend, Mobile y Data. (Puedes elegir las que quieras)

Acciones:
    1. Crea un programa que solicite el nombre del alumno y realice 10 preguntas, con cuatro posibles respuestas cada una.
    2. Cada respuesta asigna puntos a cada una de las casas (a tu eleccion).
    3. Una vez finalizado, el sombrero indica el nombre del alumno y a que casa pertenecera (resuelve el posible empate de manera aleatoria, pero indicandole al alumno que la decision ha sido complicada).
'''

import random

# Definimos las casas
houses = ["Aether",  "Aether oscuro", "Void", "Radiance"]

def crear_preguntas():
    preguntas = [] # Creamos una lista para almacenar las preguntas

    # Agregamos las preguntas a la lista
    preguntas.append({
        "pregunta": "Te encuentras en medio de una oleada masiva. ¿Cual es tu primer instinto?",
        "opciones": {
            "a": {"texto": "Buscar la ventaja tactica y curbrir a los compañeros", "puntos": {"Aether": 2, "Aether oscuro": 0, "Void": 0, "Radiance": 0}},
            "b": {"texto": "Lanzarte de frente aprovechando cualquier poder que tengas, sin importar el costo.", "puntos":
            {"Aether": 0, "Aether oscuro": 2, "Void": 0, "Radiance": 0}},
            "c": {"texto": "Mantener la calma absoluta y analizar el movimiento de los enemigos.", "puntos": {"Aether": 0, "Aether oscuro": 0, "Void": 2, "Radiance": 0}},
            "d": {"texto": "Ejecutar un plan perfecto, sin errores, como lo has practicado.", "puntos": {"Aether": 0, "Aether oscuro": 0, "Void": 0, "Radiance": 2}}
        }
    })

    preguntas.append({
        "pregunta": "Una anomalia dimensional se abre frente a ti. ¿Que haces?",
        "opciones": {
            "a": {"texto": "Intentar estabilizarla y comprender su origen.", "puntos": {"Aether": 2, "Aether oscuro": 0, "Void": 0, "Radiance": 0}},
            "b": {"texto": "Entrar sin dudar, atradio por su fuerza prohibida.", "puntos": {"Aether": 0, "Aether oscuro": 2, "Void": 0, "Radiance": 0}},
            "c": {"texto": "Observar en silencio, sintiendo como el vacio responde.", "puntos": {"Aether": 0, "Aether oscuro": 0, "Void": 2, "Radiance": 0}},
            "d": {"texto": "Sellarla para evitar que corrompa la luz del mundo.", "puntos": {"Aether": 0, "Aether oscuro": 0, "Void": 0, "Radiance": 2}}
        }
    })

    preguntas.append({
        "pregunta": "Un aliado cae herido durante la batalla. ¿Como respondes?",
        "opciones": {
            "a": {"texto": "Lo ayudas de inmediato, la unidad es lo primero.", "puntos": {"Aether": 2, "Aether oscuro": 0, "Void": 0, "Radiance": 0}},
            "b": {"texto": "Lo usas como distraccion para aprovechar una oportunidad.", "puntos": {"Aether": 0, "Aether oscuro": 2, "Void": 0, "Radiance": 0}},
            "c": {"texto": "Guardas silencio y aceptas el destino de cada ser.", "puntos": {"Aether": 0, "Aether oscuro": 0, "Void": 2, "Radiance": 0}},
            "d": {"texto": "Exiges disciplina: debio prever su error.", "puntos": {"Aether": 0, "Aether oscuro": 0, "Void": 0, "Radiance": 2}}
        }
    })

    preguntas.append({
        "pregunta": "Encuentras un artefacto antiguo lleno de energia desconocida.",
        "opciones": {
            "a": {"texto": "Lo investigas cuidadosamente.", "puntos": {"Aether": 2, "Aether oscuro": 0, "Void": 0, "Radiance": 0}},
            "b": {"texto": "Lo activas aunque pueda consumir tu alma.", "puntos": {"Aether": 0, "Aether oscuro": 2, "Void": 0, "Radiance": 0}},
            "c": {"texto": "Lo sientes como un eco del vacio y absorbes lentamente.", "puntos": {"Aether": 0, "Aether oscuro": 0, "Void": 2, "Radiance": 0}},
            "d": {"texto": "Lo purificas con luz para revelar su proposito.", "puntos": {"Aether": 0, "Aether oscuro": 0, "Void": 0, "Radiance": 2}}
        }
    })

    preguntas.append({
        "pregunta": "¿Que valor consideras mas importante en una batalla?",
        "opciones": {
            "a": {"texto": "Cooperacion", "puntos": {"Aether": 2, "Aether oscuro": 0, "Void": 0, "Radiance": 0}},
            "b": {"texto": "Poder absoluto", "puntos": {"Aether": 0, "Aether oscuro": 2, "Void": 0, "Radiance": 0}},
            "c": {"texto": "Serenidad interna", "puntos": {"Aether": 0, "Aether oscuro": 0, "Void": 2, "Radiance": 0}},
            "d": {"texto": "Precision impecable", "puntos": {"Aether": 0, "Aether oscuro": 0, "Void": 0, "Radiance": 2}}
        }
    })

    preguntas.append({
        "pregunta": "Un enemigo extremadamente poderoso aparece. ¿Cual es tu reaccion?",
        "opciones": {
            "a": {"texto": "Coordinar estategias con el equipo.", "puntos": {"Aether": 2, "Aether oscuro": 0, "Void": 0, "Radiance": 0}},
            "b": {"texto": "Desatar toda tu fuerza sin medi consecuencias", "puntos": {"Aether": 0, "Aether oscuro": 2, "Void": 0, "Radiance": 0}},
            "c": {"texto": "Esperar pacientemente su movimiento para contraatacar.", "puntos": {"Aether": 0, "Aether oscuro": 0, "Void": 2, "Radiance": 0}},
            "d": {"texto": "Destruirlo con una ejecucion perfecta", "puntos": {"Aether": 0, "Aether oscuro": 0, "Void": 0, "Radiance": 2}}
        }
    })

    preguntas.append({
        "pregunta": "Debes elegir una fuente de energia. ¿Cual resuena contigo?",
        "opciones": {
            "a": {"texto": "Energia estable del Aether.", "puntos": {"Aether": 2, "Aether oscuro": 0, "Void": 0, "Radiance": 0}},
            "b": {"texto": "Corrupcion vibrante del Aether Oscuro", "puntos": {"Aether": 0, "Aether oscuro": 2, "Void": 0, "Radiance": 0}},
            "c": {"texto": "El silencio eterno del vacio", "puntos": {"Aether": 0, "Aether oscuro": 0, "Void": 2, "Radiance": 0}},
            "d": {"texto": "La luz absoluta y purificadora", "puntos": {"Aether": 0, "Aether oscuro": 0, "Void": 0, "Radiance": 2}}
        }
    })

    preguntas.append({
        "pregunta": "¿Que te impulsa a seguir adelante?",
        "opciones": {
            "a": {"texto": "La esperanza de restaurar el equilibrio.", "puntos": {"Aether": 2, "Aether oscuro": 0, "Void": 0, "Radiance": 0}},
            "b": {"texto": "La ambicion de superar todos los limites.", "puntos": {"Aether": 0, "Aether oscuro": 2, "Void": 0, "Radiance": 0}},
            "c": {"texto": "La aceptacion y el destino y del silencio.", "puntos": {"Aether": 0, "Aether oscuro": 0, "Void": 2, "Radiance": 0}},
            "d": {"texto": "La obligacion de alcanzar la perfeccion.", "puntos": {"Aether": 0, "Aether oscuro": 0, "Void": 0, "Radiance": 2}}
        }
    })

    preguntas.append({
        "pregunta": "¿Como describes tu estilo de combate?",
        "opciones": {
            "a": {"texto": "Estrategico y cooperativo.", "puntos": {"Aether": 2, "Aether oscuro": 0, "Void": 0, "Radiance": 0}},
            "b": {"texto": "Agresivo y arriesgado.", "puntos": {"Aether": 0, "Aether oscuro": 2, "Void": 0, "Radiance": 0}},
            "c": {"texto": "Fluido y minimalista.", "puntos": {"Aether": 0, "Aether oscuro": 0, "Void": 2, "Radiance": 0}},
            "d": {"texto": "Preciso y elegante.", "puntos": {"Aether": 0, "Aether oscuro": 0, "Void": 0, "Radiance": 2}}
        }
    })

    preguntas.append({
        "pregunta": "Un ser primigenio despierta. ¿Que papel tomas?",
        "opciones": {
            "a": {"texto": "Mediador entre fuerzas opuestas.", "puntos": {"Aether": 2, "Aether oscuro": 0, "Void": 0, "Radiance": 0}},
            "b": {"texto": "El portador del caos que desatara su potencial.", "puntos": {"Aether": 0, "Aether oscuro": 2, "Void": 0, "Radiance": 0}},
            "c": {"texto": "La sombra silenciosa que lo enfrenta sin emocion", "puntos": {"Aether": 0, "Aether oscuro": 0, "Void": 2, "Radiance": 0}},
            "d": {"texto": "La luz que debe erradicarlo para preservar la pureza.", "puntos": {"Aether": 0, "Aether oscuro": 0, "Void": 0, "Radiance": 2}}
        }
    })

    return preguntas[:10]

nombre = input("Cual es tu nombre, alumno: ")

# Creamos un marcador de puntos
puntajes = {casa: 0 for casa in houses}

# Recorremos las preguntas una por una
preguntas = crear_preguntas()
for p in preguntas:
    print(p["pregunta"])
    for clave, info in p["opciones"].items():
        print(f"{clave} {info['texto']}")

    respuesta = input("Elige una opcion: ").lower()

    if respuesta not in ["a", "b", "c", "d"]:
        print("Respuesta invalida! Tomate esto enserio.")
        pass
    
    puntos_respuesta = p["opciones"][respuesta]["puntos"]

    for casa, puntos in puntos_respuesta.items():
        puntajes[casa] += puntos

mayor = max(puntajes.values())
ganadoras = [c for c, p in puntajes.items() if p == mayor]

if len(ganadoras) > 1:
    eleccion_final = random.choice(ganadoras)
    print("La decicion ha sido dificil... pero el sombrero ha hablado!")
else:
    eleccion_final = ganadoras[0]
    

print(f"Alumno: {nombre}\n"\
      f"Tu casa es: {eleccion_final}")