package ejercicio15;

import static ejercicio15.JesusWay69.*;
import java.time.LocalTime;
import java.time.temporal.ChronoUnit;
import java.util.logging.Level;
import java.util.logging.Logger;


/*
 * Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
 * asíncrona una función que tardará en finalizar un número concreto de segundos
 * parametrizables. También debes poder asignarle un nombre. La función imprime
 * su nombre, cuándo empieza, el tiempo que durará su ejecución y cuando
 * finaliza.
 */
public class JesusWay69 {

    public static void main(String[] args) throws InterruptedException {
        asynchrone(2, "Hola mundo");
        C myThreadC = new C();
        B myThreadB = new B();
        A myThreadA = new A();
        myThreadC.start();
        myThreadB.start();
        myThreadA.start(); 
        
    }

    static void asynchrone(int waitSeconds, String name) throws InterruptedException {
        LocalTime startTime = LocalTime.now();
        System.out.println("La ejecución de '" + name + "' durará " + waitSeconds + " segundos");
        System.out.println("La ejecución comienza a las " + LocalTime.now().getHour() + ":" + LocalTime.now().getMinute() + ":" + LocalTime.now().getSecond());
        Thread.sleep(waitSeconds * 1000);
        System.out.println("Ejecución terminada a las " + LocalTime.now().getHour() + ":" + LocalTime.now().getMinute() + ":" + LocalTime.now().getSecond());
        LocalTime endTime = LocalTime.now();
        System.out.println("Duración de la ejecución: " + ChronoUnit.SECONDS.between(startTime, endTime) + " segundos.");
    }

 /*
 * DIFICULTAD EXTRA (opcional):
 * Utilizando el concepto de asincronía y la función anterior, crea
 * el siguiente programa que ejecuta en este orden:
 * - Una función C que dura 3 segundos.
 * - Una función B que dura 2 segundos.
 * - Una función A que dura 1 segundo.
 * - Una función D que dura 1 segundo.
 * - Las funciones C, B y A se ejecutan en paralelo.
 * - La función D comienza su ejecución cuando las 3 anteriores han finalizado.
 */
    static void C() throws InterruptedException {
        System.out.println("Función C iniciada a las: " + LocalTime.now().getHour() + ":" + LocalTime.now().getMinute() + ":" + LocalTime.now().getSecond());
        Thread.sleep(3000);
        System.out.println("Función C terminada a las: " + LocalTime.now().getHour() + ":" + LocalTime.now().getMinute() + ":" + LocalTime.now().getSecond());
        D();
    }

    static void B() throws InterruptedException {
        System.out.println("Función B iniciada a las: " + LocalTime.now().getHour() + ":" + LocalTime.now().getMinute() + ":" + LocalTime.now().getSecond());
        Thread.sleep(2000);
        System.out.println("Función B terminada a las: " + LocalTime.now().getHour() + ":" + LocalTime.now().getMinute() + ":" + LocalTime.now().getSecond());
    }

    static void A() throws InterruptedException {
        System.out.println("Función A iniciada a las: " + LocalTime.now().getHour() + ":" + LocalTime.now().getMinute() + ":" + LocalTime.now().getSecond());
        Thread.sleep(1000);
        System.out.println("Función A terminada a las: " + LocalTime.now().getHour() + ":" + LocalTime.now().getMinute() + ":" + LocalTime.now().getSecond());
    }

    static void D() throws InterruptedException {
        System.out.println("Función D iniciada a las: " + LocalTime.now().getHour() + ":" + LocalTime.now().getMinute() + ":" + LocalTime.now().getSecond());
        Thread.sleep(1000);
        System.out.println("Función D terminada a las: " + LocalTime.now().getHour() + ":" + LocalTime.now().getMinute() + ":" + LocalTime.now().getSecond());
    }

}

class C extends Thread {

    @Override
    public void run() {
        try {
            C();
        } catch (InterruptedException ex) {
            Logger.getLogger(C.class.getName()).log(Level.SEVERE, null, ex);
        }

    }
}

class B extends Thread {

    @Override
    public void run() {
        try {
            B();
        } catch (InterruptedException ex) {
            Logger.getLogger(B.class.getName()).log(Level.SEVERE, null, ex);
        }

    }
}

class A extends Thread {

    @Override
    public void run() {
        try {
            A();
        } catch (InterruptedException ex) {
            Logger.getLogger(A.class.getName()).log(Level.SEVERE, null, ex);
        }

    }
}




