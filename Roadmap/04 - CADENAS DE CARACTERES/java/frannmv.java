import java.lang.String;
import java.util.*;

import static java.lang.StringTemplate.STR;

public class frannmv {

    public static void main(String[] args) {
    /*  ************
        Operaciones con Cadenas de Caracteres
        ************
    */
        String cadena = "RoadMap 2024";

        char caracterEspecifico = cadena.charAt(0); // Acceso a Caracter Especifico
        System.out.println(caracterEspecifico);

        System.out.println(cadena.substring(8)); // Substring - Desde la posicion pasada por parametro hasta
                                                          // el final del String

        System.out.println(cadena.substring(0,7)); // Substring - Desde la posicion pasada en el pirmer parametro hasta
                                                  // la posicion del segundo parametro - 1

        System.out.println(cadena.length()); // Longitud de la Cadena

        System.out.println(cadena.concat(" Con Java").concat(" - OOP")); // Concatenacion

        System.out.println(cadena.repeat(2)); // Repetición - El String "cadena" se repite 2 veces

        System.out.println(cadena.toUpperCase()); // Conversion a mayuscula

        System.out.println(cadena.toLowerCase()); // Conversion a minuscula

        String reemplazarCaracter = cadena.replace('4','5');
        System.out.println(reemplazarCaracter); // Reemplazar Caracter

        String reemplazarCadena = cadena.replace("RoadMap", "MapRoad");
        System.out.println(reemplazarCadena); // Reemplazar Cadena

        String nuevaCadena = "Java-Object-Oriented-Programming";
        String[] palabras = nuevaCadena.split("-"); // División
        for(String palabra : palabras){
            System.out.println(palabra);
        }

        String cadenaConcatenada = cadena + nuevaCadena;
        System.out.println(cadenaConcatenada); // Union - Concatenacion

        nuevaCadena = "Java";
        String inter = STR."Estoy programando en \{nuevaCadena}";
        System.out.println(inter); // Interpolación

        inter = String.format("Estoy programando en %s", nuevaCadena);
        System.out.println(inter); // Interpolación

        System.out.println(nuevaCadena.equals(cadena)); // Verificacion

    /*  ************
        Extra
        ************
    */
        Scanner keyboard = new Scanner(System.in);
        System.out.println("Ingrese la primera palabra: ");
        String palabra1 = keyboard.nextLine();

        System.out.println("Ingrese la segunda palabra: ");
        String palabra2 = keyboard.nextLine();

        mostrarResultados(palabra1,palabra2);
    }

    private static String darVuelta(String s){
        char[] caracteres = s.toCharArray();
        StringBuilder newString = new StringBuilder();
        for(int i = caracteres.length - 1; i >= 0; i--){
            newString.append(caracteres[i]);
        }
        return newString.toString();
    }
    private static boolean esPalindromo(String s) {
        String cadenaEnReversa = darVuelta(s);
        return s.equals(cadenaEnReversa);
    }

    private static int cantidadQueAparece(char c, char[] array){
        int vecesQueAparece = 0;
        for(int i = 0; i<array.length; i++){
            if(array[i] == c)
                vecesQueAparece++;
        }
        return vecesQueAparece;
    }
    private static void cargarMapa(Map<Character,Integer> a, String s){
        char[] c = s.toCharArray();
        for(char caracter : c){
            a.putIfAbsent(caracter,cantidadQueAparece(caracter,c));
        }
    }
    private static boolean sonAnagrama(String s1, String s2) {
        Map<Character, Integer> cadena1 = new HashMap<>();
        Map<Character, Integer> cadena2 = new HashMap<>();

        cargarMapa(cadena1,s1);
        cargarMapa(cadena2,s2);

        for(Map.Entry<Character,Integer> entry : cadena1.entrySet()){
            if(cadena2.containsKey(entry.getKey()) && entry.getValue() == cadena2.get(entry.getKey())){

            }else{
                return false;
            }
        }
        return true;
    }
   private static boolean esIsograma(String s){
       Set<Character> caracteres = new HashSet<>();
       char[] cadenaToChar = s.toCharArray();
       for(char caracter : cadenaToChar){
           caracteres.add(caracter);
       }
       return s.length() == caracteres.size();
   }
    private static void mostrarResultados(String palabra1, String palabra2){
        System.out.println(String.format("La palabra %s es palindromo: %b",palabra1,esPalindromo(palabra1)));
        System.out.println(String.format("La palabra %s es palindromo: %b",palabra2,esPalindromo(palabra2)));
        System.out.println("-----------------------------------------");

        System.out.println(String.format("Las palabra %s y %s son anagrama: %b",palabra1,palabra2, sonAnagrama(palabra1,palabra2)));
        System.out.println("-----------------------------------------");

        System.out.println(String.format("La palabra %s es isograma: %b",palabra1,esIsograma(palabra1)));
        System.out.println(String.format("La palabra %s es isograma: %b",palabra2,esIsograma(palabra2)));
        System.out.println("-----------------------------------------");
    }
}
