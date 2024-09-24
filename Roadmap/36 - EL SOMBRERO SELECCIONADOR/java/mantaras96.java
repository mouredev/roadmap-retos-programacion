import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.Scanner;

public class Mantaras96 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Respuestas respuestas = new Respuestas();

        String name = obtenerNombreAlumno(scanner);

        List<String> preguntas = cargarPreguntas();

        // Aquí podrías llamar a otras funciones para continuar el programa, por
        // ejemplo:
        realizarPreguntas(scanner, respuestas, preguntas);
        String casa = determinarCasa(respuestas);
        System.out.println("El sombrero seleccionador ha decidido que perteneces a la casa: " + casa);

        scanner.close();
    }

    public static String determinarCasa(Respuestas respuestas) {
        int maxPuntos = Math.max(Math.max(respuestas.getPuntosFront(), respuestas.getPuntosBack()),
                Math.max(respuestas.getPuntosMobile(), respuestas.getPuntosData()));
        List<String> casasEmpatadas = new ArrayList<>();

        if (respuestas.getPuntosFront() == maxPuntos) {
            casasEmpatadas.add("Frontend");
        }
        if (respuestas.getPuntosBack() == maxPuntos) {
            casasEmpatadas.add("Backend");
        }
        if (respuestas.getPuntosMobile() == maxPuntos) {
            casasEmpatadas.add("Mobile");
        }
        if (respuestas.getPuntosData() == maxPuntos) {
            casasEmpatadas.add("Data");
        }

        if (casasEmpatadas.size() > 1) {
            System.out.println("¡La decisión ha sido complicada! Hubo un empate.");
            Random random = new Random();
            return casasEmpatadas.get(random.nextInt(casasEmpatadas.size()));
        } else {
            return casasEmpatadas.get(0);
        }
    }

    public static void mostrarResultados(Respuestas respuestas) {
        String casa = determinarCasa(respuestas);
        System.out.println("El sombrero seleccionador ha decidido que perteneces a la casa: " + casa);
    }

    public static List<String> cargarPreguntas() {
        List<String> preguntas = new ArrayList<>();
        preguntas.add(
                "Pregunta 1: ¿Qué lenguaje de programación prefieres? (Responde con 1 para JavaScript, 2 para Java, 3 para Swift, 4 para Python)");
        preguntas.add(
                "Pregunta 2: ¿Qué tipo de proyectos disfrutas más? (Responde con 1 para Aplicaciones web, 2 para Sistemas empresariales, 3 para Aplicaciones móviles, 4 para Análisis de datos)");
        preguntas.add(
                "Pregunta 3: ¿Qué herramienta prefieres usar? (Responde con 1 para React, 2 para Spring, 3 para Xcode, 4 para Pandas)");
        preguntas.add(
                "Pregunta 4: ¿Cuál es tu área de interés? (Responde con 1 para Diseño de interfaces, 2 para Arquitectura de software, 3 para Desarrollo de apps, 4 para Ciencia de datos)");
        preguntas.add(
                "Pregunta 5: ¿Qué prefieres hacer en tu tiempo libre? (Responde con 1 para Crear sitios web, 2 para Trabajar en backend, 3 para Desarrollar juegos móviles, 4 para Analizar grandes conjuntos de datos)");
        preguntas.add(
                "Pregunta 6: ¿Cuál es tu rol ideal en un equipo? (Responde con 1 para Diseñador UI/UX, 2 para Ingeniero de software, 3 para Desarrollador móvil, 4 para Científico de datos)");
        preguntas.add(
                "Pregunta 7: ¿Qué tecnología te emociona más? (Responde con 1 para CSS y HTML, 2 para Microservicios, 3 para Kotlin, 4 para Machine Learning)");
        preguntas.add(
                "Pregunta 8: ¿Qué tipo de problemas te gusta resolver? (Responde con 1 para Problemas de diseño, 2 para Problemas de lógica, 3 para Problemas de accesibilidad, 4 para Problemas de análisis de datos)");
        preguntas.add(
                "Pregunta 9: ¿Qué tipo de lectura prefieres? (Responde con 1 para Blogs de diseño, 2 para Libros técnicos, 3 para Artículos sobre desarrollo móvil, 4 para Investigaciones de datos)");
        preguntas.add(
                "Pregunta 10: ¿Dónde te ves en cinco años? (Responde con 1 para Desarrollando interfaces innovadoras, 2 para Liderando equipos de backend, 3 para Creando apps revolucionarias, 4 para Descubriendo insights en datos)");
        return preguntas;
    }

    public static void realizarPreguntas(Scanner scanner, Respuestas respuestas, List<String> preguntas) {
        for (String pregunta : preguntas) {
            boolean respuestaValida = false;
            while (!respuestaValida) {
                System.out.println(pregunta);
                String respuesta = scanner.nextLine();
                try {
                    int puntos = Integer.parseInt(respuesta);
                    respuestas.addPointsToHouse(puntos);
                    respuestaValida = true;
                } catch (NumberFormatException e) {
                    System.out.println("Por favor, ingrese un número válido.");
                }
            }
        }
    }

    public static String obtenerNombreAlumno(Scanner scanner) {
        System.out.println("Bienvenido a Hogwarts. Indica tu nombre al sombrero seleccionador:");
        String name = scanner.nextLine();
        return name;
    }

    public static class Respuestas {
        int puntosFront = 0;
        int puntosBack = 0;
        int puntosMobile = 0;
        int puntosData = 0;

        public int getPuntosFront() {
            return puntosFront;
        }

        public void setPuntosFront(int puntosFront) {
            this.puntosFront = puntosFront;
        }

        public int getPuntosBack() {
            return puntosBack;
        }

        public void setPuntosBack(int puntosBack) {
            this.puntosBack = puntosBack;
        }

        public int getPuntosMobile() {
            return puntosMobile;
        }

        public void setPuntosMobile(int puntosMobile) {
            this.puntosMobile = puntosMobile;
        }

        public int getPuntosData() {
            return puntosData;
        }

        public void setPuntosData(int puntosData) {
            this.puntosData = puntosData;
        }

        public Respuestas() {
            // Constructor por defecto
        }

        public void addPointsToHouse(int points) {
            switch (points) {
                case 1:
                    this.puntosFront++;
                    break;
                case 2:
                    this.puntosBack++;
                    break;
                case 3:
                    this.puntosMobile++;
                    break;
                case 4:
                    this.puntosData++;
                    break;
            }

        }
    }
}
