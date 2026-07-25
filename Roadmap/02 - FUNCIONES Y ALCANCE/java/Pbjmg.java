public class Pbjmg {
    
    //  Función sin parámetros ni retorno
    public static void saludar() {
        System.out.println("¡Hola! Esta es una función sin parámetros ni retorno.");
    }

    //  Función con un parámetro
    public static void imprimirMensaje(String mensaje) {
        System.out.println("Mensaje recibido: " + mensaje);
    }

    //  Función con varios parámetros y retorno
    public static int sumar(int a, int b) {
        return a + b;
    }

    //  Función que llama a otra función dentro de sí misma (NO se pueden crear dentro de otras)
    public static void mostrarSuma(int x, int y) {
        int resultado = sumar(x, y);
        System.out.println("La suma de " + x + " y " + y + " es: " + resultado);
    }

    //  Uso de una función ya existente en Java
    public static void ejemploFuncionNativa() {
        double raiz = Math.sqrt(25); // Función nativa de Java para raíz cuadrada
        System.out.println("La raíz cuadrada de 25 es: " + raiz);
    }

    //  Demostración de variables locales y globales
    static int global = 100; // Variable global

    public static void variablesLocalesYGlobales() {
        int local = 50; // Variable local
        System.out.println("Variable local dentro de la función: " + local);
        System.out.println("Variable global dentro de la función: " + global);
    }

    public static void main(String[] args) {
        // Llamando a todas las funciones para probarlas
        saludar();
        imprimirMensaje("¡Este es un mensaje de prueba!");
        int resultadoSuma = sumar(5, 7);
        System.out.println("Resultado de la suma: " + resultadoSuma);
        mostrarSuma(8, 3);
        ejemploFuncionNativa();
        variablesLocalesYGlobales();

        // Llamamos a la función del desafío extra
        int vecesNumeros = desafioExtra("Fizz", "Buzz");
        System.out.println("El número de veces que se imprimió un número en lugar de un texto fue: " + vecesNumeros);
    }

    //  DIFICULTAD EXTRA: Función que recibe dos cadenas y retorna un número
    public static int desafioExtra(String palabra1, String palabra2) {
        int contador = 0;

        for (int i = 1; i <= 100; i++) {
            boolean multiploDe3 = (i % 3 == 0);
            boolean multiploDe5 = (i % 5 == 0);

            if (multiploDe3 && multiploDe5) {
                System.out.println(palabra1 + palabra2);
            } else if (multiploDe3) {
                System.out.println(palabra1);
            } else if (multiploDe5) {
                System.out.println(palabra2);
            } else {
                System.out.println(i);
                contador++; // Contamos cuántos números se imprimieron
            }
        }
        return contador;
    }

}
