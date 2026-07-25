
public class AFOXJONES{

     public static void main(String[] args) {
        // 1. Operadores
        System.out.println("=== Operadores ===");
        operadoresAritmeticos();
        operadoresLogicos();
        operadoresComparacion();
        operadoresAsignacion();
        operadoresBits();

        // 2. Estructuras de Control
        System.out.println("\n=== Estructuras de Control ===");
        condicionales();
        iterativas();
        manejoExcepciones();


        // 3. Dificultad Extra
        System.out.println("\n=== Dificultad Extra ===");
        extra();
    }

    // Métodos para operadores
    private static void operadoresAritmeticos() {
        System.out.println("-> Operadores Aritméticos");
        int suma = 5 + 3;
        int resta = 10 - 4;
        int multiplicacion = 7 * 2;
        double division = 10.0 / 3.0;
        int modulo = 10 % 3;
        System.out.printf("Suma: %d, Resta: %d, Multiplicación: %d, División: %.2f, Módulo: %d%n", 
                          suma, resta, multiplicacion, division, modulo);
    }

    private static void operadoresLogicos() {
        System.out.println("-> Operadores Lógicos");
        boolean a = true, b = false;
        System.out.println("AND: " + (a && b));
        System.out.println("OR: " + (a || b));
        System.out.println("NOT: " + (!a));
    }

    private static void operadoresComparacion() {
        System.out.println("-> Operadores de Comparación");
        int x = 5, y = 10;
        System.out.println("Igualdad: " + (x == y));
        System.out.println("Mayor que: " + (x > y));
        System.out.println("Menor que: " + (x < y));
        System.out.println("Mayor o igual: " + (x >= 5));
        System.out.println("Menor o igual: " + (y <= 10));
    }

    private static void operadoresAsignacion() {
        System.out.println("-> Operadores de Asignación");
        int z = 10;
        z += 5;
        System.out.println("z += 5: " + z);
        z -= 3;
        System.out.println("z -= 3: " + z);
        z *= 2;
        System.out.println("z *= 2: " + z);
        z /= 4;
        System.out.println("z /= 4: " + z);
    }

    private static void operadoresBits() {
        System.out.println("-> Operadores de Bits");
        int bitA = 5; // 0101 en binario
        int bitB = 3; // 0011 en binario
        System.out.println("AND: " + (bitA & bitB)); // 0001
        System.out.println("OR: " + (bitA | bitB));  // 0111
        System.out.println("XOR: " + (bitA ^ bitB)); // 0110
        System.out.println("Desplazamiento Izquierda: " + (bitA << 1)); // 1010
        System.out.println("Desplazamiento Derecha: " + (bitA >> 1)); // 0010
    }

    // Métodos para estructuras de control
    private static void condicionales() {
        System.out.println("-> Condicionales");
        int valor = 7;
        if (valor > 5) {
            System.out.println("El valor es mayor que 5");
        } else {
            System.out.println("El valor no es mayor que 5");
        }

        // Switch
        switch (valor) {
            case 5:
                System.out.println("El valor es 5");
                break;
            case 7:
                System.out.println("El valor es 7");
                break;
            default:
                System.out.println("El valor no es ni 5 ni 7");
        }
    }

    private static void iterativas() {
        System.out.println("-> Iterativas");

        // For Loop
        System.out.println("Bucle For:");
        for (int i = 1; i <= 5; i++) {
            System.out.println("i = " + i);
        }

        // While Loop
        System.out.println("Bucle While:");
        int j = 1;
        while (j <= 3) {
            System.out.println("j = " + j);
            j++;
        }

        // Do-While Loop
        System.out.println("Bucle Do-While:");
        int k = 5;
        do {
            System.out.println("k = " + k);
            k--;
        } while (k > 0);
    }

    private static void manejoExcepciones() {
        System.out.println("-> Manejo de Excepciones");
        try {
            int resultado = 10 / 0;
            System.out.println("Resultado: " + resultado);
        } catch (ArithmeticException e) {
            System.out.println("Error: División por cero");
        } finally {
            System.out.println("Bloque finally ejecutado");
        }
    }

    // punto extra
    private static void extra(){

        for(int i=10; i<=55; i++){
            if(i%2==0 && i%3!=0 && i!=16)
                System.out.println(i);
        };
    }

}