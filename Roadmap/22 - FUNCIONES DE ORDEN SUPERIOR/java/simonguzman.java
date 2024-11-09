import java.time.LocalDate;
import java.util.Arrays;
import java.util.List;
import java.util.function.Consumer;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.function.Supplier;
import java.util.stream.Collectors;

public class simonguzman {
    public static void main(String[] args) {
        //ejercicioPrincipal();
        ejercicioAdicional();
    }

    /******************** Ejercicio adicional ********************/
    public static void ejercicioAdicional(){
        List<Estudiante> estudiantes = Arrays.asList(
            new Estudiante("Juan", LocalDate.of(2000, 5, 15), Arrays.asList(8.0, 9.0, 10.0)),
            new Estudiante("Ana", LocalDate.of(1998, 11, 3), Arrays.asList(9.5, 9.0, 9.7)),
            new Estudiante("Carlos", LocalDate.of(2002, 6, 21), Arrays.asList(6.0, 7.5, 8.0))
        );
        operaciones(estudiantes);
    }

    public static void operaciones(List<Estudiante> estudiantes){
        promedioCalificaciones(estudiantes);

        List<String> mejores = mejoresEstudiantes(estudiantes);
        System.out.println("Mejores estudiantes: "+mejores);

        List<Estudiante> ordenados = ordenarPorNacimiento(estudiantes);
        System.out.println("Estudiantes ordenados por nacimiento:");
        ordenados.forEach(est -> System.out.println(est.getNombre()));

        double mayorCalificacion = obtenerMayorCalificacion(estudiantes);
        System.out.println("Mayor calificación: " + mayorCalificacion);
    }

    public static void promedioCalificaciones(List<Estudiante> estudiantes){
        estudiantes.forEach(estudiante -> {
            double promedio = estudiante.getPromedio();
            System.out.println("Estudiante: "+estudiante.getNombre()+ " ,promedio: "+promedio);
        });
    }

    public static List<String> mejoresEstudiantes(List<Estudiante> estudiantes){
        return estudiantes.stream().filter(est -> est.getPromedio() >= 9).map(Estudiante::getNombre).toList();
    }

    public static List<Estudiante> ordenarPorNacimiento(List<Estudiante> estudiantes){
        return estudiantes.stream().sorted((e1, e2) -> e2.getFechaNacimiento().compareTo(e1.getFechaNacimiento())).toList();
    }

    public static double obtenerMayorCalificacion(List<Estudiante> estudiantes){
        return estudiantes.stream().flatMap(est -> est.getCalificaciones().stream()).max(Double::compareTo).orElse(0.0);
    }
    public static class Estudiante {
        private String nombre;
        private LocalDate fechaNacimiento;
        private List<Double> calificaciones;

        public Estudiante(){

        }

        public Estudiante(String nombre, LocalDate fechaNacimiento, List<Double> calificaciones){
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

        public double getPromedio(){
            return calificaciones.stream().mapToDouble(Double::doubleValue).average().orElse(0.0);
        }
    }

    /******************** Ejercicio conceptual ********************/

    public static void ejercicioPrincipal(){
        List<Integer> numeros = Arrays.asList(1,2,3,4,5,6,7,8,9,10);
        List<Integer> numerosMultiplicados = multiplicarXDos(numeros);
        List<Integer> numerosPares = filtrarNumerosPares(numerosMultiplicados);
        imprimirNumeros(numerosPares);
        int suma = sumarNumeros(numerosPares);
        System.out.println("Suma de los números pares multiplicados por 2: " + suma);
    }

    public static List<Integer> multiplicarXDos(List<Integer> numeros){
        Function<Integer, Integer> multiplicar = (n) -> n * 2;
        return numeros.stream().map(multiplicar).collect(Collectors.toList());
    }

    public static List<Integer> filtrarNumerosPares(List<Integer> numeros){
        Predicate<Integer> esPar = (n) -> n % 2 == 0;
        return numeros.stream().filter(esPar).collect(Collectors.toList());
    }

    public static int sumarNumeros(List<Integer> numeros){
        Supplier<Integer> sumar = () -> numeros.stream().mapToInt(Integer::intValue).sum();
        return sumar.get();
    }

    public static void imprimirNumeros(List<Integer> numeros){
        Consumer<Integer> imprimir = (n) -> System.out.println("Numero: "+n);
        numeros.forEach(imprimir);
    }
}
