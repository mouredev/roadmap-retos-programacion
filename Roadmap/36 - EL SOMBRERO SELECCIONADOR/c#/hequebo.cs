class Question
{
    public string _Question { get; set; }
    public Dictionary<int, string> Options { get; set; }

    public Question(string question, Dictionary<int, string> options)
    {
        _Question = question;
        Options = options;
    }
}
class QuestionService
{
    private List<Question> _questions;
    private Dictionary<string, int> _houses = new Dictionary<string, int>
        {
            {"Frontend", 0 },
            {"Backend", 0 },
            {"Mobile", 0 },
            {"Data", 0 }
        };

    public List<Question> Questions { get {  return _questions; } }

    public QuestionService()
    {
        _questions = new List<Question>();
    }
    public void AddQuestion(Question question) => _questions.Add(question);
    public void Answer(int question, int option)
    {

        switch (option)
        {
            case 1:
                _houses["Frontend"]++;
                break;
            case 2:
                _houses["Backend"]++;
                break;
            case 3:
                _houses["Mobile"]++;
                break;
            case 4:
                _houses["Data"]++;
                break;
            default:
                Console.WriteLine("Opción no válida...");
                break;
        }
    }
    public void ShowResults()
    {
        int maxScore = _houses.Values.Max();
        var maxScoreHouses = _houses.Where(h => h.Value == maxScore);
        KeyValuePair<string, int> selectedHouse;
        if (maxScoreHouses.Count() == 1)
        {
            selectedHouse = maxScoreHouses.First();
            Console.WriteLine($"El sombrero seleccionador te ha envíado a la casa: {selectedHouse.Key}");
        } 
        else
        {
            Random random = new Random();
            selectedHouse = maxScoreHouses.ElementAt(random.Next(maxScoreHouses.Count()));
            Console.WriteLine($"Ha sido una decisión díficil, pero el sombrero seleccionador ha " +
                $"decido enviarte a la casa : {selectedHouse.Key}");
        }
    }
}
class Program
{
    static void Main(string[] args)
    {
        QuestionService questionService = new QuestionService();
        questionService.AddQuestion(
            new Question(
                "¿Qué tipo de proyectos te interesa más desarrollar?",
                new Dictionary<int, string>(){
                    {3, "1.- Aplicaciones móviles nativas para múltiples plataformas."},
                    {1, "2.- Interfaces visualmente atractivas y responsivas."},
                    {4, "3.- Procesamiento y análisis de grandes volúmenes de datos."},
                    {2, "4- Sistemas robustos y optimización de rendimiento del servidor."}

                }
            )
        );
        questionService.AddQuestion(
            new Question(
                "¿Qué aspecto del desarrollo disfrutas más?",
                new Dictionary<int, string>(){
                    {2, "1.- Resolver problemas complejos de lógica y escalabilidad."},
                    {4, "2.- Analizar datos para tomar decisiones basadas en estadísticas."},
                    {3, "3.- Crear aplicaciones móviles eficientes y funcionales."},
                    {1, "4.- Trabajar en el diseño y la experiencia de usuario."}

                }
            )
        );
        questionService.AddQuestion(
            new Question(
                "¿Qué herramienta prefieres usar en tu día a día?",
                new Dictionary<int, string>(){
                    {3, "1.- Kotlin o Swift para desarrollar apps móviles nativas."},
                    {4, "2.- Python o R para análisis de datos."},
                    {1, "3.- Frameworks como React o Angular."},
                    {2, "4.- Lenguajes como Node.js o Python para la gestión de servidores."}

                }
            )
        );
        questionService.AddQuestion(
            new Question(
                "¿Cómo te ves en un equipo de desarrollo?",
                new Dictionary<int, string>(){
                    {4, "1.- Modelando datos y construyendo dashboards de análisis."},
                    {2, "2.- Encargado de la lógica del servidor y las APIs."},
                    {3, "3.- Desarrollando la interfaz y funcionalidad de una app móvil."},
                    {1, "4.- Diseñando las interacciones y los componentes visuales."}

                }
            )
        );
        questionService.AddQuestion(
            new Question(
                "¿Qué te motiva más al trabajar en un proyecto?",
                new Dictionary<int, string>(){
                    {1, "1.- Ver cómo el diseño cobra vida en la pantalla."},
                    {4, "2.- Descubrir insights a partir del análisis de datos."},
                    {2, "3.- Optimizar el rendimiento y escalabilidad del sistema."},
                    {3, "4.- Lograr que una aplicación móvil funcione perfectamente en cualquier dispositivo."}
                }
            )
        );
        questionService.AddQuestion(
            new Question(
                "¿Cuál es tu enfoque al aprender nuevas tecnologías?",
                new Dictionary<int, string>(){
                    {4, "1.- Explorar técnicas avanzadas de análisis de datos y machine learning."},
                    {2, "2.- Aprender sobre nuevas arquitecturas y lenguajes de servidor."},
                    {3, "3.- Probar nuevas plataformas y herramientas para desarrollo móvil."},
                    {1, "4.- Experimentar con nuevas librerías y frameworks de interfaz de usuario."}
                }
            )
        );
        questionService.AddQuestion(
            new Question(
                "¿Qué tipo de desafíos disfrutas más resolver?",
                new Dictionary<int, string>(){
                    {2, "1.- Solución de problemas de concurrencia y carga en servidores."},
                    {1, "2.- Optimización de interfaces para que se vean bien en cualquier dispositivo."},
                    {4, "3.- Análisis de grandes volúmenes de datos para detectar patrones ocultos."},
                    {3, "4.- Creación de experiencias de usuario fluídas en dispositivos móviles."}
                }
            )
        );
        questionService.AddQuestion(
            new Question(
                "¿Cómo te gusta medir el éxito de tu trabajo?",
                new Dictionary<int, string>(){
                    {2, "1.- Por la estabilidad y rapidez del sistema bajo carga."},
                    {1, "2.- Mediante la satisfacción del usuario con la interfaz visual."},
                    {3, "3.- Por la fluidez y buen rendimiento de la app móvil en diferentes dispositivos."},
                    {4, "4.- Por la precisión y relevancia de los resultados obtenidos en el análisis de datos."}
                }
            )
        );
        questionService.AddQuestion(
            new Question(
                "¿Qué te resulta más interesante al trabajar con tecnologías emergentes?",
                new Dictionary<int, string>(){
                    {4, "1.- Trabajar con tecnologías de big data o inteligencia artificial."},
                    {2, "2.- Explorar nuevas arquitecturas para mejorar el rendimiento del servidor."},
                    {1, "3.- Probar nuevas herramientas y metodologías para mejorar el diseño y la UX."},
                    {3, "4.- Desarrollar apps móviles que aprovechen nuevas capacidades de hardware."}
                }
            )
        );
        questionService.AddQuestion(
            new Question(
                "¿Cómo te enfrentas a un nuevo problema en un proyecto?",
                new Dictionary<int, string>(){
                    {4, "1.- Buscando patrones y soluciones basadas en análisis de datos."},
                    {1, "2.- Replanteando la estructura visual y funcional de la interfaz."},
                    {3, "3.- Explorando cómo mejorar la experiencia del usuario en dispositivos móviles."},
                    {2, "4.- Analizando la estructura de datos y la lógica del backend."}
                }
            )
        );

        Console.WriteLine("---Sistema del sombrero seleccionador de Hogwarts---");
        Console.WriteLine("¿Cuál es tu nombre?");
        string name = Console.ReadLine();
        Console.WriteLine($"!Bienvenido {name}! a continuación te haremos una serie de " +
            $"preguntas para determinar cuál será tu casa");

        int questionId = 0;
        foreach (Question question in questionService.Questions)
        {
            Console.WriteLine(question._Question);
            foreach (var option in question.Options)
            {
                Console.WriteLine(option.Value);
            }
            Console.WriteLine("Elige una respuesta...");
            int answer = 0;
            int.TryParse(Console.ReadLine(), out answer);
            var selection = question.Options.FirstOrDefault(o => o.Value.Contains(answer.ToString()));
            questionService.Answer(questionId, selection.Key);
            questionId++;
        }
        questionService.ShowResults();

    }
}
