package _14_Fechas;

import java.time.Duration;
import java.time.LocalDateTime;
import java.time.Period;
import java.time.format.DateTimeFormatter;
import java.util.Locale;

public class FranDev200 {

    static void main() {
        /*

             EJERCICIO:
             * Crea dos variables utilizando los objetos fechaActual (date, o semejante) de tu lenguaje:
             * - Una primera que represente la fechaActual (día, mes, año, hora, minuto, segundo) actual.
             * - Una segunda que represente tu fechaActual de nacimiento (te puedes inventar la hora).
             * Calcula cuántos años han transcurrido entre ambas fechas.

         */

    DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm:ss");

    LocalDateTime fechaActual = LocalDateTime.now();
        System.out.println("Fecha actual: " + formatter.format(fechaActual));

    LocalDateTime fechaNacimiento = LocalDateTime.of(2005, 12, 13, 15, 40, 34);
        System.out.println("Fecha nacimiento: " + formatter.format(fechaNacimiento));

    Period diferenciaFechas = Period.between(fechaNacimiento.toLocalDate(), fechaActual.toLocalDate());

    int anios = diferenciaFechas.getYears();
    int mes = diferenciaFechas.getMonths();
    int dia = diferenciaFechas.getDays();

    Duration diferenciaFechasTiempo = Duration.between(fechaNacimiento, fechaActual);

    long segundosTotales = diferenciaFechasTiempo.getSeconds();
    long horas = segundosTotales / 3600;
    long minutos = (segundosTotales % 3600) / 60;
    long segundos = segundosTotales % 60;

        System.out.println("Tiempo transcurrido desde mi fecha de nacimiento");
        System.out.println("================================================");
        System.out.println("Años: " + anios);
        System.out.println("Meses: " + mes);
        System.out.println("Dias: " + dia);
        System.out.println("----------------");
        System.out.println("Horas: " + horas);
        System.out.println("Minutos: " + minutos);
        System.out.println("Segundos: " + segundos);

        /*

        DIFICULTAD EXTRA (opcional):
         * Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
         * 10 maneras diferentes. Por ejemplo:
         * - Día, mes y año.
         * - Hora, minuto y segundo.
         * - Día de año.
         * - Día de la semana.
         * - Nombre del mes.
         * (lo que se te ocurra...)

         */

    LocalDateTime fechaCumpleanios = LocalDateTime.of(2005, 12, 13, 15, 40, 34);

    DateTimeFormatter formato1 = DateTimeFormatter.ofPattern("dd/MM/yyyy");
    DateTimeFormatter formato2 = DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm:ss");
    DateTimeFormatter formato3 = DateTimeFormatter.ofPattern("DD");
    DateTimeFormatter formato4 = DateTimeFormatter.ofPattern("dd 'de' MMMM 'de' yyyy", new Locale("es", "ES"));
    DateTimeFormatter formato5 = DateTimeFormatter.ofPattern("dd 'de' MM 'de' yyyy");
    DateTimeFormatter formato6 = DateTimeFormatter.ofPattern("MM/dd/yyyy HH:mm:ss");
    DateTimeFormatter formato7 = DateTimeFormatter.ofPattern("dd 'de' MMMM 'de' yyyy", new Locale("en", "USA"));
    DateTimeFormatter formato8 = DateTimeFormatter.ofPattern("EEEE, dd 'de' MMMM 'de' yyyy", new Locale("en", "USA"));
    DateTimeFormatter formato9 = DateTimeFormatter.ofPattern("EEEE, dd 'de' MMMM 'de' yyyy", new Locale("es", "ES"));
    DateTimeFormatter formato10 = DateTimeFormatter.ofPattern("EE, dd 'de' MMM 'de' yyyy", new Locale("es", "ES"));

        System.out.println("\nEJERCICIO EXTRA");
        System.out.println("===============");

        System.out.println(formato1.format(fechaCumpleanios));
        System.out.println(formato2.format(fechaCumpleanios));
        System.out.println("Dia del año: " + formato3.format(fechaCumpleanios));
        System.out.println(formato4.format(fechaCumpleanios));
        System.out.println(formato5.format(fechaCumpleanios));
        System.out.println(formato6.format(fechaCumpleanios));
        System.out.println(formato7.format(fechaCumpleanios));
        System.out.println(formato8.format(fechaCumpleanios));
        System.out.println(formato9.format(fechaCumpleanios));
        System.out.println(formato10.format(fechaCumpleanios));
}


}
