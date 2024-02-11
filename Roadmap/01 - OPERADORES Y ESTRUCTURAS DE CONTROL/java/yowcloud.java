public class yowcloud {
    public static void main(String[] args) {
        int a = 10, b = 5;
        boolean x = true, y = false;
        System.out.println("Arithmetical operators:");
        arithmetical(a, b);

        System.out.println("Logical operators:");
        logical(x, y);

        System.out.println("Assignment operators:");
        assignment(a, b);

        System.out.println("Comparison operators:"); 
        comparison(a, b);

        System.out.println("Bits operators:");
        bits(a, b);

        System.out.println("Conditionals:");
        conditionals(a, b);

        System.out.println("Iteratives:");
        iteratives(a, b);
        
        System.out.println("Exceptions:");
        exceptions();
        
        System.out.println("DIFICULTAD EXTRA:");
        extra(10, 55);
    }
    private static void arithmetical(int a, int b) {
        System.err.println("a = " + a + " b = " + b);
        System.out.println("Add -> a + b = " + (a + b));
        System.out.println("Sub -> a - b = " + (a - b));
        System.out.println("Product -> * b = " + (a * b));
        System.out.println("Div -> a / b = " + (a / b));
        System.out.println("Mod ->a % b = " + (a % b));
    }
    private static void logical(boolean x, boolean y) {
        System.err.println("x = " + x + " y = " + y);
        System.out.println("AND lógico: x= true && y = false : " + (x && y));
        System.out.println("OR lógico: true || y = false : " + (x || y));
        System.out.println("NOT lógico: !true, : " + (!x));
    }
    private static void assignment(int a, int b){
        System.err.println("a = " + a + " b = " + b);
        a = b;
        a += b; 
        System.out.println("Asignación:a(10) = b(5), a+=b -> " + a);
    }
    private static void comparison(int a, int b) {
        System.err.println("a = " + a + " b = " + b);
        System.out.println("Equal -> a == b = " + (a == b));
        System.out.println("Not equal -> a != b = " + (a != b));
        System.out.println("Greater than -> a > b = " + (a > b));
        System.out.println("Less than -> a < b = " + (a < b));
        System.out.println("Greater than or equal to -> a >= b = " + (a >= b));
        System.out.println("Less than or equal to -> a <= b = " + (a <= b));
    }
    private static void bits(int a, int b) {
        System.out.println("a = " + a + " b = " + b);
        System.out.println("AND bit a & b = " + (a & b));
        System.out.println("OR bit a | b = " + (a | b));
        System.out.println("XOR bit a ^ b = " + (a ^ b));
        System.out.println("NOT bit ~a = " + (~a));
        System.out.println("Desplazamiento a << 2 = " + (a << 2));
        System.out.println("Desplazamiento a >> 2 = " + (a >> 2));
    }
    private static void conditionals(int a, int b) {
        System.out.println("a = " + a + " b = " + b);
        System.out.println("if-else or if:");
        if (a > b) {
            System.out.println("a > b");
        } else {
            System.out.println("a < b");
        }
        System.out.println("switch:");
        switch (a) {
            case 10:
                System.out.println("a = 10");
                break;
            case 5:
                System.out.println("a = 5");
                break;
            default:
                System.out.println("a != 10 && a != 5");
                break;
        }
    }

    private static void iteratives(int a, int b) {
        System.out.println("a = " + a + " b = " + b);
        System.out.println("for:");
        for (int i = 0; i < a; i++) {
            System.out.println("i = " + i);
        }
        
        System.out.println("while:");
        while (b > 0) {
            System.out.println("b = " + b);
            b--;
        }
        
        System.out.println("do while:");
        do {
            System.out.println("a = " + a);
            a--;
        } while (a > 0);
    }

    private static void exceptions() {
        try {
            int[] arr = new int[5];
            System.out.println(arr[5]); // This will throw an exception
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Caught exception: " + e);
        }
    }
    private static void extra(int a, int b) {
        System.out.println("a = " + a + " b = " + b);
        for (int pos = a; pos <= b; pos++) {
            if (pos % 2 == 0 && pos != 16 && pos % 3 != 0) {
                System.out.println("i = " + pos);
            }
        }
    }
}/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */
