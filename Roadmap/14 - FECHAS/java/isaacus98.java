import java.time.LocalDateTime;
import java.time.Month;
import java.time.format.DateTimeFormatter;
import java.time.format.FormatStyle;

/*
 * EJERCICIO:
 * Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
 * - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
 * - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
 * Calcula cuántos años han transcurrido entre ambas fechas.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
 * 10 maneras diferentes. Por ejemplo:
 * - Día, mes y año.
 * - Hora, minuto y segundo.
 * - Día de año.
 * - Día de la semana.
 * - Nombre del mes.
 * (lo que se te ocurra...)
 */

public class Main {
    public static void main(String[] args) {
        LocalDateTime date = LocalDateTime.now();
        LocalDateTime birthdate = LocalDateTime.of(1998, Month.FEBRUARY, 13, 07, 00,00);

        System.out.println("Han transcurrido " + date.minusYears(birthdate.getYear()).getYear() + " años");

        // reto extra
        System.out.println("Dia del año: " + birthdate.getDayOfYear());
        System.out.println("Dia de la semana: " + birthdate.getDayOfWeek());
        System.out.println("Fecha corta: " + birthdate.format(DateTimeFormatter.ofPattern("dd/MM/yyyy")));
        System.out.println("Semana del año: " + birthdate.format(DateTimeFormatter.ofPattern("w")));
        System.out.println("Hora, minuto, segundo: " + birthdate.format(DateTimeFormatter.ofPattern("HH:mm:ss")));
        System.out.println("Nombre del mes: " + birthdate.format(DateTimeFormatter.ofPattern("MMMM")));
        System.out.println("Era: " + birthdate.format(DateTimeFormatter.ofPattern("G")));
        System.out.println("Semana del mes: " + birthdate.format(DateTimeFormatter.ofPattern("F")));
        System.out.println("Trimestre del año: " + birthdate.format(DateTimeFormatter.ofPattern("qqqq")));
        System.out.println("Fecha año-mes-dia: " + birthdate.format(DateTimeFormatter.ofPattern("yyyy-MM-dd")));
    }
}