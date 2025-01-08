package ejercicio14;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.Instant;
import java.time.LocalTime;
import java.time.Month;
import java.time.ZonedDateTime;
import java.time.format.DateTimeFormatter;
import java.time.temporal.ChronoUnit;
import java.time.temporal.TemporalUnit;
import java.util.Locale;
import java.util.Scanner;


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
public class JesusWay69 {

    public static void main(String[] args) {

        LocalDate my_birth_date = LocalDate.of(1974, Month.DECEMBER, 26);
        LocalTime my_birth_time = LocalTime.of(7, 30);
        LocalDate current_date = LocalDate.now();
        LocalTime current_time = LocalTime.now();
        int current_hour = current_time.getHour();
        int current_minute = current_time.getMinute();
        int current_second = current_time.getSecond();
        String[] week_days = {"Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"};
        String[] months = {"Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"};
        LocalDateTime current_datetime = LocalDateTime.now();
        Instant current_gmt_datetime = Instant.now();
        ZonedDateTime current_location_datetime = ZonedDateTime.now();
        DateTimeFormatter esDateFormat = DateTimeFormatter.ofPattern("dd/MM/yyyy hh:mm:ss").localizedBy(Locale.ITALY);

        System.out.println("La fecha actual es: " + current_date);
        System.out.println("La hora actual es: " + current_time);
        System.out.println("Son las " + current_hour + " horas con " + current_minute + " minutos y " + current_second + " segundos.");
        System.out.println("La fecha y hora actual es: " + current_datetime);
        System.out.println("La fecha y hora GMT o UTC actual es: " + current_gmt_datetime);
        System.out.println("La fecha y hora actuales en mi ubicación son: " + current_location_datetime);
        System.out.println("Fecha de mi cumpleaños: " + my_birth_date);
        System.out.println("Fecha y hora de mi cumpleaños: " + my_birth_date.atTime(my_birth_time));
        System.out.println("Fecha y hora de mi cumpleaños2: "
                + my_birth_date.getDayOfWeek()
                + " -> " + my_birth_date.getDayOfMonth()
                + "/" + months[my_birth_date.getMonthValue() - 1]
                + "/" + my_birth_date.getYear()
                + " -> " + my_birth_time.getHour()
                + ":" + my_birth_time.getMinute());
        System.out.println("Día de la semana que nací: " + my_birth_date.getDayOfWeek());
        System.out.println("Día de la semana que nací en español: " + week_days[my_birth_date.getDayOfWeek().getValue() - 1]);
        System.out.println("Día del año que nací: " + my_birth_date.getDayOfYear());
        System.out.println(esDateFormat);
        System.out.println("\n\n\n");

        show_data(input_data(), week_days, months);

    }

