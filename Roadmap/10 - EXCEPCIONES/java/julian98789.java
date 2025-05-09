import java.util.Scanner;

import javax.swing.undo.CannotRedoException;

public class reto_10 {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        for (int i = 0; i < 1; i++) {
            try {
                int div = 10;
                int divisor = input.nextInt();
                div /= divisor;
            } catch (ArithmeticException e) {
                System.out.println("No se puede dividir por 0");
            }
        }

        try {
            processParams(0, 50);
        } catch (CustomException e) {
            System.out.println("Error capturado en el método main: " + e.getMessage());
        }

        try {
            processParams(50, -10);
        } catch (CustomException e) {
            System.out.println("Error capturado en el método main: " + e.getMessage());
        }

        try {
            processParams(60, 50);
        } catch (CustomException e) {
            System.out.println("Error capturado en el método main: " + e.getMessage());
        }

        try {
            processParams(50, 25);
        } catch (CustomException e) {
            System.out.println("Error capturado en el método main: " + e.getMessage());
        }
    }

    public static void processParams(int param1, int param2) throws CustomException {
        try {
            if (param1 == 0) {
                throw new IllegalArgumentException("El parámetro 'param1' no puede ser 0");
            } else if (param2 < 0) {
                throw new CustomException("El parámetro 'param2' no puede ser negativo");
            } else if (param1 + param2 > 100) {
                throw new IllegalStateException("La suma de los parámetros no puede ser mayor a 100");
            } else {
                System.out.println("Procesamiento de parámetros exitoso");
            }
        } catch (IllegalArgumentException e) {
            System.out.println("Error de tipo IllegalArgumentException: " + e.getMessage());
        } catch (CustomException e) {
            System.out.println("Error de tipo CustomException: " + e.getMessage());
        } catch (IllegalStateException e) {
            System.out.println("Error de tipo IllegalStateException: " + e.getMessage());
        } catch (Exception e) {
            System.out.println("Error inesperado: " + e.getClass().getName());
        } finally {
            System.out.println("La ejecución ha finalizado");
        }
    }

    public static class CustomException extends Exception {
        public CustomException(String message) {
            super(message);
        }
    }

}
