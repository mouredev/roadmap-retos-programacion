import java.util.Arrays;
import java.util.Scanner;

/**
 * #19 ENUMERACIONES
 *
 * @author martinbohorquez
 */
public class martinbohorquez {

    public static void main(String[] args) {
        System.out.println("Ingresar el número de semana que desea consultar(1 al 7):");
        Scanner sc = new Scanner(System.in);
        printDayOfWeek(sc.nextInt());

        /*
         * DIFICULTAD EXTRA: Crea un pequeño sistema de gestión del estado de pedidos.
         */
        Order order1 = new Order(1);
        order1.deliver();
        order1.ship();
        order1.deliver();
        order1.cancel();
        Order order2 = new Order(2);
        order2.ship();
        order2.cancel();
        order2.deliver();
    }

    private static void printDayOfWeek(Integer dayNumber) {
        String day = Arrays.stream(DayWeek.values())
                .filter(d -> d.getNumberDay().equals(dayNumber))
                .map(Enum::name)
                .findFirst()
                .orElse("No existe un día para el número escogido. Debe escoger un número del 1 al 7.");
        System.out.println(day);
    }

    enum DayWeek {
        MONDAY(1),
        TUESDAY(2),
        WEDNESDAY(3),
        THURSDAY(4),
        FRIDAY(5),
        SATURDAY(6),
        SUNDAY(7);
        private Integer numberDay = 0;

        private DayWeek(Integer numberDay) {
            this.numberDay = numberDay;
        }

        private Integer getNumberDay() {
            return numberDay;
        }
    }

    enum OrderStatus {
        PENDING,
        SHIPPED,
        DELIVERED,
        CANCELED;
    }

    private static class Order {
        Integer orderId;
        OrderStatus status;

        public Order(Integer orderId) {
            this.orderId = orderId;
            status = OrderStatus.PENDING;
        }

        private void ship() {
            if (status == OrderStatus.PENDING) {
                status = OrderStatus.SHIPPED;
                displayStatus();
            } else System.out.println("El pedido ya ha sido enviado o cancelado!");
        }

        private void deliver() {
            if (status == OrderStatus.SHIPPED) {
                status = OrderStatus.DELIVERED;
                displayStatus();
            } else System.out.println("El pedido necesita ser enviado antes de entregarse!");
        }

        private void cancel() {
            if (status != OrderStatus.DELIVERED) {
                status = OrderStatus.CANCELED;
                displayStatus();
            } else System.out.println("El pedido ya ha sido entregado, no es posible cancelar!");
        }

        private void displayStatus() {
            System.out.printf("El estado del pedido %d es %s%n", orderId, status);
        }
    }
}
