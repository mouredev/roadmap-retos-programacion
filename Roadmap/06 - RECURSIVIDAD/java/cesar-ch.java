public class Main {

    // #06 RECURSIVIDAD 

    public static void imprimirNumeros(int contador) {
        if (contador < 0) {
            return;
        } else {
            System.out.println(contador);
            contador--;
            imprimirNumeros(contador);
        }
    }

    public static void main(String[] args) {
        imprimirNumeros(100);
        
        System.out.println(factorial(5)); // 120

        System.out.println(fibonacci(8)); // 13
    }

     // Dificultad Extra

    public static int factorial(int numero) {
        if (numero == 0) {
            return 1;
        } else {
            return numero * factorial(numero - 1);
        }
    }

    public static int fibonacci(int numero) {
        if (numero < 1) {
            System.out.println("El número debe ser mayor o igual a 1");
            return -1;
        } else if (numero == 1) {
            return 0;
        } else if (numero == 2) {
            return 1;
        } else {
            return fibonacci(numero - 1) + fibonacci(numero - 2);
        }
    }
}
