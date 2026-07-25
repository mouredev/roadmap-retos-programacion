namespace exs36;
/*
_____________________________________
https://github.com/kenysdev
2024 - C#
_____________________________________
EL SOMBRERO SELECCIONADOR
------------------------------------
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

using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    private static readonly string[] HOUSES = ["Frontend", "Backend", "Mobile", "Data"];

    // NOTA: Preguntas y respuestas generadas por IA
    private static readonly string[] QUESTIONS = [
        "¿Qué te atrae más?",
        "¿Qué superhéroe de la programación te gustaría ser?",
        "En un proyecto de software, ¿qué rol te emociona más?",
        "Si tu código fuera una obra de arte, ¿qué estilo tendría?",
        "¿Qué animal de programación serías?",
        "En una hackathon, ¿qué tipo de proyecto propondrías?",
        "Si tu carrera en tech fuera una película, ¿de qué género sería?",
        "¿Qué herramienta de programación no puede faltar en tu caja de herramientas digital?",
        "Si pudieras resolver un gran problema en tech, ¿cuál elegirías?",
        "¿Qué tipo de equipo prefieres?"
    ];

    private static readonly string[][] ANSWERS = [
        ["Crear experiencias visuales.", "Solucionar problemas de funcionamiento.", "Innovar en dispositivos portátiles.", "Descubrir tendencias ocultas."],
        ["Diseñador de Interfaces, creando experiencias asombrosas", "Arquitecto de Sistemas, construyendo estructuras robustas", "Mago de Apps, conjurando soluciones móviles", "Explorador de Datos, descubriendo tesoros ocultos"],
        ["Director de UX, orquestando la sinfonía visual", "Ingeniero de Backend, dominando la lógica del servidor", "Desarrollador de Apps, llevando la potencia al bolsillo", "Científico de Datos, descifrando los secretos de la información"],
        ["Minimalismo elegante, como una landing page perfecta", "Arquitectura compleja, como un sistema distribuido", "Diseño adaptativo, fluyendo en diferentes dispositivos", "Visualización de datos, pintando historias con números"],
        ["Un camaleón, adaptándome a diferentes frameworks", "Un pulpo, manejando múltiples servicios a la vez", "Un colibrí, ágil y siempre en movimiento", "Una lechuza, analizando datos con sabiduría"],
        ["Una web app que revolucione la experiencia del usuario", "Un sistema de IA que optimice procesos backend", "Una app móvil que cambie la forma de interactuar con el mundo", "Un proyecto de big data que prediga tendencias futuras"],
        ["Comedia romántica con JavaScript y CSS", "Thriller de ciencia ficción con microservicios", "Aventura de acción en el mundo de las apps", "Documental profundo sobre el universo de los datos"],
        ["Un editor de código con plugins para diseño visual", "Una robusta suite de testing y depuración", "Un emulador multi-dispositivo de última generación", "Una plataforma de análisis de datos en tiempo real"],
        ["Hacer que la accesibilidad web sea universal", "Crear una arquitectura de software autorreparable", "Desarrollar una plataforma de AR/VR para educación móvil", "Construir un modelo de IA ético y transparente"],
        ["Creativos enfocados en diseño.", "Técnicos que construyen sistemas.", "Especialistas en aplicaciones móviles.", "Expertos en datos y análisis."]
    ];

    class SortingHat
    {
        private readonly Dictionary<string, int> scores = HOUSES.ToDictionary(house => house, _ => 0);

        public void AskQuestion(int qNum, string question, string[] answers)
        {
            Console.WriteLine($"\n#{qNum}: {question}");
            for (int i = 0; i < answers.Length; i++)
            {
                Console.WriteLine($"{i + 1}) {answers[i]}");
            }

            while (true)
            {
                Console.Write("Elige tu respuesta (1-4): ");
                if (int.TryParse(Console.ReadLine(), out int choice) && choice >= 1 && choice <= 4)
                {
                    scores[HOUSES[choice - 1]]++;
                    break;
                }
                else
                {
                    Console.WriteLine("Por favor, elige un número entre 1 y 4.");
                }
            }
        }

        public string SelectHouse()
        {
            int maxScore = scores.Values.Max();
            var topHouses = scores.Where(kv => kv.Value == maxScore).Select(kv => kv.Key).ToList();

            if (topHouses.Count > 1)
            {
                Console.WriteLine("\nLa decisión ha sido complicada.");
                return topHouses[new Random().Next(topHouses.Count)];
            }
            return topHouses[0];
        }
    }

    static void Main()
    {
        Console.WriteLine("EL SOMBRERO SELECCIONADOR");
        Console.Write("¿Cuál es tu nombre? : ");
        string name = Console.ReadLine() ?? string.Empty;
        var hat = new SortingHat();

        for (int i = 0; i < QUESTIONS.Length; i++)
        {
            hat.AskQuestion(i + 1, QUESTIONS[i], ANSWERS[i]);
        }

        string selectedHouse = hat.SelectHouse();
        Console.WriteLine($"\n'{name}' pertenecerá a la casa '{selectedHouse}'\n");
    }
}
