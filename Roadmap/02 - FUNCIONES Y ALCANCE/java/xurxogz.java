import java.lang.Math;

public class xurxogz {
    // EJERCICIO

    public static int suma(int num1, int num2) { // Con parámetros y con retorno
        return num1 + num2;
    }

    public static String imprimirString() { // Sin parámetros y con retorno 
        return "Hola mundo";
    }

    public static void raizCuadrada(int num1) { // Con parámetros y sin retorno
        System.out.println((int)Math.sqrt(num1));
    }

    public static void saludar() { // Sin parametros y sin retorno
        System.out.println("Hola a todos");
    }

    // DIFICULTAD EXTRA

    public static int dificultadExtra(String texto1, String texto2) {
        int i;
        for (i = 1; i <= 100; i++) {
            if (i % 3 == 0 && i % 5 == 0) {
                System.out.println(texto1 + texto2);
            } else if (i % 3 == 0) {
                System.out.println(texto1);
            } else if (i % 5 == 0) {
                System.out.println(texto2);
            } else {
                System.out.println("");
            }
        }
        return i;
    }

    public static void main(String[] args) {
        System.out.println(suma(2, 3));
        System.out.println(imprimirString());
        raizCuadrada(16);
        saludar();
        dificultadExtra("saca", "puntas");
    }
}