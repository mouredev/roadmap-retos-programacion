import java.util.Random;

public class Josegs95 {
    public static void main(String[] args) {
        //Ejercicio
        int n1 = 25;
        int n2 = 67;
        int result = sum(n1, n2, new Farewell() {
            @Override
            public void goodbye() {
                System.out.println("Los números han sido sumados. Hasta otra!");
            }
        });

        System.out.println(n1 + " + " + n2 + " = " + result);

        //Reto
        retoFinal();
    }

    public static void retoFinal(){
        ClientMessages clientMessages = new ClientMessages() {
            @Override
            public void confirmed(String orderName) {
                System.out.println("Tu pedido '" + orderName + "' está confirmado.");
            }

            @Override
            public void ready(String orderName) {
                System.out.println("Tu pedido '" + orderName + "' está listo para enviar.");
            }

            @Override
            public void delivered(String orderName) {
                System.out.println("Tu pedido '" + orderName + "' ha sido enviado.");
            }
        };
        order("Hamburguesa doble", clientMessages);
        order("Ensalada de pasta", clientMessages);
    }

    public static int sum(int n1, int n2, Farewell farewell){
        int result = n1 + n2;

        farewell.goodbye();

        return result;
    }

    public static void order(String name, ClientMessages clientMessages){
        Random rnd = new Random();
        try{
            clientMessages.confirmed(name);
            Thread.sleep(rnd.nextInt(1, 11) * 1000);

            clientMessages.ready(name);
            Thread.sleep(rnd.nextInt(1, 11) * 1000);

            clientMessages.delivered(name);
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }
    }

    public interface Farewell{
        void goodbye();
    }

    public interface ClientMessages{
        void confirmed(String orderName);
        void ready(String orderName);
        void delivered(String orderName);
    }
}
