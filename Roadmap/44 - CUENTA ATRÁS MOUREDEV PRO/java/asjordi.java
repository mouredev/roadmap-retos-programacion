import java.io.IOException;
import java.time.*;
import java.time.format.DateTimeFormatter;

public class asjordi {

    public static void main(String[] args) {
        LocalDateTime targetDate = LocalDateTime.of(2024, 11, 12, 9, 0, 0);
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm:ss");
        ZonedDateTime utcTarget = targetDate.atZone(ZoneId.systemDefault()).withZoneSameInstant(ZoneOffset.UTC);

        Thread t = new Thread(() -> {
            while (true) {
                ZonedDateTime now = ZonedDateTime.now(ZoneOffset.UTC);

                if (now.isAfter(utcTarget)) {
                    System.out.println("¡Cuenta regresiva finalizada!");
                    break;
                }

                Duration duration = Duration.between(now, utcTarget);
                long days = duration.toDays();
                long hours = duration.toHoursPart();
                long minutes = duration.toMinutesPart();
                long seconds = duration.toSecondsPart();

                try {
                    limpiarConsola();
                } catch (IOException | InterruptedException e) {
                    throw new RuntimeException(e);
                }

                System.out.println("Tiempo restante: " + days + " días, " + hours + " horas, " + minutes + " minutos, " + seconds + " segundos");
                System.out.println("Lanzamiento: " + utcTarget.format(formatter));

                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                    break;
                }
            }
        });

        t.start();
    }

    public static void limpiarConsola() throws IOException, InterruptedException {
        if (System.getProperty("os.name").contains("Windows")) new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
        else new ProcessBuilder("clear").inheritIO().start().waitFor();
    }

}
