
import java.time.LocalDate;
import java.util.*;
import java.util.function.Consumer;
import java.util.function.Function;
import java.util.stream.Stream;

@FunctionalInterface
interface Greeting {
    void accept(String name);
}

public class Roadmap {
    public static void main(String[] args) throws InterruptedException {
        Consumer<String> greeting = (n) -> System.out.println("Hola bienvenido " + n);
        welcome(greeting,"Amador");
        //EXTRA
        List<Student> students = getStudents();

        //Función para obtener el promedio de calificaciónes dado un estudiante
        Function<Student, Double> fAverage = e -> e.getQualifications().stream().mapToDouble(Double::doubleValue).average().orElse(0.0);
        //Promedio calificaciones: Obtiene una lista de estudiantes por nombre y promedio de sus calificaciones
        HashMap<String,Double> studentsWithAverageQualification = students.stream().collect(
                HashMap::new,
                (mapStudents,student) -> mapStudents.put(student.getName(),fAverage.apply(student)),
                HashMap::putAll
        );
        System.out.println(studentsWithAverageQualification);

        //Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes que tienen calificaciones con un 9 o más de promedio
        List<String> studentsWithPassingGrade = students.stream().filter(s -> fAverage.apply(s) > 9).map(Student::getName).toList();
        System.out.println(studentsWithPassingGrade);

        //Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
        Stream<Student> studentsSortedByAgeAsc = students.stream().sorted(Comparator.comparing(Student::getBirthDate, Comparator.reverseOrder()));
        studentsSortedByAgeAsc.forEach(System.out::println);

        //Mayor calificación: Obtiene la calificación más alta de entre todas las de los alumnos.
        OptionalDouble maxQualification = students.stream().mapToDouble(fAverage::apply).max();
        System.out.println("Calificación más alta es :" + maxQualification.orElse(0d));
    }
    public static void welcome(Consumer<String> f, String name){
        f.accept(name);
    }

    public static List<Student> getStudents(){
        List<Student> students = new ArrayList<>();
        students.add(new Student("Amador", LocalDate.of(1992, 5, 15), List.of(5.00, 8.2, 9.2, 10.00)));
        students.add(new Student("Sofía", LocalDate.of(1993, 3, 22), List.of(4.5, 6.3, 7.0, 8.5)));
        students.add(new Student("Mateo", LocalDate.of(1994, 7, 19), List.of(9.00, 9.0, 10.00, 9.1)));
        students.add(new Student("Isabella", LocalDate.of(1995, 11, 2), List.of(7.3, 4.9, 5.6, 9.1)));
        students.add(new Student("Sebastián", LocalDate.of(1996, 8, 13), List.of(1.2, 3.4, 5.5, 7.6)));
        students.add(new Student("Valentina", LocalDate.of(1997, 6, 25), List.of(10.00,9.0, 9.9, 8.9)));
        students.add(new Student("Daniel", LocalDate.of(1998, 9, 5), List.of(4.3, 5.6, 8.8, 6.1)));
        students.add(new Student("Mariana", LocalDate.of(1999, 2, 12), List.of(3.3, 4.4, 6.6, 7.7)));
        students.add(new Student("Lucas", LocalDate.of(1990, 10, 31), List.of(8.8, 9.9, 7.7, 6.6)));
        students.add(new Student("Martina", LocalDate.of(1991, 12, 24), List.of(5.5, 4.4, 3.3, 2.2)));
        students.add(new Student("Gabriel", LocalDate.of(1992, 4, 7), List.of(6.6, 7.7, 8.8, 9.9)));
        students.add(new Student("Emilia", LocalDate.of(1993, 1, 15), List.of(2.2, 3.3, 4.4, 5.5)));
        students.add(new Student("Diego", LocalDate.of(1994, 3, 30), List.of(7.7, 6.6, 5.5, 4.4)));
        students.add(new Student("Renata", LocalDate.of(1995, 5, 19), List.of(9.9, 9.8, 9.7, 9.00)));
        students.add(new Student("David", LocalDate.of(1996, 7, 14), List.of(1.1, 2.2, 3.3, 4.4)));
        students.add(new Student("Victoria", LocalDate.of(1997, 9, 27), List.of(5.5, 6.6, 7.7, 8.8)));
        students.add(new Student("Jorge", LocalDate.of(1998, 11, 11), List.of(2.3, 4.5, 6.7, 8.9)));
        students.add(new Student("Camila", LocalDate.of(1999, 1, 3), List.of(7.1, 8.2, 9.3, 6.4)));
        students.add(new Student("Miguel", LocalDate.of(2000, 4, 22), List.of(3.6, 4.7, 5.8, 6.9)));
        students.add(new Student("Santiago", LocalDate.of(1991, 6, 18), List.of(4.2, 5.3, 6.4, 7.5)));
        students.add(new Student("Valeria", LocalDate.of(1992, 8, 8), List.of(9.12, 10.00, 9.52, 9.00)));

        return students;
    }

    static class Student {
        private String name;
        private LocalDate birthDate;
        private List<Double> qualifications;

        public Student() {
        }

        public Student(String name, LocalDate birthDate, List<Double> qualifications) {
            this.name = name;
            this.birthDate = birthDate;
            this.qualifications = qualifications;
        }

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }

        public LocalDate getBirthDate() {
            return birthDate;
        }

        public void setBirthDate(LocalDate birthDate) {
            this.birthDate = birthDate;
        }

        public List<Double> getQualifications() {
            return qualifications;
        }

        public void setQualifications(List<Double> qualifications) {
            this.qualifications = qualifications;
        }

        @Override
        public String toString() {
            return "Student{" +
                    "name='" + name + '\'' +
                    ", birthDate=" + birthDate +
                    ", qualifications=" + qualifications +
                    '}';
        }
    }
}

