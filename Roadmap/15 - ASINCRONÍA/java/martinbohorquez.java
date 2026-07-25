import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.concurrent.CountDownLatch;

import static java.util.concurrent.TimeUnit.SECONDS;

/**
 * #15 ASINCRONÍA
 *
 * @author martinbohorquez
 */
public class martinbohorquez {

    private static final DateTimeFormatter f = DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm:ss");

    public static void main(String[] args) throws InterruptedException {
        CountDownLatch latch = new CountDownLatch(2);
        getTask("tarea 1", 3, latch);
        getTask("tarea 2", 2, latch);
        latch.await();

        /*
         * DIFICULTAD EXTRA
         */
        latch = new CountDownLatch(3);
        System.out.println("[======== DIFICULTAD EXTRA =========]");
        getTask("C", 3, latch);
        getTask("B", 2, latch);
        getTask("A", 1, latch);
        latch.await();
        getTask("D", 1, latch);

    }

    private static void getTask(String tarea, int duration, CountDownLatch latch) throws InterruptedException {
        Task task = new Task(tarea, duration, latch);
        task.start();
//        if (join) task.join();
    }

    public static class Task extends Thread {
        private final int duration;
        private final CountDownLatch latch;

        public Task(String name, int duration, CountDownLatch latch) {
            super(name);
            this.duration = duration;
            this.latch = latch;
        }

        @Override
        public void run() {
            System.out.printf("Tarea: %s | Duración: %d segundos | Inicio: %s%n",
                    getName(), duration, LocalDateTime.now().format(f));
            try {
                SECONDS.sleep(duration);
//                sleep(Duration.ofSeconds(duration));
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
            System.out.printf("Tarea: %s | Fin: %s%n", getName(), LocalDateTime.now().format(f));
            latch.countDown();
            System.out.printf("El contador de %s es: %s%n", getName(), latch.getCount());
        }
    }
}
