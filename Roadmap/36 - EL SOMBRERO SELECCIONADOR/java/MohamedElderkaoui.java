import java.util.*;

public class MohamedElderkaoui {

    static class House {
        String name;
        int score;

        House(String name) {
            this.name = name;
            this.score = 0;
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        // Initial setup of houses
        List<House> houses = Arrays.asList(
            new House("Frontend"),
            new House("Backend"),
            new House("Mobile"),
            new House("Data")
        );

        // Collect student information
        System.out.print("¡Bienvenido! ¿Cuál es tu nombre? ");
        String name = scanner.nextLine();
        System.out.print("¿Qué edad tienes? ");
        int age = scanner.nextInt();
        scanner.nextLine(); // Consume the newline
        System.out.print("¿Qué experiencia tienes en programación? (novato, intermedio, avanzado): ");
        String experience = scanner.nextLine().toLowerCase();

        // Personalized question sets based on experience
        String[][] questions = generateQuestions(experience);

        // Ask the questions with weights
        for (int i = 0; i < questions.length; i++) {
            System.out.println("\n" + questions[i][0]);
            for (int j = 1; j <= 4; j++) {
                System.out.println(j + ") " + questions[i][j]);
            }
            System.out.print("Elige una opción (1-4): ");
            int answer = scanner.nextInt();
            
            // Add weighted score to corresponding house
            addWeightedScore(houses, answer, i + 1);
        }

        // Determine the house with the highest score
        House selectedHouse = determineHouse(houses, random, age, experience);

        // Display final result with personalized feedback
        displayResult(name, selectedHouse);
        scanner.close();
    }


    private static String[][] generateQuestions(String experience) {
        if (experience.compareToIgnoreCase("novato")==0) {
            return new String[][] {
                {"¿Qué te gustaría aprender primero?", "HTML/CSS", "Bases de datos", "Desarrollo móvil básico", "Manipulación de datos"},
                {"¿Qué tipo de proyectos te motivan?", "Sitios web", "Sistemas pequeños", "Apps sencillas", "Análisis simple"},
                {"¿Cuál es tu entorno de aprendizaje preferido?", "Tutoriales en línea", "Cursos estructurados", "Aplicaciones de aprendizaje", "Proyectos con datos"},
                {"¿Cómo prefieres trabajar?", "Diseñando interfaces", "Organizando datos", "Construyendo aplicaciones", "Analizando información"},
                {"¿Qué lenguaje de programación te gustaría aprender primero?", "JavaScript", "SQL", "Kotlin", "Python"},
                {"¿Qué te parece más interesante?", "Crear páginas web", "Gestionar bases de datos", "Desarrollar apps", "Analizar datos"},
                {"¿En qué tipo de empresa te ves trabajando?", "Agencia digital", "Empresa de software", "Startup móvil", "Consultoría de datos"},
                {"¿Qué prefieres en términos de desafíos?", "Diseñar una web atractiva", "Optimizar consultas", "Mejorar la usabilidad móvil", "Descubrir patrones en datos"},
                {"¿Cuál sería tu rol/es ideal en un equipo?", "Diseñador web", "Administrador de bases de datos", "Desarrollador de apps", "Analista de datos"},
                {"¿Cómo prefieres aprender?", "Con ejercicios prácticos", "Resolviendo problemas lógicos", "Desarrollando apps pequeñas", "Trabajando con datasets simples"}
            };
            
        } else if (experience.compareToIgnoreCase("intermedio")==0) {
            return new String[][] {
                {"¿Qué disfrutas optimizar?", "Experiencia visual", "Rendimiento del servidor", "Usabilidad móvil", "Procesos de datos"},
                {"¿Qué es lo más importante en un proyecto?", "Usabilidad", "Eficiencia", "Compatibilidad", "Precisión de datos"},
                {"¿Cómo abordas la resolución de problemas?", "Con creatividad", "Con análisis profundo", "Con prototipos rápidos", "Con datos empíricos"},
                {"¿Qué prefieres en un entorno de desarrollo?", "Herramientas de diseño", "Depuradores avanzados", "Simuladores móviles", "Entornos de análisis de datos"},
                {"¿Qué te impulsa en un proyecto?", "La estética", "La lógica", "La innovación", "Los resultados basados en datos"},
                {"¿Cómo manejas el trabajo en equipo?", "Como líder de frontend", "Como arquitecto de backend", "Como desarrollador principal", "Como analista senior"},
                {"¿Qué tendencia tecnológica te atrae?", "WebAssembly", "Serverless computing", "Realidad aumentada", "Machine learning"},
                {"¿Qué lenguaje consideras esencial?", "JavaScript/TypeScript", "Go/Rust", "Swift/Java", "Python/R"},
                {"¿Qué prefieres hacer en tu tiempo libre?", "Prototipar diseños", "Contribuir a proyectos open-source", "Desarrollar apps personales", "Trabajar en proyectos de análisis de datos"},
                {"¿Cuál es tu objetivo a largo plazo?", "Ser un maestro de la experiencia de usuario", "Liderar la infraestructura de sistemas", "Crear apps de referencia", "Ser un gurú de los datos"}
            };
            
        } else {
            return new String[][] {
                {"¿Qué disfrutas optimizar?", "Experiencia visual", "Rendimiento del servidor", "Usabilidad móvil", "Procesos de datos"},
                {"¿Qué es lo más importante en un proyecto?", "Usabilidad", "Eficiencia", "Compatibilidad", "Precisión de datos"},
                {"¿Cómo abordas la resolución de problemas?", "Con creatividad", "Con análisis profundo", "Con prototipos rápidos", "Con datos empíricos"},
                {"¿Qué prefieres en un entorno de desarrollo?", "Herramientas de diseño", "Depuradores avanzados", "Simuladores móviles", "Entornos de análisis de datos"},
                {"¿Qué te impulsa en un proyecto?", "La estética", "La lógica", "La innovación", "Los resultados basados en datos"},
                {"¿Cómo manejas el trabajo en equipo?", "Como líder de frontend", "Como arquitecto de backend", "Como desarrollador principal", "Como analista senior"},
                {"¿Qué tendencia tecnológica te atrae?", "WebAssembly", "Serverless computing", "Realidad aumentada", "Machine learning"},
                {"¿Qué lenguaje consideras esencial?", "JavaScript/TypeScript", "Go/Rust", "Swift/Java", "Python/R"},
                {"¿Qué prefieres hacer en tu tiempo libre?", "Prototipar diseños", "Contribuir a proyectos open-source", "Desarrollar apps personales", "Trabajar en proyectos de análisis de datos"},
                {"¿Cuál es tu objetivo a largo plazo?", "Ser un maestro de la experiencia de usuario", "Liderar la infraestructura de sistemas", "Crear apps de referencia", "Ser un gurú de los datos"}
            };
            
        }
    }

