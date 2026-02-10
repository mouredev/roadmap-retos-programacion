import java.time.LocalTime;
import java.time.format.DateTimeFormatter;

public class FranDev200 {


    static void main() {

        /*
            EJERCICIO:
            * Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
            * asíncrona una función que tardará en finalizar un número concreto de
            * segundos parametrizables. También debes poder asignarle un nombre.
            * La función imprime su nombre, cuándo empieza, el tiempo que durará
            * su ejecución y cuando finaliza.
         */

        Hilo hilo1 = new Hilo(5, "Hilo 1");
        hilo1.start();

        try {
            hilo1.join();
        }catch (InterruptedException e){
            System.out.println(e.getMessage());
        }


        /*
            DIFICULTAD EXTRA (opcional):
            * Utilizando el concepto de asincronía y la función anterior, crea
            * el siguiente programa que ejecuta en este orden:
            * - Una función C que dura 3 segundos.
            * - Una función B que dura 2 segundos.
            * - Una función A que dura 1 segundo.
            * - Una función D que dura 1 segundo.
            * - Las funciones C, B y A se ejecutan en paralelo.
            * - La función D comienza su ejecución cuando las 3 anteriores han finalizado.
         */

        Hilo a = new Hilo(1, "Funcion A");
        Hilo b = new Hilo(2, "Funcion B");
        Hilo c = new Hilo(3, "Funcion C");
        Hilo d = new Hilo(1, "Funcion D");

        a.start();
        b.start();
        c.start();

        try {
            a.join();
            b.join();
            c.join();
        }catch (InterruptedException e){
            e.getMessage();
        }


        d.start();


    }

    static class Hilo extends Thread {

        int segundos;
        String nombre;

        Hilo(int segundos, String nombre){
            this.segundos = segundos;
            this.nombre = nombre;
        }

        @Override
        public void run() {
            DateTimeFormatter formatter = DateTimeFormatter.ofPattern("HH:mm:ss");
            LocalTime empieza = LocalTime.now();


            System.out.println("\nComienzo de la función: " + nombre + ", a las " + formatter.format(empieza));
            System.out.println("Durará: " +  segundos + " segundos.");

            try {

                Thread.sleep(segundos * 1000);

            }catch (InterruptedException e){
                e.getMessage();
            }

            LocalTime acaba = LocalTime.now();

            System.out.println(nombre + " ha finalizado, a las "  + formatter.format(acaba));
        }
    }


}
