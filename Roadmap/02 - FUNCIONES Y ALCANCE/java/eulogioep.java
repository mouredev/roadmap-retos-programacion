public class eulogioep {
    // Variable global (estática en Java)
    private static int contadorGlobal = 0;

    // 1. Método sin parámetros ni retorno
    public static void saludar() {
        System.out.println("¡Hola, mundo!");
    }

    // 2. Método con un parámetro y sin retorno
    public static void saludarPersona(String nombre) {
        System.out.println("¡Hola, " + nombre + "!");
    }

    // 3. Método con múltiples parámetros y retorno
    public static int sumar(int a, int b) {
        return a + b;
    }

    // 4. Método que demuestra una "función" dentro de otra (usando una clase interna)
    public static int operacionMatematica(int a, int b) {
        class Multiplicador {
            int multiplicar(int x, int y) {
                return x * y;
            }
        }
        Multiplicador mult = new Multiplicador();
        return mult.multiplicar(a, b) + 10;
    }

    // 5. Uso de un método incorporado en Java
    public static String obtenerFechaActual() {
        return java.time.LocalDate.now().toString();
    }

    // 6. Demostración de variable local vs global (estática)
    public static void incrementarContador() {
        int contadorLocal = 0;
        contadorLocal++;
        contadorGlobal++;
        System.out.println("Contador local: " + contadorLocal + ", Contador global: " + contadorGlobal);
    }

    // DIFICULTAD EXTRA
    public static int imprimirYContar(String texto1, String texto2) {
        int contadorNumeros = 0;

        for (int i = 1; i <= 100; i++) {
            if (i % 3 == 0 && i % 5 == 0) {
                System.out.println(texto1 + texto2);
            } else if (i % 3 == 0) {
                System.out.println(texto1);
            } else if (i % 5 == 0) {
                System.out.println(texto2);
            } else {
                System.out.println(i);
                contadorNumeros++;
            }
        }

        return contadorNumeros;
    }

    public static void main(String[] args) {
        System.out.println("1. Método sin parámetros ni retorno:");
        saludar();

        System.out.println("\n2. Método con un parámetro y sin retorno:");
        saludarPersona("Alice");

        System.out.println("\n3. Método con múltiples parámetros y retorno:");
        System.out.println("Suma de 5 y 3: " + sumar(5, 3));

        System.out.println("\n4. Método que demuestra una \"función\" dentro de otra:");
        System.out.println("Resultado de operación matemática: " + operacionMatematica(4, 5));

        System.out.println("\n5. Uso de un método incorporado en Java:");
        System.out.println("Fecha actual: " + obtenerFechaActual());

        System.out.println("\n6. Demostración de variable local vs global:");
        incrementarContador();
        incrementarContador();

        System.out.println("\nDIFICULTAD EXTRA:");
        int numerosPuros = imprimirYContar("Fizz", "Buzz");
        System.out.println("Números impresos sin ser reemplazados por texto: " + numerosPuros);
    }
}