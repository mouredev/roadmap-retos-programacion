"""
/*
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
 */
"""
#Introduction to the program
print("¡Bienvenido al Sombrero Seleccionador de Hogwarts para personalidades!")
print("Responde a las siguientes preguntas para descubrir a qué casa perteneces según tu personalidad.")
print("Por favor, elige la opción que mejor te describa en cada pregunta.")
print("Las opciones siempre son: A, B, C, D.")
print("Para responder, escribe la letra correspondiente y pulsa Enter.")
input("Pulsa Enter para comenzar...")

# Dictionary with the questions and answers
questions_answers = {
    "¿Cómo te enfrentas a los problemas complejos?": {
        "Analítico": "Divido el problema en partes y analizo cada una.",
        "Creativo": "Busco soluciones fuera de lo común.",
        "Pragmático": "Me concentro en resolverlo de la manera más efectiva y directa.",
        "Emocional": "Sigo mis instintos para encontrar la solución."
    },
    "¿Qué te motiva en tu trabajo?": {
        "Analítico": "Resolver problemas difíciles con lógica.",
        "Creativo": "Innovar y crear nuevas ideas.",
        "Pragmático": "Cumplir con las expectativas y ser eficiente.",
        "Emocional": "Trabajar en algo que me apasione."
    },
    "¿Cómo organizas tu día?": {
        "Analítico": "Creo un plan detallado y lo sigo estrictamente.",
        "Creativo": "Prefiero dejar espacio para la espontaneidad.",
        "Pragmático": "Me aseguro de completar las tareas esenciales primero.",
        "Emocional": "Organizo mi día según mi estado de ánimo."
    },
    "¿Cómo manejas la presión?": {
        "Analítico": "Mantengo la calma y analizo la situación lógicamente.",
        "Creativo": "Encuentro formas creativas de lidiar con ella.",
        "Pragmático": "Me enfoco en las prioridades y actúo con eficacia.",
        "Emocional": "Me apoyo en mis emociones para superar el estrés."
    },
    "¿Qué prefieres hacer en tu tiempo libre?": {
        "Analítico": "Resolver acertijos o problemas lógicos.",
        "Creativo": "Hacer arte o actividades creativas.",
        "Pragmático": "Realizar actividades prácticas y productivas.",
        "Emocional": "Conectar con amigos o actividades que me hagan sentir bien."
    },
    "¿Cómo tomas decisiones importantes?": {
        "Analítico": "Analizo todos los datos antes de decidir.",
        "Creativo": "Pienso en soluciones innovadoras.",
        "Pragmático": "Tomo decisiones rápidas y eficaces.",
        "Emocional": "Dejo que mis emociones me guíen."
    },
    "¿Qué prefieres en un proyecto de grupo?": {
        "Analítico": "Organizar y dividir las tareas por lógica.",
        "Creativo": "Aportar ideas nuevas y creativas.",
        "Pragmático": "Asegurar que el proyecto se mantenga en el camino correcto.",
        "Emocional": "Motivarme a través de las emociones del equipo."
    },
    "¿Cómo reaccionas cuando algo no sale según lo planeado?": {
        "Analítico": "Reevalúo el problema y busco una solución lógica.",
        "Creativo": "Pienso en alternativas fuera de lo común.",
        "Pragmático": "Busco la forma más práctica de corregirlo.",
        "Emocional": "Me dejo llevar por la frustración o tristeza pero luego encuentro una forma de avanzar."
    },
    "¿Qué prefieres en un ambiente laboral?": {
        "Analítico": "Tener claro qué hacer y cómo hacerlo.",
        "Creativo": "Espacio para innovar y explorar nuevas ideas.",
        "Pragmático": "Procesos organizados y eficientes.",
        "Emocional": "Un ambiente en el que se valoren los sentimientos y la colaboración."
    },
    "¿Cómo manejas el fracaso?": {
        "Analítico": "Lo analizo para aprender de los errores.",
        "Creativo": "Lo uso como inspiración para pensar de manera diferente.",
        "Pragmático": "Acepto el fracaso y busco la manera de corregirlo rápidamente.",
        "Emocional": "Me afecta emocionalmente, pero lo uso como motivación para mejorar."
    }
}

#Print the questions and answers to the user and save the answers
answers_user = []

# Lista de letras válidas
letter_index = ["A", "B", "C", "D"]

def ask_answer() -> str:
    # Bucle para pedir opciones al usuario
    while True:
        # Solicita la entrada del usuario
        option = input("Introduce una opción (A, B, C, D): ").upper()

        # Comprueba si la opción es válida
        if option in letter_index:
            # Devuelve la opción válida
            return option
        else:
            # Si la opción no es válida, muestra un mensaje y repite el bucle
            print("Opción inválida. Inténtalo de nuevo.")

for index, (question, answers) in enumerate(questions_answers.items()):
    print(f"{index + 1}. {question}")
    for index, (_, answer) in enumerate(answers.items()):
        print(f"  - {letter_index[index]}: {answer}")
    answers_user.append(ask_answer())

#Count answers
count ={
    "Analítico": 0,
    "Creativo": 0,
    "Pragmático": 0, 
    "Emocional": 0    
}

#Mapping the answers a, b, c, d to the personality types
count_mapping = {
    "A": "Analítico",
    "B": "Creativo",
    "C": "Pragmático",
    "D": "Emocional"
}

for answer in answers_user:
    count[count_mapping[answer]] += 1

#Check if there is a tie
max_value = max(count.values())
if list(count.values()).count(max_value) > 1:
    print("La decisión ha sido complicada, pero...")
else:
    print("El sombrero seleccionador ha decidido que...")
print("Tu casa es:")
print(max(count, key=count.get))

    




