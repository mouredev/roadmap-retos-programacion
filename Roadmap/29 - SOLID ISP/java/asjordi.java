/*
    El Principio de Segregación de Interfaces (ISP) establece que las implementaciones de una interfaz
    no deben depender de comportamientos que no usen. En otras palabras, una clase no debe implementar métodos que no necesita.
    Por lo cual, es mejor tener muchas interfaces específicas que realicen 1 o 2 tareas que una interfaz general que realice muchas tareas.
 */

public class Main {

    public static void main(String[] args) {
        SimpleBlackAndWhitePrinter bwPrinter = new SimpleBlackAndWhitePrinter();
        SimpleColorPrinter colorPrinter = new SimpleColorPrinter();
        MultifunctionPrinter multifunctionPrinter = new MultifunctionPrinter();

        bwPrinter.printBlackAndWhite();
        colorPrinter.printColor();
        multifunctionPrinter.printBlackAndWhite();
        multifunctionPrinter.printColor();
        multifunctionPrinter.scan();
        multifunctionPrinter.fax();
    }

    /*
        EJERCICIO:
        Explora el "Principio SOLID de Segregación de Interfaces (Interface Segregation Principle, ISP)"
        y crea un ejemplo simple donde se muestre su funcionamiento de forma correcta e incorrecta.
     */

    // Interfaz general que viola el ISP
    public interface Worker {
        void work();
        void eat();
    }

    // Trabajador que solo trabaja
    public static class RobotWorker implements Worker {
        @Override
        public void work() {
            System.out.println("Trabajando...");
        }

        @Override
        public void eat() {
            throw new UnsupportedOperationException("No puede comer");
        }
    }

    // Ejemplo Correcto (Aplicación del ISP)
    // Interfaz específica para trabajar
    public interface Workable {
        void work();
    }

    // Interfaz específica para comer
    public interface Eatable {
        void eat();
    }

    // Trabajador que solo trabaja
    public static class RobotWorker2 implements Workable {
        @Override
        public void work() {
            System.out.println("Trabajando...");
        }
    }

    // Trabajador humano que trabaja y come
    public static class HumanWorker implements Workable, Eatable {
        @Override
        public void work() {
            System.out.println("Trabajando...");
        }

        @Override
        public void eat() {
            System.out.println("Comiendo...");
        }
    }

    /*
        DIFICULTAD EXTRA (opcional):
        Crea un gestor de impresoras.
        Requisitos:
            1. Algunas impresoras sólo imprimen en blanco y negro.
            2. Otras sólo a color.
            3. Otras son multifunción, pueden imprimir, escanear y enviar fax.
        Instrucciones:
            1. Implementa el sistema, con los diferentes tipos de impresoras y funciones.
            2. Aplica el ISP a la implementación.
            3. Desarrolla un código que compruebe que se cumple el principio.
     */

    interface BlackAndWhitePrinter {
        void printBlackAndWhite();
    }

    interface ColorPrinter {
        void printColor();
    }

    interface Scanner {
        void scan();
    }

    interface Fax {
        void fax();
    }

    static class SimpleBlackAndWhitePrinter implements BlackAndWhitePrinter {
        @Override
        public void printBlackAndWhite() {
            System.out.println("Printing in black and white...");
        }
    }

    static class SimpleColorPrinter implements ColorPrinter {
        @Override
        public void printColor() {
            System.out.println("Printing in color...");
        }
    }

    static class MultifunctionPrinter implements BlackAndWhitePrinter, ColorPrinter, Scanner, Fax {

        @Override
        public void printBlackAndWhite() {
            System.out.println("Printing in black and white...");
        }

        @Override
        public void printColor() {
            System.out.println("Printing in color...");
        }

        @Override
        public void fax() {
            System.out.println("Sending fax...");
        }

        @Override
        public void scan() {
            System.out.println("Scanning document...");
        }
    }
}
