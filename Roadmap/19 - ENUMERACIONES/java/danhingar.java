
public class danhingar {

    public static void main(String[] args) {
        System.out.println(Days.valueOf(8));

        // EXTRA
        Order order = new Order(1);
        order.displayStatus();
        order.deliever();
        order.ship();
        order.deliever();
        order.cancel();
    }

    static class Order {
        private static int id;
        private static Status status;

        public Order(int identifier) {
            id = identifier;
            status = Status.PENDIENTE;
        }

        public void ship() {
            if (status.equals(Status.PENDIENTE)) {
                status = Status.ENVIADO;
                displayStatus();
            } else {
                System.out.println("El pedido ya ha sido enviado o cancelado");
            }
        }

        public void deliever() {
            if (status.equals(Status.ENVIADO)) {
                status = Status.ENTREGADO;
                displayStatus();
            } else {
                System.out.println("El pedido necesita ser enviado antes de entregarse");
            }
        }

        public void cancel() {
            if (!status.equals(Status.ENTREGADO)) {
                status = Status.CANCELADO;
                displayStatus();
            } else {
                System.out.println("El pedido no se puede cancelar ya que ya se ha entregado.");
            }
        }

        public void displayStatus() {
            System.out.println("El estado del pedido " + id + " es " + status);
        }

    }

}

enum Days {
    LUNES(1),
    MARTES(2),
    MIERCOLES(3),
    JUEVES(4),
    VIERNES(5),
    SABADO(6),
    DOMINGO(7);

    private int numberDay;

    private Days(int numberDay) {
        this.numberDay = numberDay;
    }

    public static String valueOf(int i) {
        return Days.values().length >= i ? Days.values()[i - 1].name() : "Selecciona un valor entre 1-7";
    }

    public int getNumberDay() {
        return numberDay;
    }

}

enum Status {
    PENDIENTE,
    ENVIADO,
    ENTREGADO,
    CANCELADO;
}
