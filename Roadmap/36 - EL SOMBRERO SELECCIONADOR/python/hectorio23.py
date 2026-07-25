# Autor: Héctor Adán
# GitHub: https://github.com/hectorio23

import random

# Casas
houses = ["Frontend", "Backend", "Mobile", "Data"]

# Preguntas y asignación de puntos
questions = [
    {"question": "¿Prefieres trabajar en interfaces visuales?", "scores": [3, 1, 2, 0]},
    {"question": "¿Te gusta optimizar el rendimiento del servidor?", "scores": [0, 3, 1, 1]},
    {"question": "¿Te interesa crear aplicaciones móviles?", "scores": [1, 0, 3, 1]},
    {"question": "¿Te apasiona analizar grandes conjuntos de datos?", "scores": [0, 1, 0, 3]},
    # Aquí podrías agregar 6 preguntas más...
]

def ask_question():
    # Función para realizar las preguntas y sumar puntos a cada casa
    scores = [0, 0, 0, 0]  # Puntos de cada casa
    for q in questions:
        print(q["question"])
        answer = int(input("Responde 1, 2, 3 o 4: ")) - 1
        # Aumentar los puntos de cada casa según la respuesta seleccionada
        for i in range(4):
            scores[i] += q["scores"][i] if i == answer else 0
    return scores

def sorting_hat():
    name = input("¿Cuál es tu nombre? ")
    scores = ask_question()
    max_score = max(scores)
    candidates = [houses[i] for i, score in enumerate(scores) if score == max_score]
    
    # Si hay empate, selecciona aleatoriamente
    if len(candidates) > 1:
        print(f"{name}, la decisión ha sido complicada...")
        assigned_house = random.choice(candidates)
    else:
        assigned_house = candidates[0]
    
    print(f"{name}, has sido asignado a {assigned_house}.")

# Ejecutar el sombrero seleccionador
sorting_hat()
