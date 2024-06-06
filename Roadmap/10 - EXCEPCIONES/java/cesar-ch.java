public class Main {
    public static void main(String[] args) {
        try {
            int resultado = dividePorCero(10, 0);
            System.out.println("El resultado de la división es: " + resultado);
        } catch (ArithmeticException e) {
            System.out.println("Error: " + e.getMessage());
        } finally {
            System.out.println("La ejecución ha finalizado.");
        }

        try {
            int[] array = {1, 2, 3};
            System.out.println("El elemento en el índice 3 es: " + array[3]);
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Error: " + e.getMessage());
        } finally {
            System.out.println("La ejecución ha finalizado.");
        }

        try {
            procesarParametros("ERROR");
        } catch (CustomException ce) {
            System.out.println("Error personalizado: " + ce.getMessage());
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        } finally {
            System.out.println("La ejecución ha finalizado.");
        }
    }

    public static void procesarParametros(String parametro) throws CustomException {
        if (parametro.equalsIgnoreCase("error")) {
            throw new CustomException("Se ha producido un error personalizado.");
        }
    }

    public static int dividePorCero(int dividendo, int divisor) {
        return dividendo / divisor;
    }
}

class CustomException extends Exception {
    public CustomException(String message) {
        super(message);
    }
}
