import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
import java.util.Scanner;
import java.util.TimeZone;
import java.util.concurrent.TimeUnit;

public class MohamedElderkaoui {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        Calendar fechaFinalizacion = Calendar.getInstance();

        // Get user input for countdown end date and time
        while (true) {
            System.out.print("Ingrese la fecha de finalización (dd/MM/yyyy HH:mm:ss): ");
            String fechaFinalizacionStr = scanner.nextLine();

            SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss");
            sdf.setTimeZone(TimeZone.getDefault());  // Assume input is in local time

            try {
                // Parse the user-provided date and set it as UTC
                Date date = sdf.parse(fechaFinalizacionStr);
                fechaFinalizacion.setTime(date);
                fechaFinalizacion.setTimeZone(TimeZone.getTimeZone("UTC"));
                System.out.println("Fecha de finalización parseada correctamente en UTC.");
                break;
            } catch (Exception e) {
                System.out.println("Error al parsear la fecha. Por favor, intente de nuevo.");
            }
        }
        scanner.close();

        // Run the countdown in a separate thread
        Thread countdownThread = new Thread(() -> startCountdown(fechaFinalizacion));
        countdownThread.start();
    }

    private static void startCountdown(Calendar fechaFinalizacion) {
        while (true) {
            Calendar fechaActual = Calendar.getInstance(TimeZone.getTimeZone("UTC"));
            long diferenciaTiempo = fechaFinalizacion.getTimeInMillis() - fechaActual.getTimeInMillis();

            if (diferenciaTiempo <= 0) {
                System.out.println("¡La cuenta atrás ha finalizado!");
                break;
            }

            long dias = TimeUnit.MILLISECONDS.toDays(diferenciaTiempo);
            long horas = TimeUnit.MILLISECONDS.toHours(diferenciaTiempo) % 24;
            long minutos = TimeUnit.MILLISECONDS.toMinutes(diferenciaTiempo) % 60;
            long segundos = TimeUnit.MILLISECONDS.toSeconds(diferenciaTiempo) % 60;

            // Clear console by printing new lines (approximation)
            System.out.print("\033[H\033[2J");  
            System.out.flush();

            System.out.printf("Faltan %02d d as, %02d horas, %02d minutos y %02d segundos.%n",
                    dias, horas, minutos, segundos);

            try {
                Thread.sleep(1000);  // Wait for one second
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }
    }
}
