# @Author Daniel Grande Calderon (Mhayhem)

from enum import Enum
from random import choice

# EJERCICIO:
# Cada 1 de septiembre, el Hogwarts Express parte hacia la escuela
# de programación de Hogwarts para magos y brujas del código.
# En ella, su famoso sombrero seleccionador ayuda a los programadores
# a encontrar su camino...
# Desarrolla un programa que simule el comportamiento del sombrero.
# Requisitos:
# 1. El sombrero realizará 10 preguntas para determinar la casa del alumno.
# 2. Deben existir 4 casas. Por ejemplo: Frontend, Backend, Mobile y Data.
#    (Puedes elegir las que quieras)
# Acciones:
# 1. Crea un programa que solicite el nombre del alumno y realice 10
#    preguntas, con cuatro posibles respuestas cada una.
# 2. Cada respuesta asigna puntos a cada una de las casas (a tu elección).
# 3. Una vez finalizado, el sombrero indica el nombre del alumno 
#    y a qué casa pertenecerá (resuelve el posible empate de manera aleatoria,
#    pero indicándole al alumno que la decisión ha sido complicada).
        
# List of questions
questions = [
    {
        "question": "¿Qué es lo que más te motiva al empezar un proyecto?",
        "options": {
            1: "Diseñar una interfaz atractiva y que sea intuitiva para el usuario.",
            2: "Definir la lógica del sistema y cómo se van a gestionar los datos.",
            3: "Crear mecánicas divertidas y mundos interactivos.",
            4: "Pensar cómo se va a usar la app en el día a día desde el móvil."
        }
    },
    {
        "question": "¿Qué tipo de problema disfrutas más resolver?",
        "options": {
            1: "Que una web se vea bien en cualquier pantalla y navegador.",
            2: "Optimizar consultas y mejorar el rendimiento del servidor.",
            3: "Ajustar físicas, colisiones o comportamiento de enemigos.",
            4: "Gestionar permisos, sensores y notificaciones del sistema."
        }
    },
    {
        "question": "Si te dan un diseño, ¿qué harías primero?",
        "options": {
            1: "Convertirlo en HTML, CSS y animaciones.",
            2: "Crear la API que soporte todas las funcionalidades.",
            3: "Implementarlo dentro del motor de juego como una escena.",
            4: "Adaptarlo a pantallas pequeñas y gestos táctiles."
        }
    },
    {
        "question": "¿Qué tecnología te llama más la atención?",
        "options": {
            1: "React, Vue o Angular.",
            2: "Django, Spring o Node.js.",
            3: "Unity, Unreal Engine o Godot.",
            4: "Swift, Kotlin o Flutter."
        }
    },
    {
        "question": "¿Qué te molesta más cuando usas una app?",
        "options": {
            1: "Que la interfaz sea fea o poco clara.",
            2: "Que tarde mucho en cargar o falle el servidor.",
            3: "Que el juego tenga bugs o mecánicas mal balanceadas.",
            4: "Que consuma mucha batería o vaya lenta en el móvil."
        }
    },
    {
        "question": "¿Cómo te imaginas tu código la mayor parte del tiempo?",
        "options": {
            1: "Relacionado con estilos, componentes y eventos de usuario.",
            2: "Lleno de reglas de negocio, validaciones y seguridad.",
            3: "Controlando estados, animaciones y lógica en tiempo real.",
            4: "Integrándose con cámaras, GPS o notificaciones."
        }
    },
    {
        "question": "¿Qué tipo de proyecto personal harías por diversión?",
        "options": {
            1: "Una web interactiva con animaciones modernas.",
            2: "Una API robusta para gestionar usuarios y datos.",
            3: "Un juego indie con niveles y puntuaciones.",
            4: "Una app para organizar tareas o hábitos diarios."
        }
    },
    {
        "question": "¿Qué frase te representa más?",
        "options": {
            1: "“Si el usuario no lo entiende, es un problema de diseño.”",
            2: "“Los datos deben ser seguros y consistentes.”",
            3: "“Si no es divertido, no funciona.”",
            4: "“Tiene que sentirse natural en el móvil.”"
        }
    },
    {
        "question": "¿Qué tipo de errores te resultan más interesantes de arreglar?",
        "options": {
            1: "Elementos desalineados o animaciones rotas.",
            2: "Errores de concurrencia o lógica compleja.",
            3: "Bugs impredecibles durante el gameplay.",
            4: "Fallos específicos de un dispositivo o sistema operativo."
        }
    },
    {
        "question": "¿Qué te gustaría que dijeran de tu trabajo?",
        "options": {
            1: "“Es bonito y muy fácil de usar.”",
            2: "“Es sólido y nunca se cae.”",
            3: "“Es muy divertido y engancha.”",
            4: "“La uso todos los días en mi móvil.”"
        }
    }
]

# init respondent and table score
class Student:
    def __init__(self, name: str):
        self.name = name.capitalize()
        self.houses = {
            "Frontend": 0,
            "Backend": 0,
            "Videogames": 0,
            "Mobile": 0
        }
    
    def add_points(self, cls: str):
        self.houses[cls] = self.houses[cls] + 1

    def high_score(self):
        max_score = max(self.houses.values())
        your_stack = [stack for stack, score in self.houses.items() if score == max_score]
        if len(your_stack) < 2:
            return f"Alumno {self.name}, tu stack ideal es: {(your_stack[0])}"
        else:
            return f"Alumno {self.name},ha sido una decisión muy complicada pero creoque tu stack ideal es: {str(choice(your_stack))}"

# Enum opf stacks
class Stacks(Enum):
    Frontend = "Frontend"
    Backend = "Backend"
    Videogames = "Videogames"
    Mobile = "Mobile"


# main app
def quitz_programming(array: list, cls=Stacks,):
    name = input("Indique el nombre del estudiante: ")
    student = Student(name)
    stacks = [stack.value for stack in Stacks]
    for question in array:
        print(question["question"])
        for key, values in question["options"].items():
            print(f"{key}: {values}")
        while True:
            try:
                answer = int(input())
                if answer > len(question["options"]) or answer <= 0:
                    print("No es una opción valida")
                else:
                    choose = stacks[answer - 1] 
                    student.add_points(choose)
                    break
            except ValueError:
                print("Usa solo números.")
        print("\n")
    print(student.high_score())

quitz_programming(questions, Stacks)