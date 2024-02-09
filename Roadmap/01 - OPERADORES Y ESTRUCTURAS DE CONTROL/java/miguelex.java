public class miguelex {
    public static void main(String[] args) {
        
        // Operadores aritmeticos

        int a = 5;
        int b = 2;

        System.out.println("Operadores aritmeticos");
        System.out.println("Suma de 5 + 2 = " + (a + b));
        System.out.println("Resta de 5 - 2 = " + (a - b));
        System.out.println("Multiplicacion de 5 * 2 = " + (a * b));
        System.out.println("Division de 5 / 2 = " + (a / b));
        System.out.println("Modulo de 5 % 2 = " + (a % b));

        // Operadores de asignacion

        System.out.println("Operadores de asignacion");
        System.out.println("a = " + a);
        System.out.println("a += 2 = " + (a += 2));

        // Operadores de comparacion

        System.out.println("Operadores de comparacion");
        System.out.println("a == b = " + (a == b));
        System.out.println("a != b = " + (a != b));
        System.out.println("a > b = " + (a > b));
        System.out.println("a < b = " + (a < b));
        System.out.println("a >= b = " + (a >= b));
        System.out.println("a <= b = " + (a <= b));

        // Operadores logicos

        boolean x = true;
        boolean y = false;

        System.out.println("Operadores logicos");
        System.out.println("true && false = " + (x && y));
        System.out.println("true || false = " + (x || y));
        System.out.println("!true = " + (!x));

        // Operadores a nivel de bit

        System.out.println("Operadores a nivel de bit");
        System.out.println("5 & 2 = " + (a & b));
        System.out.println("5 | 2 = " + (a | b));
        System.out.println("5 ^ 2 = " + (a ^ b));
        System.out.println("~5 = " + (~a));
        System.out.println("5 << 2 = " + (a << 2));
        System.out.println("5 >> 2 = " + (a >> 2));
        System.out.println("5 >>> 2 = " + (a >>> 2));

        // if ... else

        System.out.println("if ... else");
        if (a > b) {
            System.out.println("a es mayor que b");
        } else {
            System.out.println("b es mayor que a");
        }

        // switch

        System.out.println("switch");
        switch (a) {
            case 1:
                System.out.println("a es 1");
                break;
            case 2:
                System.out.println("a es 2");
                break;
            case 3:
                System.out.println("a es 3");
                break;
            default:
                System.out.println("a no es 1, 2 o 3");
                break;
        }

        // for

        System.out.println("for");
        for (int i = 0; i < 5; i++) {
            System.out.println("i = " + i);
        }

        // while

        System.out.println("while");
        int i = 0;
        while (i < 5) {
            System.out.println("i = " + i);
            i++;
        }

        // do ... while

        System.out.println("do ... while");
        i = 0;
        do {
            System.out.println("i = " + i);
            i++;
        } while (i < 5);

        // break

        System.out.println("break");
        for (int j = 0; j < 5; j++) {
            if (j == 3) {
                break;
            }
            System.out.println("j = " + j);
        }

        // continue

        System.out.println("continue");
        for (int j = 0; j < 5; j++) {
            if (j == 3) {
                continue;
            }
            System.out.println("j = " + j);
        }

        // try ... catch

        System.out.println("try ... catch");
        try {
            int result = a / 0;
            System.out.println("Resultado: " + result);
        } catch (ArithmeticException e) {
            System.out.println("Error: Division por cero");
        }

        // Extra

        System.out.println("Extra");

        for (i = 10; i <= 55; i++) {
            if (i % 2 == 0 && i != 16 && i % 3 != 0) {
                System.out.println(i);
            }
        }

        
    }
}