    public static LocalDate input_data() {
        Scanner sc = new Scanner(System.in);
        String[] thirdy_days_months = {"", "", "", "Abril", "", "Junio", "", "", "Septiembre", "", "Noviembre", ""};
        while (true) {
            System.out.print("\nEscriba su AÑO de nacimiento: ");
            String year = sc.next();
            if (year.length() > 4 || !year.matches("[0-9]{4}")) {
                System.out.println("ERROR: El año debe ser numérico de 4 cifras");
                continue;
            } else if (Integer.parseInt(year) < 1900) {
                System.out.println("Aunque seas demasiado viejo no creo que hayas nacido antes de 1900, intenta con otro año posterior");
                continue;
            } else if (Integer.parseInt(year) > LocalDate.now().getYear()) {
                System.out.println("A no ser que vengas del futuro no puedes poner un año al que todavía no hemos llegado, intenta de nuevo");
                continue;
            } else if (Integer.parseInt(year) >= LocalDate.now().getYear() - 3 && Integer.parseInt(year) <= LocalDate.now().getYear()) {
                System.out.println("Te has debido equivocar de año porque un bebé no sabe teclear en un ordenador, intenta de nuevo");
                continue;
            }
            while (true) {
                System.out.print("\nEscriba el número de su MES de nacimiento: ");
                String month = sc.next();
                if (!month.matches("[1-9]{1,2}") || month.length() > 2 || month.length() <= 0) {
                    System.out.println("ERROR: El mes debe ser numérico de 1 o 2 cifras");
                    continue;
                } else if (Integer.parseInt(month) < 1 || Integer.parseInt(month) > 12) {
                    System.out.println("ERROR: El mes no puede ser menor a 0 ni mayor a 12");
                    continue;
                }

                while (true) {
                    System.out.print("\nEscriba el DÍA de su nacimiento: ");
                    String day = sc.next();
                    if (!day.matches("[0-9]{1,2}") || day.length() > 2 || day.length() < 1) {
                        System.out.println("ERROR: El día debe ser numérico de 1 o 2 cifras");
                        continue;
                    } else if (("4".equals(month) || "6".equals(month) || "9".equals(month) || "11".equals(month)) && Integer.parseInt(day)>30) {
                        System.out.println("El mes de " + thirdy_days_months[Integer.parseInt(month)-1] + " no puede tener más de 30 días");
                        continue;
                    } else if (Integer.parseInt(day) < 1 || Integer.parseInt(day) > 31) {
                        System.out.println("ERROR: El día no puede ser menor a 0 ni mayor a 31");
                        continue;
                    }
                    if ((Integer.parseInt(year) % 4 != 0 && Integer.parseInt(year) % 100 == 0) || (Integer.parseInt(year) % 400 != 0 && Integer.parseInt(month) == 2 && Integer.parseInt(day) > 28)) {
                        System.out.println("El año " + year + " no fue bisiesto y Febrero no puede tener más de 28 días");
                        break;

                    }
                    return LocalDate.of(Integer.parseInt(year), Integer.parseInt(month), Integer.parseInt(day));
                }
            }

        }

    }

    public static void show_data(LocalDate date_object, String[] week_days, String[] months) {
        String day = Integer.toString(date_object.getDayOfMonth());
        String year = Integer.toString(date_object.getYear());
        long my_age = ChronoUnit.YEARS.between(date_object, LocalDate.now());
        int days_passed = LocalDate.now().getDayOfYear();
        int weeks_passed = LocalDate.now().getDayOfYear() / 7 + 1;
        String current_week_day = week_days[LocalDate.now().getDayOfWeek().getValue() - 1];
        String current_month = months[LocalDate.now().getMonthValue() - 1];

        System.out.println("\nHoy es " + current_week_day + " día " + LocalDate.now().getDayOfMonth() + " de " + current_month + " de " + LocalDate.now().getYear());
        System.out.println("\nY son las " + LocalTime.now().getHour() + " horas y " + LocalTime.now().getMinute() + " munutos.");
        System.out.println("\nEstamos en la semana " + weeks_passed + " y en el día " + days_passed + " de " + LocalDate.now().getYear());

        if (LocalTime.now().getHour() > 6 && LocalTime.now().getHour() < 12) {
            System.out.println("¡¡Buenos Días!!!");
        } else if (LocalTime.now().getHour() >= 12 && LocalTime.now().getHour() <= 20) {
            System.out.println("¡¡Buenas Tardes!!!");
        } else {
            System.out.println("¡¡Buenas Noches!!!");
        }

        System.out.println("\nComo has indicado que naciste el día " + day + " de " + months[date_object.getMonthValue() - 1] + " de " + year);
        System.out.println("(Por cierto naciste un " + week_days[date_object.getDayOfWeek().getValue() - 1] + "...)");

        if (LocalDate.now().getMonthValue() == date_object.getMonthValue() && LocalDate.now().getDayOfMonth() == date_object.getDayOfMonth()) {
            System.out.println("¡¡¡FELICIDADES!!! , hoy cumples " + my_age + " años, casi nada");
        } else {
            System.out.println("...tienes " + my_age + " años.");
        }

    }

}
