

/** #10 - Java -> Jesus Antonio Escamilla */

public class JesusAntonioEEscamilla {
    public static void main(String[] args) {
    //---EJERCIÓ---
        // Division en 10 / 0
        System.out.println("Dividir entre 10");
        try {
            // Código que puede generar una excepción
            int resultado = divide(10, 0);
            System.out.println("El resultado es: " + resultado);
        } catch (ArithmeticException e) {
            // Manejo de la excepción específica
            System.out.println("Error aritmético: " + e.getMessage());
        } catch (Exception e) {
            // Manejo de la excepción general
            System.out.println("Ocurrió un error: " + e.getMessage());
        } finally{
            // Este bloque siempre se ejecuta
            System.out.println("Operación finalizada");
        }

        // Identificar el numero de una lista
        System.out.println("Encontrar un indice a la lista");
        try {
            // Código que puede generar una excepción
            int newList = getElement(5);
            System.out.println("El valor es : " + newList);
        } catch (ArrayIndexOutOfBoundsException e) {
            // Manejo de la excepción específica
            System.out.println("Error obtener indice: " + e.getMessage());
        } catch (Exception e) {
            // Manejo de la excepción general
            System.out.println("Ocurrió un error: " + e.getMessage());
        } finally{
            // Este bloque siempre se ejecuta
            System.out.println("Operación finalizada");
        }
    //---EXTRA---
        // Pendiente
    }

    //---EJERCIÓ---
    public static int divide(int numerator, int denominator) throws ArithmeticException{
        if (denominator == 0) {
            throw new  ArithmeticException("No se puede dividir por cero");
        }
        return numerator / denominator;
    }

    public static int getElement(int index) throws ArrayIndexOutOfBoundsException{
        int[] number = {1, 2, 3};
        if (number[index] == index) {
            throw new ArrayIndexOutOfBoundsException("No encuentra el valor");
        }
        return number[index];
    }



    /**-----DIFICULTAD EXTRA-----*/

    // Pendiente

    /**-----DIFICULTAD EXTRA-----*/
}