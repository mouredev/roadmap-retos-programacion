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
# importo choice para elegir al azar si hay empate
from random import choice
# Casas remplazables:
casas = {
        0:"Sofistas: Se enfocan en la retórica y la persuasión. Creen que la verdad es relativa y cambiante",
        1:"Aristotélicos: Valoran la lógica, la observación empírica y el razonamiento estructurado. Buscan conocimiento a través de la experiencia",
        2:"Platónicos: Creen en un mundo de ideas eterno e inmutable. Buscan verdades absolutas más allá de lo material",
        3:"Epicúreos: Enfatizan la búsqueda del placer moderado y la eliminación del dolor como el objetivo principal de la vida"
        }

# Preguntas remplazables:
preguntas = {
        1: "¿Qué valoras más en un debate filosófico?\n"
            "A) La persuasión y la retórica\n"
            "B) La lógica y la evidencia empírica\n"
            "C) La búsqueda de verdades absolutas e inmutables\n"
            "D) La búsqueda del placer y la eliminación del dolor",

        2: "¿Cuál es tu enfoque preferido para resolver problemas?\n"
            "A) Adaptarse y usar cualquier argumento disponible\n"
            "B) Analizar sistemáticamente los datos y llegar a una conclusión lógica\n"
            "C) Buscar en el mundo de las ideas para encontrar respuestas eternas\n"
            "D) Encontrar la solución que brinde mayor paz y felicidad",

        3: "¿Qué opinas sobre la naturaleza de la realidad?\n"
            "A) La realidad es relativa y depende de la percepción individual\n"
            "B) La realidad está compuesta de sustancias y formas que podemos observar\n"
            "C) La verdadera realidad es el mundo de las ideas, más allá de lo material\n"
            "D) La realidad es material y nuestros sentidos son la clave para disfrutarla",

        4: "¿Cómo crees que se debe enseñar la sabiduría?\n"
            "A) Mediante discursos convincentes y carismáticos\n"
            "B) A través de la lógica y el razonamiento estructurado\n"
            "C) Con diálogos que lleven al interlocutor a descubrir verdades universales\n"
            "D) Enseñando a las personas cómo vivir vidas placenteras y sin angustia",

        5: "¿Cuál es el mayor objetivo de la vida?\n"
            "A) Ser capaz de influir y convencer a los demás\n"
            "B) Alcanzar el conocimiento a través de la observación y el estudio\n"
            "C) Comprender las verdades fundamentales del universo\n"
            "D) Vivir en tranquilidad y evitar el sufrimiento",

        6: "¿Qué piensas sobre el placer?\n"
            "A) Es un medio para persuadir y manipular opiniones\n"
            "B) El placer debe ser controlado por la razón y la ética\n"
            "C) Es secundario en la búsqueda de la verdad\n"
            "D) Es el objetivo principal de la vida, pero debe buscarse con prudencia",

        7: "¿Cómo responderías a una crítica?\n"
            "A) Usando argumentos retóricos y desviando el tema\n"
            "B) Presentando evidencia lógica y razonada\n"
            "C) Invitando a un diálogo filosófico para encontrar la verdad subyacente\n"
            "D) Buscando un entendimiento mutuo para minimizar el conflicto",

        8: "¿Qué es más importante: la apariencia o la realidad?\n"
            "A) La apariencia, ya que es lo que perciben los demás\n"
            "B) La realidad, que se puede comprender a través de la experiencia\n"
            "C) La realidad ideal y eterna más allá de las apariencias\n"
            "D) La realidad, en tanto proporciona placer y evita el dolor",

        9: "¿Qué tipo de conocimiento valoras más?\n"
            "A) El conocimiento práctico que se puede aplicar en la vida cotidiana\n"
            "B) El conocimiento científico y empírico\n"
            "C) El conocimiento de las ideas y principios eternos\n"
            "D) El conocimiento que nos lleva a una vida feliz y sin estrés",

        10: "¿Cómo describirías la verdad?\n"
            "A) La verdad es relativa y puede cambiar\n"
            "B) La verdad es objetiva y puede descubrirse a través de la investigación\n"
            "C) La verdad es una realidad abstracta y eterna\n"
            "D) La verdad es aquello que conduce al bienestar"
    }

class Sombrero:
    def __init__(self) -> None:
        self.calificacion = {
            "a":0,
            "b":0,
            "c":0,
            "d":0,
            }
        self.casas = casas
        self.preguntas = preguntas

    def puntuar_pregunta(self,num,pregunta):
        check = False

        while not check:
            print(f"Pregunta - {num}\n{pregunta}")
            respuesta = input("").lower()
            check = True
            match respuesta:
                case "a":
                    self.calificacion[respuesta] += 1
                    
                case "b":
                    self.calificacion[respuesta] += 1

                case "c":
                    self.calificacion[respuesta] += 1

                case "d":
                    self.calificacion[respuesta] += 1
                
                case _:
                    print(f"{respuesta} no es una de las opciones disponibles {self.nombre}")
                    check = False

    def asignar_mi_casa(self,resultado):
        match resultado[0]:
            case "a":
                self.mi_casa = self.casas[0]

            case "b":
                self.mi_casa = self.casas[1]

            case "c":
                self.mi_casa = self.casas[2]

            case "d":
                self.mi_casa = self.casas[3]

    def asignar_casa(self):
        resultado = ["",0]
        final = []
        for respuesta, cantidad in self.calificacion.items():
            if cantidad > resultado[1]:
                resultado = [respuesta,cantidad]
                final = [[respuesta,cantidad]]
            elif cantidad == resultado[1]:
                resultado = [respuesta,cantidad]
                final.append([respuesta,cantidad])
            
        if len(final) == 1:
            self.asignar_mi_casa(final[0])
        elif len(final) > 1:
            self.asignar_mi_casa(choice(final))
            print("Esta siendo difícil.\nPodrías ir a esta... pero...")

    def hablar_sombrero(self):

        print("Parece que tenemos un nuevo alumno! No seas tímido, ¿Cuál es tu nombre?")
        self.nombre = input("").capitalize()
        print(f"Un placer {self.nombre}, ahora voy ha hacerte una serie de preguntas")
        print("Esta son las casas:")
        print("--------------------")
        for casa in self.casas.values():
            print()
            print(casa)
        print("--------------------")
        
        input("Responde con la letra que corresponda\nenter para empezar preguntas: ")
        for num,pregunta in self.preguntas.items():
            print()
            self.puntuar_pregunta(num,pregunta)

        self.asignar_casa()
        print(f"{self.calificacion}\n{self.nombre} tu casa será:\n{self.mi_casa}")

# Prueba
emmanuel = Sombrero()
emmanuel.hablar_sombrero()