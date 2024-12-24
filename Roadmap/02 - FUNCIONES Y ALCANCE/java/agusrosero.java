public class agusrosero {
    public static void main(String[] args) {
        System.out.println("Hola mundo");
        System.out.println("La suma de 5 + 5 es: " + sumar(5, 5));
        System.out.println("La resta de 10 - 5 es: " + restar());
        multiplicar(5, 5);
        agusrosero ar = new agusrosero();
        ar.metodoExterno();
        imprimirNumeros("Fizz", "Buzz");
    }

    public static int sumar(int a, int b) {
        return a + b;
    }

    public static int restar() {
        return 10 - 5;
    }

    public static void multiplicar(int a, int b) {
        System.out.println("El resultado de la multiplicación es: " + (a * b));
    }

    public void metodoExterno() {
        class ClaseInterna {
            public void metodoInterno() {
                System.out.println("Método interno");
            }
        }
        ClaseInterna ci = new ClaseInterna();
        ci.metodoInterno();
    }

    // Variable LOCAL y GLOBAL
    int variableGlobal = 10;

    public void metodoExterno2() {
        int variableLocal = 5;
        System.out.println("Variable global: " + variableGlobal);
        System.out.println("Variable local: " + variableLocal);
    }

    /*
     * * DIFICULTAD EXTRA (opcional):
     * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne
     * un número.
     * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
     * - Si el número es múltiplo de 3, muestra la cadena de texto del primer
     * parámetro.
     * - Si el número es múltiplo de 5, muestra la cadena de texto del segundo
     * parámetro.
     * - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto
     * concatenadas.
     * - La función retorna el número de veces que se ha impreso el número en lugar
     * de los textos.
     */
    public static int imprimirNumeros(String texto1, String texto2) {
        int contador = 0;
        for (int i = 1; i <= 100; i++) {
            if (i % 3 == 0 && i % 5 == 0) {
                System.out.println(texto1 + texto2);
            } else if (i % 3 == 0) {
                System.out.println(texto1);
            } else if (i % 5 == 0) {
                System.out.println(texto2);
            } else {
                System.out.println(i);
            }
            contador++;
        }
        return contador;
    }
}
