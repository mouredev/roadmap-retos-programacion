/**
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * @version 1.0
 * @since 05/03/2026
 * @author Guillermo-Munoz
 */
public class GuillermoMunoz {

    // Funcion que modifica el objeto pasado com parámetro
    public static void valor(int a){
        System.out.println("Funcion Valor (Suma 10 a la variable pasada)");
        System.out.println("Valor recibido: " + a);
        a = a + 10;
        System.out.println("Suma 10 al valor a: " + a);
        System.out.println("Fin de la función Valor");
    }
    // Funcion paso por referencia
    public static void referencia(int[] b){ 
        System.out.println("Funcion Valor (Suma 10 a la variable pasada)");
        System.out.println("Valor recibido: " + b[0]);
        b[0] = b[0] + 10;
        System.out.println("Suma 10 al valor a: " + b[0]);
        System.out.println("Fin de la función Valor");
    }

    public static void main(String[] args) {
        
        //============================================
        // Asignación variable por valor
        //============================================

        int a = 5;
        valor(a);
        System.out.println("Valor de la variable pasada no se modica: " + a );

        //============================================
        // Asignación variable por referencia
        //============================================

            // En Java no existen los punteros explicitos como en (C, C++...) pero en su lugar utiliza referencias a objetos, 
            // los cuales actuan como "punteros seguros".
            // Los objetos se guardan como una dirección de memoria, los cuales al pasar como parametro se envia esa dirección de memoria, 
            // de manera que al trabajar con esos datos se modifican los datos asocidos a esa direccion de memoria

       int[] b = {10};
       referencia(b);
       System.out.println("Valor de la variable pasada por referencia: " + b[0]);

       //=============================================
       // Ejercicio Extra
       //=============================================

            /* DIFICULTAD EXTRA (opcional):
            *   Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
            *   Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
            *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
            *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
            *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
            *   Comprueba también que se ha conservado el valor original en las primeras.
            */

           //Por valor

       int valorA = 10;
       int valorB = 20;
       intercambioPorValor(valorA, valorB);
       System.out.printf("valores fuera de función: %n valorA: %d, valorB: %d %n", valorA, valorB);

           //Por referencia
        int[] ReferenciaA = {10};   
        int[] FerefenciaB = {20};
        intercambioPorReferencia(ReferenciaA, FerefenciaB);
        System.out.printf("valores fuera de función: %n referenciaA: %d, referenciaB: %d %n", ReferenciaA[0], FerefenciaB[0]);

    }
       

            //Función intercambio valor de dos variables pasado por valor
        
        public static void intercambioPorValor(int a, int b){
            System.out.println("Funcion intercambio por valor");
            System.out.printf("valorA vale: %d, valorB vale: %d %n", a, b);
            int temp = a;
            a = b;
            b = temp;
            System.out.println("Intercambio de valor");
            System.out.printf("valorA vale %d, valorB vale: %d %n", a , b);
        }

            //Función intercambio valor de dos variables pasado por referencia
        public static void intercambioPorReferencia(int[] a, int[] b){
            System.out.println("Funcion intercambio por referencia");
            System.out.printf("referenciaA vale: %d, referenciaB vale: %d %n", a[0], b[0]);
            int temp = a[0];
            a[0] = b[0];
            b[0] = temp;
            System.out.println("Intercambio de valor");
            System.out.printf("referenciaA vale %d, referenciaB vale: %d %n", a[0] , b[0]);
        }







        
    
    
}
