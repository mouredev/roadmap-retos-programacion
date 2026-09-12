import java.util.Arrays;
import java.util.HashSet;

public class DennisGD94 {
    public static void main(String[] args) {

        System.out.println("CADENAS");

        String name = "Dennis";

        //longitud
        System.out.println("Longitud: " + name.length());

        //acceso por posición
        System.out.println("Carácter índice 2: " + name.charAt(2));

        //mayúsculas
        System.out.println(name.toUpperCase());

        //minúscula
        System.out.println(name.toLowerCase());

        //subcadenas
        System.out.println(name.substring(1,3));


        String sayHello = "Hola";

        //concatenación(+)
        System.out.println(sayHello + " " + name);

        //concatenación(concat)
        System.out.println(sayHello.concat(name));

        String sayHello2 = sayHello.toUpperCase();

        //comparación
        System.out.println(sayHello.equals(sayHello2));
        System.out.println(sayHello.equalsIgnoreCase(sayHello2));

        //verificación
        System.out.println(sayHello.contains("s"));
        System.out.println(sayHello.startsWith("H"));
        System.out.println(sayHello.endsWith("O"));
        System.out.println(sayHello.isEmpty());
        System.out.println(sayHello.isBlank());

        //búsqueda
        System.out.println(sayHello.indexOf("o"));
        System.out.println(sayHello.lastIndexOf("a"));
        String spaced = "   Hola Dennis   ";

        //limpieza de espacios
        System.out.println(spaced.trim());
        System.out.println(spaced.strip());

        //union
        System.out.println(String.join(" - ", "Dennis", "Java", "Backend"));

        //división y recorrido
        String text = "Buenos días Dennis";
        String[] words = text.split(" ");
        for(String word : words){
            System.out.println(word);
        }

        //remplazo
        System.out.println(spaced.replace("Dennis", "Java"));
        System.out.println(spaced.repeat(3));





        System.out.println("RETO EXTRA");

        System.out.println("Palíndromo");

        String word = "reconocer";

        String reverse = "";

        for(int i = word.length() -1; i >= 0; i--){
            reverse += word.charAt(i);

        }
        System.out.println(reverse);
        System.out.println(word.equals(reverse));


        System.out.println("Anagrama");

        String firstWord = "amor";
        String secondWord = "roma";

        char[] array = firstWord.toCharArray();
        char[] array2 = secondWord.toCharArray();

        Arrays.sort(array);
        Arrays.sort(array2);

        System.out.println(Arrays.equals(array, array2));


        System.out.println("Isograma");

        String isoWord = "murcielago";

        HashSet<Character> list = new HashSet();
        boolean isIsogram = true;

        for(int i = 0; i < isoWord.length(); i++){
           if(!list.add(isoWord.charAt(i))){
               isIsogram = false;
               break;
           }
        }
        System.out.println(isIsogram);


    }
}
