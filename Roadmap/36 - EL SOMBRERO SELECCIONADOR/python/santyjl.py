# #36 EL SOMBRERO SELECCIONADOR
#### Dificultad: Fácil | Publicación: 02/09/24 | Corrección: 09/09/24


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

# Variables globales
front_end = 0
back_end = 0
mobile = 0
data = 0


Preguntas = [
    "¿Qué tipo de trabajo disfrutas más?",
    "¿Qué tipo de herramientas prefieres usar en tu día a día?",
    "¿Qué lenguaje de programación te llama más la atención?",
    "¿Qué prefieres al resolver problemas?",
    "¿Qué consideras más importante en un proyecto?",
    "¿Qué tipo de desafíos te motivan más?",
    "¿Cómo te sientes al trabajar con interfaces visuales?",
    "¿Qué tipo de datos prefieres manejar?",
    "¿Cómo te ves trabajando en equipo?",
    "¿Qué te interesa más del mundo de la tecnología?"
]

respuestas = [
    ["Crear interfaces amigables para usuarios (UI/UX)",
     "Diseñar sistemas robustos y funcionales",
     "Crear aplicaciones móviles innovadoras",
     "Trabajar con grandes volúmenes de datos"],

    ["Editores de diseño visual",
     "Herramientas de línea de comandos y servidores",
     "Simuladores y entornos móviles",
     "Herramientas de análisis de datos y gráficas"],

    ["JavaScript o TypeScript",
     "Python o Java",
     "Swift o Kotlin",
     "SQL o R"],

    ["Soluciones que mejoren la experiencia del usuario",
     "Implementar lógica compleja",
     "Optimizar rendimiento en dispositivos móviles",
     "Encontrar patrones en datos"],

    ["La facilidad de uso",
     "La estabilidad y escalabilidad",
     "El diseño innovador",
     "La precisión y análisis"],

    ["Construir algo visualmente impactante",
     "Resolver problemas técnicos complejos",
     "Hacer que una app funcione en todos los dispositivos",
     "Desentrañar información útil de datos"],

    ["Me emociona crear interfaces atractivas",
     "Prefiero trabajar con la lógica detrás de la interfaz",
     "Me gusta la fluidez y simplicidad en móviles",
     "Quiero analizar datos para tomar decisiones"],

    ["Estructurados y bien organizados",
     "Cualquier tipo, siempre que el sistema sea funcional",
     "Fáciles de consumir y eficientes",
     "Datos masivos y complejos"],

    ["Colaborando activamente y compartiendo ideas",
     "Contribuyendo a construir sistemas sólidos",
     "Asegurando la calidad en diferentes plataformas",
     "Proporcionando insights claros a partir de los datos"],

    ["El diseño y la experiencia de usuario",
     "El backend y la infraestructura",
     "La movilidad y accesibilidad",
     "El impacto de los datos en la toma de decisiones"]
]

def dar_puntos(valor: int):
    """Asigna puntos a las casas dependiendo del valor."""
    global front_end, back_end, mobile, data  # Usamos variables globales para modificarlas
    match valor:
        case 1:
            front_end += 1
        case 2:
            back_end += 1
        case 3:
            mobile += 1
        case 4:
            data += 1

def main():
    global front_end, back_end, mobile, data  # Aseguramos modificar las globales
    print("Buenas futuro desarrollador, te vamos a hacer unas preguntas para ver en qué casa te quedas:")

    for i in range(len(Preguntas)):
        print(f"\n{Preguntas[i]}")  # Pregunta actual
        for j in range(4):
            print(f"{j + 1}. {respuestas[i][j]}")  # Mostramos opciones empezando en 1

        while True:  # Ciclo para garantizar una entrada válida
            try:
                respuesta = int(input("Introduce la respuesta de acuerdo al índice (1-4): "))
                if 1 <= respuesta <= 4:  # Verificamos que esté en el rango
                    dar_puntos(respuesta)  # Asignamos puntos
                    break  # Salimos del ciclo si la entrada es válida
                else:
                    print("Por favor, introduce un número entre 1 y 4.")
            except ValueError:
                print("Entrada inválida. Introduce un número entre 1 y 4.")

    # Determinamos la casa final
    print("\nResultados:")
    if front_end > back_end and front_end > mobile and front_end > data:
        print("Tú irás a la casa front_end.")
    elif back_end > front_end and back_end > mobile and back_end > data:
        print("Tú irás a la casa back_end.")
    elif mobile > front_end and mobile > back_end and mobile > data:
        print("Tú irás a la casa mobile.")
    elif data > front_end and data > back_end and data > mobile:
        print("Tú irás a la casa data.")
    else:
        print("Tu eres diferente, tu tienes que ir a la casa full-stack")

# Ejecutamos el programa
main()
