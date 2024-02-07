//Definición de una función recursiva

/**
 * pguillo02
 */
public class pguillo02 {

        public static void main(String[] args) {
            recursiva(100);
        }

        public static void recursiva(int n) {
            if (n == 0){
                System.out.println("Fin de la función recursiva");
            } else{
                System.out.println(n);
                recursiva(n-1);
            }
        }

        public static int factorial(int n){
            if (n == 0){
                return 1;
            } else{
                return n*factorial(n-1);
            }
        }
} 
