
public class Worlion {

    public static void main(String[] args) {
        new Worlion().run();
    }

    public void run(){
    
        // Ejercicio de base: imprimir los numeros del 100 al 0
        printTo(100);

        extra();
    }

    /**
     * Imprime los numeros desde number (>= 0) hasta 0 con recursividad
     * @param number The first number of secuence
     */
    private void printTo(int number) {
        if(number < 0) {
            System.err.println("Error: not negative numbers allowed.");
            return;
        }
        System.out.println(number);
        if (number > 0){
            printTo(number-1);
        }
    }
    
// DIFICULTAD EXTRA (opcional): Factorial y Fibonacci

private void extra() {
    System.out.println(" \n ---- 🌩 DIFICULTAD EXTRA 🌩 ----\n");

    System.out.println(" Factorial de 10 = "+factorial(10));
    System.out.println(" Fibonacci de 10 = "+fibonacci(10));
}

/**
 * Calcula el factorial del número recibido como parametro
 * @param num numero cuyo factorial se va a calcular (>=0)
 * @return !num
 */
private int factorial(int num){
    if(num <0) {
        System.err.println("ERROR: No se puede calcular el factorial de un número negativo!");
        return -1;
    } else if( num == 0) {
        return 1;
    }
    else {
        return num*factorial(num-1);
    }
}

/**
 * 
 * @param pos Posición en la serie de Fibonacci
 * @return El valor de esa posición en la serie
 */
private int fibonacci(int pos) {
    if(pos <= 0) {
        System.err.println("ERROR: La posición en cualquier serie debe ser positiva.");
        return -1;
    }
    if(pos == 1){
        return 0;
    }
    if(pos == 2){
        return 1;
    }
    return fibonacci(pos-2) + fibonacci(pos-1);
}
}
