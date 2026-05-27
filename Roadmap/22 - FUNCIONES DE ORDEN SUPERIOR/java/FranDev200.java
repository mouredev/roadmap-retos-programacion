import java.time.LocalDate;
import java.util.*;
import java.util.function.Function;

public class FranDev200 {

    public static int operar(ArrayList<Integer> lista, Function<ArrayList<Integer>, Integer> sumar) {

        return sumar.apply(lista);

    }

    public static ArrayList<Integer> ordenar (ArrayList<Integer> lista, Function<ArrayList<Integer>, List<Integer>> ordenacion) {

        ArrayList<Integer> resultado = new ArrayList<>(ordenacion.apply(lista));

        return  resultado;
    }

    public static ArrayList<Integer> calcularPares(ArrayList<Integer> lista, Function<ArrayList<Integer>, List<Integer>> par) {

        ArrayList<Integer> resultado = new ArrayList<>(par.apply(lista));

        return  resultado;

    }

    static void main() {

        /*

        EJERCICIO:
         * Explora el concepto de funciones de orden superior en tu lenguaje
         * creando ejemplos simples (a tu elección) que muestren su funcionamiento.

         */

        ArrayList<Integer> listaNumeros = new ArrayList<>();
        listaNumeros.add(14);
        listaNumeros.add(5);
        listaNumeros.add(54);
        listaNumeros.add(12);
        listaNumeros.add(88);
        listaNumeros.add(36);
        listaNumeros.add(29);
        listaNumeros.add(67);
        listaNumeros.add(53);
        listaNumeros.add(2);
        listaNumeros.add(9);

        Function<ArrayList<Integer>, Integer> suma =
                x -> x.stream().mapToInt(Integer::intValue).sum();

        Function<ArrayList<Integer>, List<Integer>> ordenacion =
                x -> x.stream().toList().stream().sorted().toList();

        Function<ArrayList<Integer>, List<Integer>> pares =
                x -> x.stream()
                        .filter( n -> (n % 2) == 0)
                        .toList();

        System.out.println("\nSuma total de todos estos números: " + listaNumeros + " = " + operar(listaNumeros, suma));
        System.out.println("=================");
        System.out.println("Ordenacion de los numeros de la lista");
        System.out.println("-------------------------------------");
        System.out.println("Antes de ordenar: " + listaNumeros);
        System.out.println("Después de ordenar: " + ordenar(listaNumeros, ordenacion));
        System.out.println("=================");
        System.out.println("Numeros pares de la lista: " + calcularPares(listaNumeros, pares));
        System.out.println("Lista de pares, ordenados: " + ordenar(calcularPares(listaNumeros, pares), ordenacion));
        System.out.println("=================");



        /*

        DIFICULTAD EXTRA (opcional):
         * Dada una listaNumeros de estudiantes (con sus nombres, fecha de nacimiento y
         * listaNumeros de calificaciones), utiliza funciones de orden superior para
         * realizar las siguientes operaciones de procesamiento y análisis:
         * - Promedio calificaciones: Obtiene una listaNumeros de estudiantes por nombre
         *   y promedio de sus calificaciones.
         * - Mejores estudiantes: Obtiene una listaNumeros con el nombre de los estudiantes
         *   que tienen calificaciones con un 9 o más de promedio.
         * - Nacimiento: Obtiene una listaNumeros de estudiantes ordenada desde el más joven.
         * - Mayor calificación: Obtiene la calificación más alta de entre todas las
         *   de los alumnos.
         * - Una calificación debe estar comprendida entre 0 y 10 (admite decimales).

         */

        ArrayList<Estudiante> alumnos = new ArrayList<>();

        alumnos.add(new Estudiante("Ana López",
                LocalDate.of(2002, 3, 12),
                new ArrayList<>(Arrays.asList(7.5, 8.0, 6.5))));

        alumnos.add(new Estudiante("Carlos Martín",
                LocalDate.of(2001, 7, 25),
                new ArrayList<>(Arrays.asList(5.5, 6.0, 7.0))));

        alumnos.add(new Estudiante("Lucía Fernández",
                LocalDate.of(2003, 11, 9),
                new ArrayList<>(Arrays.asList(9.0, 8.5, 9.5))));

        alumnos.add(new Estudiante("David Gómez",
                LocalDate.of(2002, 1, 18),
                new ArrayList<>(Arrays.asList(4.5, 5.0, 6.0))));

        alumnos.add(new Estudiante("Marta Ruiz",
                LocalDate.of(2001, 6, 30),
                new ArrayList<>(Arrays.asList(7.0, 7.5, 8.0))));

        alumnos.add(new Estudiante("Javier Sánchez",
                LocalDate.of(2003, 2, 14),
                new ArrayList<>(Arrays.asList(6.5, 6.0, 5.5))));

        alumnos.add(new Estudiante("Elena Navarro",
                LocalDate.of(2002, 9, 22),
                new ArrayList<>(Arrays.asList(8.5, 9.0, 8.0))));

        alumnos.add(new Estudiante("Pablo Torres",
                LocalDate.of(2001, 5, 5),
                new ArrayList<>(Arrays.asList(3.5, 4.0, 5.0))));

        alumnos.add(new Estudiante("Sara Molina",
                LocalDate.of(2003, 12, 27),
                new ArrayList<>(Arrays.asList(10.0, 9.5, 9.0))));

        alumnos.add(new Estudiante("Raúl Ortega",
                LocalDate.of(2002, 8, 11),
                new ArrayList<>(Arrays.asList(6.0, 7.0, 6.5))));


        System.out.println("\n\nEJERCICIO EXTRA");
        System.out.println("===============");

        // Funcion que calcula el promedio de las notas de cada alumno
        Function<Estudiante, Double> promedioNotas =
                x -> x.getCalificaciones().stream().mapToDouble(Double::doubleValue)
                        .average().orElse(0.0);

        // Funcion que devuelve el alumno con la mayor media

        Function<ArrayList<Estudiante>, Double> mejorNota =
                x -> x.stream().mapToDouble(
                        e -> e.getCalificaciones().stream().mapToDouble(Double::doubleValue)
                                .max().orElse(0.0)).max().orElse(0.0);

        System.out.println("Calculo de las medias de los estudiantes");
        System.out.println("----------------------------------------");

        HashMap<String, Double> estudiantesNotas = notasMediaAlumnos(promedioNotas, alumnos);

        for (Map.Entry<String, Double> nota: estudiantesNotas.entrySet()) {

            System.out.printf("%-15s --> %04.2f\n", nota.getKey(), nota.getValue());

        }

        System.out.println("===============");
        System.out.println("Mejores estudiantes. [Nota media >= 9]");
        System.out.println("----------------------------------------");

        HashMap<String, Double> estudiantesSobresalientes = notasSobresalientes(promedioNotas, alumnos);

        for (Map.Entry<String, Double> nota: estudiantesSobresalientes.entrySet()) {

            System.out.printf("%-15s --> %04.2f\n", nota.getKey(), nota.getValue());

        }

        System.out.println("===============");
        System.out.println("Alumnos ordenados de más joven a más mayor");
        System.out.println("----------------------------------------");

        for (Estudiante estudiante: ordenarEstudiantesFchNacimiento(alumnos)) {
            System.out.printf("%-15s --> %s\n", estudiante.getNombre(), estudiante.getFch_nacimiento());
        }

        System.out.println("===============");
        System.out.println("La nota más alta en un examen fue: " + mejorNota(mejorNota,  alumnos));
        System.out.println("----------------------------------------");


    }

