package _14_Fechas;
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

import java.time.Duration;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.Period;
import java.time.format.DateTimeFormatter;
public class _14_Fechas {
    public static void main (String[] args){
        //Imprimimos la fecha actual
        LocalDateTime fechaActual= LocalDateTime.now();
        System.out.println(fechaActual);

        //Imprimimos la fecha de mi cumpleaños
        LocalDateTime fechaCumpleaños = LocalDateTime.of(1999,7,22,10,00);
        System.out.println(fechaCumpleaños);

        //Diferencia entre fechas

        // Calculamos la diferencia entre las fechas
        Period edad = Period.between(fechaCumpleaños.toLocalDate(), fechaActual.toLocalDate());

        // Mostramos la diferencia en años, meses y días
        System.out.println("Edad: " + edad.getYears() + " años, " +
                edad.getMonths() + " meses, " +
                edad.getDays() + " días.");

        //Dificultad EXTRA
        DateTimeFormatter formato1 = DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm:ss");
        String cumpleaños1 = fechaCumpleaños.format(formato1);
        System.out.println(cumpleaños1);
        DateTimeFormatter formato2 = DateTimeFormatter.ofPattern("HH:mm:ss");
        String cumpleaños2 = fechaCumpleaños.format(formato2);
        System.out.println(cumpleaños2);
        DateTimeFormatter formato3 = DateTimeFormatter.ofPattern("EEEE");
        String cumpleaños3 = fechaCumpleaños.format(formato3);
        System.out.println(cumpleaños3);
        DateTimeFormatter formato4 = DateTimeFormatter.ofPattern("a");
        String cumpleaños4 = fechaCumpleaños.format(formato4);
        System.out.println(cumpleaños4);
        DateTimeFormatter formato5 = DateTimeFormatter.ofPattern("E");
        String cumpleaños5 = fechaCumpleaños.format(formato5);
        System.out.println(cumpleaños5);
        DateTimeFormatter formato6 = DateTimeFormatter.ofPattern("yyyy");
        String cumpleaños6 = fechaCumpleaños.format(formato6);
        System.out.println(cumpleaños6);
        DateTimeFormatter formato7 = DateTimeFormatter.ofPattern("dd");
        String cumpleaños7 = fechaCumpleaños.format(formato7);
        System.out.println(cumpleaños7);
        DateTimeFormatter formato8 = DateTimeFormatter.ofPattern("h");
        String cumpleaños8 = fechaCumpleaños.format(formato8);
        System.out.println(cumpleaños8);
        DateTimeFormatter formato9 = DateTimeFormatter.ofPattern("EEEE-hh-mm");
        String cumpleaños9 = fechaCumpleaños.format(formato9);
        System.out.println(cumpleaños9);
        DateTimeFormatter formato10 = DateTimeFormatter.ofPattern("yyyy-MM-SSSS");
        String cumpleaños10 = fechaCumpleaños.format(formato10);
        System.out.println(cumpleaños10);

    }
}
