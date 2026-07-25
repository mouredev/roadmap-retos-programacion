import java.time.*;
import java.time.temporal.ChronoUnit;
import java.time.temporal.TemporalUnit;

public class Josegs95 {
    public static void main(String[] args) {
        new Josegs95().countdown();
    }

    public void countdown(){
        LocalDateTime targetDate = LocalDateTime.of
                (2024, 12, 15, 17, 28, 00);
        ZonedDateTime dateInUTC = targetDate.atZone(ZoneOffset.UTC);

        Thread thread = new Thread(() -> {
            while(true){
                clearConsole();
                if (printCountdown(dateInUTC))
                    break;
                try{
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    throw new RuntimeException(e);
                }
            }
        });
        thread.start();

        try {
            thread.join();
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }
        System.out.println("¡Se ha llegado a la fecha!");

    }

    private boolean printCountdown(ZonedDateTime target){
        LocalDateTime currentDate = LocalDateTime.now(ZoneOffset.UTC);
        Duration duration = Duration.between(currentDate, target);

        if (duration.isZero() || duration.isNegative())
            return true;

        Long days = duration.toDaysPart();
        int hours = duration.toHoursPart();
        int minutes = duration.toMinutesPart();
        int seconds = duration.toSecondsPart();

        System.out.print("Quedan " + days + " días, " + hours + " horas");
        System.out.println(", " + minutes + " minutos y " + seconds + " segundos");

        return false;
    }

    private void clearConsole(){
        String[] command;
        if (System.getProperty("os.name").toLowerCase().contains("windows"))
            command = new String[] {"cmd", "/c", "cls"};
        else
            command = new String[] {"clear"};

        try{
            new ProcessBuilder(command).inheritIO().start().waitFor();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }
}
