import java.time.*; // Se utiliza la libreria time de JAVA

public class Main {
    public static void main(String[] args) {
        /*
         * EJERCICIO:
         * Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
         * - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
         * - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
         * Calcula cuántos años han transcurrido entre ambas fechas.
         */


        // Ejemplo de utilizacion de los objetos segun la documentacion
        LocalDate diaActual = LocalDate.now(); // Representa la fecha actual
        LocalTime horaLocal = LocalTime.now(); // Representa la hora actual
        LocalDateTime horaDia = LocalDateTime.now(); // Representa las dos anteriores juntas

        System.out.println(diaActual); // 2024-04-18
        System.out.println(horaLocal); // 20:43:58.236592100
        System.out.println(horaDia); // 2024-04-18T20:43:58.236592100


        // Creacion de variables
        LocalDateTime fechaActual = LocalDateTime.now(); // Variable de la fecha actual
        System.out.println("La fecha actual es: " + fechaActual);

        LocalDateTime fechaNacimiento = LocalDateTime.of(1900,1,1,12,12); // Variable de la fecha de nacimiento inventada
        System.out.println("Mi fecha de nacimiento es: " + fechaNacimiento);

        // Calculo de la diferencia
        int difAnos = (fechaActual.getYear() - fechaNacimiento.getYear());
        System.out.println("Hay una diferencia de "+difAnos +" años " + " entre: " +fechaActual.getYear() +" y " +fechaNacimiento.getYear()); // 124

        // Formatos de las fechas:
        /*
         * - Día, mes y año.
         * - Hora, minuto y segundo.
         * - Día de año.
         * - Día de la semana.
         * - Nombre del mes. */

        System.out.println("Formato Dia-Mes-Año:     " +fechaActual.getDayOfMonth() +"-" + fechaActual.getMonthValue() +"-" + fechaActual.getYear()); // Formato Dia-Mes-Año:     18-4-2024
        System.out.println("Formato Hora-Minuto-Segundo:    " + fechaActual.getHour() +"horas " + fechaActual.getMinute() +"minutos " + fechaActual.getSecond() +"segundos"); // Formato Hora-Minuto-Segundo:    23horas 6minutos 35segundos
        System.out.println("Formato Día del año: " + fechaActual.getDayOfYear()); // Formato Día del año: 109
        System.out.println("Formato Día de la semana:  "  + fechaActual.getDayOfWeek()); // Formato Día de la semana:  THURSDAY
        System.out.println("Formato Nombre del mes: " + fechaActual.getMonthValue() +"--->" + fechaActual.getMonth()); // Formato Nombre del mes: 4--->APRIL
        System.out.println("Formato al revés  :" + fechaActual.getSecond() +"segundos " + fechaActual.getMinute() + "minutos " + fechaActual.getHour() + "horas " + fechaActual.getYear() +" " + fechaActual.getMonthValue() +" " + fechaActual.getDayOfMonth()); // Formato al revés  :35segundos 6minutos 23horas 2024 4 18
        
        }
}
