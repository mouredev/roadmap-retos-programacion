/*
 * TEORÍA DE CALLBACKS:
 * 
 * Un callback es una función que se pasa como argumento a otra función y se ejecuta
 * después de que ocurra un evento específico o se complete una tarea. En Java, los
 * callbacks se implementan típicamente usando interfaces funcionales o lambdas.
 * 
 * Los callbacks son útiles para:
 * 1. Programación asíncrona
 * 2. Manejo de eventos
 * 3. Personalización de comportamiento
 * 
 * En Java, podemos implementar callbacks de varias formas:
 * 1. Interfaces funcionales
 * 2. Expresiones lambda
 * 3. Referencias a métodos
 */

 import java.util.Random;
 import java.util.concurrent.TimeUnit;
 
 public class eulogioep {
     
     // Interfaces funcionales para los callbacks
     @FunctionalInterface
     interface SimpleCallback {
         void execute();
     }
     
     @FunctionalInterface
     interface StringCallback {
         void execute(String message);
     }
     
     // Ejemplo simple de callback
     public static void procesarTarea(String tarea, SimpleCallback onComplete) {
         System.out.println("Iniciando tarea: " + tarea);
         // Simulamos algún procesamiento
         try {
             Thread.sleep(1000);
         } catch (InterruptedException e) {
             e.printStackTrace();
         }
         
         // Ejecutamos el callback
         onComplete.execute();
     }
     
     // Simulador de pedidos de restaurante
     public static class RestaurantePedidos {
         private Random random = new Random();
         
         public void procesarPedido(
             String plato,
             StringCallback onConfirmacion,
             StringCallback onListo,
             StringCallback onEntrega
         ) {
             // Callback de confirmación
             onConfirmacion.execute("Pedido confirmado: " + plato);
             
             // Simular preparación
             simularTiempo();
             
             // Callback de listo
             onListo.execute("¡" + plato + " está listo!");
             
             // Simular entrega
             simularTiempo();
             
             // Callback de entrega
             onEntrega.execute(plato + " ha sido entregado. ¡Buen provecho!");
         }
         
         private void simularTiempo() {
             try {
                 int tiempoEspera = random.nextInt(10) + 1;
                 System.out.println("Procesando... (" + tiempoEspera + " segundos)");
                 TimeUnit.SECONDS.sleep(tiempoEspera);
             } catch (InterruptedException e) {
                 e.printStackTrace();
             }
         }
     }
     
     public static void main(String[] args) {
         // Ejemplo simple de callback
         System.out.println("=== Ejemplo Simple de Callback ===");
         procesarTarea("Tarea de prueba", () -> 
             System.out.println("¡Tarea completada!")
         );
         
         System.out.println("\n=== Simulador de Restaurante ===");
         RestaurantePedidos restaurante = new RestaurantePedidos();
         
         // Procesamos un pedido usando el simulador
         restaurante.procesarPedido(
             "Paella Valenciana",
             mensaje -> System.out.println("CONFIRMACIÓN: " + mensaje),
             mensaje -> System.out.println("LISTO: " + mensaje),
             mensaje -> System.out.println("ENTREGA: " + mensaje)
         );
     }
 }