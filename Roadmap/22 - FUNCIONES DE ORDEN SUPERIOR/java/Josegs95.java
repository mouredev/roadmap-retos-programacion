import java.time.LocalDate;
import java.util.*;
import java.util.function.Function;
import java.util.function.Supplier;

public class Josegs95 {
    public static void main(String[] args) {
        //Ejercicio
        //Las funciones de orden superior están muy relacionadas en java con todo el contenido del paquete
        //java.util.function y las expresiones lambda, ambos introducidos en la versión 8 de Java.

        //Pasar una función como parámetro
        int a = 8;
        int result = operate(a, x -> x * x);
        System.out.println(result);

        //Devolver una función desde otra función
        int b = 3;
        Supplier<Integer> supplier = doubleValue(b);
        System.out.println(supplier.get());

        //Reto
        retoFinal();
    }

    public static int operate(int n, Function<Integer, Integer> function){
        return function.apply(n);
    }

    public static Supplier<Integer> doubleValue(int n){
        return () -> n * 2;
    }

    public static void retoFinal(){
        List<Student> studentList = new ArrayList<>();
        studentList.add(new Student("Jose",
                LocalDate.of(1995, 2, 28),
                Arrays.asList(10.0, 8.25, 9.25, 10.0)));
        studentList.add(new Student("María",
                LocalDate.of(1997, 4, 13),
                Arrays.asList(6.5, 6.0, 8.5, 8.0)));
        studentList.add(new Student("Guillermo",
                LocalDate.of(1992, 7, 22),
                Arrays.asList(9.0, 9.5, 7.75, 8.5)));

        //Promedio calificaciones
        List<String> averageMarks = studentList.stream()
                .map(s-> {
                    double average = s.getMarkList()
                            .stream()
                            .mapToDouble(Double::doubleValue)
                            .average()
                            .getAsDouble();
                    return s.getName() + ":" + average;
                }).toList();
        System.out.println("Nota media de los estudiantes: " + averageMarks);

        //Mejores estudiantes (+9 de nota)
        List<String> bestStudents = averageMarks.stream()
                .filter(s -> {
                    double averageMark = Double.parseDouble(s.substring(s.indexOf(":") + 1));
                    return averageMark > 9.0;
                }).toList();
        System.out.println("Estudiantes con mas de un 9 de nota media: " + bestStudents);

        //Lista de estudiantes ordenada por nacimiento
        List<Student> sortedStudentList = studentList.stream()
                .sorted((x, y) -> x.getBirthday().compareTo(y.getBirthday())  * -1)
                .toList();
        System.out.println("Estudiantes ordenados ascendentemente por edad: " + sortedStudentList);

        //Mejor calificación de los estudiantes
        double bestMark = studentList.stream()
                .mapToDouble(s -> s.getMarkList()
                        .stream()
                        .max(Double::compareTo).get())
                .max().getAsDouble();
        System.out.println("Nota mas alta de entre los estudiantes: " + bestMark);

    }

    public static class Student {
        private String name;
        private LocalDate birthday;
        private List<Double> markList;

        public Student(String name, LocalDate birthday, List<Double> markList) {
            this.name = name;
            this.birthday = birthday;
            this.markList = markList;
        }

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }

        public LocalDate getBirthday() {
            return birthday;
        }

        public void setBirthday(LocalDate birthday) {
            this.birthday = birthday;
        }

        public List<Double> getMarkList() {
            return markList;
        }

        public void setMarkList(List<Double> markList) {
            this.markList = markList;
        }

        @Override
        public String toString() {
            return getName();
        }
    }
}
