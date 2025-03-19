/** #02 - Java -> Jesus Antonio Escamilla */

public class JesusAntonioEEscamilla {
    //  Variable Global
    static String globalVariable = "Soy Global";
    public static void main(String[] args) {
    //---EJERCIÓ---
        //  Función Básica
        saludar();
        //  Función con Parámetro
        personalizado("Antonio");
        //  Función con Varios Parámetros
        sumar(3, 8);
        //  Función con Retorno
        int resultado = multiplicar(6, 4);
        System.out.println("El resultado de la multiplicación es " + resultado);
        //  Funciones dentro de Funciones
        int[] resultados = operacionesComplejas(8, 4);
        System.out.println("La resta es " + resultados[0] + " y la division es " + resultados[1]);
        //  Variables Global y Local
        my_Function();

    //---EXTRA---
        EXTRA("FIZZ", "BUZZ");
    }

    // Función Básica
    public static void saludar(){
        System.out.println("¡¡Hola, Soy Jesus!!");
    }

    // Función con Parámetro
    public static void personalizado(String nombre){
        System.out.println("¡¡Hola, Mundo Soy " + nombre + "!!");
    }

    // Función con Varios Parámetros
    public static void sumar(int a, int b) {
        System.out.println("La suma de " + a + " y " + b + " es " + (a + b));
    }

    //  Función con Retorno
    public static int multiplicar(int a, int b) {
        return a * b;
    }

    //  Funciones dentro de Funciones
    private static int restar(int x, int y){
        return x - y;
    }
    private static int dividir(int x, int y){
        return y / x;
    }
    public static int[] operacionesComplejas(int a, int b){
        int resta = restar(3, 5);
        int divide = dividir(20, 4);
        return new int[] {resta, divide};
    }

    //  Variables Global y Local
    public static void my_Function(){
        String localVariable = "Soy Local";
        System.out.println(localVariable);
        System.out.println(globalVariable);
    }

    /**-----DIFICULTAD EXTRA-----*/

    public static int EXTRA(String text1, String text2){
        int cont = 0;
        for(int number = 1; number <= 100; number++){
            if (number % 3 == 0 && number % 5 == 0) {
                System.out.println(text1 + text2);
            } else if(number % 3 == 0){
                System.out.println(text1);
            } else if(number % 5 == 0){
                System.out.println(text2);
            } else {
                System.out.println(number);
            }
            cont++;
        }
        return cont;
    }

    /**-----DIFICULTAD EXTRA-----*/
}