    // Method to add weighted score to the corresponding house
    private static void addWeightedScore(List<House> houses, int answer, int questionNumber) {
        int weight = questionNumber; // More weight for later questions
        houses.get(answer - 1).score += weight;
    }

    // Method to determine the house with the highest score and handle ties
    private static House determineHouse(List<House> houses, Random random, int age, String experience) {
        houses.sort((h1, h2) -> h2.score - h1.score);
        List<House> topHouses = new ArrayList<>();
        int maxScore = houses.get(0).score;

        for (House house : houses) {
            if (house.score == maxScore) {
                topHouses.add(house);
            }
        }

        // Consider age and experience as tie-breaker criteria
        if (topHouses.size() > 1) {
            System.out.println("\n¡Fue una decisión difícil! Considerando tu edad y experiencia...");
            if (age < 20 && experience.equals("novato")) {
                return randomHouseSelection(topHouses, random, "Frontend");
            } else if (age >= 20 && experience.equals("avanzado")) {
                return randomHouseSelection(topHouses, random, "Backend");
            } else {
                return topHouses.get(random.nextInt(topHouses.size()));
            }
        }

        return topHouses.get(0);
    }

    // Method to randomly select a house, with preference based on certain conditions
    private static House randomHouseSelection(List<House> topHouses, Random random, String preferredHouse) {
        for (House house : topHouses) {
            if (house.name.equals(preferredHouse)) {
                return house;
            }
        }
        return topHouses.get(random.nextInt(topHouses.size()));
    }

    // Method to display the final result with personalized feedback
    private static void displayResult(String name, House selectedHouse) {
        System.out.println("\n¡Felicidades " + name + "! Has sido seleccionado para la casa " + selectedHouse.name + "!");
        System.out.println("Tu afinidad por la " + selectedHouse.name + " se refleja en tus respuestas.");
        if (selectedHouse.name.equals("Frontend")) {
            System.out.println("Eres una persona creativa, te encanta construir interfaces y mejorar la experiencia del usuario.");
        } else if (selectedHouse.name.equals("Backend")) {
            System.out.println("Disfrutas diseñar la lógica del servidor y crear sistemas eficientes y escalables.");
        } else if (selectedHouse.name.equals("Mobile")) {
            System.out.println("Te apasiona el desarrollo móvil y crear aplicaciones que lleguen a las manos de millones de usuarios.");
        } else if (selectedHouse.name.equals("Data")) {
            System.out.println("Te gusta analizar datos, encontrar patrones y dar sentido a la información compleja.");
        }
    }

}
