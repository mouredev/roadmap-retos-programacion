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
from random import randint, choice


def casa(backend, data_science, frontend, mobile):
    decision = "fácil"
    resultados = {"Backend": backend, "Data Science": data_science, "Frontend": frontend, "Mobile": mobile}
    maximo_puntaje = max(resultados.values())
    if [resultados.values()].count(maximo_puntaje) > 1:
        decision = "reñida"
    return choice([x for x, y in resultados.items() if y == maximo_puntaje]), decision


casas = {"Backend": [], "Data Science": [], "Frontend": [], "Mobile": []}
preguntas = {1: {"pregunta": "¿Qué valoras más en tus amigos?",
                 "respuestas": ["Lealtad",
                                "Inteligencia",
                                "Valentía",
                                "Ambición"]},
             2: {"pregunta": "¿Cuál de estas actividades prefieres hacer en tu tiempo libre?",
                 "respuestas": ["Leer un libro interesante",
                                "Explorar lugares desconocidos",
                                "Participar en un duelo amistoso",
                                "Planificar tu futuro éxito"]},
             3: {"pregunta": "Si te enfrentas a un desafío, ¿cómo reaccionas?",
                 "respuestas": ["Analizas todas las opciones antes de actuar",
                                "Enfrentas el problema de frente sin miedo",
                                "Buscas la ayuda de tus amigos y trabajas en equipo",
                                "Encuentras una forma ingeniosa de resolverlo para salir beneficiado"]},
             4: {"pregunta": "¿Cuál de estas criaturas mágicas te parece más fascinante?",
                 "respuestas": ["Un Fénix, por su capacidad de renacer",
                                "Un Dragón, por su fuerza y poder",
                                "Un Hipogrifo, por su nobleza y orgullo",
                                "Un Nundu, por su letalidad y sigilo"]},
             5: {"pregunta": "Si tuvieras que elegir una poción mágica, ¿cuál preferirías?",
                 "respuestas": ["Una poción que te hiciera invencible",
                                "Una poción de inteligencia suprema",
                                "Una poción de suerte infinita",
                                "Una poción de invisibilidad"]},
             6: {"pregunta": "¿Qué es lo más importante para ti en un líder?",
                 "respuestas": ["Su sabiduría y capacidad para guiar",
                                "Su coraje y determinación",
                                "Su integridad y justicia",
                                "Su ambición y visión"]},
             7: {"pregunta": "Si pudieras elegir una habilidad mágica, ¿cuál sería?",
                 "respuestas": ["La habilidad de volar",
                                "La capacidad de hablar con animales",
                                "El poder de la transformación",
                                "La capacidad de leer mentes"]},
             8: {"pregunta": "¿Qué tipo de compañeros de clase prefieres?",
                 "respuestas": ["Aquellos que te desafían intelectualmente",
                                "Aquellos que te apoyan en todo momento",
                                "Aquellos que te inspiran a ser valiente",
                                "Aquellos que te ayudan a alcanzar tus metas"]},
             9: {"pregunta": "¿Cómo te sentirías si tuvieras que romper las reglas para lograr algo importante?",
                 "respuestas": ["Lo haría solo si es absolutamente necesario",
                                "Lo haría con valentía y sin remordimientos",
                                "Preferiría encontrar una manera de evitar romperlas",
                                "Lo haría estratégicamente para obtener el máximo beneficio"]},
             10: {"pregunta": "¿Qué cualidad crees que te define mejor?",
                  "respuestas": ["Sabiduría",
                                 "Valentía",
                                 "Lealtad",
                                 "Ambición"]}
             }

puntaje = []

while True:
    alumno = input("\nNombre: ").title()
    if not alumno:
        break
    for numero, pregunta in preguntas.items():
        print(f'\tPregunta nro {numero}: {pregunta["pregunta"]}')
        seleccion = randint(0, 3)
        print(f'\tRespuesta: {pregunta["respuestas"][seleccion]}')
        puntaje.append(seleccion)
    casa_seleccionada, decision = casa(puntaje.count(0), puntaje.count(1), puntaje.count(2), puntaje.count(3))
    casas[casa_seleccionada].append(alumno)
    print(f"{alumno} has sido elegido para {casa_seleccionada} y fue una decisión {decision}")
    puntaje.clear()

for casa, alumnos in casas.items():
    print(f"\nLa casa {casa} tiene {alumnos.__len__()} alumnos")
    for alno in alumnos:
        print(f"\tAlumno: {alno}")
