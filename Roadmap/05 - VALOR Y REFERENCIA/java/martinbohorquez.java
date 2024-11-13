/**
 * #05 VALOR Y REFERENCIA
 *
 * @author martinbohorquez
 */

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class martinbohorquez {

    private static int num1;
    private static int num2;
    private static int[] array1;
    private static int[] array2;
    private static List<Integer> list1;
    private static List<Integer> list2;

    private static int num3;
    private static int num4;
    private static int[] array3;
    private static int[] array4;
    private static List<Integer> list3;
    private static List<Integer> list4;
    private static List<Integer> list5;
    private static List<Integer> list6;

    private static int numA;
    private static int numB;
    private static int[] arrayC;
    private static int[] arrayD;
    private static int[] arrayE;
    private static int[] arrayF;
    private static List<Integer> listG;
    private static List<Integer> listH;
    private static List listI;
    private static List listJ;

    public static void main(String[] args) {
        /*
         * Asignación de variable "por valor"
         */
        num1 = 10;
        num2 = num1;
        num2 = 20;
        System.out.printf("num1: %d y num2: %d%n", num1, num2);

        /*
         * Asignación de variable "por referencia"
         */
        //Array
        array1 = new int[]{10, 20};
        array2 = array1;
        array2[0] = 30;
        array2[1] = 40;
        System.out.printf("array1: %s y array2: %s%n",
                Arrays.toString(array1), Arrays.toString(array2));

        //List
        list1 = new ArrayList<>(Arrays.asList(10, 20));
        list2 = list1;
        list2.add(30);
        System.out.printf("list1: %s y list2: %s%n",
                list1.toString(), list2.toString());

        /*
         * Funciones con asignación de variable "por valor"
         */
        num3 = 100;
        getValue(num3);
        System.out.printf("num3: %d%n", num3);

        /*
         * Funciones con asignación de variable "por referencia"
         */
        array3 = new int[]{100, 200};
        getValue(array3);
        System.out.printf("array3: %s%n", Arrays.toString(array3));

        list3 = new ArrayList<>(Arrays.asList(100, 200));
        getReference(list3);
        System.out.printf("list3: %s%n", list3.toString());

        list5 = new ArrayList<>(Arrays.asList(100, 200));
        getValue(list5);
        System.out.printf("list5: %s%n", list5.toString());

        /**
         * DIFICULTAD EXTRA
         * Crea dos programas que reciban dos parámetros (cada uno)
         * definidos como variables anteriormente.
         */
        // valor
        arrayC = new int[]{1000, 2000};
        arrayD = reverseValue(arrayC);
        System.out.printf("arrayC: %s%n", Arrays.toString(arrayC));
        System.out.printf("arrayD: %s%n", Arrays.toString(arrayD));

        arrayE = new int[]{3000, 4000};
        arrayF = reverseValue(arrayE.clone()); //crea una nueva instancia
        System.out.printf("arrayE: %s%n", Arrays.toString(arrayE));
        System.out.printf("arrayF: %s%n", Arrays.toString(arrayF));

        listG = new ArrayList<>(Arrays.asList(5000, 6000));
        listH = new ArrayList<>(Arrays.asList(7000, 8000));
        List[] listas = reverseReference(listG, listH); //
        listI = listas[0];
        listJ = listas[1];
        System.out.printf("listG: %s, listH: %s%n", listG.toString(), listH.toString());
        System.out.printf("listI: %s, listJ: %s%n", listI.toString(), listJ.toString());

    }

    private static void getValue(int num) {
        num = 200;
        System.out.printf("num: %d%n", num);
    }

    private static void getValue(int[] array) {
        array = new int[]{300, 400}; //crea un nuevo objeto
        System.out.printf("array: %s%n", Arrays.toString(array));
    }

    private static void getReference(List<Integer> list) {
        list.add(300); //usando la misma referencia (objeto en memoria)
        list4 = list;
        list4.add(400);
        System.out.printf("list: %s%n", list.toString());
        System.out.printf("list4: %s%n", list4.toString());
    }

    private static void getValue(List<Integer> list) {
        list.add(300); //usando la misma referencia (objeto en memoria)
        list6 = new ArrayList<>(list); //se crea un nuevo objeto
        list6.add(400);
        System.out.printf("list: %s%n", list.toString());
        System.out.printf("list6: %s%n", list6.toString());
    }

    private static int[] reverseValue(int[] array) {
        int temp = array[0];
        array[0] = array[1];
        array[1] = temp;
        return array;
    }

    private static List[] reverseReference(List list1, List list2) {
        List temp = list1;
        list1 = list2;
        list2 = temp;
        return new List[]{list1, list2};
    }
}
