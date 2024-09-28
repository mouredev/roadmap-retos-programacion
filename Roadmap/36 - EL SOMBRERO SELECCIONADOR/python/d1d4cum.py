import sys, random
from typing import List


class Question:
    question: str
    answers: List[str]

    def __init__(self, question, answers) -> None:
        self.question = question
        self.answers = answers


questions = [
    Question(
        "¿Qué tipo de proyecto te interesa más desarrollar?",
        [
            "Crear una interfaz web atractiva y funcional",
            "Diseñar una API robusta que gestione la lógica del negocio",
            "Desarrollar una aplicación nativa para smartphones",
            "Analizar grandes volúmenes de datos para extraer información útil"
        ]
    ),
    Question(
        "¿Qué herramienta o lenguaje prefieres usar para trabajar?",
        [
            "HTML, CSS, o JavaScript",
            "Node.js, Java, o Python para el lado del servidor",
            "Swift o Kotlin para aplicaciones móviles",
            "SQL, Python (con Pandas), o R para análisis de datos"
        ]
    ),
    Question(
        "¿Qué te parece más interesante en tu día a día como desarrollador?",
        [
            "Mejorar la experiencia de usuario a través de interfaces intuitivas",
            "Optimizar la lógica del servidor y la eficiencia de las consultas",
            "Aprovechar las capacidades nativas de los dispositivos móviles",
            "Aplicar técnicas de machine learning para obtener predicciones y patrones"
        ]
    ),
    Question(
        "¿Qué problema preferirías resolver?",
        [
            "Un diseño web que se ve bien en todas las resoluciones de pantalla",
            "La creación de una arquitectura eficiente para gestionar múltiples usuarios y peticiones",
            "Conseguir que una aplicación funcione sin problemas tanto en iOS como en Android",
            "Limpiar y procesar grandes conjuntos de datos para hacerlos útiles"
        ]
    ),
    Question(
        "¿Qué tipo de testeo prefieres realizar?",
        [
            "Comprobar que la interfaz es accesible y responsiva",
            "Asegurarte de que las consultas a la base de datos son rápidas y precisas",
            "Testear cómo una app responde en diferentes versiones de sistemas operativos móviles",
            "Validar la precisión de un modelo predictivo en un conjunto de datos"
        ]
    ),
    Question(
        "¿En qué te gustaría especializarte?",
        [
            "Desarrollo de interfaces gráficas y usabilidad",
            "En la arquitectura de servidores y bases de datos",
            "Programación de aplicaciones nativas que utilicen recursos del dispositivo",
            "Análisis de datos, ciencia de datos, o inteligencia artificial"
        ]
    ),
    Question(
        "¿Qué te gustaría automatizar más en tu trabajo?",
        [
            "La generación de componentes reutilizables en una interfaz",
            "La ejecución de procesos en segundo plano que optimicen el rendimiento del servidor",
            "La sincronización de datos entre una app móvil y el servidor",
            "La limpieza, procesamiento y visualización de datos de forma eficiente"
        ]
    ),
    Question(
        "¿Cómo prefieres desplegar tus proyectos?",
        [
            "Configurando un CDN para entregar rápidamente archivos estáticos",
            "Desplegando un servicio web con balanceadores de carga y escalabilidad automática",
            "Publicando una aplicación en las tiendas de iOS y Android",
            "Implementando pipelines de datos para el procesamiento en tiempo real o batch"
        ]
    ),
    Question(
        "¿Qué tipo de herramientas disfrutas más usar?",
        [
            "Herramientas como React, Vue o Angular",
            "Frameworks como Django, Express o Spring",
            "IDEs como Xcode o Android Studio",
            "Herramientas de análisis de datos como Jupyter Notebook, Hadoop o Power BI"
        ]
    ),
    Question(
        "¿Qué retos técnicos prefieres enfrentar?",
        [
            "Hacer que una página web se vea increíble en diferentes navegadores",
            "Manejar eficientemente grandes volúmenes de tráfico y asegurar integridad en las transacciones",
            "Garantizar que una app aproveche bien los recursos del teléfono sin consumir demasiada batería",
            "Trabajar con datos faltantes o inconsistentes para obtener insights valiosos"
        ]
    )
]


def main():
    frontend = 0
    backend = 0
    mobile = 0
    data = 0

    for question in questions:
        print(f"\n{question.question}")
        print(f"1. {question.answers[0]}")
        print(f"2. {question.answers[1]}")
        print(f"3. {question.answers[2]}")
        print(f"4. {question.answers[3]}")

        choice = input("> ")

        match choice:
            case "1":
                frontend += 1
            case "2":
                backend += 1
            case "3":
                mobile += 1
            case "4":
                data += 1
            case _:
                print("\n⚠️ Opción no válida")
                print("Prueba finalizada con error")
                sys.exit(1)

    results = {'frontend': frontend, 'backend': backend, 'mobile': mobile, 'data': data}
    max_value = max(results.values())
    max_keys = [k for k, v in results.items() if v == max_value]
    selected_key = random.choice(max_keys)

    print(f"\nPerteneces a la casa {selected_key}")

if __name__ == '__main__':
    main()
