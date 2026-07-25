public class danhingar {

    public static void main(String[] args) {
        printRecursivo(100);
        System.out.println(factorialRecursivo(5));
        System.out.println(fibonacciRecursivo(10));
    }

    private static void printRecursivo(int number) {
        if (number >= 0) {
            System.out.println(number);
            printRecursivo(--number);
        }
    }

    // EXTRA
    private static int factorialRecursivo(int number) {
        if (number == 0) {
            return 1;
        } else if (number < 0) {
            System.out.println("No puede ser negativo");
        }
        return number * factorialRecursivo(--number);
    }

    private static int fibonacciRecursivo(int posicion) {
        if (posicion <= 0) {
            return 0;
        }else if(posicion ==1){
            return 0;
        }else if(posicion ==2){
            return 1;
        }
        return fibonacciRecursivo(posicion - 1) + fibonacciRecursivo(posicion - 2);
    }

}
