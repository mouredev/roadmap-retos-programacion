import java.util.Scanner;
public class simonguzman {
 
    public static void main(String[] args) {
        firstExercise();
        aditionalExercise();
    }
    //************************** First exercise **************************/
    public enum Days{
        LUNES,
        MARTES,
        MIERCOLES,
        JUEVES,
        VIERNES,
        SABADO,
        DOMINGO     
    }
    
    static void firstExercise(){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Ingrese un dia de la semana");
        int n = scanner.nextInt();

        System.out.println("El dia "+n+" corresponde al dia: "+getDay(n));
    }

    static Days getDay(int n){
        Days day = weekDays(n);
        return day;
    }

    static Days weekDays(int n){
        switch (n) {
            case 1: return Days.LUNES;
            case 2: return Days.MARTES;
            case 3: return Days.MIERCOLES;
            case 4: return Days.JUEVES;
            case 5: return Days.VIERNES;
            case 6: return Days.SABADO;
            case 7: return Days.DOMINGO;
            default:
                throw new IllegalArgumentException("ERROR: Numero incorrecto.");
        }
    }

    //************************** Aditional exercise **************************/  
    
    public enum statusOrder{
        PENDIENTE,
        ENVIADO,
        ENTREGADO,
        CANCELADO
    }

    static void aditionalExercise(){
        Order order = new Order(1, statusOrder.PENDIENTE);
        Scanner scanner = new Scanner(System.in);
        int n;
        do { 
            optionsMenu();
            System.out.println("Ingrese una opcion: ");
            n = scanner.nextInt();
            menu(order, n);
        } while (n != 5);
    }

    static void optionsMenu(){
        System.out.println("Menú:");
        System.out.println("1. Enviar pedido");
        System.out.println("2. Entregar pedido");
        System.out.println("3. Cancelar pedido");
        System.out.println("4. Mostrar estado del pedido");
        System.out.println("5. Salir");
    }
    static void menu(Order order, int n){
        switch (n) {
            case 1:
                order.sendOrder();
                break;
                
            case 2:
                order.deliverOrder();
                break;
            case 3:
                order.cancelOrder();
                break;
            case 4:
                System.out.println("Estado del pedido: "+order.getStatus());
                break;
            case 5:
                System.out.println("Saliendo...");
                break;
            default:
                System.out.println("ERROR: opcion incorrecta...");
        }
    }

    static class Order{
        protected double id;
        protected statusOrder status;

        public Order(){

        }

        public Order(double id, statusOrder status){
            this.id = id;
            this.status = statusOrder.PENDIENTE;
        }

        public void sendOrder(){
            if (status == statusOrder.PENDIENTE) {
                status = statusOrder.ENVIADO;
                System.out.println("Pedido: "+id+" ha sido enviado.");
            }else{
                System.out.println("El pedido: "+id+" No se puede enviar ya que no se encuentra pendiente");
            }
        }

        public void deliverOrder(){
            if(status == statusOrder.ENVIADO){
                status = statusOrder.ENTREGADO;
                System.out.println("Pedido: "+id+" ha sido entregado.");
            }else{
                System.out.println("El pedido: "+id+" No se puede enviar ya que no ha sido enviado.");
            }
        }

        public void cancelOrder(){
            if(status == statusOrder.PENDIENTE || status == statusOrder.ENVIADO){
                status = statusOrder.CANCELADO;
                System.out.println("Pedido: "+id+" ha sido cancelado.");
            }else{
                System.out.println("El pedido: "+id+" No se puede cancelar ya que ya ha sido entregado");
            }
        }

        public String getStatus(){
            switch(status){
                case PENDIENTE: return "El pedido esta pendiente";
                case ENVIADO: return "El pedido ha sido enviado";
                case ENTREGADO: return "El pedido ha sido entregado";
                case CANCELADO: return "El pedido esta pendiente";
                default:
                    return "Estado desconocido";
            }
        }

    }
}
