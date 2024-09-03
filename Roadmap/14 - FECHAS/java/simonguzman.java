
import java.time.LocalDateTime;
import java.time.Period;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;

public class simonguzman {
    public static void main(String[] args) {
        ejercicioPrincipal();
    }

    static void ejercicioPrincipal(){
        LocalDateTime fechaActual = LocalDateTime.now();
        System.out.println(fechaActual);
        LocalDateTime fechaNacimiento = LocalDateTime.of(2001, 11, 28, 9, 45, 0);
        System.out.println(fechaNacimiento);

        Period periodo = Period.between(fechaNacimiento.toLocalDate(), fechaActual.toLocalDate());
        int aniosTranscurridos = periodo.getYears();
        System.out.println(aniosTranscurridos);
    }

    static void ejercicioAdicional(){

        LocalDateTime fechaNacimiento = LocalDateTime.of(2001, 11, 28, 9, 45, 0);

        List<DateTimeFormatter> formatos = new ArrayList<>();
        DateTimeFormatter formato1 = DateTimeFormatter.ofPattern("dd/MM/yyyy");
        DateTimeFormatter formato2 = DateTimeFormatter.ofPattern("HH:mm:ss");
        DateTimeFormatter formato3 = DateTimeFormatter.ofPattern("DDD");
        DateTimeFormatter formato4 = DateTimeFormatter.ofPattern("EEEE");
        DateTimeFormatter formato5 = DateTimeFormatter.ofPattern("MMMM");
        DateTimeFormatter formato6 = DateTimeFormatter.ofPattern("dd MMMM yyyy");
        DateTimeFormatter formato7 = DateTimeFormatter.ofPattern("yyyy/MM/dd HH:mm");
        DateTimeFormatter formato8 = DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm:ss");
        DateTimeFormatter formato9 = DateTimeFormatter.ofPattern("EEEE, MMM dd, yyyy");
        DateTimeFormatter formato10 = DateTimeFormatter.ofPattern("yyyy.MM.dd G 'at' HH:mm:ss z");
    
        aplicarFormatos(fechaNacimiento, formatos);
    }

    static void aplicarFormatos(LocalDateTime fecha, List<DateTimeFormatter> formatos){
        for (DateTimeFormatter formato:formatos){
            String fechaFormateada = fecha.format(formato);
            System.out.println("Formato: "+formato+" -> "+fechaFormateada);
        }
    }
}
