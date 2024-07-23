/*
    El Principio de Inversión de Dependencia (DIP) establece que las clases de alto nivel no deben depender de clases de bajo nivel.
    Es decir, se deben fabricar abstracciones mediante interfaces y clases abstractas para asegurarse de que dos módulos
    que deben interactuar entre sí solo se comuniquen a través de estas mismas, y de esta manera para esconder sus implementaciones concretas.
 */

public class Main {

    public static void main(String[] args) {
        Email email = new Email();
        Push push = new Push();
        SMS sms = new SMS();

        SistemaNotificaciones snEmail = new SistemaNotificaciones(email);
        SistemaNotificaciones snPush = new SistemaNotificaciones(push);
        SistemaNotificaciones snSMS = new SistemaNotificaciones(sms);

        snEmail.n.notificar();
        snPush.n.notificar();
        snSMS.n.notificar();
    }

    // Ejemplo Incorrecto (Violación del DIP)
    /*
        Se tiene una clase Impresora que recibe una Factura, lo cual hace que la clase Impresora dependa de la clase Factura.
        Esto viola el DIP, ya que la clase de alto nivel (Impresora) depende de una clase de bajo nivel (Factura).
        En caso de que se quiera para una clase Carta o cualquier otro tipo de documento, se tendría que modificar la clase Impresora.
     */
    static class Factura {
        // Atributos
        // Constructor
        // Métodos
    }

    static class Impresora {
        Factura f;

        public Impresora(Factura f) {
            this.f = f;
        }
    }

    // Ejemplo Correcto (Aplicación del DIP)
    /*
        Se tiene una interfaz Imprimible que define un método imprimir(), y una clase Impresora que recibe un objeto que implemente la interfaz Imprimible.
        De esta forma, la clase Impresora no depende de una clase concreta, sino de una interfaz, lo cual cumple con el DIP.
     */

    interface Imprimible {
        void imprimir();
    }

    static class FacturaDIP implements Imprimible {
        // Atributos
        // Constructor
        // Métodos

        @Override
        public void imprimir() {
            // Imprimir la factura
        }
    }

    static class CartaDIP implements Imprimible {
        // Atributos
        // Constructor
        // Métodos

        @Override
        public void imprimir() {
            // Imprimir la carta
        }
    }

    static class ImpresoraDIP {
        Imprimible i;

        public ImpresoraDIP(Imprimible i) {
            this.i = i;
        }
    }

    /*
        DIFICULTAD EXTRA (opcional):
        Crea un sistema de notificaciones.
        Requisitos:
            1. El sistema puede enviar Email, PUSH y SMS (implementaciones específicas).
            2. El sistema de notificaciones no puede depender de las implementaciones específicas.
        Instrucciones:
            1. Crea la interfaz o clase abstracta.
            2. Desarrolla las implementaciones específicas.
            3. Crea el sistema de notificaciones usando el DIP.
            4. Desarrolla un código que compruebe que se cumple el principio.
     */

    interface Notificable {
        void notificar();
    }

    static class Email implements Notificable {
        @Override
        public void notificar() {
            System.out.println("Enviando notificación por email");
        }
    }

    static class Push implements Notificable {
        @Override
        public void notificar() {
            System.out.println("Enviando notificación por push");
        }
    }

    static class SMS implements Notificable {
        @Override
        public void notificar() {
            System.out.println("Enviando notificación por SMS");
        }
    }

    static class SistemaNotificaciones {
        Notificable n;

        public SistemaNotificaciones(Notificable n) {
            this.n = n;
        }
    }


}
