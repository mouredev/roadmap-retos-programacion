
public class reto_6 {
    
    public static void main(String[] args) {

        numRecursivo(0);
        System.out.println("\n **********************");
        int factorial = factorial(5);

        System.out.println("Factorial: " + factorial +"\n");

        int Fibonacci = Fibonacci(5);

        System.out.println("El numero es: " + Fibonacci);
    }

    public static void numRecursivo( int n){
    
        if (n > 100) {
            return;
        }
        System.out.println(n);
        numRecursivo(n+1);

 
    }
    public static int factorial( int n){

        if (n == 0 || n == 1) {
            return 1;
        }
        return n * factorial(n - 1);
    }

    public static int Fibonacci ( int n){

        if (n <= 1) {
            return n;
        }else{
            return (Fibonacci( n - 1) + Fibonacci( n- 2));
        }
    }  
}

