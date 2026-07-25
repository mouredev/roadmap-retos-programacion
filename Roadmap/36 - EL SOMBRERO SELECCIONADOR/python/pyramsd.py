import random

casas = {
    "a":"Fronted",
    "b":"Backend",
    "c":"Mobile",
    "d":"Data"
}

preguntas_y_alternativas = [
    {
        "pregunta":"1. ¿Qué enfoque es clave para garantizar una experiencia de usuario atractiva y funcional?",
        "alternativas":[
            "a) Diseño responsivo ",
            "b) Creación de una API robusta",
            "c) Optimización de la aplicación para múltiples dispositivos",
            "d) Uso eficiente de análisis de datos"
        ]
    },
    {
        "pregunta":"2. ¿Cuál es la prioridad principal al trabajar con seguridad en un proyecto?",
        "alternativas":[
            "a) Sanitizar entradas en formularios",
            "b) Implementar autenticación y control de acceso",
            "c) Garantizar permisos correctos en aplicaciones móviles",
            "d) Cifrar datos sensibles almacenados"
        ]
    },
    {
        "pregunta":"3. ¿Qué se debe considerar al mejorar el rendimiento de un sistema?",
        "alternativas":[
            "a) Minimizar archivos CSS y JavaScript",
            "b) Optimizar consultas a la base de datos",
            "c) Reducir el tamaño de la app para descargas rápidas",
            "d) Procesar grandes volúmenes de datos en paralelo"
        ]
    },
    {
        "pregunta":"4. ¿Cuál sería el mejor enfoque para personalizar la experiencia del usuario?",
        "alternativas":[
            "a) Usar cookies o almacenamiento local para recordar preferencias",
            "b) Crear endpoints específicos para cada usuario",
            "c) Integrar notificaciones push personalizadas",
            "d) Utilizar modelos de recomendación basados en datos"
        ]
    },
    {
        "pregunta":"5. ¿Qué técnica es fundamental para la escalabilidad de un sistema?",
        "alternativas":[
            "a) Usar frameworks modernos para optimizar el DOM",
            "b) Implementar microservicios",
            "c) Escalar la aplicación a diferentes plataformas",
            "d) Aplicar particionamiento en bases de datos"
        ]
    },
    {
        "pregunta":"6. ¿Qué enfoque es esencial para un desarrollo ágil y colaborativo?",
        "alternativas":[
            "a) Uso de componentes reutilizables en UI",
            "b) Configuración de un servidor de desarrollo local",
            "c) Pruebas en múltiples simuladores y dispositivos",
            "d) Versionamiento adecuado de conjuntos de datos"
        ]
    },
    {
        "pregunta":"7. ¿Qué característica mejora la accesibilidad del sistema?",
        "alternativas":[
            "a) Implementar navegación por teclado y lectores de pantalla",
            "b) Generar mensajes de error claros desde el servidor",
            "c) Ajustar el tamaño del texto y elementos táctiles",
            "d) Garantizar datos fácilmente interpretables en visualizaciones"
        ]
    },
    {
        "pregunta":"8. ¿Qué aspecto es crítico al realizar pruebas en el desarrollo?",
        "alternativas":[
            "a) Validar interacciones y animaciones de la interfaz",
            "b) Probar endpoints de la API con datos de prueba",
            "c) Verificar comportamiento en distintas versiones del sistema operativo",
            "d) Evaluar precisión de los modelos predictivos"
        ]
    },
    {
        "pregunta":"9. ¿Cómo manejar eficientemente errores en el sistema?",
        "alternativas":[
            "a) Mostrar mensajes amigables y descriptivos para el usuario",
            "b) Registrar errores en archivos de log centralizados",
            "c) Implementar seguimiento de fallos con herramientas como Crashlytics",
            "d) Detectar valores anómalos en flujos de datos"
        ]
    },
    {
        "pregunta":"10. ¿Qué es importante al trabajar con integraciones de terceros?",
        "alternativas":[
            "a) Implementar SDKs con compatibilidad garantizada",
            "b) Configurar endpoints para servicios externos",
            "c) Gestionar dependencias de bibliotecas móviles",
            "d) Normalizar los datos provenientes de múltiples fuentes"
        ]
    }
]

pnts = {"a":0, "b":0, "c":0, "d":0}

print("\t\t\tBinvenido a la escuela de desarrollo!\
    \n\t\t\t-------------------\
    \nEl sombrero seleccionardor se encargará de seleccionar tu casa de desarrollo\
    \n--------------------------------------------------------------------------")

r_valida = False

while not r_valida:
    try:
        for pregunta in preguntas_y_alternativas:
            print(f'\n{pregunta["pregunta"]}')
            for alternativa in pregunta["alternativas"]:
                print(alternativa)
            r = input("Rpta (a, b, c, d): ").lower()
            if r not in pnts:
                raise ValueError(f"Alternativa no válida: {r}")
            pnts[r] += 1
        r_valida = True
    except ValueError as e:
        print(f"Error: {e}\nIntente de nuevo")

max_pnts = max(pnts.values())
empates = [casa for casa, puntos in pnts.items() if puntos == max_pnts]

if len(empates) > 1:
    print("\nLa decisión fue complicada...")
    casa_final = casas[random.choice(empates)]
else:
    casa_final = casas[empates[0]]

print(f"Eres {casa_final}!")
