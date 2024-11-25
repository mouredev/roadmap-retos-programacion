public class simonguzman {
    public static void main(String[] args) {
        exampleNoIsp();
        exampleIsp();
        adittionalExerciseNoIsp();
        adittionalExerciseIsp();
    }

    /******************************** Ejercicio adicional con isp ********************************/
    static void adittionalExerciseIsp(){
        Printer blackAndWhitePrinter = new BlackAndWhitePrinter();
        blackAndWhitePrinter.print("Documento en blanco y negro");

        ColorPrinter colorPrinter = new ColorOnlyPrinter();
        colorPrinter.printColor("Documento a color");

        MultiFunctionPrinter multiFunctionPrinter = new MultiFunctionPrinter();

        multiFunctionPrinter.print("Documento multifunción en blanco y negro");
        multiFunctionPrinter.printColor("Documento multifunción a color");
        multiFunctionPrinter.scan("Escaneando un documento");
        multiFunctionPrinter.sendFax("Enviando fax del documento");

    }
    static interface Printer {
        void print(String content);
    }
    
    static interface ColorPrinter {
        void printColor(String content);
    }
    
    static interface Scanner {
        void scan(String content);
    }
    
    static interface Fax {
        void sendFax(String content);
    }
    
    static class BlackAndWhitePrinter implements Printer {
        @Override
        public void print(String content) {
            System.out.println("Imprimiendo en blanco y negro: " + content);
        }
    }
    
    static class ColorOnlyPrinter implements ColorPrinter {
        @Override
        public void printColor(String content) {
            System.out.println("Imprimiendo a color: " + content);
        }
    }
    
    static class MultiFunctionPrinter implements Printer, ColorPrinter, Scanner, Fax {
        @Override
        public void print(String content) {
            System.out.println("Imprimiendo en blanco y negro: " + content);
        }
    
        @Override
        public void printColor(String content) {
            System.out.println("Imprimiendo a color: " + content);
        }
    
        @Override
        public void scan(String content) {
            System.out.println("Escaneando: " + content);
        }
    
        @Override
        public void sendFax(String content) {
            System.out.println("Enviando fax: " + content);
        }
    }
    

    /******************************** Ejercicio adicional sin isp ********************************/
    static void adittionalExerciseNoIsp(){
        UniversalPrinter basicPrinter = new BasicPrinter();

        basicPrinter.print("Documento básico en blanco y negro");
        basicPrinter.printColor("Intentando imprimir a color (no soportado)");
        basicPrinter.scan("Intentando escanear (no soportado)");
        basicPrinter.sendFax("Intentando enviar fax (no soportado)");
    }

    static interface UniversalPrinter {
        void print(String content);
        void printColor(String content);
        void scan(String content);
        void sendFax(String content);
    }
    
    static class BasicPrinter implements UniversalPrinter {
        @Override
        public void print(String content) {
            System.out.println("Imprimiendo en blanco y negro: " + content);
        }
    
        @Override
        public void printColor(String content) {
            // No soportado por esta impresora
        }
    
        @Override
        public void scan(String content) {
            // No soportado por esta impresora
        }
    
        @Override
        public void sendFax(String content) {
            // No soportado por esta impresora
        }
    }
    

    /******************************** Ejemplo con isp ********************************/
    static void exampleIsp(){
        Workable robotIsp = new RobotIsp();
        robotIsp.work();

        Employee employee = new Employee();
        employee.work();
        employee.eat();
    }

    static interface Workable {
        void work();
    }

    static interface Eatable {
        void eat();
    }

    static class RobotIsp implements Workable {
        @Override
        public void work() {
            System.out.println("El robot está trabajando.");
        }
    }

    static class Employee implements Workable, Eatable {
        @Override
        public void work() {
            System.out.println("El empleado está trabajando.");
        }

        @Override
        public void eat() {
            System.out.println("El empleado está comiendo.");
        }
    }
    /******************************** Ejemplo sin isp ********************************/
    static void exampleNoIsp(){
        Worker robot = new Robot();
        robot.work();  // Solo debería trabajar
        robot.eat();
    }

    static interface Worker {
        void work();
        void eat();
    }

    static class Robot implements Worker {
        @Override
        public void work() {
            System.out.println("El robot está trabajando.");
        }

        @Override
        public void eat() {
            // No tiene sentido para un robot
        }
    }

}
