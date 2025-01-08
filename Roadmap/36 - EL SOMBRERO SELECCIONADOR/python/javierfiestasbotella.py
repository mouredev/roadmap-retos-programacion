'''* EJERCICIO:
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
 */'''
Frontend = 0
Backend = 0
Mobile = 0
Data = 0

def puntaje(n):
    global Frontend
    global Backend
    global Mobile
    global Data
    if n == 1:
        Frontend += 3
        Backend += 1
        Mobile += 2
        Data += 0
    elif n == 2:
        Frontend += 1
        Backend += 3
        Mobile += 0
        Data += 2
    elif n == 3:
        Frontend += 1
        Backend += 0
        Mobile += 3
        Data += 1
    elif n == 4:
        Frontend += 0
        Backend += 2
        Mobile += 0
        Data += 3
    else:
        print("Respuesta no válida, por favor elige una opción entre 1 y 4.")

if __name__ == "__main__":
    name = input('Introduce tu nombre: ')
    print(f'{name}, voy a realizarte 10 preguntas para asignarte un perfil de desarrollador.')

    preguntas = [
        '''¿Cuál es tu principal motivación al desarrollar?
        1) Crear interfaces visuales atractivas.
        2) Optimizar la lógica de procesamiento.
        3) Hacer que la aplicación funcione de manera fluida en dispositivos móviles.
        4) Analizar grandes volúmenes de datos para extraer información útil.''',
        
        '''¿Qué lenguaje te gusta usar más?
        1) JavaScript o TypeScript.
        2) Python o Java.
        3) Swift o Kotlin.
        4) R o SQL.''',

        '''¿Qué herramienta usas con más frecuencia?
        1) Frameworks como React o Angular.
        2) Servidores y bases de datos como Node.js o PostgreSQL.
        3) IDEs para desarrollo móvil como Android Studio o Xcode.
        4) Herramientas de análisis de datos como Pandas o TensorFlow.''',

        '''¿Qué disfrutas más de tu trabajo?
        1) Crear experiencias de usuario.
        2) Gestionar y procesar datos en servidores.
        3) Desarrollar aplicaciones móviles que funcionen bien en diferentes dispositivos.
        4) Resolver problemas usando análisis de datos.''',

        '''¿Qué tipo de bugs disfrutas resolviendo?
        1) Errores en el diseño o comportamiento de la interfaz.
        2) Fallos en la lógica del servidor o base de datos.
        3) Problemas de compatibilidad entre dispositivos.
        4) Inconsistencias en los modelos de datos o análisis.''',

        '''¿Cómo prefieres abordar la resolución de un problema?
        1) Pensando en cómo afectará la experiencia del usuario.
        2) Optimizando los procesos en el backend para mayor eficiencia.
        3) Asegurando que la solución funcione en cualquier dispositivo móvil.
        4) Aplicando algoritmos de análisis de datos.''',

        '''¿Qué tipo de proyecto te resulta más interesante?
        1) Un sitio web interactivo y visualmente impresionante.
        2) Una API robusta y escalable.
        3) Una aplicación móvil innovadora.
        4) Un sistema de análisis de grandes datos para insights de negocio.''',

        '''¿Con qué tipo de tecnologías te sientes más cómodo?
        1) HTML, CSS, JavaScript.
        2) Node.js, Django, Ruby on Rails.
        3) Flutter, React Native.
        4) Spark, Hadoop.''',

        '''¿Qué prefieres hacer en tu tiempo libre?
        1) Jugar con diseños y CSS para hacer una web más bonita.
        2) Crear una API que haga un proceso más eficiente.
        3) Probar nuevas aplicaciones móviles y crear las tuyas.
        4) Trabajar con grandes conjuntos de datos.''',

        '''¿Cuál consideras tu principal fortaleza?
        1) Cuidar la experiencia y diseño visual del usuario.
        2) Crear procesos eficientes y escalables.
        3) Adaptar aplicaciones móviles para múltiples dispositivos.
        4) Interpretar y analizar datos complejos.'''
    ]

    for pregunta in preguntas:
        while True:
            try:
                p = int(input(pregunta + '\n'))
                if p >= 1 and p <= 4:
                    puntaje(p)
                    break
                else:
                    print("Por favor, elige una opción válida entre 1 y 4.")
            except ValueError:
                print("Por favor, introduce un número válido.")

    dic = {'Frontend': Frontend, 'Backend': Backend, 'Mobile': Mobile, 'Data': Data}
    
    casa = max(dic, key=dic.get)

    print(f'{name}, La casa que le ha sido otorgada es: {casa}')
