import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

public class eulogioep {
    // Clase Estudiante para almacenar la información de cada alumno
    static class Estudiante {
        private String nombre;
        private LocalDate fechaNacimiento;
        private List<Double> calificaciones;

        public Estudiante(String nombre, LocalDate fechaNacimiento, List<Double> calificaciones) {
            this.nombre = nombre;
            this.fechaNacimiento = fechaNacimiento;
            // Validamos que las calificaciones estén entre 0 y 10
            this.calificaciones = calificaciones.stream()
                .filter(calif -> calif >= 0 && calif <= 10)
                .collect(Collectors.toList());
        }

        public String getNombre() { return nombre; }
        public LocalDate getFechaNacimiento() { return fechaNacimiento; }
        public List<Double> getCalificaciones() { return calificaciones; }
    }

    public static void main(String[] args) {
        // Creamos una lista de estudiantes de ejemplo
        List<Estudiante> estudiantes = Arrays.asList(
            new Estudiante("Ana García", 
                LocalDate.of(2000, 5, 15),
                Arrays.asList(9.5, 8.7, 9.2, 9.8)),
            new Estudiante("Carlos Pérez",
                LocalDate.of(1999, 3, 20),
                Arrays.asList(7.5, 8.0, 6.5, 7.8)),
            new Estudiante("María López",
                LocalDate.of(2001, 8, 10),
                Arrays.asList(9.0, 9.5, 9.3, 9.7))
        );

        // 1. Promedio de calificaciones
        // Usamos map() para transformar cada estudiante en un nuevo objeto con nombre y promedio
        System.out.println("Promedios de calificaciones:");
        estudiantes.stream()
            .map(e -> {
                double promedio = e.getCalificaciones().stream()
                    .mapToDouble(Double::doubleValue)
                    .average()
                    .orElse(0.0);
                return String.format("%s: %.2f", e.getNombre(), promedio);
            })
            .forEach(System.out::println);

        // 2. Mejores estudiantes (promedio >= 9)
        System.out.println("\nMejores estudiantes (promedio >= 9):");
        estudiantes.stream()
            .filter(e -> e.getCalificaciones().stream()
                .mapToDouble(Double::doubleValue)
                .average()
                .orElse(0.0) >= 9)
            .map(Estudiante::getNombre)
            .forEach(System.out::println);

        // 3. Estudiantes ordenados por fecha de nacimiento (más joven primero)
        System.out.println("\nEstudiantes ordenados por edad (más joven primero):");
        estudiantes.stream()
            .sorted(Comparator.comparing(Estudiante::getFechaNacimiento).reversed())
            .map(e -> String.format("%s (%s)", 
                e.getNombre(), 
                e.getFechaNacimiento()))
            .forEach(System.out::println);

        // 4. Mayor calificación de todos los estudiantes
        double maxCalificacion = estudiantes.stream()
            .flatMap(e -> e.getCalificaciones().stream())
            .max(Double::compare)
            .orElse(0.0);
        System.out.println("\nMayor calificación: " + maxCalificacion);
    }
}