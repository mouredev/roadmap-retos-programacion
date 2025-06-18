package source;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Verschlingendenacht {
    
    public static void main(String[] args){
        //arrays();
        //_2darrays();
        //arraylist();
    }

    public static void arrays(){
        String[] colors = new String[5];

        colors[0] = "Green";
        colors[1] = "Yellow";
        colors[2] = "Purple";
        colors[3] = "Red";
        colors[4] = "Blue";

        System.out.println(Arrays.toString(colors));

        int[] numbers = {100, 200, 300};

        for(int i = 0; i < numbers.length; i++){
            System.out.println(numbers[i]);
        }

        for(int i = numbers.length-1; i >= 0; i--){
            System.out.println(numbers[i]);
        }

        for(int number : numbers){
            System.out.println(number);
        }

        Arrays.stream(numbers).forEach(System.out::println);
        //el doble :: nos permite referenciar una funcion o metodo sin llamarla dentro de otra funcion como foreach

        //La clase arrays contiene muchos metodos para lidiar con arreglos
    }

    public static void _2darrays(){

        char[][] board = new char[3][3];

        for(int i = 0; i < 3; i++){
            for(int j = 0; j < 3; j++){
                board[i][j] = '-';
            }
        }

        System.out.println(Arrays.deepToString(board)); //usamos deepToString ya que es un arreglo bidimensional

        char[][] board2 = {
                new char[] {'-','-','-'},
                new char[] {'-','-','-'},
                new char[] {'-','-','-'}
        };

        System.out.println(Arrays.deepToString(board2));

    }

    public static void arraylist(){
        /*
        las listas son implentaciones de las colecciones (las listas son interfaces que al mismo tiempo implementan a las colecciones)
        la diferencia entre una coleccion y una lista es que la lista contiene mas informacion y metodos
         */

        //A pesar de que podemos hacer algo como esto como hariamos en Python:
        List colors = new ArrayList();
        colors.add("Blue");
        colors.add("Purple");
        colors.add(1);
        colors.add(true);
        colors.add(new Object());

        //O esto:

        ArrayList names = new ArrayList();
        names.add("Alejandro");
        names.add("Carlos");
        names.add("Oscar");

        //Debemos tomar preferencia por determinar el tipo a almacenar usando <> (formalizacion) y usar el contrato en la declaracion de la lista
        List<String> colors2 = new ArrayList<>();
        colors2.add("Red");
        colors2.add("Yellow");
        //colors2.add(1); Esta linea resulta en un error de restriccion

        //Al usar List en la declaracion no nos preocupamos por la implementacion que usemos en la asignacion, en la asignacion solo referenciaremos el constructor de alguna implementacion de List como ArrayList

        System.out.println(colors2); //Imprime los contenidos de la lista por defecto
        System.out.println(colors2.contains("Yellow")); //Imprime la existencia o no del elemento especificado

        //Tambien podemos iterar listas de la forma clasica
        for(String color : colors2){
            System.out.println(color);
        }

        colors2.forEach(System.out::println);

        //List tambien nos permite simular tuplas por medio del metodo of el cual retorna una lista inmutable
        List<String> colorsUnmodifiable = List.of("blue","red","black");
        //colorsUnmodifiable.add("white"); Esta linea resulta en un error de modificacion

        System.out.println(colorsUnmodifiable);

    }

}
