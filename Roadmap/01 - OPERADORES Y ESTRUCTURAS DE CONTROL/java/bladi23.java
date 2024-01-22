public class bladi23 {
    public static void main(String[] args) {

        // Tipos de operadores en java

        // Operadores aritmeticos
        int a = 2, b = 4;
        System.out.println("a + b = " + (a + b));
        System.out.println("a - b = " + (a - b));
        System.out.println("a * b = " + (a * b));
        System.out.println("b / a = " + (b / a));
        System.out.println("b % a = " + (b % a));
        System.out.println("a++ = " + (a++));
        System.out.println("b-- = " + (b--));
        // Operadores de asignacion
        a += 2;
        System.out.println("a += 2 = " + a);

        // Operadores de comparacion
        System.out.println("a == b: " + (a == b));
        System.out.println("a != b: " + (a != b));
        System.out.println("a > b: " + (a > b));
        System.out.println("a < b: " + (a < b));
        System.out.println("b >= a: " + (b >= a));
        System.out.println("b <= a: " + (b <= a));
        // Operadores logicos
        System.out.println("(a == b) && (a < b): " + ((a == b) && (a < b)));
        System.out.println("(a == b) || (a < b): " + ((a == b) || (a < b)));
        System.out.println("!(a == b): " + !(a == b));

        // Operadores de incremento y decremento
        a++; // incremento
        a--; // decremento

        // Operadores de concatenacion
        String texto1 = "Hola, ";
        String texto2 = "¿cómo estás?";
        System.out.println(texto1 + texto2);

        // Operadores ternarios
        String result = (a > b) ? "a es mayor que b" : "b es mayor o igual que a";
        System.out.println(result);
        // Operadores de instancia
        String texto = "Hola";
        if (texto instanceof String) {
            System.out.println("texto es una instancia de String");
        }

        // Tipos de estructura de control en java

        // Estructura if
        if (a > b) {
        } else if (a == b) {
        } else {
            System.out.println("a es menor que b");
        }

        // Estructura switch
        switch (a) {
            case 1:
                System.out.println("a es igual a 1");
                break;
            case 2:
                System.out.println("a es igual a 2");
                break;
            default:
                System.out.println("a no es igual a 1 ni a 2");
                break;
        }

        // Estructura while
        while (a < b) {
            System.out.println("a es menor que b");
            a++;
        }

        // Estructura do while
        do {
            System.out.println("a es menor que b");
            a++;
        } while (a < b);

        // Estructura for
        for (int i = 0; i < 10; i++) {
            System.out.println("i es igual a " + i);
        }

        // Estructura for each
        int[] numeros = { 1, 2, 3, 4, 5 };
        for (int numero : numeros) {
            System.out.println("numero es igual a " + numero);
        }

        // Estructura break
        for (int i = 0; i < 10; i++) {
            if (i == 5) {
                break;
            }
            System.out.println("i es igual a " + i);
        }
        // Estructura continue
        for (int i = 0; i < 10; i++) {
            if (i == 5) {
                continue;
            }
            System.out.println("i es igual a " + i);
        }

        /*
         * DIFICULTAD EXTRA (opcional):
         * Crea un programa que imprima por consola todos los números comprendidos
         * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
         */

        for (int i = 10; i <= 55; i++) {
            if (i % 2 == 0 && i != 16 && i % 3 != 0) {
                System.out.println(i);
            }
        }
    }
}
