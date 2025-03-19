public interface DiegoSilvaL {
    static void main(String... args) {
        // Ejemplo sin usar OCP
        var triangle = new Triangle(10, 3);
        System.out.printf("El área del triángulo es: %f%n", getArea(triangle));
        var circle = new Circle(10);
        System.out.printf("El área del círculo es  : %f%n", getArea(circle));

        // Ejemplo usando OCP
        var ocpTriangle = new OcpTriangle(10, 3);
        System.out.printf("El área del triángulo es: %f%n", getArea(ocpTriangle));
        var ocpCircle = new OcpCircle(10);
        System.out.printf("El área del círculo es  : %f%n", getArea(ocpCircle));

        // Dificultad Extra
        System.out.printf("La suma     es:%f%n", getCalculate(new Addition(), 10, 20));
        System.out.printf("La resta    es:%f%n", getCalculate(new Subtraction(), 10, 20));
        System.out.printf("El producto es:%f%n", getCalculate(new Multiplication(), 10, 20));
        System.out.printf("El cociente es:%f%n", getCalculate(new Division(), 10, 20));
        System.out.printf("La potencia es:%f%n", getCalculate(new Power(), 10, 20));

    }

    /**
     * Obteniendo el área de una figura sin usar OCP.
     * Cada vez que hay una nueva figura, se deberá modificar esta función agregando
     * una condición más
     * 
     * @param iShape
     * @return el área de la figura
     */
    static double getArea(IShape iShape) {
        if (iShape instanceof Circle circle)
            return circle.getRadius() * circle.getRadius() * Math.PI;
        if (iShape instanceof Triangle triangle)
            return triangle.getBase() * triangle.getHeight() / 2.0;
        return 0.0;
    }

    /**
     * Obteniendo el área de una figura usando OCP.
     * Como se ve en el código, no necesita conocerse cómo se cálcula cada área.
     * Éste está en la implementación de cada figura.
     * 
     * @param iShape
     * @return el área de la figura
     */
    static double getArea(IOcpShape iShape) {
        return iShape.getArea();
    }

    static double getCalculate(CalculatorTwoNumbers calculator, double a, double b) {
        return calculator.calculate(a, b);
    }
}

/**
 * Interfaz genérica para que se puedan utilizar las figuras
 */
interface IShape {

}

class Triangle implements IShape {
    private final double base;
    private final double height;

    public Triangle(double base, double height) {
        this.base = base;
        this.height = height;
    }

    public double getBase() {
        return base;
    }

    public double getHeight() {
        return height;
    }

}

class Circle implements IShape {
    private final double radius;

    public Circle(double radius) {
        this.radius = radius;
    }

    public double getRadius() {
        return radius;
    }

}

/**
 * Interfaz preparada para aplicar OCP
 * 
 */
interface IOcpShape {
    /**
     * El cálculo del área de cada figura depende de la implementación de la figura
     * 
     * @return
     */
    double getArea();
}

class OcpTriangle implements IOcpShape {
    private final double base;
    private final double height;

    public OcpTriangle(double base, double height) {
        this.base = base;
        this.height = height;
    }

    public double getBase() {
        return base;
    }

    public double getHeight() {
        return height;
    }

    @Override
    public double getArea() {
        return height * base / 2.0;
    }

}

class OcpCircle implements IOcpShape {
    private final double radius;

    public OcpCircle(double radius) {
        this.radius = radius;
    }

    public double getRadius() {
        return radius;
    }

    @Override
    public double getArea() {
        return radius * radius * Math.PI;
    }

}

/**
 * Interfaz de calculadora que permite el cálculo con dos números
 */
interface CalculatorTwoNumbers {
    double calculate(double a, double b);
}

class Addition implements CalculatorTwoNumbers {

    @Override
    public double calculate(double a, double b) {
        return a + b;
    }

}

class Subtraction implements CalculatorTwoNumbers {
    @Override
    public double calculate(double a, double b) {
        return a - b;
    }
}

class Multiplication implements CalculatorTwoNumbers {
    @Override
    public double calculate(double a, double b) {
        return a * b;
    }
}

class Division implements CalculatorTwoNumbers {
    @Override
    public double calculate(double a, double b) {
        return a / b;
    }
}

class Power implements CalculatorTwoNumbers {
    @Override
    public double calculate(double a, double b) {
        return Math.pow(a, b);
    }
}