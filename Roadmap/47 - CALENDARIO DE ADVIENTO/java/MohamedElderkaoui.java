import java.util.*;

public class MohamedElderkaoui {

    // Lista de regalos para los días
    static final String[] prices = {
            "Curso de lógica de programación", "Diplomado sobre Metodologías Ágiles", 
            "Desarrollo de interfaces con Qt4", "Introducción a la programación funcional", 
            "Desarrollo en C#", "Buenas prácticas de programación en Java Springboot", 
            "¿Cómo hacer Smart Commits?", "Uso básico de la terminal Linux", 
            "Primeros pasos en Django Rest Framework (DRF)", 
            "Práctica aplicada de los patrones SOLID en Java", 
            "Introducción de Base de Datos", "Buenas prácticas dentro de Python", 
            "Paradigma de Metodologías Tradicionales ¿Aún tienen uso? ¿En qué casos es aplicable?", 
            "Data Science con Python y R", "GO ¿El lenguaje del futuro?", 
            "Patrones de Diseño de Software aplicados en Python", 
            "Algoritmos de optimización aplicados en C++", 
            "Fundamentos de la Inteligencia Artificial", 
            "Aplicación en la actualidad del IoT", 
            "Uso de librería numpy y pandas dentro de Python", 
            "POO aplicada en Java", "0 a héroe en PostgreSQL", 
            "Generación de servicios REST con AWS Api Gateway y Lambda"
    };

    public static void main(String[] args) {
        // Array para rastrear los días descubiertos
        boolean[] discovered = new boolean[24];
        Scanner scanner = new Scanner(System.in);

        while (true) {
            printCalendar(discovered);
            System.out.println("Ingrese el día que quiere descubrir (1-24) o 0 para salir:");
            
            int dia;
            try {
                dia = scanner.nextInt();
                if (dia == 0) {
                    System.out.println("¡Gracias por participar en el aDEViento! 🎉");
                    break;
                }
                if (dia < 1 || dia > 24) {
                    System.out.println("⚠️ El día debe estar entre 1 y 24.");
                    continue;
                }

                // Revisar si el día ya está descubierto
                if (discovered[dia - 1]) {
                    System.out.println("⚠️ Ya has descubierto este día.");
                } else {
                    discovered[dia - 1] = true; // Marcar como descubierto
                    System.out.println("🎁 Regalo del día " + dia + ": " + prices[dia - 1]);
                }
            } catch (InputMismatchException e) {
                System.out.println("⚠️ Entrada no válida. Debes ingresar un número.");
                scanner.next(); // Limpiar el scanner
            }
        }
        scanner.close();
    }

    // Método para imprimir el calendario
    private static void printCalendar(boolean[] discovered) {
        System.out.println("Calendario de aDEViento:");
        for (int i = 0; i < 24; i++) {
            if (i % 6 == 0) System.out.println(); // Nueva fila cada 6 días

            if (discovered[i]) {
                // Si el día ya está descubierto, mostramos cuadrícula llena
                System.out.print("**** ");
            } else {
                // Mostrar día con formato
                System.out.printf("*%02d* ", i + 1);
            }
        }
        System.out.println("\n");
    }
}
