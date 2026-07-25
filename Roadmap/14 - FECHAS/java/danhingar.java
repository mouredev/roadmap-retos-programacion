
import java.time.LocalDateTime;
import java.time.Month;
import java.time.format.DateTimeFormatter;
import java.time.temporal.ChronoUnit;

public class danhingar {
    public static void main(String[] args) {

        LocalDateTime now = LocalDateTime.now();
        LocalDateTime birthdate = LocalDateTime.of(1997, 3, 2, 16, 30, 10);

        Long years = birthdate.until(now, ChronoUnit.YEARS);

        System.out.println("Años transcurridos " + years);

        // Extra
        DateTimeFormatter format1 = DateTimeFormatter.ofPattern("dd-MM-yyyy");
        DateTimeFormatter format2 = DateTimeFormatter.ofPattern("HH:mm:ss");
        DateTimeFormatter format3 = DateTimeFormatter.ofPattern("dd/MM/YYYY");
        DateTimeFormatter format4 = DateTimeFormatter.ofPattern("YYYY/MM/dd");
        DateTimeFormatter format5 = DateTimeFormatter.ofPattern("YYYY-MM-dd");
        DateTimeFormatter format6 = DateTimeFormatter.ofPattern("YYYY-MM-dd hh:mm:ss a");
        System.out.println(birthdate.format(format1));
        System.out.println(birthdate.format(format2));
        System.out.println(birthdate.format(format3));
        System.out.println(birthdate.format(format4));
        System.out.println(birthdate.format(format5));
        System.out.println(birthdate.getDayOfYear());
        System.out.println(birthdate.getDayOfWeek());
        System.out.println(birthdate.getDayOfMonth());
        System.out.println(Month.of(birthdate.getMonthValue()));
        System.out.println(birthdate.format(format6));
    

    }

}
