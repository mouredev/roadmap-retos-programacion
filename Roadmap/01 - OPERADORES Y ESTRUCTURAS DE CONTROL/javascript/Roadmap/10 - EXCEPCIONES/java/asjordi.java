public class Main {

    /**
     * Una excepción es un evento que ocurre durante la ejecución de un programa y que interrumpe el flujo normal de las instrucciones.
     * Existen dos tipos de excepciones: las comprobadas y las no comprobadas.
     * Las excepciones comprobadas (CHECKED) son aquellas que el compilador obliga a manejar,
     * mientras que las excepciones no comprobadas (UNCHECKED) son aquellas que el compilador no obliga a manejar.
     * Generalmente las de tipo Checked estan asociadas a problemas externos al código, como por ejemplo la lectura de un archivo que no existe.
     * Las de tipo Unchecked estan asociadas a problemas internos del código, como por ejemplo una división por cero.
     */

    public static void main(String[] args) throws MiExcepcion {

        ejemploExcepcion();
        procesarParametros(0, new int[]{1, 2, 3, 4, 5});


    }

    /**
     * EJERCICIO:
     * Explora el concepto de manejo de excepciones según tu lenguaje.
     * Fuerza un error en tu código, captura el error, imprime dicho error
     * y evita que el programa se detenga de manera inesperada.
     * Prueba a dividir "10/0" o acceder a un índice no existente
     * de un listado para intentar provocar un error.
     */
    static void ejemploExcepcion() {
        int a = 10;
        int b = 0;
        int c = 0;

        try {
            c = a / b;
        } catch (ArithmeticException e) {
            System.out.println("No se puede dividir por cero");
            e.printStackTrace();
        }

        System.out.println("El resultado de la división es: " + c);
    }

    /**
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
    static class MiExcepcion extends Exception {
        public MiExcepcion(String mensaje) {
            super(mensaje);
        }
    }

    static void procesarParametros(int a, int[] arr) throws MiExcepcion {
        // división por cero
        try {
            int c = arr[0] / a;
        } catch (ArithmeticException e) {
            System.out.println("No se puede dividir por cero");
            e.printStackTrace();
        }

        // acceso a un índice no existente
        try {
            int d = arr[10];
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("El índice no existe");
            e.printStackTrace();
        }

        // lanzar excepción personalizada
        if (a == 0) {
            throw new MiExcepcion("El valor de a no puede ser 0");
        }
    }
}
