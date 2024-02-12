public class Solucion_02_Java {

    // Variable global
    static String esto_es_una_variable_global = "Variable_local";

    // Método sin parámetros
    public static void funcion_sin_parametros() {
        System.out.println("Esto es una función sin parámetros");
    }

    // Método que recibe un parámetro
    public static void funcion_con_parametros(String nombre) {
        System.out.println("Esto es un saludo para => " + nombre);
    }

    // Método con un parámetro y tipo de dato definido
    public static void funcion_con_tipo_de_datos_definido(String ciudad) {
        System.out.println("Quiero viajar a " + ciudad);
    }

    // Método con parámetros definidos y tipos de datos
    public static void funcion_con_parametros_definidos_suma(int a, int b) {
        System.out.println("El resultado es " + (a + b));
    }

    // Método con retorno y parámetro definido
    public static String funcion_con_retorno(String comida) {
        return "Quisiera probar " + comida + " algún día";
    }

    // Método que muestra una variable global
    public static void funcion_mostrando_variable_global() {
        System.out.println(esto_es_una_variable_global);
    }

    // Método que muestra las tablas de multiplicar según una variable local
    public static void funcion_con_variable_local() {
        java.util.Scanner scanner = new java.util.Scanner(System.in);
        System.out.print("Escribe una tabla de multiplicar => ");
        int tabla_de_multiplicar = scanner.nextInt();

        for (int i = 0; i < 12; i++) {
            System.out.println(tabla_de_multiplicar + " * " + i + " = " + (tabla_de_multiplicar * i));
        }
        scanner.close();
    }


    /*
    * Extra
    * */

    public static int extra(String texto_1, String texto_2) {
        int contador = 0;
        // Mostramos los números del 1 al 100
        for (int i = 1; i <= 100; i++) {
            if (i % 3 == 0 && i % 5 == 0) {
                System.out.println(texto_1 + " y " + texto_2);
            } else if (i % 3 == 0) {
                System.out.println(texto_1);
            } else if (i % 5 == 0) {
                System.out.println(texto_2);
            } else {
                System.out.println(i);
                contador++;
            }
        }
        return contador;
    }
    // Método main para probar los demás métodos
    public static void main(String[] args) {
        funcion_sin_parametros();
        funcion_con_parametros("Juan");
        funcion_con_tipo_de_datos_definido("Leon");
        funcion_con_parametros_definidos_suma(3, 5);
        String resultado_retorno = funcion_con_retorno("Nacatamal");
        System.out.println(resultado_retorno);
        funcion_mostrando_variable_global();
        funcion_con_variable_local();

        //llamamos a la funcion extra
        System.out.println(extra("Mi abuelito me ama", "Mi abuelita me ama"));
    }
}
