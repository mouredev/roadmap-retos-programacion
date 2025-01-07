import java.util.Random;
import java.util.function.Consumer;

public class danhingar {

    public static void main(String[] args) throws InterruptedException {
        GreetConsumerProcess.greet_process("Daniel", GreetConsumerProcess::greet_callback);
        GreetInterfacesProcess.process("Pepe", new CallbackImpl());

        // Extra
        Restaurant.createOrderWithThread("Pizza Barbacoa");
        Restaurant.createOrderWithThread("Pizza Carbonara");
        Restaurant.createOrderWithThread("Pizza 4 Quesos");
        Restaurant.createOrderWithThread("Pizza Margarita");
    }

}

// Usando Consumer
class GreetConsumerProcess {

    public static void greet_process(String name, Consumer<String> callback) {
        System.out.println("Ejecutando el proceso de saludo...");
        callback.accept(name);
    }

    public static void greet_callback(String name) {
        System.out.printf("Hola, %s", name + "\n");
    }
}

// Usando interfaz
interface Callback {
    void greet(String name);
}

class CallbackImpl implements Callback {

    @Override
    public void greet(String name) {
        System.out.printf("Hola, %s\n", name);
    }

}

class GreetInterfacesProcess {

    static void process(String name, Callback callback) {
        System.out.println("Ejecutando el proceso de saludo...");
        callback.greet(name);
    }

}

// EXTRA

class Restaurant {

    public static void createOrderWithThread(String dishName) {
        Thread thread = new Thread(() -> {
            try {
                orderProcess(dishName, Restaurant::confirmOrder, Restaurant::orderReady,
                        Restaurant::orderDelivered);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        });
        thread.start();

    }

    public static void orderProcess(String dishName, Consumer<String> confirmCallback, Consumer<String> readyCallback,
            Consumer<String> deliveredCallback) throws InterruptedException {
        Random random = new Random();
        confirmCallback.accept(dishName);
        Thread.sleep(random.nextInt(1, 11) * 1000);
        readyCallback.accept(dishName);
        Thread.sleep(random.nextInt(1, 11) * 1000);
        deliveredCallback.accept(dishName);
    }

    public static void confirmOrder(String dishName) {

        System.out.printf("Tu pedido %s ha sido confirmado\n", dishName);
    }

    public static void orderReady(String dishName) {
        System.out.printf("Tu pedido %s está listo\n", dishName);
    }

    public static void orderDelivered(String dishName) {
        System.out.printf("Tu pedido %s ha sido entregado\n", dishName);
    }
}