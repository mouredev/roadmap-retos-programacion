import java.util.ArrayList;
import java.util.Scanner;

public class FranDev200 {

    enum DiasSemana{
        Lunes, Martes, Miercoles, Jueves, Viernes, Sabado, Domingo
    }

    static ArrayList<Pedido> pedidos = new ArrayList<>();

    static void main() {

        /*

         * EJERCICIO:
         * Empleando tu lenguaje, explora la definición del tipo de dato
         * que sirva para definir enumeraciones (Enum).
         * Crea un Enum que represente los días de la semana del lunes
         * al domingo, en ese orden. Con ese enumerado, crea una operación
         * que muestre el nombre del día de la semana dependiendo del número entero
         * utilizado (del 1 al 7).

         */

        Scanner sc = new Scanner(System.in);
/*
        for(int i=1 ; i <= 7 ; i++) {

            System.out.println(i + " --- " + DiasSemana.values()[i - 1]);

        }

        while(true) {

            try {

                System.out.print("Indica un numero del 1 al 7: ");
                int dia = Integer.parseInt(sc.nextLine());
                System.out.println( dia + " --- " + DiasSemana.values()[dia - 1]);

            }catch (ArrayIndexOutOfBoundsException e) {

                System.out.println("Numero fuera de rango.");
                break;

            }catch (NumberFormatException e) {

                System.out.println("Numero invalido.");
                break;

            }



        }


            DIFICULTAD EXTRA (opcional):
            * Crea un pequeño sistema de gestión del estado de pedidos.
            * Implementa una clase que defina un pedido con las siguientes características:
            * - El pedido tiene un identificador y un estado.
            * - El estado es un Enum con estos valores: PENDIENTE, ENVIADO, ENTREGADO y CANCELADO.
            * - Implementa las funciones que sirvan para modificar el estado:
            *   - Pedido enviado
            *   - Pedido cancelado
            *   - Pedido entregado
            *   (Establece una lógica, por ejemplo, no se puede entregar si no se ha enviado, etc...)
            * - Implementa una función para mostrar un texto descriptivo según el estado actual.
            * - Crea diferentes pedidos y muestra cómo se interactúa con ellos.
         */

        pedidos.add(new Pedido("GGTDGT345"));
        pedidos.add(new Pedido("GGTDGT346"));
        pedidos.add(new Pedido("GGTDGT347"));
        pedidos.add(new Pedido("GGTDGT348"));
        pedidos.add(new Pedido("GGTDGT349"));
        pedidos.add(new Pedido("GGTDGT350"));
        pedidos.add(new Pedido("GGTDGT351"));

        System.out.println("\nEjercicio EXTRA");
        System.out.println("===============");

        while (true) {

            int respuesta = 0;
            String id;

            System.out.println("\n- - - - - - - - - - - - - - - - - - - - - - - -");
            System.out.println("1 - Comprobar el estado de los pedidos.");
            System.out.println("2 - Comprobar el estado de un pedido concreto.");
            System.out.println("3 - Cambiar el estado de un pedido.");
            System.out.println("4 - Salir.");
            System.out.println("- - - - - - - - - - - - - - - - - - - - - - - -");
            System.out.print("Respuesta: ");

            try {
                respuesta = Integer.parseInt(sc.nextLine());
            } catch (NumberFormatException e) {
                System.out.println("Error - " + e.getMessage());
            }

            switch (respuesta) {
                case 1:
                    System.out.println("\nEstado de los pedidos:");
                    System.out.println("----------------------");
                    for (Pedido pedido : pedidos) {
                        System.out.println(pedido.getId() + " --> " + pedido.getEstado());
                    }
                    break;

                case 2:

                    System.out.print("Indica el ID del pedido: ");
                    id = sc.nextLine();
                    comprobarEstadoPedido(id);
                    break;

                case 3:
                    System.out.print("Indica el ID del pedido: ");
                    id = sc.nextLine();
                    cambiarEstado(id);
                    break;

                case 4:
                    System.out.println("Saliendo del programa.");
                    System.exit(0);
            }

        }

    }

    public static void comprobarEstadoPedido(String id){

        Pedido pedido = null;

        for(Pedido p : pedidos){
            if(p.getId().equals(id)){
                pedido = p;
                break;
            }
        }

        if(pedido != null){
            System.out.println("El estado del pedido con ID, " + pedido.getId() + ", es " + pedido.getEstado());
        }else{
            System.out.println("Este pedido no está guardado en la Base de Datos.");
        }


    }

    public static void cambiarEstado(String id){

        Scanner sc = new Scanner(System.in);

        Pedido pedido = null;
        for(Pedido p : pedidos){
            if(p.getId().equals(id)){

                pedido = p;

                if(pedido.getEstado().equals(Estado.PENDIENTE)){

                    System.out.println("¿Quieres cancelarlo?[Si|No]");
                    String respuesta =  sc.nextLine();

                    if(respuesta.equalsIgnoreCase("si")){
                        pedido.pedidoCancelado();
                    }else if(respuesta.equalsIgnoreCase("no")){
                        pedido.pedidoEnviado();
                    }

                } else if (pedido.getEstado().equals(Estado.ENVIADO)) {
                    pedido.pedidoEntregado();
                } else if (pedido.getEstado().equals(Estado.ENTREGADO)) {
                    System.out.println("El pedido con id " + pedido.getId() + " ya fue entregado.");
                } else if (pedido.getEstado().equals(Estado.CANCELADO)) {
                    System.out.println("El pedido con id " + pedido.getId() + " fue cancelado anteriormente.");
                }

                break;

            }

        }

        if(pedido == null){
            System.out.println("No se ha encontrado un pedido con ese ID.");
        }


    }

    enum Estado{
        PENDIENTE, ENVIADO, ENTREGADO, CANCELADO
    }

    static class Pedido{
        private String id;
        private Estado estado;

        public Pedido(String id) {
            this.id = id;
            this.estado = Estado.PENDIENTE;
        }

        public String getId() { return id; }

        public void setId(String id) { this.id = id; }

        public Estado getEstado() { return estado; }

        public void setEstado(Estado estado) { this.estado = estado; }

        public void pedidoEnviado(){
            setEstado(Estado.ENVIADO);
            System.out.println("El pedido con ID " + getId() + " ha cambiado de estado a " +  getEstado());
        }

        public void pedidoCancelado(){
            setEstado(Estado.CANCELADO);
            System.out.println("El pedido con ID " + getId() + " ha cambiado de estado a " +  getEstado());
        }

        public  void pedidoEntregado(){
            setEstado(Estado.ENTREGADO);
            System.out.println("El pedido con ID " + getId() + " ha cambiado de estado a " +  getEstado());
            System.out.println("PAQUETE ENTREGADO CON EXITO !!!");
        }

    }

}
