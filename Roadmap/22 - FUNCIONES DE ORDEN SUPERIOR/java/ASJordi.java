import java.time.LocalDate;
import java.util.Arrays;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.List;
import java.util.function.Function;

/**
 * Funciones de Orden Superior
 * Son funciones que pueden tomar otras funciones como argumentos y/o devolver funciones como resultado.
 * Esto permite la creación de abstracciones más complejas y potentes.
 * En Java, las funciones de orden superior se pueden implementar utilizando interfaces funcionales,
 * que son interfaces con un único método abstracto.
 * Java 8 introdujo varias interfaces funcionales predefinidas en el paquete java.util.function,
 * como Function, Predicate, Consumer, Supplier, etc.
 */
public class Main {

    public static void main(String[] args) {
//        System.out.println(iva.apply(100.0));
//        System.out.println(applyTwice(x -> x + 1, 5));
        administrarEstudiantes();
    }

    /**
     * EJERCICIO:
     * Explora el concepto de funciones de orden superior en tu lenguaje
     * creando ejemplos simples (a tu elección) que muestren su funcionamiento.
     */

    /**
     * Función que calcula el IVA de un precio
     * @param x Precio
     * @return Precio con IVA
     */
    public static Function<Double, Double> iva = x -> x + (x * 0.16);

    /**
     * Función de orden superior que aplica una función dos veces
     * @param f Función a aplicar dos veces
     * @param x Valor a aplicar
     * @return Resultado de aplicar la función dos veces al valor dado x
     */
    public static Integer applyTwice(Function<Integer, Integer> f, Integer x) {
        return f.apply(f.apply(x));
    }

    /**
     * DIFICULTAD EXTRA (opcional):
     * Dada una lista de estudiantes (con sus nombres, fecha de nacimiento y lista de calificaciones),
     * utiliza funciones de orden superior para realizar las siguientes operaciones de procesamiento y análisis:
     * - Promedio calificaciones: Obtiene una lista de estudiantes por nombre y promedio de sus calificaciones.
     * - Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes que tienen calificaciones con un 9 o más de promedio.
     * - Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
     * - Mayor calificación: Obtiene la calificación más alta de entre todas las de los alumnos.
     * - Una calificación debe estar comprendida entre 0 y 10 (admite decimales).
     */
    public static void administrarEstudiantes() {
        Function<Estudiante, Double> fPromedio = e -> e.getCalificaciones().stream().mapToDouble(Double::doubleValue).average().orElse(0.0);
        Function<List<Estudiante>, Double> fCalificacionMasAlta = l -> l.stream().mapToDouble(e -> e.getCalificaciones().stream().mapToDouble(Double::doubleValue).max().orElse(0.0)).max().orElse(0.0);

        var promedios = obtenerPromedios(fPromedio, obtenerEstudiantes());
        promedios.forEach(e -> System.out.println(Arrays.toString(e)));

        var mejoresEstudiantes = obtenerMejoresEstudiantes(fPromedio, obtenerEstudiantes());
        System.out.println("Mejores estudiantes: " + mejoresEstudiantes);

        var estudiantesOrdenados = obtenerEstudiantesOrdenadosPorFechaNacimiento(obtenerEstudiantes());
        estudiantesOrdenados.forEach(System.out::println);

        var calificacionMasAlta = obtenerCalificacionMasAlta(fCalificacionMasAlta, obtenerEstudiantes());
        System.out.println("Calificación más alta: " + calificacionMasAlta);
    }

    public static List<String[]> obtenerPromedios(Function<Estudiante, Double> f, List<Estudiante> l) {
        List<String[]> result = new LinkedList<>();
        l.forEach(e -> result.add(new String[]{e.getNombre(), f.apply(e).toString()}));
        return result;
    }

    public static List<String> obtenerMejoresEstudiantes(Function<Estudiante, Double> f, List<Estudiante> l) {
        List<String> result = new LinkedList<>();
        l.forEach(e -> {
            if (f.apply(e) >= 9.0) result.add(e.getNombre());
        });
        return result;
    }

    public static List<Estudiante> obtenerEstudiantesOrdenadosPorFechaNacimiento(List<Estudiante> l) {
        l.sort(Comparator.comparing(Estudiante::getFechaNacimiento));
        return l;
    }

    public static Double obtenerCalificacionMasAlta(Function<List<Estudiante>, Double> f, List<Estudiante> l) {
        return f.apply(l);
    }

    static class Estudiante {
        private String nombre;
        private LocalDate fechaNacimiento;
        private List<Double> calificaciones;

        public Estudiante(String nombre, LocalDate fechaNacimiento) {
            this.nombre = nombre;
            this.fechaNacimiento = fechaNacimiento;
            this.calificaciones = new LinkedList<>();
        }

        public void setCalificaciones(List<Double> calificaciones) {
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


        @Override
        public String toString() {
            return "Estudiante{" + "nombre='" + nombre + '\'' +
                    ", fechaNacimiento=" + fechaNacimiento +
                    ", calificaciones=" + calificaciones +
                    '}';
        }
    }

    /**
     * Método que devuelve una lista de estudiantes
     * @return
     */
    public static List<Estudiante> obtenerEstudiantes() {
        List<Estudiante> list = new LinkedList<>();

        Estudiante e1 = new Estudiante("Juan", LocalDate.of(2010, 1, 1));
        List<Double> c1 = List.of(8.0, 9.0, 7.0, 10.0, 8.5);
        e1.setCalificaciones(c1);

        Estudiante e2 = new Estudiante("Pedro", LocalDate.of(2001, 2, 2));
        List<Double> c2 = List.of(7.0, 6.0, 8.0, 9.0, 7.5);
        e2.setCalificaciones(c2);

        Estudiante e3 = new Estudiante("Maria", LocalDate.of(2002, 3, 3));
        List<Double> c3 = List.of(10.0, 10.0, 9.5, 9.0, 9.2);
        e3.setCalificaciones(c3);

        Estudiante e4 = new Estudiante("Ana", LocalDate.of(2003, 4, 4));
        List<Double> c4 = List.of(6.0, 7.0, 6.5, 8.0, 7.2);
        e4.setCalificaciones(c4);

        list.add(e1);
        list.add(e2);
        list.add(e3);
        list.add(e4);
        return list;
    }
}
