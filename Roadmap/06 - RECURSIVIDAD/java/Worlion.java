
public class Worlion {

    public static void main(String[] args) {
        new Worlion().run();
    }

    public void run(){
    
        // Ejercicio de base: imprimir los numeros del 100 al 0
        printTo(100);

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

}
