import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Random random = new Random();

        int[] puntos = new int[Casas.values().length];

        welcome();
        System.out.println("¿Cómo te llamas?");
        String nombre = sc.nextLine();

        String[] preguntas = {
                "¿Cuál es tu lenguaje de programación favorito?",
                "¿Qué prefieres hacer en tu tiempo libre?",
                "¿Qué tipo de proyectos disfrutas más?",
                "¿Cuál es tu herramienta preferida?",
                "¿Qué prefieres aprender?",
                "¿Qué tipo de desafíos te motivan más?",
                "¿Cómo prefieres resolver problemas?",
                "¿Qué tecnología te parece más interesante?",
                "¿Cómo te gustaría que te reconocieran?",
                "¿Qué tipo de ambiente de trabajo prefieres?"
        };

        String[][] respuestas = {
                {"JavaScript", "Java", "Kotlin", "Python"},
                {"Diseñar interfaces", "Desarrollar APIs", "Crear apps móviles", "Analizar datos"},
                {"Sitios web", "Sistemas de backend", "Apps móviles", "Modelos de IA"},
                {"Figma", "Postman", "Android Studio", "Jupyter Notebook"},
                {"React", "Spring Boot", "Flutter", "Pandas"},
                {"UX/UI", "Optimización", "Innovación", "Precisión"},
                {"Prototipando", "Refactorizando", "Experimentando", "Investigando"},
                {"HTML/CSS", "Microservicios", "IoT", "Big Data"},
                {"Creatividad", "Eficiencia", "Innovación", "Precisión"},
                {"Flexible", "Estructurado", "Dinámico", "Analítico"}
        };

        int[][] asignacionPuntos = {
                {10, 5, 2, 8},  // Respuestas a la pregunta 1
                {8, 5, 10, 2},  // Respuestas a la pregunta 2
                {10, 5, 8, 2},  // Respuestas a la pregunta 3
                {5, 8, 10, 2},  // Respuestas a la pregunta 4
                {10, 2, 5, 8},  // Respuestas a la pregunta 5
                {8, 5, 10, 2},  // Respuestas a la pregunta 6
                {10, 8, 5, 2},  // Respuestas a la pregunta 7
                {5, 10, 8, 2},  // Respuestas a la pregunta 8
                {10, 8, 5, 2},  // Respuestas a la pregunta 9
                {8, 5, 10, 2}   // Respuestas a la pregunta 10
        };

        for (int i = 0; i < preguntas.length; i++) {
            System.out.println(preguntas[i]);
            for (int j = 0; j < respuestas[i].length; j++) {
                System.out.println((j + 1) + ". " + respuestas[i][j]);
            }
            System.out.print("Selecciona una opción (1-4): ");
            int opcion = sc.nextInt() - 1;
            for (int j = 0; j < puntos.length; j++) {
                puntos[j] += asignacionPuntos[i][opcion];
            }
        }

        int maxPuntos = 0;
        int casaSeleccionada = -1;
        boolean empate = false;

        for (int i = 0; i < puntos.length; i++) {
            if (puntos[i] > maxPuntos) {
                maxPuntos = puntos[i];
                casaSeleccionada = i;
                empate = false;
            } else if (puntos[i] == maxPuntos) empate = true;
        }

        if (empate) {
            casaSeleccionada = random.nextInt(puntos.length);
            System.out.println("¡Ha sido una decisión difícil!");
        }

        System.out.println("El sombrero seleccionador ha decidido...");
        System.out.println(nombre + ", ¡pertenecerás a la casa " + Casas.values()[casaSeleccionada] + "!");

        sc.close();
    }

    private static void welcome() {
        System.out.println("Bienvenido al Hogwarts Express");
        System.out.println("Con rumbo hacia la escuela de programación de Hogwarts para magos y brujas del código!");
        System.out.println("Soy el Sombrero Seleccionador, y te ayudaré a encontrar tu casa en la escuela de programación de Hogwarts.");
        System.out.println("Te haré unas preguntas y según tus respuestas, te asignaré a una de las cuatro casas de la escuela.");
        System.out.println("¡Vamos a empezar!");
    }


    enum Casas {
        FRONTEND, BACKEND, MOBILE, DATA
    }

}
