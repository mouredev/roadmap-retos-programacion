/**
 * Solución al ejercicio #06 RECURSIVIDAD.
 * 
 * @author AbelADE
 */
public class AbelADE {

    public static void recursive(int number) {
        if (number >= 0) {
            System.out.println(number--);
            recursive(number);
        }
    }
    
    // DIFICULTAD EXTRA (opcional):

    public static Long factorial(int number) {
        if (number < 0) {
            System.out.println("No acepta números negativos");
            return -1L;
        }else if (number == 0) {
            return 1L;
        }
        
        return number * factorial(number -1);
    }
    
    public static Long fibonacci(int number) {
        if (number <= 0) {
            System.out.println("No acepta números negativos");
            return -1L;
        }else if (number == 1) {
            return 0L;
        }else if (number == 2) {
            return 1L;
        }
        
        return fibonacci(number -1) + fibonacci(number -2);
    }

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        System.out.println("Recursividad: ");
        System.out.println();
        
        System.out.println("Imprimir números: ");
        recursive(100);
        System.out.println();
        
        System.out.println("Factorial: ");
        System.out.println(factorial(4));
        System.out.println();
        
        System.out.println("Fibonacci: ");
        System.out.println(fibonacci(10));
    }

}
