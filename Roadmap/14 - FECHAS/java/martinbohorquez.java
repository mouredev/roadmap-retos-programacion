import java.time.LocalDateTime;
import java.time.Period;
import java.time.format.DateTimeFormatter;

/**
 * #14 FECHAS
 *
 * @author martinbohorquez
 */
public class martinbohorquez {

    public static void main(String[] args) {
        LocalDateTime now = LocalDateTime.now();
        LocalDateTime birthDate = LocalDateTime.of(1994, 9, 26,
                18, 30, 45);
        System.out.printf("La fecha actual es: %s%n", now);
        System.out.printf("La fecha de nacimiento es: %s%n", birthDate);

        System.out.printf("La edad es: %s%n", Period.between(birthDate.toLocalDate(),
                now.toLocalDate()));
        System.out.printf("La edad es: %s%n", Period.between(birthDate.toLocalDate(),
                now.toLocalDate()).getYears());
        System.out.printf("Los meses son: %s%n", Period.between(birthDate.toLocalDate(),
                now.toLocalDate()).getMonths());
        System.out.printf("Los días son: %s%n", Period.between(birthDate.toLocalDate(),
                now.toLocalDate()).getDays());

        /*
         * DIFICULTAD EXTRA
         */
        // Día, mes y año.
        DateTimeFormatter f = DateTimeFormatter.ofPattern("dd/MM/yyyy");
        System.out.printf("La fecha de nacimiento (Día, mes y año) es: %s%n",
                birthDate.toLocalDate().format(f));
        // Hora, minuto y segundo.
        f = DateTimeFormatter.ofPattern("HH:mm:ss");
        System.out.printf("La hora de nacimiento (Hora, mínuto y segundo) es: %s%n",
                birthDate.toLocalTime().format(f));
        // Día del año.
        System.out.printf("La día del año de la fecha nacimiento es: %s%n",
                birthDate.getDayOfYear());
        // Día del mes.
        System.out.printf("El día del mes de la fecha nacimiento es: %s%n",
                birthDate.getDayOfMonth());
        // Día de la semana.
        System.out.printf("El día de la semana de la fecha de nacimiento (Día, mes y año) es: %s%n",
                birthDate.getDayOfWeek().getValue());
        // Nombre del mes.
        System.out.printf("El nombre del mes de la fecha nacimiento es: %s%n",
                birthDate.getMonth().name());
        // Nombre del día de la semana.
        System.out.printf("El nombre del día de la semana de la fecha de nacimiento es: %s%n",
                birthDate.getDayOfWeek().name());

        f = DateTimeFormatter.ofPattern("EE MMM dd HH:mm:ss yyyy");

        System.out.printf("La fecha de nacimiento (Día, mes y año) es: %s%n",
                birthDate.format(f).toUpperCase());
    }
}
