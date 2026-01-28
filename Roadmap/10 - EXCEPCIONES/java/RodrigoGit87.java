
import java.util.InputMismatchException;

public class RodrigoGit87 {

    public static void main(String[] args) {

        try {
            int dividir = 10 / 0;
        } catch (ArithmeticException a) { // Excepcion aritmetica
            System.err.println("Error aritmetico: " + a.getMessage());
        } finally {
            System.out.println("programa continua... ");
        }
        System.out.println("");

        // ------- EXTRA ----------
        RodrigoGit87.calcularDivision(20, 4); // Division correcta
        System.out.println("");
        RodrigoGit87.calcularDivision(20, 0); // Division por 0, debe fallar
        System.out.println("");
        RodrigoGit87.calcularDivision(-20, 4); // Division con numero negativo, debe fallar por excepcion personalizada,
                                               // no por que no se pueda aritmeticamente.
    }

    public static void calcularDivision(int num1, int num2) {
        try {
            if (num1 < 0 || num2 < 0) {
                throw new ExcepcionPersonalizada("No se permite dividir numeros negativos"); // Excepcion personalizada
            }
            int resultado = num1 / num2;
            System.out.println("Resultado: " + resultado);
        } catch (InputMismatchException e) { // Excepcion inputmismatch se lanza cuando se introduce un tipo de dato
                                             // incorrecto
            System.err.println("Error: " + e.getMessage());
        } catch (Exception h) { // Excepcion general
            System.err.println("Error: " + h.getMessage());
        } finally {
            System.out.println("programa continua... ");
        }
    }

    public static class ExcepcionPersonalizada extends Exception {
        public ExcepcionPersonalizada(String message) {
            super(message);
        }
    }
}
