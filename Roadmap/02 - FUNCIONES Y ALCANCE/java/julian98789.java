package MauroDevRetos;

public class reto_2 {

    // Variable global
    static int variableGlobal = 10;

    // Función sin parámetros ni retorno
    public static void funcionSinParametrosNiRetorno() {
        System.out.println("Función sin parámetros ni retorno ejecutada.");
    }

    // Función con parámetros y sin retorno
    public static void funcionConParametros(int a, int b) {
        int suma = a + b;
        System.out.println("Función con parámetros ejecutada. Suma: " + suma);
    }

    // Función con parámetros y con retorno
    public static int funcionConRetorno(int a, int b) {
        return a * b;
    }

    // Función que llama a otras funciones
    public static void funcionQueLlamaOtrasFunciones(int a, int b) {
        funcionSinParametrosNiRetorno();
        funcionConParametros(a, b);
        int resultado = funcionConRetorno(a, b);
        System.out.println("Resultado de la función con retorno: " + resultado);
    }

    // Función anidada (dentro de otra función)
    public static void funcionAnidada() {
        System.out.println("Función externa ejecutada.");

        // Función anidada
        int valorExterno = 5;
        int resultado = sumar(valorExterno, 3);
        System.out.println("Resultado de la función anidada: " + resultado);
    }

    public static int sumar(int a, int b) {
        return a + b;
    }

    // ********Desafio extra*************

    public static int impreso(String c1, String c2) {
        int cont = 0;
        for (int i = 1; i <= 100; i++) {
            if (i % 3 == 0 && i % 5 == 0) {
                System.out.println(c1 + " " + c2);
            } else if (i % 5 == 0) {
                System.out.println(c2);
            } else if (i % 3 == 0) {
                System.out.println(c1);
            } else {
                cont++;
            }

        }
        return cont;
    }

    // Función principal (main) donde se ejecutan las funciones
    public static void main(String[] args) {
        funcionSinParametrosNiRetorno();

        funcionConParametros(3, 7);

        int resultado = funcionConRetorno(4, 6);
        System.out.println("Resultado de la función con retorno: " + resultado);

        funcionQueLlamaOtrasFunciones(2, 4);

        funcionAnidada();

        sumar(2, 4);

        // Accediendo a la variable global desde main
        System.out.println("Valor de la variable global: " + variableGlobal);

        System.out.println(impreso("cadena 1", "cadena 2"));
    }
}
