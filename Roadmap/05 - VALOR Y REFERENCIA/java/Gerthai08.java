import com.sun.security.jgss.GSSUtil;

import java.util.Arrays;
import java.util.LinkedList;

public class Gerthai08 {
    public static void main(String[] args) {

        int value = 10;
        LinkedList<String> reference = new LinkedList<String>();

        //Asignación de variables por "VALOR"
        System.out.println("=====Asignación de variables por \"VALOR\"=====\n");
        System.out.println("Antes de llamar al método \"updateValue\": " + value);
        updateValue(value);
        System.out.println("Después de llamar al método \"updateValue\": " + value);

        //Asignación de variables por "REFERENCIA"
        System.out.println("\n=====Asignación de variables por \"REFERENCIA\"=====\n");
        reference.add("Juan");
        reference.add("Pedro");
        reference.add("Esteban");
        reference.add("Carlos");

        System.out.println("Recorriendo arrayList:");
        displayNames(reference);

        System.out.println("\nRecorriendo la lista antes de llamar al método \"displayNamesWithModification\"");
        displayNamesWithModification(reference);
        System.out.println(" ");
        //Los cambios se mantienen porque el método recibe una referencia al mismo objeto en memoria.
        displayNames(reference);
        }

    //Método para "asignación de variables"
    private static void updateValue(int value) {
        System.out.println("Valor recibido en \"updateValue\": " + value);
        value = 20;
        System.out.println("Valor después de la modificación en \"updateValue\": " + value);
    }

    //Métodos para "asignación por referencias"
    //Recorriendo la lista "reference"
    private static void displayNames(LinkedList<String> reference) {
        for(String name : reference){
            System.out.println(name);
        }
    }

    private static void displayNamesWithModification(LinkedList<String> reference) {
        System.out.println("\nVisualizando nombres dentro del método:");
        for(String name : reference){
            System.out.println(name);
        }

        //Modificando un elemento de la arrayList
        reference.set(0,"German");
        System.out.println("\nNombres después de la modificación:");
        for(String name : reference){
            System.out.println(name);
        }

        //Ejercicio extra
        System.out.println("\n=====Asignación de variables por valor=====");
        int value1 = 10;
        int value2 = 20;
        System.out.println(investedValue(value1,value2));
        System.out.println("valores llamados después del método valor1: " + value1 + " valor2: " + value2);

        System.out.println("\n=====Asignación de variables por referencia=====");
        String[] array1 = {"Juan","Pedro","Samuel"};
        String[] array2 = {"German","Sofia","Estaban"};
        System.out.println(investedReference(array1,array2));
        System.out.println("valores llamados despues del método: " + Arrays.toString(array1) + " array2: " + Arrays.toString(array2));
    }

    private static String investedReference(String[] array1, String[] array2){
        String previousReference = "valores antes del método array1: " + Arrays.toString(array1) + " array2: " + Arrays.toString(array2);
        //invirtiendo arrays
        for (int i = 0; i < array1.length; i++) {
            String temp = array1[i];
            array1[i] = array2[i];
            array2[i] = temp;
        }
        String afterReference = "\nvalores modificados en el método array1: " + Arrays.toString(array1) + " array2: " + Arrays.toString(array2);
        return previousReference + afterReference;
    }

    private static String investedValue(int value1, int value2){
        String previousValue = "valores antes del método valor1: " + value1 + " valor2: " + value2;
        //Invirtiendo variables
        value1 = 20;
        value2 = 10;
        String updateValue = "\nvalores modificados en el método valor1: " + value1 + " valor2: " + value2;
        return previousValue + updateValue ;
    }
}
