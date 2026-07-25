import java.text.DecimalFormat;

/**
 * 02 FUNCIONES Y ALCANCE
 *
 * @author martinbohorquez
 */
public class martinbohorquez {
    /*
     * Diferentes típos de funciones (en Java, métodos, que suelen estar asociados a objetos.):
     *       -- Estructura: modificador retorno nombre (parámetros).
     *       -- Tipos de métodos:
     *              * Métodos sin retorno.
     *              * Métodos con retorno.
     *              * Métodos sin parámetros.
     *              * Métodos con parámetros.
     *              * Métodos estáticos (no están asociados a objetos).
     *              * Métodos constructores: Se utilizan para inicializar un objeto cuando se crea.
     *              * Métodos abstractos: Se declaran en clases abstractas y deben ser implementados por las subclases.
     */

    /**
     * Ejemplo de Constructor
     */
    public martinbohorquez() {
    }

    /**
     * Ejemplo de Método sin retorno y sin parámetros.
     * Método estático, es decir que se puede llamar dentro de la clase,
     * sin crear un objeto como instancia.
     */
    private static void saludar() {
        System.out.println("Hola,  Java!");
    }

    /**
     * Ejemplo de Método sin retorno, con parámetros.
     *
     * @param name tipo string.
     */
    private static void saludar(String name) {
        System.out.println("Hola, " + name + "!");
    }

    /**
     * Ejemplo de Método con retorno y sin parámetros.
     *
     * @return con un hola kotlin, tipo string.
     */
    private static String saludarKotlin() {
        return "Hola,  Kotlin!";
    }

    /**
     * Ejemplo de Método con retorno y parámetros.
     *
     * @param salario       tipo double.
     * @param percentAhorro tipo double.
     * @return ahorro mensual, tipo double.
     */
    private static double calcularAhorroMensual(double salario, double percentAhorro) {
        return salario * percentAhorro;
    }

    public static void main(String[] args) {
        martinbohorquez mbohorquez = new martinbohorquez();
        System.out.println("---- SALUDAR ----");
        saludar();
        saludar("Python");
        saludar("Typescript");
        System.out.println(saludarKotlin());

        System.out.println("---- CALCULAR AHORRO ----");
//        double salario = 2500;
//        double percentAhorro = 52.75 / 100;
//        double tasaAnual = 8.00 / 100;
//        int periodos = 60;
        double salario = 4000;
        double percentAhorro = 62.5 / 100;
        double tasaAnual = 8.00 / 100;
        int periodos = 3 * 12;

        DecimalFormat df = new DecimalFormat("$ #,###.00");
        DecimalFormat dfp = new DecimalFormat("#.00 %");

        System.out.println("Salario: " + df.format(salario));
        System.out.println("Porcentaje de ahorro (%): " + dfp.format(percentAhorro));
        System.out.println("Periodos de ahorro (meses): " + periodos);
        System.out.println("Tasa de interés anual (%): " + dfp.format(tasaAnual));

        double ahorroMensual = calcularAhorroMensual(salario, percentAhorro);
        System.out.println("El ahorro mensual: " + df.format(ahorroMensual));

        double ahorroTotal = mbohorquez.calcularAhorro(ahorroMensual, tasaAnual, periodos);
        System.out.println("El ahorro total generado es: " + df.format(ahorroTotal));
        System.out.println();

        salario = 1500;
        percentAhorro = 67.5 / 100;
        tasaAnual = 7.50 / 100;
        periodos = 2 * 12;

        System.out.println("Salario: " + df.format(salario));
        System.out.println("Porcentaje de ahorro (%): " + dfp.format(percentAhorro));
        System.out.println("Periodos de ahorro (meses): " + periodos);
        System.out.println("Tasa de interés anual (%): " + dfp.format(tasaAnual));

        double ahorroTotal2 = mbohorquez.calcularAhorro(salario, percentAhorro, tasaAnual, periodos);
        System.out.println("El ahorro total generado es: " + df.format(ahorroTotal2));
        System.out.println();

        System.out.println("DIFICULTAD EXTRA");
        int numeros = mbohorquez.funcion("fizz", "buzz");
        System.out.println("numeros de: " + numeros);
    }

    /**
     * Ejemplo de Método con retorno y parámetros.
     * No son métodos estáticos, se necesita un objeto como instancia
     * para llamar al método.
     *
     * @param ahorroMensual tipo double.
     * @param tasaAnual     tipo double.
     * @param periodos      tipo integer.
     * @return ahorro total, tipo double.
     */
    private double calcularAhorro(double ahorroMensual, double tasaAnual, int periodos) {
        int periodosPorAnio = 12; // Capitalización mensual
        double tasaMensual = Math.pow(tasaAnual + 1, (double) 1 / periodosPorAnio) - 1; // Tasa mensual
        return ahorroMensual * ((Math.pow(1 + (tasaMensual), periodos) - 1) / (tasaMensual));
    }

    /**
     * Ejemplo de Método con retorno y parámetros.
     * Se llaman a otros métodos dentro del mismo.
     *
     * @param salario       tipo double.
     * @param percentAhorro tipo double.
     * @param tasaAnual     tipo double.
     * @param periodos      tipo integer.
     * @return ahorro total, tipo double.
     */
    private double calcularAhorro(double salario, double percentAhorro, double tasaAnual, int periodos) {
        double pago = calcularAhorroMensual(salario, percentAhorro);
        return calcularAhorro(pago, tasaAnual, periodos);
    }

    /**
     * DIFICULTAD EXTRA (Ejercicio fizz buzz)
     * Una función que imprima los números del 1 al 100, pero si el número es
     * múltiplo de 3, muestre una palabra, si es múltiplo de 5 muestre otra
     * y si es múltiplo de los dos muestre las dos palabras.
     *
     * @param texto1 el texto para los divisores de 3.
     * @param texto2 el texto para los divisores de 5.
     * @return el número de veces que mostró números y no texto.
     */
    public int funcion(String texto1, String texto2) {
        int counter = 0;
        StringBuilder result;
        for (int i = 1; i <= 100; i++) {
            result = new StringBuilder();

            if (i % 3 == 0) {
                result.append(texto1);
            }

            if (i % 5 == 0) {
                result.append(texto2);
            }

            if (result.isEmpty()) {
                result.append(i);
                counter++;
            }
            System.out.println(result);
        }
        return counter;
    }
}
