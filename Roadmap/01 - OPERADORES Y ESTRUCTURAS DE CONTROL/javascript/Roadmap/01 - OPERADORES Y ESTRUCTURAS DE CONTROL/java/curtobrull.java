public class curtobrull {
    public static void main(String[] args) {

        // Ejemplos con todos los tipos de operadores
        int a = 10;
        int b = 5;

        // Operadores aritméticos
        int sum = a + b;
        int sub = a - b;
        int prod = a * b;
        int div = a / b;
        int mod = a % b;

        System.out.println("Suma: " + a + "+" + b + "=" + sum);
        System.out.println("Resta: " + a + "-" + b + "=" + sub);
        System.out.println("Producto: " + a + "*" + b + "=" + prod);
        System.out.println("División: " + a + "/" + b + "=" + div);
        System.out.println("Módulo: " + a + "%" + b + "=" + mod);

        // Operadores de asignación
        int c = 10;
        c += 5;
        System.out.println("Suma y asignación c += 5:" + c);

        c = 10;
        c -= 5;
        System.out.println("Resta y asignación c -= 5:" + c);

        c = 10;
        c *= 5;
        System.out.println("Producto y asignación c *= 5:" + c);

        c = 10;
        c /= 5;
        System.out.println("División y asignación c /= 5:" + c);

        c = 10;
        c %= 5;
        System.out.println("Módulo y asignación c %= 5:" + c);

        // Operadores de comparación
        System.out.println("a == b: " + (a == b));
        System.out.println("a != b: " + (a != b));
        System.out.println("a > b: " + (a > b));
        System.out.println("a < b: " + (a < b));
        System.out.println("a >= b: " + (a >= b));
        System.out.println("a <= b: " + (a <= b));

        // Operadores lógicos
        boolean trueBool = true;
        boolean falseBool = false;

        System.out.println("trueBool && f: " + (trueBool && falseBool));
        System.out.println("trueBool || f: " + (trueBool || falseBool));
        System.out.println("!trueBool: " + (!trueBool));

        // Operadores de incremento y decremento
        int d = 10;
        d++;
        System.out.println("d = 10 Incremento d++: " + d);

        d = 10;
        d--;
        System.out.println("d = 10 Decremento d--: " + d);

        // Operadores de desplazamiento
        int e = 10;
        System.out.println("e << 1: " + (e << 1));
        System.out.println("e >> 1: " + (e >> 1));


        // Operadores de condicional
        int f = (a > b) ? a : b;
        System.out.println("f = (a > b) ? a : b: " + f);

        // Ejemplos que representen todos los tipos de estructuras de control

        // Estructura de control if
        System.out.println("Estructura de control if");
        if (a > b) {
            System.out.println("a es mayor que b");
        } else {
            System.out.println("a no es mayor que b");
        }

        // Estructura de control switch (mejorado)
        System.out.println("Estructura de control switch");
        int dayNum = 7;

        String day = switch (dayNum) {
            case 1 -> "Lunes";
            case 2 -> "Martes";
            case 3 -> "Miércoles";
            case 4 -> "Jueves";
            case 5 -> "Viernes";
            case 6 -> "Sábado";
            case 7 -> "Domingo";
            default -> "Día no válido";
        };

        System.out.println("El día es: " + day);

        // Estructura de control for
        System.out.println("Estructura de control for");
        for (int i = 0; i < 10; i++) {
            System.out.println("i: " + i);
        }

        // For mejorado
        System.out.println("For mejorado");
        int[] numbers = {1, 2, 3};
        for (int number : numbers) {
            System.out.println("number: " + number);
        }

        // Estructura de control while
        System.out.println("Estructura de control while");
        int numWhile = 0;
        while (numWhile < 3) {
            System.out.println("numWhile: " + numWhile);
            numWhile++;
        }

        // Estructura de control do-while
        System.out.println("Estructura de control do-while");
        int numDoWhile = 0;
        do {
            System.out.println("i: " + numDoWhile);
            numDoWhile++;
        } while (numDoWhile < 3);

        // Estructura de control con break
        System.out.println("Estructura de control con break");
        for (int j = 0; j < 10; j++) {
            if (j == 3) {
                break;
            }
            System.out.println("Break. j: " + j);
        }

        // Estructura de control con continue
        System.out.println("Estructura de control con continue");
        for (int j = 0; j < 5; j++) {
            if (j == 3) {
                continue;
            }
            System.out.println("Continue. j: " + j);
        }

        // Ejercicio extra
        /*
        Imprimir por consola todos los números comprendidos entre 10 y 55 (incluidos), pares,
        y que no son ni el 16 ni múltiplos de 3.
         */

        System.out.println("Ejercicio extra");
        for (int i = 10; i <= 55; i++) {
            if (i == 16 || i % 3 == 0) {
                continue;
            }
            if (i % 2 == 0) {
                System.out.print(i + " ");
            }
        }
    }
}