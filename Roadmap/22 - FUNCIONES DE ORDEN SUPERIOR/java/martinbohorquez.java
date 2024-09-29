import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.function.Function;

public class martinbohorquez {

    public static void main(String[] args) {
        //Función como argumento
        String name = "MartinDev";
        System.out.printf("La longitud '%s' es: %s%n", name, applyFunction(String::length, name));
        System.out.printf("El nombre '%s' en mayúscula es: %s%n", name, applyFunction(String::toUpperCase, name));

        //Retorno de función
        int intA = 3;
        int intB = 4;
        System.out.printf("La multiplicación de %d y %d es: %d%n", intA, intB, applyMultiplier(intA).apply(intB));
        //Uso de API Stream con interfaces funcionales: Predicate<T>, Function<T, R>, Consumer<T>, Supplier<R>,
        // BiPredicate<T, U>, BiFunction<T, U, R>, BiConsumer<T, U>, UnaryOperator<T>, BinaryOperator<T>
        List<Integer> numbers = new ArrayList<>(Arrays.asList(1, 3, 4, 2, 5));
        System.out.printf("La lista de números '%s' multiplicada por 2 es: %s%n", numbers,
                numbers.stream().map(n -> n * 2).toList()); //<R> Stream<R> map(Function<? super T, ? extends R> mapper)
        System.out.printf("La lista de números '%s' filtrada por números pares es: %s%n", numbers,
                numbers.stream().filter(n -> n % 2 == 0).toList()); //Stream<T> filter(Predicate<? super T> predicate)
        System.out.printf("La lista de números '%s' ordenada de forma ascendente es: %s%n", numbers,
                numbers.stream().sorted().toList());
        System.out.printf("La lista de números '%s' ordenada de forma descendente es: %s%n", numbers,
                numbers.stream().sorted().toList().reversed());
        System.out.printf("La lista de números '%s' ordenada de forma descendente es: %s%n", numbers,
                numbers.stream().sorted(Comparator.reverseOrder()).toList()); //Uso de Comparator
        //UnaryOperator<T> == Function<T, R> cuando las clases T, U son iguales.
        //BinaryOperator<T> == BiFunction<T, U, R> cuando las clases T, U, R son iguales.
        System.out.printf("La suma de todos los elementos de la lista '%s' es: %d%n", numbers,
                numbers.stream().reduce(0, Integer::sum)); //T reduce(T identity, BinaryOperator<T> accumulator)

        /*
         * DIFICULTAD EXTRA
         */
        List<Student> students = Arrays.asList(
                new Student("Piero", LocalDate.of(1997, 12, 23), Arrays.asList(9.0, 9.0, 9.5)),
                new Student("Katherine", LocalDate.of(1996, 6, 1), Arrays.asList(9.5, 9.0, 9.5)),
                new Student("Marshall", LocalDate.of(1994, 3, 18), Arrays.asList(8.0, 7.5, 8.0)),
                new Student("Martin", LocalDate.of(1994, 9, 20), Arrays.asList(9.0, 9.7, 9.5)),
                new Student("Jimena", LocalDate.of(1997, 4, 29), Arrays.asList(8.5, 9.5, 9.5)),
                new Student("Marcos", LocalDate.of(1995, 9, 20), Arrays.asList(8.0, 8.0, 9.5))
        );

        System.out.printf("La lista de estudiantes con su respectivo promedio de calificaciones es: %n%s%n",
                students.stream().map(Student::toStringNameAveragegradePoint).toList());

        System.out.printf("La lista de estudiantes con promedio de calificaciones mayores a 9 es: %s%n",
                students.stream()
                        .filter(s -> s.getAverageGradePoint() > 9)
                        .map(Student::getName)
                        .toList());

        students.sort(Comparator.comparing(Student::getBirthDate));
        System.out.printf("La lista de estudiantes ordenada por edad (ascendente) es: %s%n",
                students.stream()
                        .map(Student::getName)
                        .toList());

        System.out.printf("La calificación más alta entre la de todos los alumnos es: %.2f%n",
                students.stream()
                        .map(student -> student.getGradesList().stream().max(Double::compareTo).orElse(0.0))
                        .max(Double::compareTo)
                        .orElse(0.00));


        System.out.printf("La calificación más alta entre la de todos los alumnos es: %.2f%n",
                students.stream()
                        .flatMap(s -> s.getGradesList().stream())
                        .max(Double::compareTo)
                        .orElse(0.00));

    }

    private static Function<Integer, Integer> applyMultiplier(int n) {
        return x -> x * n;
    }

    public static <T, R> R applyFunction(Function<T, R> function, T x) {
        return function.apply(x);
    }

    private static class Student {
        private String name;
        private LocalDate birthDate;
        private List<Double> gradesList;

        public Student(String name, LocalDate birthDate, List<Double> gradesList) {
            this.name = name;
            this.birthDate = birthDate;
            this.gradesList = gradesList;
        }

        public String getName() {
            return name;
        }

        public LocalDate getBirthDate() {
            return birthDate;
        }

        public List<Double> getGradesList() {
            return gradesList;
        }

        public Double getAverageGradePoint() {
            return getGradesList().stream().mapToDouble(Double::doubleValue).average().orElse(0.0);
        }

        public String toStringNameAveragegradePoint() {
            String averageGradePoint = String.format("%.2f", getAverageGradePoint());
            return "{name = '" + name + "', " +
                    "average = " + averageGradePoint + "}";
        }
    }
}
