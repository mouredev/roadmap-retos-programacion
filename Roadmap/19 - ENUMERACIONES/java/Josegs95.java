public class Josegs95 {

    public enum DayOfWeek{
        LUNES("Lunes"),
        MARTES("Martes"),
        MIÉRCOLES("Miércoles"),
        JUEVES("Jueves"),
        VIERNES("Viernes"),
        SÁBADO("Sábado"),
        DOMINGO("Domingo");

        private String title;

        private DayOfWeek(String title){
            this.title = title;
        }

        public static void printDay(int index){
            if (index > DayOfWeek.values().length || index < 1)
                return;
            System.out.println(DayOfWeek.values()[index - 1]);
        }

        @Override
        public String toString() {
            return title;
        }
    }

    public static void main(String[] args) {
        //Ejercicio
        //Día de la semana: 2
        DayOfWeek.printDay(2);

        //Día de la semana: 5
        DayOfWeek.printDay(5);

        //Reto
        retoFinal();
    }

    public static void retoFinal(){
        Order order1 = new Order(1);
        Order order2 = new Order(2);
        Order order3 = new Order(3);

        order1.ship();
        order2.cancel();

        order1.printStatus();
        order2.printStatus();
        order3.printStatus();

        order1.deliver();
        order2.deliver();
        order3.deliver();

        order1.printStatus();
        order2.printStatus();
        order3.printStatus();

        order1.cancel();
    }

    public static class Order{
        private final int id;
        private OrderStatus status;

        enum OrderStatus{
            PENDIENTE,
            ENVIADO,
            ENTREGADO,
            CANCELADO
        }

        Order(int id){
            this.id = id;
            status = OrderStatus.PENDIENTE;
        }

        public void ship(){
            if (status == OrderStatus.CANCELADO){
                System.out.println("El pedido " + id + " ha sido cancelado y no se puede entregar.");
                return;
            } else if (status == OrderStatus.ENTREGADO){
                System.out.println("El pedido " + id + " ya ha sido enviado y entregado.");
                return;
            }
            status = OrderStatus.ENVIADO;
        }

        public void deliver(){
            if (status == OrderStatus.CANCELADO){
                System.out.println("El pedido " + id + " ha sido cancelado y no se puede entregar.");
                return;
            } else if (status == OrderStatus.PENDIENTE){
                System.out.println("El pedido " + id + " necesita ser enviado antes de poder entregarlo.");
                return;
            }
            status = OrderStatus.ENTREGADO;
        }

        public void cancel(){
            if (status == OrderStatus.ENTREGADO){
                System.out.println("El pedido " + id + " ha sido entregado y no se puede cancelar.");
                return;
            }
            status = OrderStatus.CANCELADO;
        }

        public void printStatus(){
            switch (status){
                case PENDIENTE -> System.out.println("El paquete " + id + " está pendiente aún.");
                case ENVIADO -> System.out.println("El paquete " + id + " ha sido enviado.");
                case ENTREGADO -> System.out.println("El paquete " + id + " ha sido entregado.");
                case CANCELADO -> System.out.println("El paquete " + id + " ha sido cancelado.");
            }
        }
    }
}
