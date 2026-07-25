import java.util.Random;

public class AnaLauDB {

    // Interfaz para callback simple
    interface Callback {
        void ejecutar(String mensaje);
    }

    // Ejemplo simple de callback
    public static void procesarDatos(String datos, Callback callback) {
        System.out.println("Procesando datos: " + datos);
        // Simular procesamiento
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        // Ejecutar callback
        callback.ejecutar("Datos procesados correctamente");
    }

    // DIFICULTAD EXTRA: Simulador de restaurante
    interface CallbackConfirmacion {
        void confirmar(String plato);
    }

    interface CallbackListo {
        void listo(String plato);
    }

    interface CallbackEntrega {
        void entregado(String plato);
    }

    public static void procesarPedido(String plato,
            CallbackConfirmacion confirmacion,
            CallbackListo listo,
            CallbackEntrega entrega) {
        Random random = new Random();

        // 1. Confirmación
        confirmacion.confirmar(plato);

        try {
            // Tiempo aleatorio entre 1-10 segundos para cocinar
            int tiempoCocinar = random.nextInt(10) + 1;
            Thread.sleep(tiempoCocinar * 1000);

            // 2. Plato listo
            listo.listo(plato);

            // Tiempo aleatorio entre 1-10 segundos para entregar
            int tiempoEntrega = random.nextInt(10) + 1;
            Thread.sleep(tiempoEntrega * 1000);

            // 3. Entrega
            entrega.entregado(plato);

        } catch (InterruptedException e) {
            System.out.println("Error en el procesamiento del pedido");
        }
    }

    public static void main(String[] args) {
        // Ejemplo simple de callback
        System.out.println("=== Ejemplo simple de callback ===");
        procesarDatos("información importante", mensaje -> {
            System.out.println("Callback ejecutado: " + mensaje);
        });

        System.out.println("\n=== Simulador de restaurante ===");

        // Callbacks del restaurante
        CallbackConfirmacion confirmacion = plato -> {
            System.out.println(" Pedido confirmado: " + plato);
            System.out.println(" Comenzando preparación...");
        };

        CallbackListo listo = plato -> {
            System.out.println(" Plato listo: " + plato);
            System.out.println(" Preparando entrega...");
        };

        CallbackEntrega entrega = plato -> {
            System.out.println(" Plato entregado: " + plato);
            System.out.println("¡Que disfrute su comida!");
        };

        // Procesar varios pedidos
        procesarPedido("Pizza Margherita", confirmacion, listo, entrega);
        System.out.println("---");
        procesarPedido("Hamburguesa con papas", confirmacion, listo, entrega);
    }
}
