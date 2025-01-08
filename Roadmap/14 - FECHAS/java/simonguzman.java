
import java.time.LocalDateTime;
import java.time.Period;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;

public class simonguzman {
    public static void main(String[] args) {
        ejercicioPrincipal();
        ejercicioAdicional();
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
        formatos.add(DateTimeFormatter.ofPattern("dd/MM/yyyy"));
        formatos.add(DateTimeFormatter.ofPattern("HH:mm:ss"));
        formatos.add(DateTimeFormatter.ofPattern("DDD"));
        formatos.add(DateTimeFormatter.ofPattern("EEEE"));
        formatos.add(DateTimeFormatter.ofPattern("MMMM"));
        formatos.add(DateTimeFormatter.ofPattern("dd MMMM yyyy"));
        formatos.add(DateTimeFormatter.ofPattern("yyyy/MM/dd HH:mm"));
        formatos.add(DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm:ss"));
        formatos.add(DateTimeFormatter.ofPattern("EEEE, MMM dd, yyyy"));
   
        aplicarFormatos(fechaNacimiento, formatos);
    }

    static void aplicarFormatos(LocalDateTime fecha, List<DateTimeFormatter> formatos){
        for (DateTimeFormatter formato:formatos){
            String fechaFormateada = fecha.format(formato);
            System.out.println("Formato: "+formato+" -> "+fechaFormateada);
        }
    }
}
