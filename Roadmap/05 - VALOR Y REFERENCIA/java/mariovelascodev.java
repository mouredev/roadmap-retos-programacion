import java.util.ArrayList;
import java.util.HashSet;

public class mariovelascodev {
    public static void main(String[] args) {
        //Paso por valor
        int number1 = 5;
        int number2 = number1;
        System.out.println("La variable number2 vale: "+number2);
        number2 = 2;
        System.out.println("La variable number2 vale: "+number2);
        System.out.println("La variable number1 vale: "+number1);

        modificarValor(number1);
        System.out.println("La variable number1 vale: "+number1);

        modificarValor(number2);
        System.out.println("La variable number2 vale: "+number2);

        //Paso por referencia
        int [] numbers = {10, 20,30};
        int []  numbers2 = numbers;

        System.out.println("Números del array numbers");
        for(int i=0; i<numbers.length;i++){
            System.out.println(numbers[i]);
        }

        System.out.println("\nNumeros del array numbers2");
        for(int i=0; i<numbers2.length;i++){
            System.out.println(numbers2[i]);
        }

        //Modificamos el array numbers2
        numbers2[0] = 11;

        System.out.println("\nNúmeros del array numbers");
        for(int i=0; i<numbers.length;i++){
            System.out.println(numbers[i]);
        }
        System.out.println("\nNumeros del array numbers2");
        for(int i=0; i<numbers2.length;i++){
            System.out.println(numbers2[i]);
        }

        System.out.println("\nNumeros de los arrays tras llamar a la función");
        modificarArray(numbers2);

        System.out.println("\nNúmeros del array numbers");
        for(int i=0; i<numbers.length;i++){
            System.out.println(numbers[i]);
        }
        System.out.println("\nNumeros del array numbers2");
        for(int i=0; i<numbers2.length;i++){
            System.out.println(numbers2[i]);
        }


        System.out.println("\n-------------EXTRA--------------\n");

        String name = "mario";
        String height = "1.80";

        HashSet<String> lista = new HashSet<>();
        HashSet<String> language = new HashSet<>();

        lista.add("10");
        lista.add("20");
        lista.add("30");
        lista.add("40");

        language.add("Inglés");
        language.add("Frances");
        language.add("Español");

        System.out.println("Name: "+name);
        System.out.println("Altura: "+height);
        cambioPorValor(name, height);
        System.out.println("Name: "+name);
        System.out.println("Altura: "+height);

        System.out.println("HashSet Lista:"+ lista);
        System.out.println("HashSet Language"+language);
        cambioPorReferencia(lista,language);
    }


    //Función paso por valor
    public static void modificarValor(int number){
        number = 23;
        System.out.println("En la función la variable vale: "+number);
    }

    //Función paso por referencia
    public static void modificarArray(int[] array){
        array[0] = 1;
    }

    //EXTRA
    public static void cambioPorValor(String name, String height){
        name = height;
        height = name;
        System.out.println("El valor de la variable name: "+name);
        System.out.println("El valor de la variable height: "+height);
    }

    public static void cambioPorReferencia(HashSet<String> lista, HashSet<String> language){
         lista = language;
         System.out.println("El valor de lista: "+lista);
         System.out.println("El valor de language: "+language);

    }
}
