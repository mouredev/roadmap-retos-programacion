import java.util.Random;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

public class martinbohorquez {
    public static void main(String[] args) {
        callbackExample();
        orderProcess("Pizza Carbonara");
        orderProcess("Pizza Margarita");
        orderProcess("Pizza Pepperoni");
        orderProcess("Pizza Barbacoa");
    }

    private static void orderProcess(String dishName) {
        orderProcess(dishName, martinbohorquez::confirmOrder, martinbohorquez::orderReady, martinbohorquez::orderDelivered);
    }

    private static void callbackExample() {
        System.out.println("Iniciando el programa...");
        Processor processor = new Processor();
        processor.process(message -> System.out.println("Callback recibido: " + message));
        System.out.println("Programa finalizado.");
    }

    public static void orderProcess(String dishName, ConfirmCallback confirmCallback,
                                    ReadyCallback readyCallback, DeliveredCallback deliveredCallback) {
        ExecutorService executor = Executors.newSingleThreadExecutor();
        executor.submit(() -> {
            Random random = new Random();
            try {
                confirmCallback.execute(dishName);
                TimeUnit.SECONDS.sleep(random.nextInt(1, 10));
                readyCallback.execute(dishName);
                TimeUnit.SECONDS.sleep(random.nextInt(1, 10));
                deliveredCallback.execute(dishName);
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
        });
        executor.shutdown();
    }

    private static void confirmOrder(String dishName) {
        System.out.printf("Tu pedido %s ha sido confirmado!%n", dishName);
    }

    private static void orderReady(String dishName) {
        System.out.printf("Tu pedido %s está listo!%n", dishName);
    }

    private static void orderDelivered(String dishName) {
        System.out.printf("Tu pedido %s ha sido entregado!%n", dishName);
    }

    private interface Callback {
        void execute(String message);
    }

    // Interfaces para los callbacks
    public interface ConfirmCallback {
        void execute(String dishName);
    }

    public interface ReadyCallback {
        void execute(String dishName);
    }

    public interface DeliveredCallback {
        void execute(String dishName);
    }

    private static class Processor {
        public void process(Callback callback) {
            System.out.println("Procesando...");
            try {
                Thread.sleep(4000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            callback.execute("Proceso completo");
        }
    }
}