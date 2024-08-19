import java.time.DayOfWeek;

public class vandresca {
    public static void main(String[] args) {
        printDaysOfWeek();

        Order order1 = new Order();
        Order order2 = new Order();
        Order order3 = new Order();
        Order order4 = new Order();
        Order order5 = new Order();
        Order order6 = new Order();
        Order order7 = new Order();
        Order order8 = new Order();
        Order order9 = new Order();
        Order order10 = new Order();
        Order order11 = new Order();
        System.out.println();

        //Ciclo completo del pedido
        System.out.println("Ciclo completo del pedido");
        order1.getOrderSate();
        order1.sendOrder();
        order1.getOrderSate();
        order1.deliverOrder();
        order1.getOrderSate();
        System.out.println();

        //Cancelar en estado pendiente
        System.out.println("Cancelar en estado pendiente");
        order2.getOrderSate();
        order2.cancelOrder();
        System.out.println();

        //Cancelar en estado enviado
        System.out.println("Cancelar en estado enviado");
        order3.getOrderSate();
        order3.sendOrder();
        order3.getOrderSate();
        order3.cancelOrder();
        order3.getOrderSate();
        System.out.println();

        //Cancelar en estado entregado
        System.out.println("Cancelar en estado entregado");
        order4.getOrderSate();
        order4.sendOrder();
        order4.getOrderSate();
        order4.deliverOrder();
        order4.getOrderSate();
        order4.cancelOrder();
        order4.getOrderSate();
        System.out.println();

        //Cancelar en estado cancelado
        System.out.println("Cancelar en estado cancelado");
        order5.getOrderSate();
        order5.cancelOrder();
        order5.getOrderSate();
        order5.cancelOrder();
        order5.getOrderSate();
        System.out.println();

        //Enviar sin estar pendiente
        System.out.println("Enviar sin estar pendiente");
        order6.getOrderSate();
        order6.deliverOrder();
        order6.getOrderSate();
        System.out.println();

        //Enviar estando entregado
        System.out.println("Enviar estando entregado");
        order7.getOrderSate();
        order7.sendOrder();
        order7.getOrderSate();
        order7.deliverOrder();
        order7.getOrderSate();
        order7.sendOrder();
        order7.getOrderSate();
        System.out.println();

        //Enviar estando cancelado
        System.out.println("Enviar estando cancelado");
        order8.getOrderSate();
        order8.cancelOrder();
        order8.getOrderSate();
        order8.sendOrder();
        order8.getOrderSate();
        System.out.println();

        //Entregar estando pendiente
        System.out.println("Entregar estando pendiente");
        order9.getOrderSate();
        order9.deliverOrder();
        order9.getOrderSate();
        System.out.println();

        //Entregar estando entregado
        System.out.println("Entregar estando entregado");
        order10.getOrderSate();
        order10.sendOrder();
        order10.getOrderSate();
        order10.deliverOrder();
        order10.getOrderSate();
        order10.deliverOrder();
        order10.getOrderSate();
        System.out.println();

        //Entregar estando cancelado
        System.out.println("Entregar estando cancelado");
        order11.getOrderSate();
        order11.cancelOrder();
        order11.getOrderSate();
        order11.sendOrder();
        order11.getOrderSate();
    }

    public static void printDaysOfWeek(){
        System.out.println(WeekDay.getDayOfWeek(7));
        System.out.println(WeekDay.getDayOfWeek(6));
        System.out.println(WeekDay.getDayOfWeek(5));
        System.out.println(WeekDay.getDayOfWeek(4));
        System.out.println(WeekDay.getDayOfWeek(3));
        System.out.println(WeekDay.getDayOfWeek(2));
        System.out.println(WeekDay.getDayOfWeek(1));
    }
}

enum WeekDay{
    LUNES(1),
    MARTES(2),
    MIERCOLES(3),
    JUEVES(4),
    VIERNES(5),
    SABADO(6),
    DOMINGO(7);

    private int numberDay = 0;
    WeekDay(int numberDay){
        this.numberDay=numberDay;
    }
    private int getNumberDay(){
        return this.numberDay;
    }

    public static String getDayOfWeek(int numberDay){
        for(WeekDay day: values()){
            if(day.getNumberDay()==numberDay) return day.name();
        }
        return "";
    }
}

 //////////////////////////
 //                      //
 //   DIFICULTAD EXTRA   //
 //                      //
 //////////////////////////

class Order{
    private int id = 0;
    private static int count= 0;
    private OrderState orderState = OrderState.PENDIENTE;

    public Order(){
        count++;
        id = count;
    }

    public void getOrderSate(){
        System.out.println("Estado del pedido "+id+ ":  "+orderState.name());
    }

    public void sendOrder(){
        if(orderState.equals(OrderState.PENDIENTE)){
            orderState = OrderState.ENVIADO;
            System.out.println("El pedido ha cambiado a estado enviado");
        }else{
            System.out.println(">> ERROR: No es posible pasar el pedido a enviado " +
                    "pues no se encuentra en estado pendiente");
        }
    }
    public void cancelOrder(){
        if(orderState.equals(OrderState.PENDIENTE) || orderState.equals(OrderState.ENVIADO)){
            orderState = OrderState.CANCELADO;
            System.out.println("El pedido ha sido cancelado");
        }else if(orderState.equals(OrderState.CANCELADO)){
            System.out.println(">> ERROR: El pedido ya se encuentra cancelado");
        }else if(orderState.equals(OrderState.ENTREGADO)){
            System.out.println(">> ERROR: El pedido no puede ser cancelado pues ya se ha entregado");
        }
    }
    public void deliverOrder(){
        if(orderState.equals(OrderState.ENVIADO)){
            orderState = OrderState.ENTREGADO;
            System.out.println("El pedido ha sido entregado con exito");
        }else if(orderState.equals(OrderState.CANCELADO)){
            System.out.println(">> ERROR: El pedido no ha sido entregado porque ha sido cancelado");
        }else if(orderState.equals(OrderState.PENDIENTE)){
            System.out.println(">> ERROR: Para ser entregado el pedido, primero debe ser enviado");
        }else if(orderState.equals(OrderState.ENTREGADO)){
            System.out.println(">> ERROR: El pedido ya se encuentra entregado");
        }
    }
}

enum OrderState{
    PENDIENTE,
    ENVIADO,
    ENTREGADO,
    CANCELADO;
}
