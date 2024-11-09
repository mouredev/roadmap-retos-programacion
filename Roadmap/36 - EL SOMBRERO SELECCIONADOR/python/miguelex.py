import random

class Casa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntos = 0

    def get_nombre(self):
        return self.nombre

    def agregar_puntos(self, puntos):
        self.puntos += puntos

    def get_puntos(self):
        return self.puntos

class Alumno:
    def __init__(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

class Pregunta:
    def __init__(self, pregunta, opciones):
        self.pregunta = pregunta
        self.opciones = opciones

    def mostrar_pregunta(self):
        print(self.pregunta)
        for idx, opcion in enumerate(self.opciones):
            print(f"{idx + 1}: {opcion['texto']}")

    def obtener_casa_segun_respuesta(self, respuesta):
        return self.opciones[respuesta - 1]['casa']

class SombreroSeleccionador:
    def __init__(self, casas, preguntas):
        self.casas = casas
        self.preguntas = preguntas

    def asignar_casa(self, alumno):
        preguntas_seleccionadas = self.seleccionar_preguntas()
        for pregunta in preguntas_seleccionadas:
            pregunta.mostrar_pregunta()
            respuesta = self.leer_respuesta()
            casa = pregunta.obtener_casa_segun_respuesta(respuesta)
            self.casas[casa].agregar_puntos(1)

        self.mostrar_resultado(alumno)

    def seleccionar_preguntas(self):
        preguntas_seleccionadas = []
        indices_seleccionados = set()

        while len(preguntas_seleccionadas) < 10:
            indice = random.randint(0, len(self.preguntas) - 1)
            if indice not in indices_seleccionados:
                indices_seleccionados.add(indice)
                preguntas_seleccionadas.append(self.preguntas[indice])

        return preguntas_seleccionadas

    def leer_respuesta(self):
        while True:
            try:
                respuesta = int(input("Selecciona una opción (1-4): "))
                if 1 <= respuesta <= 4:
                    return respuesta
                else:
                    print("Por favor, elige un número entre 1 y 4.")
            except ValueError:
                print("Por favor, introduce un número válido.")

    def mostrar_resultado(self, alumno):
        casas_ordenadas = sorted(self.casas.values(), key=lambda casa: casa.get_puntos(), reverse=True)

        max_puntos = casas_ordenadas[0].get_puntos()
        ganadoras = [casa for casa in casas_ordenadas if casa.get_puntos() == max_puntos]

        if len(ganadoras) > 1:
            print("\n\nLa decisión fue difícil...")
            ganadora = random.choice(ganadoras)
        else:
            ganadora = ganadoras[0]

        print(f"\n\n{alumno.get_nombre()}, el sombrero seleccionador te ha asignado a la casa {ganadora.get_nombre().upper()}!!!!\n")


# Definir las casas
casas = {
    'frontend': Casa('Frontend'),
    'backend': Casa('Backend'),
    'mobile': Casa('Mobile'),
    'data': Casa('Data')
}

# Definir las preguntas
preguntas = [
    Pregunta("¿Qué prefieres?", [
        {'texto': 'Diseñar interfaces', 'casa': 'frontend'},
        {'texto': 'Crear APIs', 'casa': 'backend'},
        {'texto': 'Desarrollar apps móviles', 'casa': 'mobile'},
        {'texto': 'Analizar datos', 'casa': 'data'}
    ]),
    Pregunta("¿Cuál es tu lenguaje de programación favorito?", [
        {'texto': 'JavaScript', 'casa': 'frontend'},
        {'texto': 'Python', 'casa': 'backend'},
        {'texto': 'Kotlin', 'casa': 'mobile'},
        {'texto': 'R', 'casa': 'data'}
    ]),
    Pregunta("¿Qué herramienta utilizas más a menudo?", [
        {'texto': 'Figma o Sketch', 'casa': 'frontend'},
        {'texto': 'Docker o Kubernetes', 'casa': 'backend'},
        {'texto': 'Android Studio o Xcode', 'casa': 'mobile'},
        {'texto': 'Jupyter Notebooks o Excel', 'casa': 'data'}
    ]),
    Pregunta("¿Qué te interesa más aprender?", [
        { 'texto': 'HTML/CSS y JavaScript avanzado', 'casa': 'frontend' },
        { 'texto': 'Patrones de diseño y arquitectura de software', 'casa': 'backend' },
        { 'texto': 'Programación nativa para dispositivos móviles', 'casa': 'mobile' },
        { 'texto': 'Estadística y Machine Learning', 'casa': 'data' }
    ]),
    Pregunta("¿Qué tipo de proyecto te gustaría liderar?", [
        { 'texto': 'Un sitio web interactivo y atractivo', 'casa': 'frontend' },
        { 'texto': 'Una plataforma escalable con microservicios', 'casa': 'backend' },
        { 'texto': 'Una app móvil innovadora', 'casa': 'mobile' },
        { 'texto': 'Un sistema de recomendación basado en datos', 'casa': 'data' }
    ]),
    Pregunta("¿Qué es lo más importante para ti en un proyecto?", [
        { 'texto': 'La experiencia de usuario', 'casa': 'frontend' },
        { 'texto': 'El rendimiento y la escalabilidad', 'casa': 'backend' },
        { 'texto': 'La adaptabilidad a diferentes dispositivos', 'casa': 'mobile' },
        { 'texto': 'La precisión de los análisis', 'casa': 'data' }
    ]),
    Pregunta("¿Qué prefieres trabajar?", [
        {'texto' : 'En un entorno donde el diseño visual es clave', 'casa' :'frontend'},
        {'texto' : 'En la lógica del negocio y la arquitectura', 'casa' :'backend'},
        {'texto' : 'En apps móviles con buen rendimiento', 'casa' :'mobile'},
        {'texto' : 'En el análisis y visualización de datos', 'casa' :'data'}
    ]),
    Pregunta("¿Qué framework te parece más interesante?", [
        {'texto' : 'React o Angular', 'casa' :'frontend'},
        {'texto' : 'Spring o Django', 'casa' :'backend'},
        {'texto' : 'Flutter o React Native', 'casa' :'mobile'},
        {'texto' : 'TensorFlow o Pandas', 'casa' :'data'}
    ]),
    Pregunta("¿Qué tipo de reto disfrutas más?", [
        {'texto' : 'Hacer que un sitio web sea accesible y rápido', 'casa' :'frontend'},
        {'texto' : 'Optimizar la comunicación entre servicios', 'casa' :'backend'},
        {'texto' : 'Mejorar la experiencia del usuario en móviles', 'casa' :'mobile'},
        {'texto' : 'Encontrar patrones ocultos en los datos', 'casa' :'data'}
    ]),
    Pregunta("¿Qué prefieres resolver?", [
        {'texto' : 'Problemas de diseño y maquetación', 'casa' :'frontend'},
        {'texto' : 'Problemas de concurrencia y escalabilidad', 'casa' :'backend'},
        {'texto' : 'Problemas de rendimiento en aplicaciones móviles', 'casa' :'mobile'},
        {'texto' : 'Problemas de predicción y análisis de datos', 'casa' :'data'}
    ]),
    Pregunta("¿Qué es lo que más te emociona en tecnología?", [
        {'texto' : 'La evolución de las interfaces de usuario', 'casa' :'frontend'},
        {'texto' : 'La innovación en la arquitectura de software', 'casa' :'backend'},
        {'texto' : 'Las nuevas capacidades de los dispositivos móviles', 'casa' :'mobile'},
        {'texto' : 'Los avances en inteligencia artificial y análisis de datos', 'casa' : 'data'}
    ]),
    Pregunta("¿Qué te gusta hacer en tu tiempo libre?", [
        {'texto' : 'Diseñar sitios web personales o interfaces', 'casa': 'frontend'},
        {'texto' : 'Hacer proyectos con servidores y APIs', 'casa': 'backend'},
        {'texto' : 'Crear apps móviles para resolver problemas cotidianos', 'casa': 'mobile'},
        {'texto' : 'Hacer análisis de datos para tomar decisiones mejor informadas', 'casa': 'data'}
    ]),
    Pregunta("¿Qué te gustaría dominar?", [
        {'texto' : 'Animaciones y transiciones en la web', 'casa': 'frontend'},
        {'texto' : 'Arquitectura de microservicios', 'casa': 'backend'},
        {'texto' : 'Optimización de aplicaciones móviles', 'casa': 'mobile'},
        {'texto' : 'Modelos predictivos y análisis de datos', 'casa': 'data'}
    ]),
    Pregunta("¿Qué tipo de problema prefieres resolver en un hackathon?", [
        {'texto' : 'Mejorar la interfaz de usuario de una aplicación', 'casa': 'frontend'},
        {'texto' : 'Optimizar el rendimiento de una API', 'casa': 'backend'},
        {'texto' : 'Crear una aplicación móvil desde cero', 'casa': 'mobile'},
        {'texto' : 'Generar insights a partir de grandes conjuntos de datos', 'casa': 'data'}
    ]),
    Pregunta("¿Qué prefieres al trabajar en equipo?", [
        {'texto' : 'Encargarte de la parte visual y de interacción del usuario', 'casa': 'frontend'},
        {'texto' : 'Asegurarte de que la lógica y los datos fluyan correctamente', 'casa': 'backend'},
        {'texto' : 'Hacer que la app funcione bien en diferentes dispositivos', 'casa': 'mobile'},
        {'texto' : 'Proveer métricas y análisis para tomar mejores decisiones', 'casa': 'data'}
    ]),
    Pregunta("¿Cuál es tu prioridad al optimizar código?", [
        {'texto' : 'Que la interfaz cargue rápido y sea amigable', 'casa': 'frontend'},
        {'texto' : 'Que los servicios backend sean escalables y eficientes', 'casa': 'backend'},
        {'texto' : 'Que la app móvil consuma pocos recursos y sea fluida', 'casa': 'mobile'},
        {'texto' : 'Que el procesamiento de datos sea rápido y preciso', 'casa': 'data'}
    ]),
    Pregunta("¿Qué prefieres al probar una aplicación?", [
        {'texto' : 'Verificar que el diseño y la usabilidad sean impecables', 'casa': 'frontend'},
        {'texto' : 'Asegurar que las funcionalidades y la lógica sean correctas', 'casa' :'backend'},
        {'texto' : 'Revisar que la app funcione correctamente en múltiples dispositivos', 'casa' : 'mobile'},
        {'texto' : 'Validar que los resultados de los análisis sean exactos', 'casa' : 'data'}
    ]),
    Pregunta("¿Qué tipo de proyectos sigues en la industria?", [
        {'texto' : 'Proyectos de diseño web innovador y UX', 'casa' : 'frontend'},
        {'texto' : 'Nuevas tecnologías de servidores y backends', 'casa' : 'backend'},
        {'texto' : 'Aplicaciones móviles disruptivas y eficientes', 'casa' : 'mobile'},
        {'texto' : 'Proyectos de inteligencia artificial y ciencia de datos', 'casa' : 'data'}
    ]),
    Pregunta("¿Qué harías para mejorar una plataforma existente?", [
        {'texto' : 'Mejorar la apariencia y usabilidad de la interfaz', 'casa' : 'frontend'},
        {'texto' : 'Optimizar el rendimiento de las consultas y los servidores', 'casa' : 'backend'},
        {'texto' : 'Hacer que la plataforma sea accesible desde dispositivos móviles', 'casa' : 'mobile'},
        {'texto' : 'Incluir más análisis de datos para obtener mejor información', 'casa' : 'data'}
    ]),
    Pregunta("¿Qué aspecto del desarrollo de software te parece más retador?", [
        {'texto' : 'Hacer que una aplicación web sea visualmente atractiva', 'casa' : 'frontend'},
        {'texto' : 'Crear sistemas backend que manejen millones de usuarios', 'casa' : 'backend'},
        {'texto' : 'Optimizar la app móvil para diferentes sistemas operativos', 'casa' : 'mobile'},
        {'texto' : 'Gestionar grandes volúmenes de datos y extraer conclusiones útiles', 'casa' : 'data'}
    ]),
]

# Solicitar nombre del alumno
nombre_alumno = input("Por favor, introduce tu nombre: ")
alumno = Alumno(nombre_alumno)

# Crear instancia del sombrero seleccionador y asignar casa
sombrero = SombreroSeleccionador(casas, preguntas)
sombrero.asignar_casa(alumno)
