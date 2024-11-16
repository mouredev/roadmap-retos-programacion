import java.time.LocalDateTime;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class danhingar {

    public static void main(String[] args) throws InterruptedException {
        Thread thread = taskThread("1", 10);
        thread.start();
        taskExecutor("1", 10);

        // Ejercicio extra
        extraThread();

    }

    private static Thread taskThread(String name, int seconds) {
        return new Thread(() -> {
            try {
                System.out.println("Tarea: " + name + ". Duración: " + seconds + "s. Inicio: " + LocalDateTime.now());
                Thread.sleep(seconds * 1000);
                System.out.println("Tarea: " + name + ". Fin: " + LocalDateTime.now());
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        });
    }

    private static void taskExecutor(String name, int seconds) {
        ExecutorService threadpool = Executors.newCachedThreadPool();
        threadpool.submit(() -> {
            System.out.println("Tarea: " + name + ". Duración: " + seconds + "s. Inicio: " + LocalDateTime.now());
            try {
                Thread.sleep(seconds * 1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println("Tarea: " + name + ". Fin: " + LocalDateTime.now());
        });
        threadpool.shutdown();
    }

    private static void extraThread() {
        Thread threadC = taskThread("C", 3);
        Thread threadB = taskThread("B", 2);
        Thread threadA = taskThread("A", 1);

        threadC.start();
        threadB.start();
        threadA.start();

        try {
            threadC.join();
            threadB.join();
            threadA.join();
        } catch (Exception e) {
            System.out.println("Error al terminar la ejecución");
        }

        Thread threadD = taskThread("D", 1);
        threadD.start();
    }
}
