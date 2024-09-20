public class simonguzman {

    public static void main(String[] args) {
        contadorInversoRecursivo(100);
        System.out.println(factorialRecursivo(5));
        System.out.println(fibonacciRecursivo(6));
    }

    //Contador de 100 a 0 recursivo
    public static void contadorInversoRecursivo(int numero){
        if (numero >= 0 ){
            System.out.println(numero);
            contadorInversoRecursivo(numero - 1);
        }
    }

    //Factorial recursivo
    public static int factorialRecursivo(int numero){
        if(numero < 0){
            return 0;
        }else if(numero == 0 || numero == 1){
                return 1;
        }else{
            return (numero * factorialRecursivo(numero - 1));
        }
    }

    //Fibonacci por posicion recursivo
    public static int fibonacciRecursivo(int posicion){
        if (posicion == 0 ){
            return 0;
        }else if ( posicion == 1 ){
            return 1;
        }else{
            return ((fibonacciRecursivo(posicion - 1)) + (fibonacciRecursivo(posicion - 2)));
        }
    }
}
