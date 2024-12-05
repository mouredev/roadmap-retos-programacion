import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.time.temporal.ChronoUnit;
import java.time.temporal.TemporalUnit;

public class Josegs95 {
    public static void main(String[] args) {
        //Ejercicio
        LocalDateTime nowTime = LocalDateTime.now();
        LocalDateTime birthdayTime = LocalDateTime.of(1995, 02, 28, 17, 30, 0);
        System.out.println("Fecha y hora actual: " + nowTime);
        System.out.println("Fecha y hora cuando nací: " + birthdayTime);

        System.out.println("Años entre mi nacimiento y ahora: " + birthdayTime.until(nowTime, ChronoUnit.YEARS));
        //Reto
        System.out.println("\n");
        retoFinal(birthdayTime);
    }

    public static void retoFinal(LocalDateTime birthdayTime){
        System.out.println("Mi fecha de nacimiento en diferentes formatos: ");
        //Estándar
        System.out.println(birthdayTime);
        //Dia-mes-año
        System.out.println(birthdayTime.format(DateTimeFormatter.ofPattern("dd-MM-YYYY")));
        //Hora-minuto-segundo
        System.out.println(birthdayTime.format(DateTimeFormatter.ofPattern("kk:mm:ss")));
        //Dia del año
        System.out.println(birthdayTime.format(DateTimeFormatter.ofPattern("DDD")));
        //Dia de la semana
        System.out.println(birthdayTime.format(DateTimeFormatter.ofPattern("EEEE")));
        //Nombre del mes
        System.out.println(birthdayTime.format(DateTimeFormatter.ofPattern("LLLL")));
        //Quadrimestre
        System.out.println(birthdayTime.format(DateTimeFormatter.ofPattern("QQ")));
        //Semana del año
        System.out.println(birthdayTime.format(DateTimeFormatter.ofPattern("ww")));
        //Semana del mes
        System.out.println(birthdayTime.format(DateTimeFormatter.ofPattern("W")));
        //Hora-minuto AM/PM
        System.out.println(birthdayTime.format(DateTimeFormatter.ofPattern("hh:mm a")));
        //Dia de la semana, Dia-mes-año, hora:minuto
        System.out.println(birthdayTime.format(DateTimeFormatter.ofPattern("EEEE, dd-MM-YYYY 'a las' kk:mm")));

    }
}
