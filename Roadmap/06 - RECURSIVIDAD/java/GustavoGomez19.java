public class GustavoGomez19 {

    // Función recursiva que imprime los números del 100 al 0
    public static void funcRecursiva(int num){
        if(num >= 0){
            System.out.println(num);
            funcRecursiva(num - 1);
        }
    }

    public static int factorial(int num){
        // Caso base, cuando el número es 0, el factorial es 1
        if(num == 0){
            return 1;
        } else {
            // Caso de recursividad
            return num * factorial(num - 1);
        }
    }

    public static int fibonacci(int pos){
        if(pos <=1){
            // El valor Fibonacci para pos <=1 es pos
            return pos;
        } else {
            // El valor Fibonacci para pos es la suma de los valores de Fibonacci para pos - 1 y pos - 2
            return fibonacci(pos - 1) + factorial(pos - 2);
        }        
    }

    public static void main(String[] args) {
        // Función recursiva que imprime los números del 100 al 0
        funcRecursiva(100);
        
        // Ejercicio factorial
        int num = 10;
        int resultado = factorial(num);
        System.out.println("El factorial de " + num + " es " + resultado);

        // Ejercicio valor elemento sucesión Fibonacci
        int posicion = 10;
        int valor = fibonacci(posicion);
        System.out.println("El valor del elemento en la posición " + posicion + " de la secuencia Fibonacci es " + valor);
    }
    
}
