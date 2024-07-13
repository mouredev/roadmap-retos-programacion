
import java.util.Arrays;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class reto4_4 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String str = "Hola, Mundo";

        // Acceso a caracteres específicos
        char caracter = str.charAt(0);
        System.out.println("Caracter en la posición 0: " + caracter);

        // Subcadenas
        String subcadena = str.substring(0, 4);
        System.out.println("Subcadena (0-4): " + subcadena);

        // Longitud
        int longitud = str.length();
        System.out.println("Longitud: " + longitud);

        // Concatenación
        String saludo = "Hola" + ", " + "Mundo";
        System.out.println("Concatenación: " + saludo);

        // Repetición
        String repetida = "Hola".repeat(3);
        System.out.println("Repetición: " + repetida);

        // Recorrido
        System.out.print("Recorrido: ");
        for (char c : str.toCharArray()) {
            System.out.print(c + " ");
        }
        System.out.println();

        // Conversión a mayúsculas y minúsculas
        String mayusculas = str.toUpperCase();
        String minusculas = str.toLowerCase();
        System.out.println("Mayúsculas: " + mayusculas);
        System.out.println("Minúsculas: " + minusculas);

        // Reemplazo
        String reemplazo = str.replace('o', 'a');
        String reemplazoPalabra = str.replace("Hola", "Adios");
        System.out.println("Reemplazo de caracteres: " + reemplazo);
        System.out.println("Reemplazo de palabras: " + reemplazoPalabra);

        // División
        String[] palabras = str.split(", ");
        System.out.println("División: ");
        for (String palabra : palabras) {
            System.out.println(palabra);
        }

        // Unión
        String[] partes = { "Hola", "Mundo" };
        String unido = String.join(", ", partes);
        System.out.println("Unión: " + unido);

        // Interpolación (Formateo de cadenas)
        String nombre = "Juan";
        int edad = 30;
        String mensaje = String.format("Mi nombre es %s y tengo %d años.", nombre, edad);
        System.out.println("Interpolación: " + mensaje);

        // Verificación
        boolean empiezaCon = str.startsWith("Hola");
        boolean terminaCon = str.endsWith("Mundo");
        boolean contiene = str.contains("Mundo");
        System.out.println("Empieza con 'Hola': " + empiezaCon);
        System.out.println("Termina con 'Mundo': " + terminaCon);
        System.out.println("Contiene 'Mundo': " + contiene);

        System.out.println("\n ****Desafio**** \n");

        System.out.println("ingrese la primera palabra \n");
        String p1 = input.nextLine();

        System.out.println("ingrese la segunda palabra \n");
        String p2 = input.nextLine();

        if (anagrama(p1, p2)) {
            System.out.println(p1 + " y " + p2 + " Es un anagrma \n");
        } else {
            System.out.println(p1 + " y " + p2 + " No es un anagrma\n");
        }

        polindromo(p1, p2);
        isograma(p1, p2);
    }

    public static void polindromo(String p1, String p2) {
        p1.replaceAll("\\s", "").toLowerCase();
        p2.replaceAll("\\s", "").toLowerCase();

        int n1 = p1.length();
        int n2 = p2.length();
        boolean poli1 = true;
        boolean poli2 = true;

        for (int i = 0; i <= n1 / 2; i++) {

            if (p1.charAt(i) != p1.charAt(n1 - 1 - i)) {

                poli1 = false;
            }
        }
        if (poli1) {
            System.out.println("La palabra " + p1 + " es polindroma \n");
        } else {
            System.out.println("La palabra " + p1 + " no es polindroma \n");
        }

        for (int i = 0; i <= n2 / 2; i++) {
            if (p2.charAt(i) != p2.charAt(n2 - 1 - i)) {

                poli2 = false;

            }

        }
        if (poli2) {
            System.out.println("La palabra " + p2 + " es polindroma \n");
        } else {
            System.out.println("La palabra " + p2 + " no es polindroma \n");
        }

    }

    public static boolean anagrama(String p1, String p2) {
        p1.replaceAll("\\s", "").toLowerCase();
        p2.replaceAll("\\s", "").toLowerCase();

        if (p1.length() != p2.length()) {
            return false;
        }

        char arr1[] = p1.toCharArray();

        char arr2[] = p2.toCharArray();

        Arrays.sort(arr1);
        Arrays.sort(arr2);

        return Arrays.equals(arr1, arr2);
    }

    public static void isograma(String p1, String p2) {
        p1.replaceAll("\\s", "").toLowerCase();
        p2.replaceAll("\\s", "").toLowerCase();

        int n = p1.length();
        int n2 = p2.length();
        boolean iso = true;
        boolean iso2 = true;
        
      Set<Character> vistoCharacters = new HashSet<>();

      for (int i = 0; i < n; i++) {
        char caracterActual = p1.charAt(i);
        if (vistoCharacters.contains(caracterActual)) {
            iso = false;
            break;
        }
        vistoCharacters.add(caracterActual);
      }
        if (iso) {
            System.out.println("La palabra " + p1 + "SI es un isograma \n");
        }else{
            System.out.println("La palabra " + p1 + "no es un isograma \n");
        }

        for (int i = 0; i < n2; i++) {
            char caracterActual = p2.charAt(i);
            if (vistoCharacters.contains(caracterActual)) {
                iso = false;
                break;
            }
            vistoCharacters.add(caracterActual);
          }
            if (iso) {
                System.out.println("La palabra " + p2 + " SI es un isograma\n");
            }else{
                System.out.println("La palabra " + p2 + " No es un isograma \n");
            }
    }
}
