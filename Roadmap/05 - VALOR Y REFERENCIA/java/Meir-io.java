import java.util.*;
import java.util.ArrayList;

public class Meir {
    public static void main(String[] args) {

        int a = 10;
        int b = a;
        b = 20;
        System.out.println("a: " + a);
        System.out.println("b: " + b);


        int[] array1 = {1, 2, 3};
        int[] array2 = array1;
        array2[0] = 99;
        System.out.println("array1[0]: " + array1[0]);
        System.out.println("array2[0]: " + array2[0]);


        String s1 = "Hola";
        String s2 = s1;
        s2 = "Mundo";
        System.out.println("s1: " + s1);
        System.out.println("s2: " + s2);

        int numero = 10;
        modificarValor(numero);
        System.out.println("Después de función: " + numero);


        ArrayList<String> lista = new ArrayList<>();
        lista.add("Java");
        modificarReferencia(lista);
        System.out.println("Después de función: " + lista);

        int x = 5;
        int y = 5;
        System.out.println(x == y);


        String str1 = new String("Java");
        String str2 = new String("Java");
        System.out.println(str1 == str2);
        System.out.println(str1.equals(str2));


        int valor = 4;
        int valor2 = 3;

        ArrayList<Integer> referencia = new ArrayList<>(2);
        ArrayList<Integer> referencia2 = new ArrayList<>(2);
        referencia.add(1);
        referencia.add(2);
        referencia2.add(3);
        referencia2.add(4);


        programa1(valor, valor2);
        programa2(referencia,referencia2);
    }

    static void programa1(int valor,int  valor2) {
        int temp = valor;
        valor = valor2;
        valor2 = temp;
        System.out.println(valor + " " + valor2);
    }
    static void programa2(ArrayList<Integer> lista, ArrayList<Integer> lista2) {
        ArrayList<Integer> temp = lista;
        lista = lista2;
        lista2 = temp;
        System.out.println(lista + " " + lista2);
    }


    static void modificarValor(int numero) {
        numero = 99;
        System.out.println("Dentro de función: " + numero);
    }

    static void modificarReferencia(ArrayList<String> lista) {
        lista.add("Python");
        System.out.println("Dentro de función: " + lista);
    }
}
