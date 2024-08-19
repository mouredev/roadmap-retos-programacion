public class Main {
    public static int division() throws ArithmeticException {
        return 10/0;
    }
    public static int multiplication() {
        return 10*10;
    }
    public static int errorResult(int number) throws AbelException, ArithmeticException, IllegalArgumentException {
        if (number < 0) {
            throw new AbelException("El número no puede ser negativo");
        } else if (number == 0) {
            throw new ArithmeticException("El número no puede ser igual a 0");
        }else if (number >1000) {
            throw new IllegalArgumentException("El número no puede ser mayor de 1000");
        }
        return number;
    }

    public static void main(String[] args) {
        try{
            int div = division();
            System.out.println("Resultado de la division: " + div);
        }catch (ArithmeticException ex){
            System.out.println("Error: " + ex.getMessage());
        }

        int result = multiplication();
        System.out.println("Resultado de la multiplicación: " + result);

        /*DIFICULTAD EXTRA*/

        System.out.println("\n----------DIFICULTAD EXTRA-----------\n");

        try {
            int result2 = errorResult(0);
            System.out.println("No se produce ningún error");
            System.out.println("Resultado del método: " + result2);
        } catch (AbelException e) {
            System.out.println("Error personalizado: " + e.getMessage());
        } catch (ArithmeticException eA) {
            System.out.println("Error 1: " + eA.getMessage());
        } catch (IllegalArgumentException eI) {
            System.out.println("Error 2: " + eI.getMessage());
        }finally {
            System.out.println("Fin del programa");
        }

    }
}

class AbelException extends Exception{
    /**
     * Constructs a new exception with the specified detail message.  The
     * cause is not initialized, and may subsequently be initialized by
     * a call to {@link #initCause}.
     *
     * @param message the detail message. The detail message is saved for
     *                later retrieval by the {@link #getMessage()} method.
     */
    public AbelException(String message) {
        super(message);
    }
}
