package com.amsoft.roadmap.example36;


import java.util.Arrays;
import java.util.Scanner;


enum House {
    FRONTEND("🌐"),
    BACKEND("🔙"),
    MOBILE("📱"),
    DATA("💾");

    private final String emoji;

    House(String emoji) {
        this.emoji = emoji;
    }

    public String getEmoji() {
        return emoji;
    }

}

record Question(String question, String[] answers) {
}
public class Example36 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Question[] questions = {
                new Question("¿Qué lenguaje de programación prefieres?", new String[]{"JavaScript", "Java", "Kotlin", "Python"}),
                new Question("¿Qué tipo de proyecto te gustaría desarrollar?", new String[]{"Web", "Backend", "Mobile", "Big Data"}),
                new Question("¿Qué tipo de dispositivo prefieres?", new String[]{"PC", "Servidor", "Smartphone", "Servidor"}),
                new Question("¿Qué tipo de base de datos prefieres?", new String[]{"MongoDB", "MySQL", "SQLite", "PostgreSQL"}),
                new Question("¿Qué tipo de sistema operativo prefieres?", new String[]{"Windows", "Linux", "Android", "MacOS"}),
                new Question("¿Qué tipo de IDE prefieres?", new String[]{"Visual Studio Code", "IntelliJ IDEA", "Android Studio", "PyCharm"}),
                new Question("¿Qué tipo de framework prefieres?", new String[]{"React", "Spring", "Flutter", "Django"}),
                new Question("¿Qué tipo de control de versiones prefieres?", new String[]{"Git", "SVN", "Git", "Git"}),
                new Question("¿Qué tipo de metodología prefieres?", new String[]{"Agile", "Waterfall", "Scrum", "Kanban"}),
                new Question("¿Qué tipo de testing prefieres?", new String[]{"Unit", "Integration", "UI", "Performance"})
        };
        System.out.println("¡Bienvenido al Sombrero Seleccionador de Hogwarts!");
        System.out.println("Te haré unas preguntas y según tus respuestas, te asignaré a una de las cuatro casas de la escuela.");
        System.out.println("¡Vamos a empezar!");
        System.out.println("Por favor, introduce tu nombre:");
        String name = scanner.nextLine();
        System.out.println("¡Hola, " + name + "!");
        System.out.println("Por favor, responde a las siguientes preguntas con el número de la respuesta que prefieras:");
        int[] points = new int[House.values().length];
        for (Question question : questions) {
            System.out.println(question.question());
            for (int i = 0; i < question.answers().length; i++) {
                System.out.println((i + 1) + ". " + question.answers()[i]);
            }
            int answer = scanner.nextInt();
            if(answer < 1 || answer > question.answers().length) {
                System.out.println("Respuesta no válida. Por favor, introduce un número entre 1 y " + question.answers().length);
                continue;
            }
            points[answer - 1] += 1;
        }
        int maxPoints = points[0];
        int houseIndex = 0;
        boolean tie = false;
        System.out.println("¡El Sombrero Seleccionador ha terminado de analizar tus respuestas!");
        for (int i = 1; i < points.length; i++) {
            if (points[i] > maxPoints) {
                maxPoints = points[i];
                houseIndex = i;
                tie = false;
            } else if (points[i] == maxPoints) {
                tie = true;
            }
        }
        House house = House.values()[houseIndex];
        System.out.println("¡Enhorabuena, " + name + "!");
        if (tie) {
            System.out.println("¡La decisión ha sido complicada!");
        }
        System.out.println("¡Tu casa es " + house + " " + house.getEmoji() + "!");

        scanner.close();





    }
}
