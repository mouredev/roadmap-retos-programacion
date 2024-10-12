public class eulogioep {
    public static void main(String[] args) {
        // Ejemplos de operadores en Java

        // 1. Operadores Aritméticos
        System.out.println("--- Operadores Aritméticos ---");
        System.out.println("Suma: 5 + 3 = " + (5 + 3));
        System.out.println("Resta: 10 - 4 = " + (10 - 4));
        System.out.println("Multiplicación: 6 * 2 = " + (6 * 2));
        System.out.println("División: 15 / 3 = " + (15 / 3));
        System.out.println("Módulo: 17 % 5 = " + (17 % 5));
        System.out.println("Incremento: int a = 5; a++; a = " + (new Object() { int run() { int a = 5; a++; return a; }}.run()));
        System.out.println("Decremento: int b = 8; b--; b = " + (new Object() { int run() { int b = 8; b--; return b; }}.run()));

        // 2. Operadores de Asignación
        System.out.println("\n--- Operadores de Asignación ---");
        int x = 10;
        System.out.println("Asignación simple: x = 10; " + x);
        x += 5;
        System.out.println("Suma y asignación: x += 5; " + x);
        x *= 2;
        System.out.println("Multiplicación y asignación: x *= 2; " + x);

        // 3. Operadores de Comparación
        System.out.println("\n--- Operadores de Comparación ---");
        System.out.println("Igualdad: 5 == 5 es " + (5 == 5));
        System.out.println("Desigualdad: 5 != 6 es " + (5 != 6));
        System.out.println("Mayor que: 7 > 5 es " + (7 > 5));
        System.out.println("Menor o igual que: 10 <= 10 es " + (10 <= 10));

        // 4. Operadores Lógicos
        System.out.println("\n--- Operadores Lógicos ---");
        System.out.println("AND lógico: true && false es " + (true && false));
        System.out.println("OR lógico: true || false es " + (true || false));
        System.out.println("NOT lógico: !true es " + (!true));

        // 5. Operadores de Tipo
        System.out.println("\n--- Operadores de Tipo ---");
        System.out.println("instanceof: \"\" instanceof String es " + ("" instanceof String));

        // 6. Operadores de Bits
        System.out.println("\n--- Operadores de Bits ---");
        System.out.println("AND a nivel de bits: 5 & 3 = " + (5 & 3));
        System.out.println("OR a nivel de bits: 5 | 3 = " + (5 | 3));
        System.out.println("XOR a nivel de bits: 5 ^ 3 = " + (5 ^ 3));
        System.out.println("Desplazamiento a la izquierda: 5 << 1 = " + (5 << 1));

        // Ejemplos de estructuras de control

        // 1. Estructura Condicional: if-else
        System.out.println("\n--- Estructura Condicional: if-else ---");
        int numero = 15;
        if (numero > 10) {
            System.out.println("El número es mayor que 10");
        } else if (numero < 10) {
            System.out.println("El número es menor que 10");
        } else {
            System.out.println("El número es igual a 10");
        }

        // 2. Estructura Condicional: switch
        System.out.println("\n--- Estructura Condicional: switch ---");
        String dia = "Lunes";
        switch (dia) {
            case "Lunes":
                System.out.println("Hoy es Lunes");
                break;
            case "Martes":
                System.out.println("Hoy es Martes");
                break;
            default:
                System.out.println("Es otro día de la semana");
        }

        // 3. Estructura Iterativa: for
        System.out.println("\n--- Estructura Iterativa: for ---");
        for (int i = 0; i < 5; i++) {
            System.out.println("Iteración for: " + i);
        }

        // 4. Estructura Iterativa: while
        System.out.println("\n--- Estructura Iterativa: while ---");
        int contador = 0;
        while (contador < 3) {
            System.out.println("Iteración while: " + contador);
            contador++;
        }

        // 5. Estructura Iterativa: do-while
        System.out.println("\n--- Estructura Iterativa: do-while ---");
        int j = 0;
        do {
            System.out.println("Iteración do-while: " + j);
            j++;
        } while (j < 3);

        // 6. Manejo de Excepciones: try-catch
        System.out.println("\n--- Manejo de Excepciones: try-catch ---");
        try {
            throw new Exception("Este es un error de ejemplo");
        } catch (Exception e) {
            System.out.println("Error capturado: " + e.getMessage());
        } finally {
            System.out.println("Este bloque siempre se ejecuta");
        }

        // DIFICULTAD EXTRA
        System.out.println("\n--- DIFICULTAD EXTRA ---");
        for (int num = 10; num <= 55; num++) {
            if (num % 2 == 0 && num != 16 && num % 3 != 0) {
                System.out.println(num);
            }
        }
    }
}