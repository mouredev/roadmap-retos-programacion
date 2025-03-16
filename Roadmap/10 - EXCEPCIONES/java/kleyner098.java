import java.util.ArrayList;
import java.util.Arrays;

public class kleyner098 {
    /*
     * EJERCICIO:
     * Explora el concepto de manejo de excepciones según tu lenguaje.
     * Fuerza un error en tu código, captura el error, imprime dicho error
     * y evita que el programa se detenga de manera inesperada.
     * Prueba a dividir "10/0" o acceder a un índice no existente
     * de un listado para intentar provocar un error.
     */

    public static void main(String[] args) {

        try {
            int num1 = 10;
            int num2 = 0;
            int num3 = num1 / num2;
            System.out.println(num3);
        } catch (ArithmeticException e) {
            System.out.println("Error, division entre 0");
        }

        try {

            // Mi calculadora solo puede hacer restas si  el primer número es mayor al segundo

            int resultado = calculadora(10, 0, "+");
            // int resultado = calculadora(0, 1, "-");      // Excepción IllegalArgumentException
            // int resultado = calculadora(10, 0, "/");     // Excepción ArithmeticException
            // int resultado = calculadora(10, 0, "+a");    // Excepción personalizada MyException
            System.out.println("Operación realizada. El resultado es " + resultado );
        } catch (Exception e) {
            System.out.println(e.getMessage());
        } finally {
            System.out.println("Ejecución del programa finalizado");
        }

    }

    /*
     * DIFICULTAD EXTRA (opcional):
     * Crea una función que sea capaz de procesar parámetros, pero que también
     * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
     * corresponderse con un tipo de excepción creada por nosotros de manera
     * personalizada, y debe ser lanzada de manera manual) en caso de error.
     * - Captura todas las excepciones desde el lugar donde llamas a la función.
     * - Imprime el tipo de error.
     * - Imprime si no se ha producido ningún error.
     * - Imprime que la ejecución ha finalizado.
     */

    static class MyException extends Exception {
        MyException(String mensaje) {
            super(mensaje);
        }

    }

    public static int calculadora(int a, int b, String operacion) throws MyException {

        final String[] operaciones = { "+", "-", "*", "/" };
        int resultado = 0;

        if (!(Arrays.asList(operaciones).contains(operacion))) {
            throw new MyException("Error: Operación incorrecta. Se introdujo " + operacion);
        }
        if (b == 0 && operacion == "/") {
            throw new ArithmeticException("Error: División entre 0");
        }

        if (a < b  && operacion == "-") {
            throw new IllegalArgumentException("Error: " + a + " es menor " + b);
        }

        switch (operacion) {
            case "+":
                resultado = a + b;
                break;
            case "-":
                resultado = a - b;
                break;
            case "*":
                resultado = a * b;
                break;
            case "/":
                resultado = a / b;
                break;

        }
        return resultado;
    }
}
