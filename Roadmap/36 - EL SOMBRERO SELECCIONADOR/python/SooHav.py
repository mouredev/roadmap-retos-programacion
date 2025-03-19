# 36 EL SOMBRERO SELECCIONADOR

def menu():
    while True:
        print("\nMenú:")
        print("1. Responder preguntas del sombrero")
        print("2. Calcular puntos")
        print("3. Asignar casa")
        print("4. Salir")
        opcion = input("Ingrese una opción: ")
        try:
            return int(opcion)
        except ValueError:
            print("Opción inválida. Por favor, ingrese un número entero.")


lista_preguntas = {
    "1. ¿Qué es una base de datos NoSQL y cuándo es preferible utilizarla en lugar de una base de datos relacional?": {
        "a": {"respuesta": "Una base de datos NoSQL es un sistema de gestión de bases de datos que no se basa en el modelo relacional tradicional de tablas, filas y columnas.", "puntaje": 10, "habilidad": "Data"},
        "b": {"respuesta": "Las bases de datos NoSQL son ideales para aplicaciones que requieren almacenar grandes cantidades de datos con alta disponibilidad y baja latencia.", "puntaje": 10, "habilidad": "Backend"},
        "c": {"respuesta": "Las bases de datos NoSQL ofrecen una variedad de modelos de datos, como documentos, clave-valor, gráficos y columnas, lo que permite elegir el modelo más adecuado para cada tipo de aplicación.", "puntaje": 10, "habilidad": "Data"},
        "d": {"respuesta": "Las bases de datos NoSQL son más lentas y menos eficientes que las bases de datos relacionales.", "puntaje": -5, "habilidad": None}
    },
    "2. ¿Por qué es importante utilizar un sistema de control de versiones como Git?": {
        "a": {"respuesta": "Git permite realizar un seguimiento de los cambios en el código a lo largo del tiempo.", "puntaje": 5, "habilidad": "Backend"},
        "b": {"respuesta": "Git facilita la colaboración entre desarrolladores y permite revertir cambios si es necesario.", "puntaje": 10, "habilidad": "Backend"},
        "c": {"respuesta": "Git solo se utiliza para almacenar código fuente.", "puntaje": -5, "habilidad": None},
        "d": {"respuesta": "Git permite resolver conflictos de manera eficiente cuando varios desarrolladores modifican el mismo archivo al mismo tiempo.", "puntaje": 10, "habilidad": "Backend"}
    },
    "3. ¿Qué herramientas y plataformas se utilizan para el despliegue de aplicaciones web y móviles?": {
        "a": {"respuesta": "Docker, Kubernetes.", "puntaje": 10, "habilidad": "Backend"},
        "b": {"respuesta": "AWS, Azure, GCP.", "puntaje": 10, "habilidad": "Backend"},
        "c": {"respuesta": "Flutter, React Native.", "puntaje": 10, "habilidad": "Mobile"},
        "d": {"respuesta": "VSCode.", "puntaje": -25, "habilidad": None}
    },
    "4. ¿Cuáles son las operaciones más frecuentes que se realizan con Git?": {
        "a": {"respuesta": "Clonar.", "puntaje": 5, "habilidad": "Backend"},
        "b": {"respuesta": "Commit.", "puntaje": 5, "habilidad": "Backend"},
        "c": {"respuesta": "Push y Pull.", "puntaje": 10, "habilidad": "Backend"},
        "d": {"respuesta": "Rebase.", "puntaje": -5, "habilidad": None}
    },
    "5. ¿Cuáles son las ventajas de utilizar la nube?": {
        "a": {"respuesta": "Escalabilidad.", "puntaje": 10, "habilidad": "Data"},
        "b": {"respuesta": "Flexibilidad.", "puntaje": 10, "habilidad": "Backend"},
        "c": {"respuesta": "Reducción de costos.", "puntaje": 10, "habilidad": "Data"},
        "d": {"respuesta": "Menor seguridad.", "puntaje": -15, "habilidad": None}
    },
    "6. ¿Cuáles son los diferentes tipos de pruebas que se pueden realizar en un software?": {
        "a": {"respuesta": "Las pruebas unitarias verifican el funcionamiento correcto de unidades individuales de código.", "puntaje": 10, "habilidad": "Backend"},
        "b": {"respuesta": "Las pruebas de integración aseguran que los diferentes componentes de la aplicación interactúen correctamente.", "puntaje": 10, "habilidad": "Backend"},
        "c": {"respuesta": "Las pruebas de aceptación validan que el software cumpla con los requisitos del usuario.", "puntaje": 10, "habilidad": "Frontend"},
        "d": {"respuesta": "Las pruebas manuales permiten detectar errores que las pruebas automatizadas no pueden encontrar.", "puntaje": -5, "habilidad": None}
    },
    "7. ¿Cuáles son las principales diferencias entre HTML, CSS y JavaScript?": {
        "a": {"respuesta": "HTML estructura el contenido de una página web, CSS define su estilo y apariencia, y JavaScript agrega interactividad y dinamismo.", "puntaje": 10, "habilidad": "Frontend"},
        "b": {"respuesta": "HTML, CSS y JavaScript son sinónimos y se utilizan indistintamente para crear páginas web.", "puntaje": -5, "habilidad": None},
        "c": {"respuesta": "HTML es el esqueleto, CSS la piel y JavaScript el cerebro de una página web.", "puntaje": 10, "habilidad": "Frontend"},
        "d": {"respuesta": "JavaScript puede modificar el DOM (Document Object Model) creado por HTML y CSS para cambiar el contenido y el estilo de una página en tiempo real.", "puntaje": 10, "habilidad": "Frontend"}
    },
    "8. ¿Qué es un API y cuál es su función en una aplicación?": {
        "a": {"respuesta": "Un API (Interfaz de Programación de Aplicaciones) es un conjunto de reglas y especificaciones que permiten que diferentes aplicaciones se comuniquen entre sí.", "puntaje": 10, "habilidad": "Backend"},
        "b": {"respuesta": "En una aplicación web, el frontend utiliza un API para solicitar datos al backend y mostrarlos al usuario.", "puntaje": 10, "habilidad": "Frontend"},
        "c": {"respuesta": "Un API es un lenguaje de programación utilizado para crear aplicaciones web.", "puntaje": -15, "habilidad": None},
        "d": {"respuesta": "Las APIs permiten que diferentes aplicaciones se integren y compartan datos.", "puntaje": 10, "habilidad": "Backend"}
    },
    "9. ¿Cuáles son los principales métodos HTTP?": {
        "a": {"respuesta": "GET se utiliza para obtener datos.", "puntaje": 10, "habilidad": "Frontend"},
        "b": {"respuesta": "POST para crear nuevos recursos.", "puntaje": 10, "habilidad": "Backend"},
        "c": {"respuesta": "PUT para actualizar recursos existentes.", "puntaje": 10, "habilidad": "Backend"},
        "d": {"respuesta": "DELETE para eliminar recursos.", "puntaje": 10, "habilidad": "Backend"}
    },
    "10. ¿Cuál de las siguientes afirmaciones sobre el DOM (Document Object Model) es CORRECTA?": {
        "a": {"respuesta": "El DOM es una estructura jerárquica que representa los elementos de una página web como objetos.", "puntaje": 10, "habilidad": "Frontend"},
        "b": {"respuesta": "JavaScript es el lenguaje principal para manipular el DOM y crear interfaces interactivas.", "puntaje": 10, "habilidad": "Frontend"},
        "c": {"respuesta": "El DOM es estatico y no se actualiza constantemente.", "puntaje": -10, "habilidad": None},
        "d": {"respuesta": "JavaScript puede crear, modificar y eliminar elementos del DOM.", "puntaje": 10, "habilidad": "Frontend"}
    }
}

