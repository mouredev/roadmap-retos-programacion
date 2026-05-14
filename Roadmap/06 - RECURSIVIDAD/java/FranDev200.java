import java.util.Scanner;

public class FranDev200 {

    static int numero = 100;

    static int resultadoFactorial = 1;


    static int contadorPosicion = 1;
    static int  a = 0, b = 1, c = 0;

    static void main() {
        /*

            Entiende el concepto de recursividad creando una función recursiva que imprima
            números del 100 al 0.

         */

        recursividad();

        /*

         DIFICULTAD EXTRA (opcional):
          Utiliza el concepto de recursividad para:
          - Calcular el factorial de un número concreto (la función recibe ese número).
          - Calcular el valor de un elemento concreto (según su posición) en la
          sucesión de Fibonacci (la función recibe la posición).

         */
        Scanner scan = new Scanner(System.in);
        System.out.print("Introduce el numero para calcular su factorial: ");
        int numFactorial = Integer.parseInt(scan.nextLine());
        System.out.println("Factorial de " + numFactorial + ": " + factorial(numFactorial));

        System.out.print("Introduce la posicion de la sucesion de Fibonacci que quieres ver: ");
        int posicionFibonacci = Integer.parseInt(scan.nextLine());
        System.out.println("Numero de la sucesion de Fibonacci de la posicion " + posicionFibonacci
                + ": " + fibonacci(posicionFibonacci));

    }

    public static void recursividad(){

        if(numero >= 0){
            System.out.println(numero);
            numero--;
            recursividad();
        }

    }

    // - Calcular el factorial de un número concreto (la función recibe ese número).
    public static int factorial(int num){

        if(num > 0){
            resultadoFactorial = resultadoFactorial * num;
            num--;
            factorial(num);
        }
        return resultadoFactorial;
    }

    // - Calcular el valor de un elemento concreto (según su posición) en la sucesión de Fibonacci (la función recibe la posición).

    public static int fibonacci(int posicion){
        if(contadorPosicion < posicion){

            c = a + b;
            a = b;
            b = c;

            contadorPosicion++;
            fibonacci(posicion);
        }

        return c;

    }

}
