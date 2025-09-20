import java.time.LocalDateTime;
import java.time.LocalDate;
import java.time.Period;
import java.time.format.DateTimeFormatter;
import java.time.DayOfWeek;
import java.time.Month;

public class AnaLauDB {
    public static void main(String[] args) {

        // 1. Fecha y hora actual
        LocalDateTime ahora = LocalDateTime.now();
        System.out.println("Fecha y hora actual: " + ahora);

        // 2. Fecha de nacimiento
        LocalDateTime nacimiento = LocalDateTime.of(2002, 5, 9, 15, 30, 15);
        System.out.println("Fecha de nacimiento: " + nacimiento);

        // 3. Calcular años transcurridos
        LocalDate hoy = LocalDate.now();
        LocalDate cumple = nacimiento.toLocalDate();
        Period periodo = Period.between(cumple, hoy);
        System.out.println("Años transcurridos: " + periodo.getYears());

        // DIFICULTAD EXTRA: 10 formatos diferentes
        System.out.println("\nFormatos de la fecha de nacimiento:");
        // 1. Día, mes y año
        System.out.println("1. Día/Mes/Año: " + nacimiento.format(DateTimeFormatter.ofPattern("dd/MM/yyyy")));
        // 2. Hora, minuto y segundo
        System.out.println("2. Hora:Minuto:Segundo: " + nacimiento.format(DateTimeFormatter.ofPattern("HH:mm:ss")));
        // 3. Día de la semana
        DayOfWeek diaSemana = nacimiento.getDayOfWeek();
        System.out.println("3. Día de la semana: " + diaSemana);
        // 4. Día del año
        System.out.println("4. Día del año: " + nacimiento.getDayOfYear());
        // 5. Nombre del mes
        Month mes = nacimiento.getMonth();
        System.out.println("5. Nombre del mes: " + mes);
        // 6. Fecha larga
        System.out.println(
                "6. Fecha larga: " + nacimiento.format(DateTimeFormatter.ofPattern("EEEE, d 'de' MMMM 'de' yyyy")));
        // 7. Fecha y hora ISO
        System.out.println("7. ISO: " + nacimiento.toString());
        // 8. Año y mes
        System.out.println("8. Año y mes: " + nacimiento.format(DateTimeFormatter.ofPattern("yyyy-MM")));
        // 9. Solo año
        System.out.println("9. Solo año: " + nacimiento.getYear());
        // 10. Fecha y hora personalizada
        System.out.println(
                "10. Personalizado: " + nacimiento.format(DateTimeFormatter.ofPattern("dd MMM yyyy, hh:mm a")));
    }
}
