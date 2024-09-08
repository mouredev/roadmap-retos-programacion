# _____________________________________
# https://github.com/kenysdev
# 2024 - Python
# _____________________________________
# 36 EL SOMBRERO SELECCIONADOR
# ------------------------------------
# * Cada 1 de septiembre, el Hogwarts Express parte hacia la escuela
#  * de programación de Hogwarts para magos y brujas del código.
#  * En ella, su famoso sombrero seleccionador ayuda a los programadores
#  * a encontrar su camino...
#  * Desarrolla un programa que simule el comportamiento del sombrero.
#  * Requisitos:
#  * 1. El sombrero realizará 10 preguntas para determinar la casa del alumno.
#  * 2. Deben existir 4 casas. Por ejemplo: Frontend, Backend, Mobile y Data.
#  *    (Puedes elegir las que quieras)
#  * Acciones:
#  * 1. Crea un programa que solicite el nombre del alumno y realice 10
#  *    preguntas, con cuatro posibles respuestas cada una.
#  * 2. Cada respuesta asigna puntos a cada una de las casas (a tu elección).
#  * 3. Una vez finalizado, el sombrero indica el nombre del alumno
#  *    y a qué casa pertenecerá (resuelve el posible empate de manera aleatoria,
#  *    pero indicándole al alumno que la decisión ha sido complicada).

from random import choice
from typing import List

HOUSES = ["Frontend", "Backend", "Mobile", "Data"]

# Nota: Preguntas y respuestas generadas por IA

QUESTIONS = [
    "¿Qué te atrae más?",
    "¿Qué superhéroe de la programación te gustaría ser?",
    "En un proyecto de software, ¿qué rol te emociona más?",
    "Si tu código fuera una obra de arte, ¿qué estilo tendría?",
    "¿Qué animal de programación serías?",
    "En una hackathon, ¿qué tipo de proyecto propondrías?",
    "Si tu carrera en tech fuera una película, ¿de qué género sería?",
    "¿Qué herramienta de programación no puede faltar en tu caja de herramientas digital?",
    "Si pudieras resolver un gran problema en tech, ¿cuál elegirías?",
    "¿Qué tipo de equipo prefieres?"
]

ANSWERS = [
    ["Crear experiencias visuales.", "Solucionar problemas de funcionamiento.", "Innovar en dispositivos portátiles.", "Descubrir tendencias ocultas."],
    ["Diseñador de Interfaces, creando experiencias asombrosas", "Arquitecto de Sistemas, construyendo estructuras robustas", "Mago de Apps, conjurando soluciones móviles", "Explorador de Datos, descubriendo tesoros ocultos"],
    ["Director de UX, orquestando la sinfonía visual", "Ingeniero de Backend, dominando la lógica del servidor", "Desarrollador de Apps, llevando la potencia al bolsillo", "Científico de Datos, descifrando los secretos de la información"],
    ["Minimalismo elegante, como una landing page perfecta", "Arquitectura compleja, como un sistema distribuido", "Diseño adaptativo, fluyendo en diferentes dispositivos", "Visualización de datos, pintando historias con números"],
    ["Un camaleón, adaptándome a diferentes frameworks", "Un pulpo, manejando múltiples servicios a la vez", "Un colibrí, ágil y siempre en movimiento", "Una lechuza, analizando datos con sabiduría"],
    ["Una web app que revolucione la experiencia del usuario", "Un sistema de IA que optimice procesos backend", "Una app móvil que cambie la forma de interactuar con el mundo", "Un proyecto de big data que prediga tendencias futuras"],
    ["Comedia romántica con JavaScript y CSS", "Thriller de ciencia ficción con microservicios", "Aventura de acción en el mundo de las apps", "Documental profundo sobre el universo de los datos"],
    ["Un editor de código con plugins para diseño visual", "Una robusta suite de testing y depuración", "Un emulador multi-dispositivo de última generación", "Una plataforma de análisis de datos en tiempo real"],
    ["Hacer que la accesibilidad web sea universal", "Crear una arquitectura de software autorreparable", "Desarrollar una plataforma de AR/VR para educación móvil", "Construir un modelo de IA ético y transparente"],
    ["Creativos enfocados en diseño.", "Técnicos que construyen sistemas.", "Especialistas en aplicaciones móviles.", "Expertos en datos y análisis."]
]

class SortingHat:
    def __init__(self, name: str):
        self.name = name
        self.scores = {house: 0 for house in HOUSES}

    def ask_question(self, q_num: int, question: str, answers: List[str]):
        print(f"\n#{q_num}: {question}")
        for i, answer in enumerate(answers, start=1):
            print(f"{i}) {answer}")
        
        while True:
            try:
                choice = int(input("Elige tu respuesta (1-4): ")) - 1
                if 0 <= choice < len(HOUSES):
                    self.scores[HOUSES[choice]] += 1
                    break
                else:
                    print("Por favor, elige un número entre 1 y 4.")
            except ValueError:
                print("Por favor, ingresa un número válido.")

    def select_house(self) -> str:
        max_score = max(self.scores.values())
        top_houses = [house for house, score in self.scores.items() if score == max_score]
        
        if len(top_houses) > 1:
            print("\nLa decisión ha sido complicada.")
            return choice(top_houses)
        return top_houses[0]

def main():
    print("EL SOMBRERO SELECCIONADOR")
    name = input("¿Cuál es tu nombre? : ")
    hat = SortingHat(name)

    for i, (question, answers) in enumerate(zip(QUESTIONS, ANSWERS), start=1):
        hat.ask_question(i, question, answers)

    selected_house = hat.select_house()
    print(f"\n'{name}' pertenecerá a la casa '{selected_house}'\n")

if __name__ == "__main__":
    main()

