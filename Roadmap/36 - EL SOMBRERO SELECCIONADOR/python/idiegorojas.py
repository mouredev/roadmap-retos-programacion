"""
# 36 - Sombrero seleccionador
"""
#  Desarrolla un programa que simule el comportamiento del sombrero.

"""
Requisitos:
"""
#  1. El sombrero realizará 10 preguntas para determinar la casa del alumno.
#  2. Deben existir 4 casas. Por ejemplo: Frontend, Backend, Mobile y Data.
#  (Puedes elegir las que quieras)


""" Acciones: """

#  1. Crea un programa que solicite el nombre del alumno y realice 10 preguntas, con cuatro posibles respuestas cada una.
#  2. Cada respuesta asigna puntos a cada una de las casas (a tu elección).
#  3. Una vez finalizado, el sombrero indica el nombre del alumno y a qué casa pertenecerá (resuelve el posible empate de manera aleatoria, pero indicándole al alumno que la decisión ha sido complicada).

import random


all_questions = {
    "¿Qué valoras más en ti mismo?": {
        "a": "Creatividad y diseño",
        "b": "Lógica y resolución de problemas",
        "c": "Adaptabilidad y portabilidad",
        "d": "Análisis y patrones"
    },
    "¿Qué herramienta te gustaría dominar?": {
        "a": "Figma y librerías de UI",
        "b": "Docker y bases de datos",
        "c": "Flutter o Swift",
        "d": "Python y bibliotecas de análisis"
    },
    "¿Qué tipo de proyecto te emociona más?": {
        "a": "Una interfaz innovadora e intuitiva",
        "b": "Una API robusta y escalable",
        "c": "Una app que funcione en cualquier dispositivo",
        "d": "Un modelo predictivo preciso"
    },
    "¿Cuál es tu mayor fortaleza?": {
        "a": "Atención al detalle visual",
        "b": "Pensamiento estructurado",
        "c": "Adaptabilidad a diferentes entornos",
        "d": "Pensamiento analítico"
    },
    "¿Qué te gusta aprender en tu tiempo libre?": {
        "a": "Tendencias de diseño y experiencia de usuario",
        "b": "Arquitectura de sistemas y patrones",
        "c": "Nuevos frameworks móviles",
        "d": "Técnicas de machine learning"
    },
    "¿Qué problema te gustaría resolver?": {
        "a": "Mejorar la interacción humano-computador",
        "b": "Crear sistemas distribuidos eficientes",
        "c": "Llevar la tecnología a todas partes",
        "d": "Extraer conocimiento de datos complejos"
    },
    "¿Qué tipo de feedback valoras más?": {
        "a": "Sobre la usabilidad y apariencia",
        "b": "Sobre el rendimiento y mantenibilidad",
        "c": "Sobre la experiencia en distintos dispositivos",
        "d": "Sobre la precisión de los resultados"
    },
    "¿Qué habilidad quieres mejorar?": {
        "a": "Diseño de interfaces atractivas",
        "b": "Diseño de arquitectura de software",
        "c": "Optimización para diferentes dispositivos",
        "d": "Modelado estadístico"
    },
    "¿Qué te motiva a programar?": {
        "a": "Ver cómo los usuarios interactúan con mi producto",
        "b": "Construir sistemas robustos que soporten todo",
        "c": "Crear aplicaciones que la gente lleve consigo",
        "d": "Descubrir insights ocultos en los datos"
    },
    "¿Qué consideras un código exitoso?": {
        "a": "El que brinda una experiencia fluida al usuario",
        "b": "El que es escalable, mantenible y eficiente",
        "c": "El que funciona en todos los dispositivos sin problemas",
        "d": "El que transforma datos en información útil"
    }
}


class SombreroSeleccionador:
    def __init__(self):
        self.frontend = 0
        self.backend = 0
        self.mobile = 0
        self.data = 0
        
    def hacer_preguntas(self):
        print("\n🎩 EL SOMBRERO SELECCIONADOR 🎩")
        print("================================")
        
        nombre = input("\nBienvenido/a, ¿cuál es tu nombre? ")
        
        print(f"\nMuy bien {nombre}, te haré 10 preguntas para determinar tu casa.")
        print("Para cada pregunta, elige la opción (a, b, c, d) que más te identifique.\n")
        
        for i, (pregunta, opciones) in enumerate(all_questions.items(), 1):
            print(f"\nPregunta {i}: {pregunta}")
            for letra, respuesta in opciones.items():
                print(f"{letra}) {respuesta}")
            
            respuesta = ""
            while respuesta not in ["a", "b", "c", "d"]:
                respuesta = input("Tu respuesta (a/b/c/d): ").lower()
                
            # Asignar puntos según la respuesta
            if respuesta == "a":
                self.frontend += 1
            elif respuesta == "b":
                self.backend += 1
            elif respuesta == "c":
                self.mobile += 1
            elif respuesta == "d":
                self.data += 1
        
        return nombre
                
    def determinar_casa(self):
        puntuaciones = {
            "Frontend": self.frontend,
            "Backend": self.backend, 
            "Mobile": self.mobile,
            "Data": self.data
        }
        
        # Encontrar el puntaje máximo
        max_puntuacion = max(puntuaciones.values())
        
        # Encontrar todas las casas con la puntuación máxima
        casas_maximas = [casa for casa, puntuacion in puntuaciones.items() 
                         if puntuacion == max_puntuacion]
        
        # Si hay empate, elegir aleatoriamente
        casa_elegida = random.choice(casas_maximas)
        
        return casa_elegida, len(casas_maximas) > 1
    
    def iniciar(self):
        nombre = self.hacer_preguntas()
        casa, hubo_empate = self.determinar_casa()
        
        print("\n" + "=" * 50)
        print(f"\n🎩 Mmm, interesante {nombre}...")
        
        if hubo_empate:
            print("La decisión ha sido complicada, pero finalmente...")
        
        print(f"\n¡TU CASA ES {casa.upper()}! 🎉")
        
        if casa == "Frontend":
            print("\n✨ Tienes un ojo para el diseño y una pasión por crear experiencias de usuario excepcionales.")
        elif casa == "Backend":
            print("\n🔧 Tu fortaleza está en construir sistemas robustos y eficientes que sostienen todo lo demás.")
        elif casa == "Mobile":
            print("\n📱 Tienes el talento para llevar la tecnología a todos los dispositivos y a cualquier lugar.")
        elif casa == "Data":
            print("\n📊 Tu capacidad analítica te permite descubrir información valiosa donde otros no la ven.")


# Ejecutar el programa si se ejecuta como script principal
if __name__ == "__main__":
    sombrero = SombreroSeleccionador()
    sombrero.iniciar()