    static class Estudiante{

        private String nombre;
        private LocalDate fch_nacimiento;
        private ArrayList<Double> calificaciones;

        public Estudiante(String nombre, LocalDate fch_nacimiento, ArrayList<Double> calificaciones) {
            this.nombre = nombre;
            this.fch_nacimiento = fch_nacimiento;
            this.calificaciones = calificaciones;
        }

        public Estudiante(String nombre, ArrayList<Double> calificaciones) {
            this.nombre = nombre;
            this.calificaciones = calificaciones;
        }

        public String getNombre() {
            return nombre;
        }

        public void setNombre(String nombre) {
            this.nombre = nombre;
        }

        public LocalDate getFch_nacimiento() {
            return fch_nacimiento;
        }

        public void setFch_nacimiento(LocalDate fch_nacimiento) {
            this.fch_nacimiento = fch_nacimiento;
        }

        public ArrayList<Double> getCalificaciones() {
            return calificaciones;
        }

        public void setCalificaciones(ArrayList<Double> calificaciones) {
            this.calificaciones = calificaciones;
        }
    }

    public static HashMap<String, Double> notasMediaAlumnos(Function<Estudiante, Double> promedioNotas, ArrayList<Estudiante> estudiantes){

        HashMap<String, Double> notasMediaAlumnos = new HashMap<>();

        estudiantes.forEach(estudiante -> {
            notasMediaAlumnos.put(estudiante.getNombre(), promedioNotas.apply(estudiante));
        });

        return notasMediaAlumnos;

    };

    public static HashMap<String, Double> notasSobresalientes(Function<Estudiante, Double> promedioNotas, ArrayList<Estudiante> estudiantes){

        HashMap<String, Double> notasMediaAlumnos = new HashMap<>();

        estudiantes.forEach(estudiante -> {

            if(promedioNotas.apply(estudiante) >= 9){
                notasMediaAlumnos.put(estudiante.getNombre(), promedioNotas.apply(estudiante));
            }

        });

        return notasMediaAlumnos;

    };

    public static List<Estudiante> ordenarEstudiantesFchNacimiento(ArrayList<Estudiante> estudiantes){

        estudiantes.sort(Comparator.comparing(Estudiante::getFch_nacimiento));
        return estudiantes;

    }



    public static Double mejorNota(Function<ArrayList<Estudiante>, Double> mejorEstudiante, ArrayList<Estudiante> estudiantes){

        return mejorEstudiante.apply(estudiantes);

    };

}
