import java.util.*;

public class MohamedElderkaoui {
    
    // Clase principal
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        // Puntos para cada casa
        int frontend = 0, backend = 0, mobile = 0, data = 0;

        // Preguntas y respuestas
        String[] questions = {
            "¿Qué tipo de proyectos prefieres?",
            "¿Qué es lo más importante para ti en un lenguaje de programación?",
            "¿Cuál es tu entorno de desarrollo ideal?",
            "¿Qué tipo de problemas disfrutas resolver?",
            "¿Qué te emociona más aprender?",
            "¿Qué tipo de interfaces prefieres trabajar?",
            "¿Qué te gusta más en cuanto a la estructura de datos?",
            "¿Qué tipo de desarrollo te parece más interesante?",
            "¿Dónde prefieres aplicar tu código?",
            "¿Qué prefieres optimizar?"
        };

        String[][] options = {
            {"Aplicaciones web interactivas", "Sistemas robustos", "Aplicaciones móviles", "Análisis de datos"},
            {"Simplicidad y eficiencia", "Escalabilidad", "Compatibilidad multiplataforma", "Manejo de grandes volúmenes de datos"},
            {"Un navegador web", "Un servidor", "Un dispositivo móvil", "Un entorno de análisis de datos"},
            {"Interfaces de usuario atractivas", "Lógica de negocio compleja", "Experiencia de usuario fluida", "Descubrimiento de patrones en datos"},
            {"Frameworks de frontend", "Tecnologías de backend", "Desarrollo móvil", "Ciencia de datos"},
            {"UI/UX", "APIs y microservicios", "Interfaces móviles", "Dashboards y visualizaciones"},
            {"Arreglos y listas", "Bases de datos y consultas", "Modelos de datos móviles", "Conjuntos de datos masivos"},
            {"Desarrollo de frontend", "Desarrollo de backend", "Desarrollo de apps", "Análisis de datos"},
            {"En el cliente", "En el servidor", "En dispositivos móviles", "En la nube"},
            {"Carga y tiempo de respuesta", "Consumo de recursos", "Usabilidad y rendimiento", "Procesamiento de datos"}
        };

        // Solicitar nombre del alumno
        System.out.print("¡Bienvenido! ¿Cuál es tu nombre? ");
        String name = scanner.nextLine();

        // Realizar las preguntas
        for (int i = 0; i < questions.length; i++) {
            System.out.println("\n" + (i + 1) + ". " + questions[i]);
            System.out.println("1) " + options[i][0]);
            System.out.println("2) " + options[i][1]);
            System.out.println("3) " + options[i][2]);
            System.out.println("4) " + options[i][3]);
            System.out.print("Elige una opción (1-4): ");
            int answer = scanner.nextInt();

            // Asignar puntos según la respuesta
            switch (answer) {
                case 1:
                    frontend++;
                    break;
                case 2:
                    backend++;
                    break;
                case 3:
                    mobile++;
                    break;
                case 4:
                    data++;
                    break;
                default:
                    System.out.println("Opción no válida, no se asignaron puntos.");
                    break;
            }
        }

        // Determinar la casa con más puntos
        int maxPoints = Math.max(Math.max(frontend, backend), Math.max(mobile, data));
        String selectedHouse = "";
        boolean tie = false;

        // Resolver posibles empates
        if (frontend == maxPoints) {
            selectedHouse = "Frontend";
        }
        if (backend == maxPoints) {
            if (!selectedHouse.isEmpty()) tie = true;
            selectedHouse = "Backend";
        }
        if (mobile == maxPoints) {
            if (!selectedHouse.isEmpty()) tie = true;
            selectedHouse = "Mobile";
        }
        if (data == maxPoints) {
            if (!selectedHouse.isEmpty()) tie = true;
            selectedHouse = "Data";
        }

        // Desempatar si es necesario
        if (tie) {
            String[] houses = {"Frontend", "Backend", "Mobile", "Data"};
            selectedHouse = houses[random.nextInt(4)];
            System.out.println("\n¡Vaya, esto fue difícil! El sombrero estaba muy indeciso...");
        }

        // Resultado final
        System.out.println("\n¡Felicidades " + name + "! Has sido seleccionado para la casa " + selectedHouse + "!");
        scanner.close();
    }
}
