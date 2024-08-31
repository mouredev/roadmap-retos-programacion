public class bladi23 {
    
        // Variable global
        static int globalVar = 10;
    
        // Función sin parámetros ni retorno
        static void printHello() {
            System.out.println("Hello, world!");
        }
    
        // Función con un parámetro y sin retorno
        static void printNumber(int num) {
            System.out.println("Number: " + num);
        }
    
        // Función con varios parámetros y sin retorno
        static void suma(int num1, int num2) {
            System.out.println("Sum: " + (num1 + num2));
        }
    
        // Función con retorno
        static int conRetorno(int num) {
            return num * 2;
        }
    
        // Función que utiliza una función ya creada en el lenguaje (Math.sqrt)
        static double getSquareRoot(int num) {
            return Math.sqrt(num);
        }
    
        // Función que prueba el concepto de variable local y global
        static void variableLocalyGlobal() {
            int localVar = 5; // Variable local
            System.out.println("Global variable: " + globalVar);
            System.out.println("Local variable: " + localVar);
        }
    
        static int extra(String str1, String str2) {
            int contador = 0;
            for (int i = 1; i <= 100; i++) {
                if (i % 3 == 0 && i % 5 == 0) {
                    System.out.println(str1 + str2);
                } else if (i % 3 == 0) {
                    System.out.println(str1);
                } else if (i % 5 == 0) {
                    System.out.println(str2);
                } else {
                    System.out.println(i);
                    contador++;
                }
            }
            return contador;
        }
    
        public static void main(String[] args) {
            printHello();
            printNumber(5);
            suma(3, 4);
            System.out.println("Double: " + conRetorno(7));
            System.out.println("Square root: " + getSquareRoot(9));
            variableLocalyGlobal();
            int count = extra("Fizz", "Buzz");
            System.out.println("Count: " + count);
        }
    }

