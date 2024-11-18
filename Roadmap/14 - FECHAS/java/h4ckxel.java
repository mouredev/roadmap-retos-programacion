import java.time.*;
import java.time.format.DateTimeFormatter;
import java.time.temporal.ChronoUnit;

public class Main {

public static void main(String[] args) {
        // Fecha actual
        LocalDate fechaActual = LocalDate.now();
        // Fecha de nacimiento
        LocalDate fechaNacimiento = LocalDate.of(2005, 4, 15);

        // Calculando la diferencia en años
        long añosTranscurridos = ChronoUnit.YEARS.between(fechaNacimiento, fechaActual);
        System.out.println("Han transcurrido " + añosTranscurridos + " años desde mi nacimiento.");

        /*
         * DIFICULTAD EXTRA 
        */ 
        System.out.println("1. Día, mes y año: " + fechaNacimiento.getDayOfMonth() + "/"
                + fechaNacimiento.getMonthValue() + "/" + fechaNacimiento.getYear());

        System.out.println("2. Hora, minuto y segundo: " + fechaNacimiento.atTime(LocalTime.NOON).getHour() + ":"
                + fechaNacimiento.atTime(LocalTime.NOON).getMinute() + ":"
                + fechaNacimiento.atTime(LocalTime.NOON).getSecond());

        System.out.println("3. Día de año: " + fechaNacimiento.getDayOfYear());

        System.out.println("4. Día de la semana: " + fechaNacimiento.getDayOfWeek());

        System.out.println("5. Nombre del mes: " + fechaNacimiento.getMonth());

        System.out.println("6. Mes abreviado y año: " + fechaNacimiento.getMonth().name().substring(0, 3) + " "
                + fechaNacimiento.getYear());

        System.out.println("7. Hora en formato de 12 horas: "
                + DateTimeFormatter.ofPattern("hh:mm:ss a").format(fechaNacimiento.atTime(LocalTime.NOON)));

        System.out.println("8. Edad en días: " + ChronoUnit.DAYS.between(fechaNacimiento, fechaActual));

        System.out.println("9. Edad en meses: " + ChronoUnit.MONTHS.between(fechaNacimiento, fechaActual));

        System.out.println("10. Día de la semana abreviado, día de mes y año: "
                + fechaNacimiento.getDayOfWeek().name().substring(0, 3) + ", " + fechaNacimiento.getDayOfMonth()
                + " de " + fechaNacimiento.getMonth() + " de " + fechaNacimiento.getYear());
        }
}
