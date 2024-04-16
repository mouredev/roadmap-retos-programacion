import java.time.LocalTime;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.TimeUnit;

public class Main {

    public static void main(String[] args) {
        asyncFunction("Function Z", 5);
        asyncFunctions();
    }

    /**
     * Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
     * asíncrona una función que tardará en finalizar un número concreto de
     * segundos parametrizables. También debes poder asignarle un nombre.
     * La función imprime su nombre, cuándo empieza, el tiempo que durará
     * su ejecución y cuando finaliza.
     */

    static void asyncFunction(String name, int seconds) {
        var future = CompletableFuture.runAsync(() -> {
            System.out.println(name + " started at " + LocalTime.now() + " and will run for " + seconds + " seconds");
            try {
                TimeUnit.SECONDS.sleep(seconds);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println(name + " finished at " + LocalTime.now());
        });
        future.join();
    }

    /**
     * DIFICULTAD EXTRA (opcional):
     * Utilizando el concepto de asincronía y la función anterior, crea
     * el siguiente programa que ejecuta en este orden:
     * - Una función C que dura 3 segundos.
     * - Una función B que dura 2 segundos.
     * - Una función A que dura 1 segundo.
     * - Una función D que dura 1 segundo.
     * - Las funciones C, B y A se ejecutan en paralelo.
     * - La función D comienza su ejecución cuando las 3 anteriores han finalizado
     */

    static void asyncFunctions() {
        var futureA = CompletableFuture.runAsync(() -> asyncFunction("Function A", 1));
        var futureB = CompletableFuture.runAsync(() -> asyncFunction("Function B", 2));
        var futureC = CompletableFuture.runAsync(() -> asyncFunction("Function C", 3));
        CompletableFuture.allOf(futureA, futureB, futureC).join();
        asyncFunction("Function D", 1);
    }
}
