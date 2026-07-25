public class danhingar {

    public static void main(String[] args) {
        Machine machine = new Machine();
        machine.eat();
        Human human = new Human();
        human.eat();

        //CON ISP
        Machine1 machine1 = new Machine1();
        machine1.work();

        Human1 human1 = new Human1();
        human1.eat();
        human1.work();

        //Extra
        Printer printer1 = new Printer();
        printer1.print("doc.pdf");

        ColorPrinter printer2 = new ColorPrinter();
        printer2.printColor("doc.pdf");

        MultifunctionPrinter printer3 = new MultifunctionPrinter();
        printer3.print("doc.pdf");
        printer3.printColor("doc.pdf");
        printer3.scan("doc.pdf");
        printer3.sendFax("doc.pdf");
    }

}

// SIN ISP
interface WorkerInteface {

    void work();

    void eat();
}

class Human implements WorkerInteface {

    @Override
    public void eat() {
        System.out.println("Comiendo");
    }

    @Override
    public void work() {
        System.out.println("Trabajando");
    }

}

class Machine implements WorkerInteface {

    @Override
    public void eat() {
    }

    @Override
    public void work() {
        System.out.println("Trabajando");
    }

}

// CON ISP

interface WorkInterface {
    void work();

}

interface EatInterface {
    void eat();

}


class Human1 implements WorkInterface,EatInterface {

    @Override
    public void eat() {
        System.out.println("Comiendo");
    }

    @Override
    public void work() {
        System.out.println("Trabajando");
    }

}

class Machine1 implements WorkInterface {

    @Override
    public void work() {
        System.out.println("Trabajando");
    }

}


//EXTRA
interface PrinterInterface{
    void print(String document);
}

interface PrinterColorInterface {
    void printColor(String document);
}

interface ScannerInterface{
    void scan(String document);
}

interface FaxInterface{
    void sendFax(String document);
}

class Printer implements PrinterInterface{

    @Override
    public void print(String document) {
        System.out.printf("Imprimiendo en blanco y negro el documento %s.\n",document);
    }

    
}

class ColorPrinter implements PrinterColorInterface {

    @Override
    public void printColor(String document) {
        System.out.printf("Imprimiendo a color el documento %s.\n",document);
    }

}

class MultifunctionPrinter implements PrinterInterface,PrinterColorInterface,ScannerInterface,FaxInterface {

    @Override
    public void sendFax(String document) {
        System.out.printf("Enviado por fax el documento %s.\n",document);
    }

    @Override
    public void scan(String document) {
        System.out.printf("Escaneando el documento %s.\n",document);
        System.out.printf("Documento %s escaneado.\n",document);
    }

    @Override
    public void printColor(String document) {
        System.out.printf("Imprimiendo a color el documento %s.\n",document);
    }

    @Override
    public void print(String document) {
        System.out.printf("Imprimiendo en blanco y negro el documento %s.\n",document);
    }

    
}




