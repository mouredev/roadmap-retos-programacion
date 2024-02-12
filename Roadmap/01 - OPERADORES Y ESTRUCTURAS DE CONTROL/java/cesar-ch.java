public class Main {
    public static void main(String[] args) {
        // Operadores Aritméticos
        int a = 5;
        int b = 2;
        System.out.println("Suma: " + (a + b));
        System.out.println("Resta: " + (a - b));
        System.out.println("Multiplicación: " + (a * b));
        System.out.println("División: " + (a / (double) b));
        System.out.println("Módulo: " + (a % b));
        System.out.println("Incremento: " + (++a));
        System.out.println("Decremento: " + (--b));

        // Operadores de Comparación
        int x = 10;
        String y = "10";
        System.out.println("Igualdad: " + (x == Integer.parseInt(y)));
        System.out.println("Igualdad estricta: " + (x == Integer.parseInt(y)));
        System.out.println("Desigualdad: " + (a != b));
        System.out.println("Mayor que: " + (a > b));
        System.out.println("Menor que o igual: " + (a <= b));

        // Operadores Lógicos
        boolean p = true;
        boolean q = false;
        System.out.println("AND lógico: " + (p && q));
        System.out.println("OR lógico: " + (p || q));
        System.out.println("NOT lógico: " + (!p));

        // Operadores de Asignación
        int c = 3;
        c += 2;
        System.out.println("Asignación con adición: " + c);

        // Operadores de Identidad
        System.out.println("Identidad: " + (x == 10));
        System.out.println("No identidad: " + (Integer.parseInt(y) != 10));

        // Operadores de Pertenencia
        int[] arreglo = {1, 2, 3};
        System.out.println("Pertenece al arreglo: " + (contains(arreglo, 2)));

        // Operadores de Bits
        int num1 = 5; // Representación binaria: 0101
        int num2 = 3; // Representación binaria: 0011
        System.out.println("AND a nivel de bits: " + (num1 & num2)); // Resultado: 0001 (1 en binario)
        System.out.println("OR a nivel de bits: " + (num1 | num2)); // Resultado: 0111 (7 en binario)
        System.out.println("Desplazamiento a la izquierda: " + (num1 << 1)); // Resultado: 1010 (10 en binario)
        System.out.println("Desplazamiento a la derecha: " + (num1 >> 1)); // Resultado: 0010 (2 en binario)

        // Estructuras de Control
        // Condicionales
        int edad = 18;
        if (18 <= edad && edad <= 125) {
            System.out.println("Eres mayor de edad");
        } else if (edad < 18) {
            System.out.println("Eres menor de edad");
        } else {
            System.out.println("Edad no válida");
        }

        // Excepciones
        try {
            double resultado = 10 / 0;
            System.out.println("Resultado: " + resultado);
        } catch (ArithmeticException e) {
            System.out.println("Error: " + e.getMessage());
        } finally {
            System.out.println("Finalizado el bloque try-catch");
        }

        // Programa
        for (int i = 10; i <= 55; i++) {
            if (i % 2 == 0 && i != 16 && i % 3 != 0) {
                System.out.println(i);
            }
        }
    }

    private static boolean contains(int[] array, int targetValue) {
        for (int value : array) {
            if (value == targetValue) {
                return true;
            }
        }
        return false;
    }
}
