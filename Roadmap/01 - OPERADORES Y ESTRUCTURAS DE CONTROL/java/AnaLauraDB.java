public class AnaLauraDB {
    public static void main(String[] args) {
        // Operadores aritmeticos
        int a = 10;
        int b = 3;

        int suma = a + b;
        int resta = a - b;
        int multiplicacion = a * b;
        int division = a / b;
        int modulo = a % b;

        System.out.println("Suma: " + suma);
        System.out.println("Resta: " + resta);
        System.out.println("Multiplicación: " + multiplicacion);
        System.out.println("División: " + division);
        System.out.println("Módulo: " + modulo);
        System.out.println();
        // Operadores de comparación
        boolean esIgual = (a == b);
        boolean esDiferente = (a != b);
        boolean esMayor = (a > b);
        boolean esMenor = (a < b);
        boolean esMayorOIgual = (a >= b);
        boolean esMenorOIgual = (a <= b);
        System.out.println("Es igual: " + esIgual);
        System.out.println("Es diferente: " + esDiferente);
        System.out.println("Es mayor: " + esMayor);
        System.out.println("Es menor: " + esMenor);
        System.out.println("Es mayor o igual: " + esMayorOIgual);
        System.out.println("Es menor o igual: " + esMenorOIgual);
        System.out.println();
        // Operadores lógicos
        boolean x = true;
        boolean y = false;
        boolean and = x && y;
        boolean or = x || y;
        boolean not = !x;
        System.out.println("AND: " + and);
        System.out.println("OR: " + or);
        System.out.println("NOT: " + not);
        System.out.println();
        // Operadores de asignación
        int c = 5;
        c += 4;
        System.out.println("Asignación con suma: " + c);
        c -= 2;
        System.out.println("Asignación con resta: " + c);
        c *= 3;
        System.out.println("Asignación con multiplicación: " + c);
        c /= 2;
        System.out.println("Asignación con división: " + c);
        c %= 3;
        System.out.println("Asignación con módulo: " + c);
        System.out.println();
        // Operadores de identidad
        String str1 = new String("Hola");
        String str2 = new String("Hola");
        boolean sonIdenticos = (str1 == str2);
        boolean sonIguales = str1.equals(str2);
        System.out.println("Son idénticos: " + sonIdenticos);
        System.out.println("Son iguales: " + sonIguales);
        System.out.println();
        // Operadores de bits
        int x1 = 5; // 0101 en binario
        int x2 = 3; // 0011 en binario
        int andBit = x1 & x2; // 0001 en binario
        int orBit = x1 | x2; // 0111 en binario
        int xorBit = x1 ^ x2; // 0110 en binario
        int notBit = ~x1; // 1010 en binario (complemento a 1)
        int desplazamientoIzq = x1 << 1; // 1010 en binario (desplazamiento a la izquierda)
        int desplazamientoDerecha = x1 >> 1; // 0010 en binario (desplazamiento a la derecha)
        System.out.println("AND bit a bit: " + andBit);
        System.out.println("OR bit a bit: " + orBit);
        System.out.println("XOR bit a bit: " + xorBit);
        System.out.println("NOT bit a bit: " + notBit);
        System.out.println("Desplazamiento a la izquierda: " + desplazamientoIzq);
        System.out.println("Desplazamiento a la derecha: " + desplazamientoDerecha);
        System.out.println();
        // Operadores de pertenencia
        String[] frutas = { "manzana", "banana", "naranja" };
        boolean contieneManzana = false;
        for (String fruta : frutas) {
            if (fruta.equals("manzana")) {
                contieneManzana = true;
                break;
            }
        }
        // Estructuras de control

        // Condicionales
        if (suma > resta) {
            suma += c;
            System.out.println("Suma actual: " + suma);
        } else if (suma < resta) {
            resta -= c;
            System.out.println("Resta actual: " + resta);
        } else {
            System.out.println("Laura ha creado un reto de programación.");
        }

        // Iterativas
        System.err.println(" ");
        for (b = 0; b < 10; b++) {
            System.out.println("Iteración: " + b);
        }

        System.err.println(" ");
        while (b <= 10) {
            System.out.println("B es menor o igual a 10: " + b);
            b++;
        }

        System.err.println(" ");
        // Do-While
        do {
            System.out.println("B es menor o igual a 10: " + b);
            b--;
        } while (b > 0);

        // Manejo de excepciones
        try {
            int resultado = a / 0; // Esto generará una excepción de división por cero
        } catch (ArithmeticException e) {
            System.out.println("Error: División por cero no permitida.");
        } finally {
            System.out.println("Bloque finally ejecutado.");
        }

        // Extra
        for (int i = 10; i <= 55; i++) {
            if (i % 2 == 0 && i != 16 && i % 3 != 0) {
                System.out.println(i);
            }
        }
    }
}
