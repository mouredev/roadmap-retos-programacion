import java.time.LocalDate;
import java.util.Comparator;
import java.util.Date;
import java.util.List;
import java.util.function.Function;

public class danhingar {

    public static void main(String[] args) {
        System.err.println(applyFunc(String::length, "Daniel"));

        Function<Integer, Integer> number = applyMultiplier(5);
        int result = number.apply(5);
        System.out.println(result);

        List<Integer> numbers = List.of(1, 3, 4, 2, 5);
        System.out.println(numbers.stream().map(num -> num * 2).toList());

        System.out.println(numbers.stream().filter(num -> num % 2 == 0).toList());

        System.out.println(numbers.stream().sorted().toList());

        System.out.println(numbers.stream().sorted(Comparator.reverseOrder()).toList());

        System.out.println(numbers.stream().reduce(0, Integer::sum));

        // EXTRA
        List<Student> students = List.of(
                new Student("PEPE", java.sql.Date.valueOf(LocalDate.parse("1987-04-29")), List.of(5.0, 8.5, 3.0, 10.0)),
                new Student("JUAN", java.sql.Date.valueOf(LocalDate.parse("1995-08-04")), List.of(1.0, 9.5, 2.0, 4.0)),
                new Student("LUIS", java.sql.Date.valueOf(LocalDate.parse("2000-12-15")), List.of(4.0, 6.5, 5.0, 2.0)),
                new Student("MATEO", java.sql.Date.valueOf(LocalDate.parse("1980-01-25")), List.of(10.0, 9.0, 9.7, 9.9)));

        //Promedio
        System.out.println(students.stream().map(s -> String.format("%s:%.2f", s.getName(), s.average())).toList());

        //Mejores
        System.out.println(students.stream().filter(s-> s.average()>=9.0).map(Student::getName).toList());

        //Fecha de nacimiento ordenada
        System.out.println(students.stream().sorted(Comparator.comparing(Student::getBirthdate, Comparator.nullsLast(Comparator.reverseOrder()))).toList());

        //Califiación más alta
        System.out.println(students.stream().map(Student::getGrades).flatMap(List::stream).mapToDouble(Double::doubleValue).max().getAsDouble());
    }

    public static <W, X> X applyFunc(Function<W, X> function, W cadena) {
        return function.apply(cadena);
    }

    public static Function<Integer, Integer> applyMultiplier(int n) {
        return (number) -> number * n;
    }

}

class Student {
    private String name;
    private Date birthdate;
    private List<Double> grades;

    public Student(String name, Date birthdate, List<Double> grades) {
        this.name = name;
        this.birthdate = birthdate;
        this.grades = grades;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Date getBirthdate() {
        return birthdate;
    }

    public void setBirthdate(Date birthdate) {
        this.birthdate = birthdate;
    }

    public List<Double> getGrades() {
        return grades;
    }

    public void setGrades(List<Double> grades) {
        this.grades = grades;
    }

    public Double average() {
        return this.grades.stream().reduce(0.0, Double::sum) / this.grades.size();
    }

    @Override
    public String toString() {
        return "Student [name=" + name + ", birthdate=" + birthdate + ", grades=" + grades + "]";
    }

}
