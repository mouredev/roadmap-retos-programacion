public class Josegs95 {
    public static void main(String[] args) {
        //Ejercicio
        //Forma incorrecta
        WrongPigeon pidgeon1 = new WrongPigeon();
        WrongHuman human1 = new WrongHuman();

        pidgeon1.walk();
        pidgeon1.fly();
        human1.walk();
        human1.fly();

        //Forma correcta
        Pigeon pigeon2 = new Pigeon();
        Human human2 = new Human();

        pigeon2.fly();
        pigeon2.walk();
        human2.walk();

        //Reto
        new Josegs95().retoFinal();
    }

    public void retoFinal(){
        OldPrinter printer1 = new OldPrinter();
        MediumPrinter printer2 = new MediumPrinter();
        ModernPrinter printer3 = new ModernPrinter();

        printer1.print("Texto ejemplo");
        printer2.print("Texto ejemplo");
        printer3.print("Texto ejemplo");

        System.out.println(printer3.scan());
        printer3.fax("Texto por fax");
    }

    //Forma incorrecta
    public interface WrongAnimal{
        public void walk();
        public void fly();
    }
    public static class WrongPigeon implements WrongAnimal{

        @Override
        public void walk() {
            System.out.println("La paloma camina...");
        }

        @Override
        public void fly() {
            System.out.println("La paloma vuela...");
        }
    }
    public static class WrongHuman implements WrongAnimal{

        @Override
        public void walk() {
            System.out.println("El humano camina...");
        }

        @Override
        public void fly() {} //Los humanos no vuelan
    }
    //Forma correcta
    public interface WalkableAnimal{
        public void walk();
    }
    public interface FlyingAnimal {
        public void fly();
    }
    public static class Pigeon implements WalkableAnimal, FlyingAnimal {

        @Override
        public void walk() {
            System.out.println("La paloma camina...");
        }

        @Override
        public void fly() {
            System.out.println("La paloma vuela...");
        }
    }
    public static class Human implements WalkableAnimal{

        @Override
        public void walk() {
            System.out.println("El humano camina...");
        }
    }
    //Reto
    public abstract class Printer{
        public void print(String text){
            System.out.println(text);
        }
    }
    public interface BWPrinter{
        public void printBW(String text);
    }
    public interface ColorPrinter{
        public void printColor(String text);
    }
    public interface MultiFunctionPrinter{
        public String scan();
        public void fax(String text);
    }
    public class OldPrinter extends Printer implements BWPrinter{

        @Override
        public void printBW(String text) {
            super.print("\"" + text + "\" en blanco y negro");
        }

        @Override
        public void print(String text) {
            printBW(text);
        }
    }
    public class MediumPrinter extends Printer implements ColorPrinter{

        @Override
        public void printColor(String text) {
            super.print("\"" + text + "\" a color");
        }

        @Override
        public void print(String text) {
            printColor(text);
        }
    }
    public class ModernPrinter extends Printer implements ColorPrinter, MultiFunctionPrinter{

        @Override
        public void printColor(String text) {
            super.print("\"" + text + "\" a color");
        }

        @Override
        public String scan() {
            return "Texto escaneado";
        }

        @Override
        public void fax(String text) {
            System.out.println("Texto enviado por fax con éxito");
        }

        @Override
        public void print(String text) {
            printColor(text);
        }
    }
}
