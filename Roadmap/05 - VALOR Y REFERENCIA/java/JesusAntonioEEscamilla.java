/** #05 - Java -> Jesus Antonio Escamilla */

public class JesusAntonioEEscamilla {
    public static void main(String[] args) {
    //---EJERCIÓ---
        System.out.println("Asignación de Variable");
        System.out.println("Por Valor");
        variablePorValor();
        System.out.println("Por Referencia");
        variablePorReferencia();
        System.out.println("Variable a Función");
        System.out.println("Por Valor");
        funciónPorValor();
        System.out.println("Por Referencia");
        funciónPorReferencia();
    }

    //---EJERCIÓ---
    
    //--Asignación de Variables--
    // VALOR
    public static void variablePorValor(){
        int a = 5;
        int b = a;

        System.out.println("a: " + a);
        System.out.println("b: " + b);

        b = 10;
        System.out.println("a: " + a);
        System.out.println("b: " + b);
    }

    // REFERENCIA
    public static void variablePorReferencia(){
        int[] array1 = {1, 2, 3};
        int[] array2 = array1;

        System.out.println(java.util.Arrays.toString(array1));
        System.out.println(java.util.Arrays.toString(array2));

        array2[0] = 10;
        System.out.println(java.util.Arrays.toString(array1));
        System.out.println(java.util.Arrays.toString(array2));
    }


    //--Variables a Funciones--
    // VALOR
    public static void modificarValor(int x) {
        x = 10;
    }

    public static void funciónPorValor(){
        int a = 5;
        modificarValor(a);
        System.out.println(a);
    }

    // REFERENCIA
    public static void modificarReferencial(int[] array){
        array[0] = 10;
    }

    public static void funciónPorReferencia(){
        int[] array1 = {1, 2, 3};
        modificarReferencial(array1);
        System.out.println(java.util.Arrays.toString(array1));
    }

    /**-----DIFICULTAD EXTRA-----*/

    //Pendiente

    /**-----DIFICULTAD EXTRA-----*/
}