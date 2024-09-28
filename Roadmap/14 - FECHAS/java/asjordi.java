import java.time.LocalDateTime;
import java.time.Period;
import java.time.format.DateTimeFormatter;
import java.time.format.FormatStyle;

public class Main {

    public static void main(String[] args) {
        calculateYears();
        dateFormat();
    }

    /**
     * Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
     * - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
     * - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
     * Calcula cuántos años han transcurrido entre ambas fechas.
     */
    static void calculateYears() {
        LocalDateTime currentDate = LocalDateTime.now();
        LocalDateTime birthDate = LocalDateTime.of(1999, 1, 10, 9, 30, 5);
        Period p = Period.between(birthDate.toLocalDate(), currentDate.toLocalDate());
        System.out.println("Years: " + p.getYears());
    }

    /**
     * DIFICULTAD EXTRA (opcional):
     * Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
     * 10 maneras diferentes. Por ejemplo:
     * - Día, mes y año.
     * - Hora, minuto y segundo.
     * - Día de año.
     * - Día de la semana.
     * - Nombre del mes.
     */
    static void dateFormat() {
        LocalDateTime date = LocalDateTime.of(1999, 1, 10, 9, 30, 5);
        System.out.println("yyyy-MM-dd HH:mm:ss: -> " + date.format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss")));
        System.out.println("dd/MM/yyyy HH:mm:ss: -> " + date.format(DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm:ss")));
        System.out.println("dd/MM/yyyy -> " + date.format(DateTimeFormatter.ofPattern("dd/MM/yyyy")));
        System.out.println("dd/MM/yyyy HH:mm: -> " + date.format(DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm")));
        System.out.println("hh:mm:ss a -> " + date.format(DateTimeFormatter.ofPattern("hh:mm:ss a")));
        System.out.println("HH:mm:ss -> " + date.format(DateTimeFormatter.ofPattern("HH:mm:ss")));
        System.out.println("yyyy-MM-dd -> " + date.format(DateTimeFormatter.ofPattern("yyyy-MM-dd")));
        System.out.println(DateTimeFormatter.ofLocalizedDate(FormatStyle.FULL).format(date));
        System.out.println(DateTimeFormatter.ofLocalizedDate(FormatStyle.MEDIUM).format(date));
        System.out.println(DateTimeFormatter.ofLocalizedDate(FormatStyle.SHORT).format(date));
        System.out.println("u -> " + date.format(DateTimeFormatter.ofPattern("u")));
        System.out.println("M -> " + date.format(DateTimeFormatter.ofPattern("M")));
        System.out.println("d -> " + date.format(DateTimeFormatter.ofPattern("d")));
    }

}
