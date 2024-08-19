import java.util.List;
import java.util.Random;
import java.util.concurrent.TimeUnit;
import java.util.function.Function;

/**
 * Un callback en Java es un concepto que permite a una función llamar a otra función.
 * En Java los callbacks se implementan a través de interfaces.
 * Una interfaz de callback es una interfaz con un método que se invocará cuando se produzca un evento en particular.
 * Un objeto que implementa esta interfaz se registra con otro objeto, que llama al método de callback cuando ocurre el evento.
 */

public class Main {

    public static void main(String[] args) {
        System.out.println(saludar("Pedro", s -> s.toUpperCase()));
        procesarPedidos("Ceviche", s -> "Confirmado", s-> "Listo", s -> "Entregado");

    }

    /**
     * EJERCICIO:
     * Explora el concepto de callback en tu lenguaje creando un ejemplo
     * simple (a tu elección) que muestre su funcionamiento.
     * @param nombre Nombre a saludar
     * @param f Callback que transforma el nombre
     * @return Retorna un saludo con el nombre transformado por el callback f
     */
    public static String saludar(String nombre, Function<String, String> f) {
        return "Hola " + f.apply(nombre) + "!";
    }

    /**
     * DIFICULTAD EXTRA (opcional):
     * Crea un simulador de pedidos de un restaurante utilizando callbacks.
     * Estará formado por una función que procesa pedidos.
     * Debe aceptar el nombre del plato, una callback de confirmación, una
     * de listo y otra de entrega.
     * - Debe imprimir un confirmación cuando empiece el procesamiento.
     * - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre procesos.
     * - Debe invocar a cada callback siguiendo un orden de procesado.
     * - Debe notificar que el plato está listo o ha sido entregado.
     * @param nombre
     * @param fConfirmado
     * @param fListo
     * @param fEntregado
     */
    public static void procesarPedidos(String nombre, Function<String, String> fConfirmado, Function<String, String> fListo, Function<String, String> fEntregado) {
        Random r = new Random();
        List<Function<String, String>> procesos = List.of(fConfirmado, fListo, fEntregado);
        System.out.println("Procesando pedido...");

        procesos.forEach(p -> {
            try {
                int t = r.nextInt(1, 11);
                System.out.println("El plato " + nombre + " se encuentra " + p.apply(nombre) + " en " + t + " segundos.");
                TimeUnit.SECONDS.sleep(t);
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
        });

        System.out.println("Pedido procesado exitosamente!");
    }

}