resultados = []
puntaje_total = 0
alumno = ""

while True:
    opcion = menu()

    if opcion == 1:
        if not alumno:
            alumno = input(
                "Si quieres saber tu casa, ingresa tu nombre: ").lower()
            print(f"Soy el sombrero seleccionador! {
                  alumno}, necesito que respondas algunas preguntas!\n")

        # Mostrar preguntas
        if not resultados:
            for pregunta, respuestas in lista_preguntas.items():
                print(pregunta)
                for letra, detalles in respuestas.items():
                    print(f"{letra}) {detalles['respuesta']}")
                print()

                puntos = input(f"Ingrese su respuesta para '{
                               pregunta}' (a, b, c o d): ")
                print()
                if puntos in respuestas:
                    puntaje = respuestas[puntos]["puntaje"]
                    resultados.append(puntaje)
                else:
                    print("Respuesta no válida, intenta nuevamente.")

        else:
            print("Ya has respondido las preguntas. Pasa a la opción 2 para calcular tus puntos o la opción 3 para asignar casa.\n")

    elif opcion == 2:
        if resultados:
            puntaje_total = sum(resultados)
            print(f"¡Excelente, {alumno}! Tu puntaje total es: {
                  puntaje_total}")
        else:
            print("Primero responde las preguntas en la opción 1.\n")

    elif opcion == 3:
        if puntaje_total:
            if puntaje_total > 90:
                print(f"{alumno}, te he asignado a la casa Mobile.")
            elif 70 < puntaje_total <= 90:
                print(f"{alumno}, te he asignado a la casa Backend.")
            elif 60 < puntaje_total <= 70:
                print(f"{alumno}, te he asignado a la casa Frontend.")
            else:
                print(f"{alumno}, te he asignado a la casa Data.")
        else:
            print("Primero calcula tu puntaje en la opción 2.\n")

        if puntaje_total:
            if 85 < puntaje_total < 95 or 65 < puntaje_total < 75 or 55 < puntaje_total < 65:
                print(f"La decisión fue muy difición de tomar!")

    elif opcion == 4:
        print("¡Hasta el próximo año!")
        break
    else:
        print("Opción no válida. Intenta nuevamente.")
