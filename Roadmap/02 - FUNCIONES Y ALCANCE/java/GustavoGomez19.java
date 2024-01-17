public class GustavoGomez19 {

    // Punto 1: Funciones básicas
    // Función sin parámetros ni retorno de valor
    private static void sinParamatrosNiRetorno() {
        System.out.println("Función sin parámetros ni retorno de valor");
    }

    // Función con parámetros
    private static void saludar(String saludo) {
        System.out.println(saludo);
    }

    // Función con varios parámetros y retorno de valor
    private static int sumar(int num1, int num2) {
        return num1 + num2;
    }

    // Punto 2: Funciones anidadas
    private static String funcion(String value) {
        return value;
    }

    private static void funcionAnidada(String value, int a, int b) {
        System.out.println("Hola " + funcion(value) + " La suma de los 2 valores a y b es: " + sumar(a, b));
    }

    // Punto dificultad extra
    private static int desafioExtra(String texto1, String texto2) {
        int contador = 0;
        for (int num = 1; num <= 100; num++) {
            if (num % 3 == 0 && num % 5 == 0) {
                System.out.println(texto1 + " " + texto2);
            } else if (num % 3 == 0) {
                System.out.println(texto1);
            } else if (num % 5 == 0) {
                System.out.println(texto2);
            } else {
                System.out.println(num);
                contador += 1;
            }

        }
        System.out.println("De los 100 números se imprimieron (" + contador + ") números.");
        return contador;
    }

    public static void main(String[] args) {

        sinParamatrosNiRetorno();
        saludar("¡Hola, Java!");
        System.out.println("La suma es : " + sumar(5, 5));
        funcionAnidada("Java", 5, 10);
        System.out.println(desafioExtra("Fizz", "Buzz"));

        // Punto 3: Funciones del lenguaje
        // Función Math.pow() --> eleva un número a la potencia
        System.out.println(Math.pow(2, 3));
        // Función println --> imprime mensaje por consola con salto de línea
        System.out.println("Mensaje por consola");
        /*
         * Función .length de la clase String --> permite conocer el número de
         * caracteres de una cadena de texto
         */
        String nombre = "Gustavo";
        int largoNombre = nombre.length();
        System.out.println(largoNombre);
        /* Función .toUpperCase() --> Convierte la cadena de texto a mayúscula */
        System.out.println(nombre.toUpperCase());
        /* Función .toULowerCase() --> Convierte la cadena de texto a minúscula */
        System.out.println(nombre.toLowerCase());

        // Punto 4: Variable local y variable global
        /*
         * Variable local, se ejecuta solo dentro del ambito donde es declarada
         * si se intenta ejecutar desde afuera de ese ambito el resultado sería un error
         */
        // Declaracioón de variable global
        int edad = 31;
        {
            String variableLocal = "Esta es una variable local ";
            System.out.println(variableLocal + "\n" + "Valor de la variable global " + edad);
            /*
             * Se hace el llamado de la variable 'edad' la cual está definidad por fuera
             * de este bloqued de código y se ejecuta sin problema
             */
        }

    }
}
