package com.amsoft.roadmap.example29;

import javax.naming.OperationNotSupportedException;

/**
 * ISP: Este principio establece que los clientes no deberían estar obligados a depender de interfaces que no usan
 *
 * */
public class Example29 {
    public static void main(String[] args) {
        NotifiableEmail emailNotification = new EmailNotification();
        emailNotification.sendEmail("hello");
        /*EXTRA*/
        Printer printer = new Printer();
        ColorPrinter colorPrinter = new ColorPrinter();
        MultiFunctionalPrinter multiFunctionalPrinter = new MultiFunctionalPrinter();

        printer.print();
        colorPrinter.colorPrint();
        multiFunctionalPrinter.colorPrint();
        multiFunctionalPrinter.scan();
        multiFunctionalPrinter.sendFax();
    }
}

/*Viola ISP*/
interface Notifiable {
    void sendEmail(String message);
    void sendSMS(String message);
}

/*
* Supongamos que solo quiero implementar el envio de notificación por email
* */
class EmailNotificationBad implements Notifiable {

    @Override
    public void sendEmail(String message) {
        System.out.println("Notification sending email: " + message);
    }

    @Override
    public void sendSMS(String message)  {
        // No necesito implementar pero me obliga y debe lanzar un error
        throw new RuntimeException("Not support");
    }
}

/*
* Para solucionar separamos la interfaz
*
* */

interface NotifiableEmail  {
    void sendEmail(String message);
}

interface NotifiableSMS  {
    void sendSMS(String message);
}

/*Ahora ya no estoy obligado a implementar todo*/

class EmailNotification implements NotifiableEmail{

    @Override
    public void sendEmail(String message) {
        System.out.println("Notification sending email: " + message);
    }
}


/*EXTRA*/
interface Printable {
    void print();
}

interface ColorPrintable {
    void colorPrint();
}

interface Scannable {
    void scan();
}

interface Faxable {
    void sendFax();
}

class Printer implements Printable {

    @Override
    public void print() {
        System.out.println("print monochromatic");
    }
}

class ColorPrinter implements ColorPrintable {

    @Override
    public void colorPrint() {
        System.out.println("print multi color");
    }
}

class MultiFunctionalPrinter implements ColorPrintable, Scannable, Faxable {

    @Override
    public void colorPrint() {
        System.out.println("print multi color");
    }

    @Override
    public void scan() {
        System.out.println("use scan function");
    }

    @Override
    public void sendFax() {
        System.out.println("sending fax");
    }
}
