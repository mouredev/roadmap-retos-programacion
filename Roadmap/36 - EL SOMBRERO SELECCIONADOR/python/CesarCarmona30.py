'''
  EJERCICIO
'''

import random, time

houses = {
  "a": ["Frontend", 0],
  "b": ["Backend", 0],
  "c": ["Desarrollo de videojuegos", 0],
  "d": ["Ciberseguridad", 0]
}

pets = {
   "Frontend": "𖤍",
   "Backend": "𓅓",
   "Desarrollo de videojuegos": "𓅛",
   "Ciberseguridad": "𓃠"
}

print(f"""Bienvenido a la escuela de la programación de Hogwarts para magos y brujas del código.
A continuación el sombrero te guiará a través de preguntas para encontrar tu camino hacia tu casa ideal.
Cuál de estás casas será la que te consolide...\n""")

for house, animal in pets.items():
   print(f'{animal} {house} {animal}')

name = input("\nEmpecemos... ¿Cuál es tu nombre?: ")

questions = [
  { 1: "¿Qué parte de un proyecto te resulta más interesante?",
    "options": {
      "a": "Crear una interfaz de usuario atractiva y fácil de usar.",
      "b": "Desarrollar la lógica de negocio y gestionar bases de datos.",
      "c": "Diseñar mecánicas y físicas de inmersivas.",
      "d": "Asegurar la protección de los datos y prevenir ataques."
    }},
    { 2: "¿Qué herramienta preferirías utilizar?",
    "options": {
      "a": "Figma o Sketch.",
      "b": "Docker o Kubernetes.",
      "c": "Unity o Unreal Engine.",
      "d": "Wireshark o Burp Suite."
    }},
    { 3: "¿Qué tipo de errores disfrutas resolver?",
    "options": {
      "a": "Fallos de estilo o funcionalidad en una página web.",
      "b": "Bugs en la lógica del servidor o en una base de datos.",
      "c": "Problemas de comportamiento o física en un juego.",
      "d": "Vulnerabilidades en el sistema o posibles puntos de ataque."
    }},
    { 4: "Lenguaje de programación (o tecnología) favorito:",
    "options": {
      "a": "JavaScript o TypeScript.",
      "b": "Python, Java o Node.js.",
      "c": "C++ o C#.",
      "d": "C, Python o Bash."
    }},
    { 5: "¿Qué prefieres optimizar en un proyecto?",
    "options": {
      "a": "La experiencia de usuario y la velocidad de carga de la interfaz.",
      "b": "El rendimiento del servidor y las consultas de la base de datos.",
      "c": "Los gráficos y la jugabilidad en tiempo real.",
      "d": "La seguridad de los datos y la prevención de intrusiones."
    }},
    { 6: "¿Qué tipo de desafíos te emocionan más?",
    "options": {
      "a": "Crear animaciones fluidas y transiciones en la interfaz.",
      "b": "Diseñar una API robusta y eficiente.",
      "c": "Implementar inteligencia artificial para NPCs en un videojuego.",
      "d": "Descubrir y mitigar una nueva vulnerabilidad de seguridad."
    }},
    { 7: "¿Qué tecnología te gustaría dominar?",
    "options": {
      "a": "React, Vue o Angular",
      "b": "Express, Django o Flask",
      "c": "Unreal Engine o Unity",
      "d": "Metasploit o herramientas de análisis forense digital."
    }},
    { 8: "¿En qué área preferirías trabajar a largo plazo?",
    "options": {
      "a": "Creación de interfaces y experiencias de usuario visuales.",
      "b": "Diseño de la lógica interna y los servicios de backend.",
      "c": "Desarrollo de mundos y mecánicas en videojuegos.",
      "d": "Auditoría de seguridad y pentesting."
    }},
    { 9: "¿Qué proyecto te resulta más atractivo?",
    "options": {
      "a": "Desarrollar una aplicación web interactiva y dinámica.",
      "b": "Crear una API que sirva datos a múltiples plataformas.",
      "c": "Desarrollar un videojuego inmersivo en 3D.",
      "d": "Desarrollar un sistema de protección contra ataques DDoS."
    }},
    { 10: "¿Qué prefieres como objetivo principal en tu trabajo?",
    "options": {
      "a": "Hacer que la aplicación sea visualmente atractiva y fácil de usar.",
      "b": "Asegurarte de que la aplicación funcione sin problemas en el servidor.",
      "c": "Crear una experiencia de juego envolvente y divertida.",
      "d": "Garantizar que los sistemas estén seguros contra ataques."
    }}
]
  

for id, question in enumerate(questions):
  print(f"\nPregunta {id + 1}: {question[id + 1]}")
  for option, answer in question["options"].items():
    print(f"{option}) {answer}")

  reply = input("Elige una opción:\n>_ ").lower()

  while reply not in question["options"]:
    reply = input("Opción no válida. Por favor intenta de nuevo. a) b) c) o d): ").lower()

  houses[reply][1] += 1

max_score = max(house[1] for house in houses.values())
winning_houses = [house_name for house_name, house in houses.items() if house[1] == max_score]

chosen_house = None

print(f"¡Felicidades {name.capitalize()}!")

if len(winning_houses) > 1:
    chosen_house_key = random.choice(winning_houses)
    chosen_house = houses[chosen_house_key][0]
    print(f"¡La decisión ha sido complicada! Pero finalmente, el sombrero te ha asignado a la casa...")
else:
    chosen_house = houses[winning_houses[0]][0]
    print(f"El sombrero te ha asignado a la casa...")

for sec in range(1, 4):
   time.sleep(1)
   print('.' * sec)

time.sleep(1)
print(f'{pets[chosen_house]}' * 20, end='')
print(f"\n──⊹¡{chosen_house.upper()}!⊹──")
print(f'{pets[chosen_house]}' * 20, end='')