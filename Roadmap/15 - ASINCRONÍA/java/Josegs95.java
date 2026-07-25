import java.time.LocalTime;
import java.util.concurrent.BrokenBarrierException;
import java.util.concurrent.CyclicBarrier;

public class Josegs95 {
    public static void main(String[] args) {
        //Ejercicio
        Thread thread = new Thread(new Task("Tarea 1", 5, false));
        thread.start();

        //Reto
        System.out.println("\n");
        retoFinal();
        System.out.println("Finaliza el programa");
    }

    private static CyclicBarrier barrier;

    public static void retoFinal(){
        Thread thread1 = new Thread(new Task("Función C", 3, true));
        Thread thread2 = new Thread(new Task("Función B", 2, true));
        Thread thread3 = new Thread(new Task("Función A", 1, true));
        Thread thread4 = new Thread(new Task("Función D", 1, false));

        barrier = new CyclicBarrier(3, thread4);

        thread1.start();
        thread2.start();
        thread3.start();
    }

    public static class Task implements Runnable{

        private String name;
        private int duration;
        private boolean useBarrier;

        public Task(String name, int duration, boolean useBarrier){
            this.name = name;
            this.duration = duration;
            this.useBarrier = useBarrier;
        }

        @Override
        public void run() {
            System.out.println(name + " empieza a las " + LocalTime.now() + " y durará " + duration + " segundos");
            try {
                Thread.sleep(duration * 1000);
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
            System.out.println(name + " finaliza a las " + LocalTime.now());

            if (useBarrier){
                try {
                    barrier.await();
                } catch (InterruptedException e) {
                    throw new RuntimeException(e);
                } catch (BrokenBarrierException e) {
                    throw new RuntimeException(e);
                }
            }
        }
    }
}
