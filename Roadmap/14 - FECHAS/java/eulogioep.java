import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.time.temporal.ChronoUnit;
import java.time.Month;
import java.time.DayOfWeek;

public class eulogioep {
    public static void main(String[] args) {
        // PARTE 1: Crear variables de fecha y calcular años transcurridos
        
        // Creamos la fecha actual usando LocalDateTime.now()
        LocalDateTime fechaActual = LocalDateTime.now();
        
        // Creamos una fecha de nacimiento (ejemplo)
        LocalDateTime fechaNacimiento = LocalDateTime.of(1990, 5, 15, 14, 30, 0);
        
        // Calculamos los años transcurridos entre ambas fechas
        long añosTranscurridos = ChronoUnit.YEARS.between(fechaNacimiento, fechaActual);
        
        System.out.println("Fecha actual: " + fechaActual);
        System.out.println("Fecha de nacimiento: " + fechaNacimiento);
        System.out.println("Años transcurridos: " + añosTranscurridos);
        
        // PARTE 2: DIFICULTAD EXTRA - Formatear la fecha de 10 maneras diferentes
        
        System.out.println("\nDIFERENTES FORMATOS DE FECHA:");
        
        // 1. Día, mes y año
        DateTimeFormatter fmt1 = DateTimeFormatter.ofPattern("dd/MM/yyyy");
        System.out.println("1. Día, mes y año: " + fechaNacimiento.format(fmt1));
        
        // 2. Hora, minuto y segundo
        DateTimeFormatter fmt2 = DateTimeFormatter.ofPattern("HH:mm:ss");
        System.out.println("2. Hora, minuto y segundo: " + fechaNacimiento.format(fmt2));
        
        // 3. Día del año
        System.out.println("3. Día del año: " + fechaNacimiento.getDayOfYear());
        
        // 4. Día de la semana
        System.out.println("4. Día de la semana: " + fechaNacimiento.getDayOfWeek());
        
        // 5. Nombre del mes
        System.out.println("5. Nombre del mes: " + fechaNacimiento.getMonth());
        
        // 6. Formato largo con día de la semana
        DateTimeFormatter fmt6 = DateTimeFormatter.ofPattern("EEEE, d 'de' MMMM 'de' yyyy");
        System.out.println("6. Formato largo: " + fechaNacimiento.format(fmt6));
        
        // 7. Formato corto de 12 horas
        DateTimeFormatter fmt7 = DateTimeFormatter.ofPattern("dd-MM-yy hh:mm a");
        System.out.println("7. Formato 12 horas: " + fechaNacimiento.format(fmt7));
        
        // 8. Semana del año
        System.out.println("8. Semana del año: " + (fechaNacimiento.getDayOfYear() / 7 + 1));
        
        // 9. Trimestre del año
        System.out.println("9. Trimestre del año: " + ((fechaNacimiento.getMonthValue() - 1) / 3 + 1));
        
        // 10. ISO fecha y hora
        System.out.println("10. Formato ISO: " + fechaNacimiento.format(DateTimeFormatter.ISO_LOCAL_DATE_TIME));
    }
}