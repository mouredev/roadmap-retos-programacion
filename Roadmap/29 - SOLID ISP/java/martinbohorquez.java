/**
 * #29 SOLID: PRINCIPIO DE SEGREGACIÓN DE INTERFACES (ISP)
 *
 * @author martinbohorquez
 */
public class martinbohorquez {
    public static void main(String[] args) {
        incorrectISP();
        correctISP();
        /*
         * DIFICULTAD EXTRA
         */
        testPrinter();

    }

    private static void incorrectISP() {
        Worker humano = new Humano();
        humano.work();
        humano.eat();
        Worker maquina = new Machine();
        maquina.work();
        maquina.eat();//incorrecto: no se implementa el método "eat()", pero se obliga a definir.
    }

    private static void correctISP() {
        Human human = new Human();
        human.work();
        human.eat();
        Robot robot = new Robot();
        robot.work();
//        robot.eat();//correcto: no se implementa ni existe el método "eat()" para Robot.
    }

    private static void testPrinter() {
        Printer printer = new PrinterImpl();
        String document = "doc.pdf";
        printer.print(document);
        ColorPrinter colorPrinter = new ColorPrinterImpl();
        colorPrinter.printColor(document);
        Multifunction multifunctionPrinter = new Multifunction();
        multifunctionPrinter.print(document);
        multifunctionPrinter.printColor(document);
        multifunctionPrinter.scan(document);
        multifunctionPrinter.sendFax(document);
    }
}

interface Worker {
    void work();

    void eat();
}

class Humano implements Worker {
    @Override
    public void work() {
        System.out.println("Trabajando!");
    }

    @Override
    public void eat() {
        System.out.println("Comiendo!");
    }
}

class Machine implements Worker {
    @Override
    public void work() {
        System.out.println("Trabajando!");
    }

    @Override
    public void eat() {
        // Robot no comen
    }
}

interface Work {
    void work();
}

interface Eat {
    void eat();
}

class Human implements Work, Eat {
    @Override
    public void work() {
        System.out.println("Trabajando!");
    }

    @Override
    public void eat() {
        System.out.println("Comiendo!");
    }
}

class Robot implements Work {
    @Override
    public void work() {
        System.out.println("Trabajando!");
    }
}

interface Printer {
    void print(String document);
}

interface ColorPrinter {
    void printColor(String document);
}

interface Scanner {
    String scan(String document);
}

interface Fax {
    void sendFax(String document);
}

class PrinterImpl implements Printer {
    @Override
    public void print(String document) {
        System.out.printf("Imprimiendo en blanco y negro el documento '%s'%n", document);
    }
}

class ColorPrinterImpl implements ColorPrinter {
    @Override
    public void printColor(String document) {
        System.out.printf("Imprimiendo a color el documento '%s'%n", document);
    }
}

class Multifunction implements Printer, ColorPrinter, Scanner, Fax {

    @Override
    public void print(String document) {
        System.out.printf("Imprimiendo en blanco y negro el documento '%s'%n", document);
    }

    @Override
    public void printColor(String document) {
        System.out.printf("Imprimiendo a color el documento '%s'%n", document);
    }

    @Override
    public String scan(String document) {
        System.out.printf("Escaneando el documento '%s'%n", document);
        return "Documento " + document + " escaneado.";
    }

    @Override
    public void sendFax(String document) {
        System.out.printf("Enviando por fax el documento '%s'%n", document);
    }
}