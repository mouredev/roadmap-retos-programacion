
import java.util.concurrent.TimeUnit;
import java.util.function.Consumer;

@FunctionalInterface
interface Greeting {
    void accept(String name);
}

public class Roadmap {
    public static void main(String[] args) throws InterruptedException {
        //Callbacks con functional interface, en ese caso la función greetByName recibe una función y un nombre
        Greeting greeting = (n) -> System.out.println("Hola bienvenido " + n);
        GreetingConsumer.greetByName(greeting, "Amador");

        //EXTRA
        String dishOrder = "Tacos";
        Consumer<String> onConfirm = (n) -> System.out.println("Pedido de " + n + " confirmado");
        Consumer<String> onReady = (n) -> System.out.println("Pedido de " + n + " está listo");
        Consumer<String> onDelivery = (n) -> System.out.println("Pedido de " + n + " entregado");

        Restaurant.processOrder(dishOrder, onConfirm, onReady, onDelivery);


    }
}

class GreetingConsumer {
    public static void greetByName(Greeting callback, String name) {
        callback.accept(name);
    }
}

class Restaurant {
    public static void processOrder(
            String orderName,
            Consumer<String> confirm,
            Consumer<String> ready,
            Consumer<String> delivery
    ) throws InterruptedException {
        int durationProcess;
        System.out.println("Preparación del plato");

        durationProcess = (int) (Math.floor(Math.random() * (1 - 10 + 1) + 10));
        System.out.println("Tiempo del proceso confirmación " + durationProcess);
        TimeUnit.SECONDS.sleep(durationProcess);
        confirm.accept(orderName);

        durationProcess = (int) (Math.floor(Math.random() * (1 - 10 + 1) + 10));
        System.out.println("Tiempo del proceso listo " + durationProcess);
        TimeUnit.SECONDS.sleep(durationProcess);
        ready.accept(orderName);

        durationProcess = (int) (Math.floor(Math.random() * (1 - 10 + 1) + 10));
        System.out.println("Tiempo del proceso entregado " + durationProcess);
        TimeUnit.SECONDS.sleep(durationProcess);
        delivery.accept(orderName);
    }
}