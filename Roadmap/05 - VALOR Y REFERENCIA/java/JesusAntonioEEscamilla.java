import java.util.Arrays;

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

    //---EXTRA---
        System.out.println("Extra por Valor");
        extraValor();
        System.out.println("Extra por Referencia");
        extraReferencia();
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

    // Por VALOR
    // Función para intercambiar valores de tipo primitivo
    public static int[] intercambioValores(int a, int b){
        int temp = a;
        a = b;
        b = temp;
        return new int[]{a, b};
    }

    public static void extraValor(){
        // Variables originales
        int x = 5;
        int y = 10;

        // Llamada la nuevas variables en funciones
        int[] resultados = intercambioValores(x, y);
        int nuevoX = resultados[0];
        int nuevoY = resultados[1];

        // Los mostramos el resultado en la consola
        System.out.println("Originales: x = " + x + ", y = " + y);
        System.out.println("Nuevas: nuevoX = " + nuevoX + ", nuevoY = " + nuevoY);
    }


    // Por REFERENCIA
    // Clase contenedor para las lista de referencia
    public static class ListaContenedor {
        int[] lista1;
        int[] lista2;

        public ListaContenedor(int[] lista1, int[] lista2){
            this.lista1 = lista1;
            this.lista2 = lista2;
        }
    }

    // Función para intercambiar las referencia de las lista
    public static ListaContenedor intercambiarLista(ListaContenedor contenedor){
        int[] temp = contenedor.lista1;
        contenedor.lista1 = contenedor.lista2;
        contenedor.lista2 = temp;
        return contenedor;
    }

    public static void extraReferencia(){
        // Variables Originales
        int[] listaA = {1, 2, 3};
        int[] listaB = {4, 5, 6};

        // Crear copias de las listas
        int[] listAOriginal = Arrays.copyOf(listaA, listaA.length);
        int[] listBOriginal = Arrays.copyOf(listaB, listaB.length);

        // Crear contenedores y llamar a la función
        ListaContenedor contenedor = new ListaContenedor(listaA, listaB);
        ListaContenedor nuevasLista = intercambiarLista(contenedor);

        // Los mostramos el resultado en la consola
        System.out.println("Originales: listaA: " + Arrays.toString(listAOriginal) + ", listaB: " + Arrays.toString(listBOriginal));
        System.out.println("Nuevas: listaA: " + Arrays.toString(nuevasLista.lista1) + ", listaB: " + Arrays.toString(contenedor.lista2));
    }

    /**-----DIFICULTAD EXTRA-----*/
}