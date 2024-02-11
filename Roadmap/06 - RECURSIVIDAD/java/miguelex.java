public class miguelex {
    
    public static void main(String[] args) {
        System.out.print("De 100 a 0: ");
        cuentaAtras(100);
        System.out.println();
        
        System.out.println("La suma de 5 + 3 es: " + sumaRecursiva(5, 3));
        System.out.println("El valor de 2^3 es: " + potenciaRecursiva(2, 3));
        System.out.println("El valor de 5! es: " + factorial(5));
        System.out.println("El 10º numero de Fibonacci es: " + fibonacci(10));

        System.out.println("Introduce el numero del que queires calcualr el factorial: ");
        int numero = Integer.parseInt(System.console().readLine());
        System.out.println("El factorial de " + numero + " es: " + factorial(numero));

        System.out.println("Introduce el numero de la serie de Fibonacci que quieres calcular: ");
        int n = Integer.parseInt(System.console().readLine());
        System.out.println("El " + n + "º numero de Fibonacci es: " + fibonacci(n));
    }
    
    public static void cuentaAtras (int n) {
        if (n >= 0) {
            System.out.print(n + " ");
            cuentaAtras(n - 1);
        }        
    }

    public static int sumaRecursiva (int a, int b) {
        if (b == 0) {
            return a;
        }
        return sumaRecursiva(a + 1, b - 1);
    }

    public static int potenciaRecursiva(int base, int exponente) {
        if (exponente == 0) {
            return 1;
        }
        return base * potenciaRecursiva(base, exponente - 1);
    }

    // Metodo para calcular el factorial de un numero
    public static int factorial(int n) {
        if (n == 0) {
            return 1;
        }
        return n * factorial(n - 1);
    }
    
    public static int fibonacci(int n) {
        if (n == 0) {
            return 0;
        }
        if (n == 1) {
            return 1;
        }
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
}
