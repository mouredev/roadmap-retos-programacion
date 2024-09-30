import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * #27 SOLID: PRINCIPIO ABIERTO-CERRADO (OCP)
 *
 * @author martinbohorquez
 */
public class martinbohorquez {
    public static void main(String[] args) {
        drawFormaTest();
        drawFormOCPTest();

        /*
         * DIFICULTAD EXTRA
         */
        calculatorOCPTest();

    }

    private static void drawFormaTest() {
        Forma forma = new Forma();
        forma.drawSquare();
        forma.drawCircle();
        forma.drawTriangle();
    }

    private static void drawFormOCPTest() {
        Form square = new Square();
        square.draw();
        Form circle = new Circle();
        circle.draw();
        Form triangle = new Triangle();
        triangle.draw();
    }

    static class Forma {
        private void drawSquare() {
            System.out.println("Dibuja un cuadrado!");
        }

        private void drawCircle() {
            System.out.println("Dibuja un círculo!");
        }

        private void drawTriangle() {
            System.out.println("Dibuja un triángulo!");
        }
    }

    interface Form {
        void draw();
    }

    static class Square implements Form {

        @Override
        public void draw() {
            System.out.println("Dibuja un cuadrado!");
        }
    }

    static class Circle implements Form {

        @Override
        public void draw() {
            System.out.println("Dibuja un círculo!");
        }
    }

    static class Triangle implements Form {

        @Override
        public void draw() {
            System.out.println("Dibuja un triángulo!");
        }
    }

    private static void calculatorOCPTest() {
        Calculator calculator = new Calculator();
        calculator.addOperation("addition", new Addition());
        calculator.addOperation("subtraction", new Subtraction());
        calculator.addOperation("multiplication", new Multiplication());
        calculator.addOperation("division", new Division());
        calculator.addOperation("power", new Power());

        calculator.calculate("addition", 10, 5);
        calculator.calculate("subtraction", 10, 5);
        calculator.calculate("multiplication", 10, 5);
        calculator.calculate("division", 10, 2.5);
        calculator.calculate("power", 5, 3);

    }

    interface Operation {
        double execute(double a, double b);
    }

    static class Addition implements Operation {

        @Override
        public double execute(double a, double b) {
            return a + b;
        }
    }

    static class Subtraction implements Operation {

        @Override
        public double execute(double a, double b) {
            return a - b;
        }
    }

    static class Multiplication implements Operation {

        @Override
        public double execute(double a, double b) {
            return a * b;
        }
    }

    static class Division implements Operation {

        @Override
        public double execute(double a, double b) {
            return a / b;
        }
    }

    static class Power implements Operation {

        @Override
        public double execute(double a, double b) {
            return Math.pow(a, b);
        }
    }

    static class Calculator {
        List<Map<String, Operation>> operations;

        public Calculator() {
            operations = new ArrayList<>();
        }

        private void addOperation(String name, Operation operation) {
            Map<String, Operation> operationMap = new HashMap<>();
            operationMap.put(name, operation);
            operations.add(operationMap);
        }

        private void calculate(String name, double a, double b) {
            operations.stream()
                    .filter(o -> o.containsKey(name))
                    .findFirst()
                    .ifPresentOrElse(operation ->
                                    System.out.printf("%s de %.1f y %.1f: %.2f%n",
                                            name, a, b, operation.get(name).execute(a, b)),
                            () -> System.out.printf("La operación '%s' no está soportada", name));
        }
    }
}
