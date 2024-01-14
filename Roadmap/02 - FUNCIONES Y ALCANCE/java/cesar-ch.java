public class Main {
    static int variableGlobal = 10;

    public static void main(String[] args) {
        // Función sin parámetros ni retorno
        saludar();
        // Función con un parámetro y retorno
        int num = 5;
        int resultadoCuadrado = cuadrado(num);
        System.out.println("Cuadrado de " + num + ": " + resultadoCuadrado);
        // Función con varios parámetros y retorno
        int x = 3;
        int y = 7;
        int resultadoSuma = suma(x, y);
        System.out.println("Suma de " + x + " y " + y + ": " + resultadoSuma);
        // Función dentro de una función
        int resultadoOperacion = operacionMatematica(2, 3);
        System.out.println("Resultado de operación compleja: " + resultadoOperacion);
        // Variable local y global
        funcionConVariables();
        System.out.println("Variable global fuera de la función: " + variableGlobal);
        // DIFICULTAD EXTRA
        int vecesImpreso = imprimirNumerosConTexto("Fizz", "Buzz");
        System.out.println("Número de veces impreso: " + vecesImpreso);

    }

    // Función sin parámetros ni retorno
    static void saludar() {
        System.out.println("¡Hola, mundo!");
    }

    // Función con un parámetro y retorno
    static int cuadrado(int numero) {
        return numero * numero;
    }

    // Función con varios parámetros y retorno
    static int suma(int a, int b) {
        return a + b;
    }

    // Función dentro de una función
    static int cuadruple(int num) {
        return num * 4;
    }

    static int operacionMatematica(int x, int y) {
        return cuadruple(x) + cuadruple(y);
    }

    // Función con variables local y global
    static void funcionConVariables() {
        int variableLocal = 5;
        System.out.println("Variable local dentro de la función: " + variableLocal);
        System.out.println("Variable global dentro de la función: " + variableGlobal);
    }

    // DIFICULTAD EXTRA
    static int imprimirNumerosConTexto(String texto1, String texto2) {
        int contador = 0;

        for (int i = 1; i <= 100; i++) {
            if (i % 3 == 0 && i % 5 == 0) {
                System.out.println(texto1 + texto2);
            } else if (i % 3 == 0) {
                System.out.println(texto1);
            } else if (i % 5 == 0) {
                System.out.println(texto2);
            } else {
                System.out.println(i);
                contador++;
            }
        }

        return contador;
    }
}
