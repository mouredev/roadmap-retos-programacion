import java.util.*;
import java.util.concurrent.atomic.AtomicReference;

/**
 * #36 EL SOMBRERO SELECCIONADOR
 *
 * @author martinbohorquez
 */
public class martinbohorquez {
    static List<QuestionAnswers> questionAnswers = new ArrayList<>();
    static Map<House, Integer> houses = new LinkedHashMap<>();
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        houses.put(House.FRONTED, 0);
        houses.put(House.BACKEND, 0);
        houses.put(House.MOBILE, 0);
        houses.put(House.DATA, 0);

        questionAnswers = setQuestions();
        System.out.println("""
                ¡Bienvenido a Hogwarts, la escuela de programación para magos y brujas del código!
                El sombrero seleccionador decidirá cuál es tu casa como programador.
                """);
        System.out.print("Indicar su nombre: ");
        String name = sc.nextLine();

        displayQuestions();
        displayResult(name);
    }

    private static List<QuestionAnswers> setQuestions() {
        // QuestionAnswers 1
        String question1 = "¿Qué tipo de proyectos te interesa más desarrollar?";
        List<Answer> answers1 = new ArrayList<>(List.of(
                new Answer("Interfaces visualmente atractivas y responsivas.", House.FRONTED),
                new Answer("Sistemas robustos y optimización de rendimiento del servidor.", House.BACKEND),
                new Answer("Aplicaciones móviles nativas para múltiples plataformas.", House.MOBILE),
                new Answer("Procesamiento y análisis de grandes volúmenes de datos.", House.DATA)
        ));
        Collections.shuffle(answers1);
        questionAnswers.add(new QuestionAnswers(question1, answers1));

        // QuestionAnswers 2
        String question2 = "¿En qué parte del ciclo de desarrollo te sientes más cómodo?";
        List<Answer> answers2 = new ArrayList<>(List.of(
                new Answer("Creación de interfaces de usuario.", House.FRONTED),
                new Answer("Desarrollo de sistemas de backend.", House.BACKEND),
                new Answer("Diseño y arquitectura de bases de datos.", House.DATA),
                new Answer("Desarrollo de aplicaciones móviles con gran experiencia de usuario.", House.MOBILE)
        ));
        Collections.shuffle(answers2);
        questionAnswers.add(new QuestionAnswers(question2, answers2));

        // QuestionAnswers 3
        String question3 = "¿Qué herramienta prefieres usar en tu día a día?";
        List<Answer> answers3 = new ArrayList<>(List.of(
                new Answer("Figma o Sketch para diseño UI/UX.", House.FRONTED),
                new Answer("Postman o cURL para probar APIs.", House.BACKEND),
                new Answer("SQL o Python para análisis de datos.", House.DATA),
                new Answer("Android Studio o Xcode.", House.MOBILE)
        ));
        Collections.shuffle(answers3);
        questionAnswers.add(new QuestionAnswers(question3, answers3));

        // QuestionAnswers 4
        String question4 = "¿Qué lenguaje de programación prefieres?";
        List<Answer> answers4 = new ArrayList<>(List.of(
                new Answer("JavaScript o TypeScript.", House.FRONTED),
                new Answer("Java o Kotlin.", House.MOBILE),
                new Answer("Python o R.", House.DATA),
                new Answer("Java o Go.", House.BACKEND)
        ));
        Collections.shuffle(answers4);
        questionAnswers.add(new QuestionAnswers(question4, answers4));

        // QuestionAnswers 5
        String question5 = "¿Qué es lo que más disfrutas resolver en un proyecto?";
        List<Answer> answers5 = new ArrayList<>(List.of(
                new Answer("Diseñar y construir pantallas interactivas.", House.FRONTED),
                new Answer("Optimizar la comunicación entre servidores y bases de datos.", House.BACKEND),
                new Answer("Extraer información valiosa de grandes conjuntos de datos.", House.DATA),
                new Answer("Optimizar el rendimiento de una aplicación móvil.", House.MOBILE)
        ));
        Collections.shuffle(answers5);
        questionAnswers.add(new QuestionAnswers(question5, answers5));

        // QuestionAnswers 6
        String question6 = "¿Qué consideras esencial para un proyecto exitoso?";
        List<Answer> answers6 = new ArrayList<>(List.of(
                new Answer("Una interfaz intuitiva y atractiva.", House.FRONTED),
                new Answer("Un backend eficiente y seguro.", House.BACKEND),
                new Answer("Datos limpios y bien estructurados.", House.DATA),
                new Answer("Una aplicación móvil sin fallos y rápida.", House.MOBILE)
        ));
        Collections.shuffle(answers6);
        questionAnswers.add(new QuestionAnswers(question6, answers6));

        // QuestionAnswers 7
        String question7 = "¿Cómo prefieres abordar un problema complejo?";
        List<Answer> answers7 = new ArrayList<>(List.of(
                new Answer("Dividiéndolo en pequeños componentes visuales.", House.FRONTED),
                new Answer("Optimizando el procesamiento del servidor.", House.BACKEND),
                new Answer("Modelando los datos de manera eficiente.", House.DATA),
                new Answer("Dividiendo la funcionalidad entre distintas plataformas móviles.", House.MOBILE)
        ));
        Collections.shuffle(answers7);
        questionAnswers.add(new QuestionAnswers(question7, answers7));

        // QuestionAnswers 8
        String question8 = "¿En qué contexto te sientes más productivo?";
        List<Answer> answers8 = new ArrayList<>(List.of(
                new Answer("Diseñando interfaces responsivas.", House.FRONTED),
                new Answer("Construyendo APIs o microservicios.", House.BACKEND),
                new Answer("Analizando grandes volúmenes de datos.", House.DATA),
                new Answer("Desarrollando aplicaciones para Android o iOS.", House.MOBILE)
        ));
        Collections.shuffle(answers8);
        questionAnswers.add(new QuestionAnswers(question8, answers8));

        // QuestionAnswers 9
        String question9 = "¿Qué tecnología te gustaría dominar más?";
        List<Answer> answers9 = new ArrayList<>(List.of(
                new Answer("React o Angular.", House.FRONTED),
                new Answer("Django o Spring Boot.", House.BACKEND),
                new Answer("Hadoop o Spark.", House.DATA),
                new Answer("Flutter o React Native.", House.MOBILE)
        ));
        Collections.shuffle(answers9);
        questionAnswers.add(new QuestionAnswers(question9, answers9));

        // QuestionAnswers 10
        String question10 = "¿Qué tipo de problemas te entusiasma resolver?";
        List<Answer> answers10 = new ArrayList<>(List.of(
                new Answer("Hacer que las aplicaciones sean visualmente impactantes.", House.FRONTED),
                new Answer("Garantizar la seguridad y escalabilidad del sistema.", House.BACKEND),
                new Answer("Procesar y extraer conocimientos de datos complejos.", House.DATA),
                new Answer("Optimizar el rendimiento en aplicaciones móviles.", House.MOBILE)
        ));
        Collections.shuffle(answers10);
        questionAnswers.add(new QuestionAnswers(question10, answers10));
        Collections.shuffle(questionAnswers);
        return questionAnswers;
    }

    private static void displayQuestions() {
        AtomicReference<Integer> id = new AtomicReference<>(1);
        questionAnswers.forEach(questionAnswers -> {
                    AtomicReference<Integer> idA = new AtomicReference<>(1);
                    while (true) {
                        System.out.println("-".repeat(80));
                        System.out.printf("Pregunta %d: %s%n", id.get(), questionAnswers.question());
                        questionAnswers.answers.forEach(answer -> System.out.printf("%d. %s%n",
                                idA.getAndSet(idA.get() + 1), answer.option()));
                        System.out.print("Selecciona una respuesta entre 1 y 4: ");
                        try {
                            int choice = Integer.parseInt(sc.nextLine());

                            House house = questionAnswers.answers().get(choice - 1).house();
                            houses.replace(house, houses.get(house), houses.get(house) + 1);
                            id.set(id.get() + 1);
                            break;
                        } catch (NumberFormatException | IndexOutOfBoundsException e) {
                            idA.set(1);
                            System.out.println("Esa opción no es valida! Volver a responder la pregunta.");
                        }
                    }
                }
        );
    }

    private static void displayResult(String name) {
        House assignedHouse = Collections.max(houses.entrySet(), Map.Entry.comparingByValue()).getKey();
        List<Integer> scores = houses.values().stream().toList();
        System.out.println("-".repeat(80));
        System.out.println("<----- RESULTADOS DEL TEST ----->");
        System.out.println("Tus preferencias son:");
        houses.forEach((house, integer) ->
                System.out.println(house + " -> " + ("|" + house.getEmoji() + "|").repeat(integer)));

        Integer maxScore = scores.stream().max(Integer::compareTo).orElse(null);
        List<Integer> maxScores = scores.stream().filter(s -> s.equals(maxScore)).toList();
        if (maxScores.size() > 1) {

            Random random = new Random();
            assignedHouse = new ArrayList<>(houses.entrySet().stream()
                    .filter(houseIntegerEntry -> houseIntegerEntry.getValue().equals(maxScore))
                    .map(Map.Entry::getKey)
                    .toList())
                    .get(random.nextInt(0, maxScores.size()));
            System.out.printf("""
                    Hmmm... Ha sido una decisión muy complicada %s.
                    ¡Pero finalmente tu casa será %s [%s]
                    """, name, assignedHouse, assignedHouse.getEmoji());
        } else {
            System.out.printf("""
                    Hmmm... Enhorabuena %s.
                    ¡Tu casa será %s [%s]
                    """, name, assignedHouse, assignedHouse.getEmoji());
        }
    }

    private record QuestionAnswers(String question, List<Answer> answers) {
    }

    private record Answer(String option, House house) {
    }

    private enum House {
        FRONTED("Fronted", "🌐"),
        BACKEND("Backend", "💻"),
        MOBILE("Mobile", "📲"),
        DATA("Data", "📊");

        private final String displayName;
        private final String emoji;

        House(String displayName, String emoji) {
            this.displayName = displayName;
            this.emoji = emoji;
        }

        public String getEmoji() {
            return emoji;
        }

        @Override
        public String toString() {
            return displayName;
        }
    }
}
