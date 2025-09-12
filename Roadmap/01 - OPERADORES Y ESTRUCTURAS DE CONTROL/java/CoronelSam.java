public class CoronelSam {
    public static void main(String[] args) {
        // Operadores aritméticos
        int a = 10;
        int b = 5;
        System.out.println("Suma: " + (a + b));
        System.out.println("Resta: " + (a - b));
        System.out.println("Multiplicación: " + (a * b));
        System.out.println("División: " + (a / b));
        System.out.println("Módulo: " + (a % b));

        // Operadores lógicos
        boolean c = true;
        boolean d = false;
        System.out.println("AND: " + (c && d));
        System.out.println("OR: " + (c || d));
        System.out.println("NOT: " + (!c));

        // Operadores de comparación
        System.out.println("Igualdad: " + (a == b));
        System.out.println("Desigualdad: " + (a != b));
        System.out.println("Mayor que: " + (a > b));
        System.out.println("Menor que: " + (a < b));
        System.out.println("Mayor o igual que: " + (a >= b));
        System.out.println("Menor o igual que: " + (a <= b));

        // Operadores de asignación
        int e = 10;
        e += 5;
        System.out.println("Suma y asignación: " + e);
        e -= 5;
        System.out.println("Resta y asignación: " + e);
        e *= 5;
        System.out.println("Multiplicación y asignación: " + e);
        e /= 5;
        System.out.println("División y asignación: " + e);
        e %= 5;
        System.out.println("Módulo y asignación: " + e);

        // Operadores de identidad
        System.out.println("Igualdad de objetos: " + (a == b));
        System.out.println("Desigualdad de objetos: " + (a != b));

        // Operadores de pertenencia
        int[] f = {1, 2, 3, 4, 5};
        System.out.println("Pertenece: " + (f instanceof int[]));

        // Operadores de bits
        int g = 60; // 60 = 0011 1100
        int h = 13; // 13 = 0000 1101
        System.out.println("AND a nivel de bits: " + (g & h)); // 12 = 0000 1100
        System.out.println("OR a nivel de bits: " + (g | h)); // 61 = 0011 1101
        System.out.println("XOR a nivel de bits: " + (g ^ h)); // 49 = 0011 0001
        System.out.println("Complemento a nivel de bits: " + (~g)); // -61 = 1100 0011
        System.out.println("Desplazamiento a la izquierda: " + (g << 2)); // 240 = 1111 0000
        System.out.println("Desplazamiento a la derecha: " + (g >> 2)); // 15 = 0000 1111
        System.out.println("Desplazamiento a la derecha sin signo: " + (g >>> 2)); // 15 = 0000 1111
        
        // Estructuras de control
        // Condicionales
        if (a > b) {
            System.out.println("a es mayor que b");
        } else {
            System.out.println("a no es mayor que b");
        }

        // Iterativas
        for (int i = 0; i < 5; i++) {
            System.out.println("Iteración " + i);
        }

        // Excepciones
        try {
            int j = 1 / 0;
        } catch (ArithmeticException ex) {
            System.out.println("División por cero");
        }

        // Números entre 10 y 55, pares y no múltiplos de 3 ni 16
        System.out.println("Los numeros son: ");
        for (int k = 10; k <= 55; k++) {
            if (k % 2 == 0 && k != 16 && k % 3 != 0) {
                System.out.println(k);
            }
        }


    }    
}

