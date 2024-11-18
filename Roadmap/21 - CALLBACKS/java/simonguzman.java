import java.util.Random;
import java.util.concurrent.TimeUnit;

public class simonguzman {
    public static void main(String[] args) {
        //callbackExample();
        restaurantExercise();
    }

    /********************** Ejercicio adicional **********************/

    public static void restaurantExercise(){
        RestaurantOrder order = new RestaurantOrder();
        
        // Procesar pedido con callbacks
        order.processOrder("Pizza", 
            (dish) -> System.out.println("Confirmación: Se ha confirmado el pedido de " + dish),
            (dish) -> System.out.println("Listo: El plato " + dish + " está listo para ser servido"),
            (dish) -> System.out.println("Entregado: El plato " + dish + " ha sido entregado")
        ); 
    }
    public static interface ConfirmCallback{
        void OnConfirm(String dish);
    }

    public static interface ReadyCallback{
        void OnReady(String dish);
    }

    public static interface DeliveryCallback{
        void OnDelivery(String dish);
    }

    public static class RestaurantOrder{
        private Random random = new Random();
        public void processOrder(String dish, ConfirmCallback confirmcallback, ReadyCallback readyCallback, DeliveryCallback deliveryCallback){
            confirmcallback.OnConfirm(dish);
            proccessRestaurant(dish, confirmcallback, readyCallback, deliveryCallback);
        }

        public void proccessRestaurant(String dish, ConfirmCallback confirmcallback, ReadyCallback readyCallback, DeliveryCallback deliveryCallback){
            
            try {
                int preparationTime = random.nextInt(10) + 1;
                TimeUnit.SECONDS.sleep(preparationTime);

                readyCallback.OnReady(dish);

                int deliveryTime = random.nextInt(10) + 1;
                TimeUnit.SECONDS.sleep(deliveryTime);

                deliveryCallback.OnDelivery(dish);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    /********************** Ejercicio principal - Ejemplo de Callback **********************/
    public static void callbackExample(){
        System.out.println("Iniciando el programa...");
        Processor processor = new Processor();
        processor.process(message -> System.out.println("Callback recibido: " + message));
        System.out.println("Programa finalizado.");
    }

    public static interface Callback{
        void execute(String message);
    }

    public static class Processor{
        public void process(Callback callback){
            System.out.println("Procesando...");
            try {
                Thread.sleep(2000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            callback.execute("Proceso completo");
        }
    }
}
