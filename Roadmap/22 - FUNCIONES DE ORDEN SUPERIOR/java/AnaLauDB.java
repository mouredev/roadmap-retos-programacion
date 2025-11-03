import java.util.*;
import java.util.stream.Collectors;
import java.time.LocalDate;
import java.util.function.*;

public class AnaLauDB {

    // Clase Estudiante para la dificultad extra
    static class Estudiante {
        private String nombre;
        private LocalDate fechaNacimiento;
        private List<Double> calificaciones;

        public Estudiante(String nombre, LocalDate fechaNacimiento, List<Double> calificaciones) {
            this.nombre = nombre;
            this.fechaNacimiento = fechaNacimiento;
            this.calificaciones = calificaciones;
        }

        public String getNombre() {
            return nombre;
        }

        public LocalDate getFechaNacimiento() {
            return fechaNacimiento;
        }

        public List<Double> getCalificaciones() {
            return calificaciones;
        }

        public double getPromedio() {
            return calificaciones.stream()
                    .mapToDouble(Double::doubleValue)
                    .average()
                    .orElse(0.0);
        }

        @Override
        public String toString() {
            return String.format("%s (Promedio: %.2f)", nombre, getPromedio());
        }
    }

    // Ejemplos de funciones de orden superior
    public static void ejemplosBasicos() {
        List<Integer> numeros = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

        // 1. map() - transforma cada elemento
        List<Integer> cuadrados = numeros.stream()
                .map(x -> x * x)
                .collect(Collectors.toList());
        System.out.println("Cuadrados: " + cuadrados);

        // 2. filter() - filtra elementos
        List<Integer> pares = numeros.stream()
                .filter(x -> x % 2 == 0)
                .collect(Collectors.toList());
        System.out.println("Números pares: " + pares);

        // 3. reduce() - reduce a un solo valor
        int suma = numeros.stream()
                .reduce(0, (a, b) -> a + b);
        System.out.println("Suma total: " + suma);

        // 4. forEach() - ejecuta acción en cada elemento
        System.out.print("Números: ");
        numeros.stream().forEach(x -> System.out.print(x + " "));
        System.out.println();
    }

    // Función que acepta otra función como parámetro
    public static <T> List<T> filtrarLista(List<T> lista, Predicate<T> condicion) {
        return lista.stream()
                .filter(condicion)
                .collect(Collectors.toList());
    }

    // Función que retorna otra función
    public static Function<Integer, Integer> multiplicarPor(int factor) {
        return x -> x * factor;
    }

    public static void main(String[] args) {
        System.out.println("=== Ejemplos básicos de funciones de orden superior ===");
        ejemplosBasicos();

        // Ejemplo de función que acepta otra función
        List<String> palabras = Arrays.asList("Java", "Python", "JavaScript", "C++");
        List<String> palabrasLargas = filtrarLista(palabras, p -> p.length() > 4);
        System.out.println("Palabras largas: " + palabrasLargas);

        // Ejemplo de función que retorna otra función
        Function<Integer, Integer> multiplicarPor3 = multiplicarPor(3);
        System.out.println("5 * 3 = " + multiplicarPor3.apply(5));

        System.out.println("\n=== DIFICULTAD EXTRA: Análisis de estudiantes ===");

        // Crear lista de estudiantes
        List<Estudiante> estudiantes = Arrays.asList(
                new Estudiante("Ana", LocalDate.of(2000, 5, 15),
                        Arrays.asList(8.5, 9.0, 7.5, 8.0)),
                new Estudiante("Luis", LocalDate.of(1999, 3, 22),
                        Arrays.asList(9.5, 9.0, 9.8, 9.2)),
                new Estudiante("María", LocalDate.of(2001, 8, 10),
                        Arrays.asList(7.0, 6.5, 8.0, 7.5)),
                new Estudiante("Carlos", LocalDate.of(2000, 12, 3),
                        Arrays.asList(9.0, 9.5, 8.5, 9.8)),
                new Estudiante("Sofía", LocalDate.of(2002, 1, 28),
                        Arrays.asList(6.0, 7.0, 6.5, 7.5)));

        // 1. Promedio de calificaciones por estudiante
        System.out.println("1. Promedio de calificaciones:");
        estudiantes.stream()
                .map(e -> e.getNombre() + ": " + String.format("%.2f", e.getPromedio()))
                .forEach(System.out::println);

        // 2. Mejores estudiantes (promedio >= 9.0)
        System.out.println("\n2. Mejores estudiantes (promedio >= 9.0):");
        estudiantes.stream()
                .filter(e -> e.getPromedio() >= 9.0)
                .map(Estudiante::getNombre)
                .forEach(System.out::println);

        // 3. Estudiantes ordenados por edad (más joven primero)
        System.out.println("\n3. Estudiantes ordenados por edad (más joven primero):");
        estudiantes.stream()
                .sorted((e1, e2) -> e2.getFechaNacimiento().compareTo(e1.getFechaNacimiento()))
                .map(e -> e.getNombre() + " (" + e.getFechaNacimiento() + ")")
                .forEach(System.out::println);

        // 4. Mayor calificación de todos los estudiantes
        double mayorCalificacion = estudiantes.stream()
                .flatMap(e -> e.getCalificaciones().stream())
                .mapToDouble(Double::doubleValue)
                .max()
                .orElse(0.0);
        System.out.println("\n4. Mayor calificación: " + mayorCalificacion);
    }
}
