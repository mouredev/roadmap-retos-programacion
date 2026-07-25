public class Josegs95 {
    public static void main(String[] args) {
        //Método recursivo de 100 a 0
        printNumDesc(100);

        //Reto
        System.out.println("\n");
        retoFinal();
    }

    public static void printNumDesc(int n){
        System.out.println(n);
        if (n != 0)
            printNumDesc(n - 1);
        else
            return;
    }

    public static void retoFinal(){
        int a = 5;
        System.out.println("El factorial de 5 es: " + calcFactorial(a)); //Out: 'El factorial de 5 es: 120'

        int b = 7;
        System.out.println("El número en la posición " + b + " en la sucesión de Fibonacci es : " + calcNumFibFromPos(b));
            //Out: El número en la posición 7 en la sucesión de Fibonacci es : 13

    }

    private static int calcFactorial(int n){
        if (n != 0)
            return n * calcFactorial(n - 1);
        else
            return 1;
    }

    private static int calcNumFibFromPos(int pos){
        if (pos < 2)
            return pos;

        return calcNumFibFromPos(pos - 1) + calcNumFibFromPos(pos - 2);
    }
}
