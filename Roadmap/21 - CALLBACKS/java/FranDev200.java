import java.util.Random;
import java.util.Scanner;

public class FranDev200 {

    interface Callback{
        void mensajeFinal(String mensaje);
    }

    static class Temporizador implements Runnable{

        public void cuentaAtras(Callback callback){

            System.out.println("Inciando la cuenta atrás...");

            run();

            String mensajeCallback = "Tiempo finalizado";

            callback.mensajeFinal(mensajeCallback);

        }

        @Override
        public void run() {

            int contador = 3;

            while (true) {

                if(contador != 0){
                    System.out.println(contador-- + "...");
                }else{
                    System.out.println(contador--);
                }


                if(contador < 0){
                    break;
                }

                try {
                    Thread.sleep(1000);
                }catch (InterruptedException e){
                    System.out.println(e.getMessage());
                }

            }


        }
    }

    static void main() {

        /*

        EJERCICIO:
         * Explora el concepto de callback en tu lenguaje creando un ejemplo
         * simple (a tu elección) que muestre su funcionamiento.

         */

        Temporizador temporizador = new Temporizador();

        temporizador.cuentaAtras(new Callback(){

            public void mensajeFinal(String mensaje){

                System.out.println(mensaje);

                System.out.println("Cerrando el temporizador...");

            }

        });

        System.out.println("Mensaje, fuera del temporizador.");
        System.out.println("Terminando el programa.");


        /*

        DIFICULTAD EXTRA (opcional):
         * Crea un simulador de pedidos de un restaurante utilizando callbacks.
         * Estará formado por una función que procesa pedidos.
         * Debe aceptar el nombre del plato, una callback de confirmación, una
         * de listo y otra de entregaDomicilio.
         * - Debe imprimir un confirmación cuando empiece el procesamiento.
         * - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre
         *   procesos.
         * - Debe invocar a cada callback siguiendo un orden de procesado.
         * - Debe notificar que el plato está listo o ha sido entregado.

         */

        System.out.println("\nEjercicio Extra");

        Scanner sc = new Scanner(System.in);
        boolean entregaDomicilio = false;

        Pedido pedido1 = new Pedido();
        Pedido pedido2 = new Pedido();
        Pedido pedido3 = new Pedido();
        Pedido pedido4 = new Pedido();

        entregaDomicilio = pedir(sc);
        System.out.print("Que quiere para comer: ");
        String comando = sc.nextLine();

        pedido1.realizarPedido(comando, new Callback2() {
            @Override
            public void confirmacion(String plato) {
                System.out.println("Su pedido ha sido recibido correctamente.");
                System.out.println(" - Plato: " + plato);
            }

            @Override
            public void preparado(String plato) {
                System.out.println("Ya ha sido preparado el plato.");
            }

            @Override
            public void entregado(String plato) {
                System.out.println(plato + " entregado/a");
            }
        }, entregaDomicilio);

        entregaDomicilio = pedir(sc);
        System.out.print("Que quiere para comer: ");
        comando = sc.nextLine();


        pedido2.realizarPedido(comando, new Callback2() {
            @Override
            public void confirmacion(String plato) {
                System.out.println("Su pedido ha sido recibido correctamente.");
                System.out.println(" - Plato: " + plato);
            }

            @Override
            public void preparado(String plato) {
                System.out.println("Ya ha sido preparado el plato.");
            }

            @Override
            public void entregado(String plato) {
                System.out.println(plato + " entregado/a");
            }
        },  entregaDomicilio);

        entregaDomicilio = pedir(sc);
        System.out.print("Que quiere para comer: ");
        comando = sc.nextLine();

        pedido3.realizarPedido(comando, new Callback2() {
            @Override
            public void confirmacion(String plato) {
                System.out.println("Su pedido ha sido recibido correctamente.");
                System.out.println(" - Plato: " + plato);
            }

            @Override
            public void preparado(String plato) {
                System.out.println("Ya ha sido preparado el plato.");
            }

            @Override
            public void entregado(String plato) {
                System.out.println(plato + " entregado/a");
            }
        },  entregaDomicilio);

        entregaDomicilio = pedir(sc);
        System.out.print("Que quiere para comer: ");
        comando = sc.nextLine();

        pedido4.realizarPedido(comando, new Callback2() {
            @Override
            public void confirmacion(String plato) {
                System.out.println("Su pedido ha sido recibido correctamente.");
                System.out.println(" - Plato: " + plato);
            }

            @Override
            public void preparado(String plato) {
                System.out.println("Ya ha sido preparado el plato.");
            }

            @Override
            public void entregado(String plato) {
                System.out.println(plato + " entregado/a");
            }
        },  entregaDomicilio);

    }

    private static boolean pedir(Scanner sc) {

        boolean retorno = false;

        System.out.print("\nModo de entregaDomicilio [Domicilio | Caja]");
        String respuesta = sc.nextLine();

        if(respuesta.equals("Domicilio")){
            retorno = true;
        }else if(respuesta.equals("Caja")){
            retorno = false;
        }
        return retorno;
    }

    static class  Pedido{

        public void realizarPedido(String nombrePlato, Callback2 callback, boolean entregaDomicilio){

            Random rand = new Random();

            callback.confirmacion(nombrePlato);

            System.out.println("Su plato esta preparandose.");

            int tiempoPreparar = rand.nextInt(10) + 1;

            System.out.println("Tardará unos " + tiempoPreparar + " segundos.");

            try {
                Thread.sleep(tiempoPreparar * 1000);
            } catch (InterruptedException e) {
                System.out.println(e.getMessage());
            }

            callback.preparado(nombrePlato);

            if(entregaDomicilio){

                int tiempoEntrega = rand.nextInt(10) + 1;

                System.out.println("Su plato se entregará en " +  tiempoEntrega + " segundos.");

                try {
                    Thread.sleep(tiempoEntrega * 1000);
                } catch (InterruptedException e) {
                    System.out.println(e.getMessage());
                }



            }

            callback.entregado(nombrePlato);

            System.out.println("Pedido finalizado con exito.");
        }

    }

    interface Callback2{
        void confirmacion(String plato);
        void preparado(String plato);
        void entregado(String plato);
    }

}
