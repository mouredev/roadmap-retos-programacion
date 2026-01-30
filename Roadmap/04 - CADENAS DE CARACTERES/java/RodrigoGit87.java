/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */
import java.util.*;
import java.util.ArrayList;

public class RodrigoGit87 {

    // extra
    public static void checkWord(String string1, String string2) {
        // Normalizar las palabras (convertir a minúsculas y eliminar espacios)
        String palabra1 = string1.toLowerCase().replace(" ", "");
        String palabra2 = string2.toLowerCase().replace(" ", "");

        System.out.println("\n=== ANÁLISIS DE PALABRAS ===");
        System.out.println("Palabra 1: " + string1);
        System.out.println("Palabra 2: " + string2);
        System.out.println("============================\n");

        // Verificar palíndromos
        boolean esPalindromo1 = esPalindromo(palabra1);
        boolean esPalindromo2 = esPalindromo(palabra2);

        System.out.println("¿'" + string1 + "' es palíndromo? " + esPalindromo1);
        System.out.println("¿'" + string2 + "' es palíndromo? " + esPalindromo2);

        // Verificar anagramas
        boolean sonAnagramas = sonAnagramas(palabra1, palabra2);
        System.out.println("\n¿Son anagramas? " + sonAnagramas);

        // Verificar isogramas
        boolean esIsograma1 = esIsograma(palabra1);
        boolean esIsograma2 = esIsograma(palabra2);

        System.out.println("\n¿'" + string1 + "' es isograma? " + esIsograma1);
        System.out.println("¿'" + string2 + "' es isograma? " + esIsograma2);
    }

    // Método auxiliar para verificar si una palabra es palíndromo
    private static boolean esPalindromo(String palabra) {
        int longitud = palabra.length();
        for (int i = 0; i < longitud / 2; i++) {
            if (palabra.charAt(i) != palabra.charAt(longitud - 1 - i)) {
                return false;
            }
        }
        return true;
    }

    // Método auxiliar para verificar si dos palabras son anagramas
    private static boolean sonAnagramas(String palabra1, String palabra2) {
        // Si tienen diferente longitud, no pueden ser anagramas
        if (palabra1.length() != palabra2.length()) {
            return false;
        }

        // Convertir las palabras a arrays de caracteres y ordenarlos
        char[] chars1 = palabra1.toCharArray();
        char[] chars2 = palabra2.toCharArray();

        Arrays.sort(chars1);
        Arrays.sort(chars2);

        // Comparar los arrays ordenados
        return Arrays.equals(chars1, chars2);
    }

    // Método auxiliar para verificar si una palabra es isograma
    private static boolean esIsograma(String palabra) {
        // Usar un conjunto para verificar caracteres únicos
        java.util.HashSet<Character> caracteresVistos = new java.util.HashSet<>();

        for (int i = 0; i < palabra.length(); i++) {
            char c = palabra.charAt(i);
            // Si el carácter ya existe en el conjunto, no es isograma
            if (caracteresVistos.contains(c)) {
                return false;
            }
            caracteresVistos.add(c);
        }
        return true;
    }

    public static void main(String[] args) {
        // --- STRINGS ---
        System.out.println("--- operaciones básicas con Strings ");
        //los Strings son objetos (no tipos primitivos) y tienen una característica fundamental: son inmutables.
        // Esto significa que cuando creas un String, no puedes modificarlo.
        // Cuando "modificas" un String (por ejemplo, pasándolo a mayúsculas), Java no cambia el original, sino que crea uno nuevo en memoria
        String vacio = "";
        String saludo = "Hola Mundo";
        // .length devuelve la longitud
        IO.println(vacio.length()); // <-- 0
        IO.println(saludo.length()); // <-- 11
        // .isEmpty, booleano, devuelve true si el length == 0
        IO.println(vacio.isEmpty());
        IO.println(saludo.isEmpty());
        // isBlank(): Devuelve true si la cadena está vacía o solo contiene espacios en
        IO.println(vacio.isBlank());
        IO.println(saludo.isBlank());

        System.out.println("--- operaciones comparación con Strings ");
        // .equals(otro string) y equalsIgnoreCase(otro string), comparan el string d la
        // variable con el string entre parentesis
        IO.println(saludo.equalsIgnoreCase("hola mundo"));
        IO.println(saludo.equalsIgnoreCase(vacio));
        // compareTo(otro string): Devuelve un número (0 si son iguales, negativo si la
        // primera es menor alfabéticamente, positivo si es mayor). Muy útil para
        // ordenar listas.
        String saludoInverso = "Mundo Hola";
        IO.println(saludo.compareToIgnoreCase(saludoInverso));

        System.out.println("--- operaciones busqueda y acceso");
        // charAt(int indice)
        IO.println(saludo.charAt(0));
        // contains(CharSequence s) Devuelve true si la cadena contiene la secuencia
        // indicada
        IO.println(saludoInverso.contains("Mundo")); // true, por que "Mundo" si esta contenido en saludoInverso
        // indexof, Devuelve la posición de la primera aparición del texto buscado.
        // Devuelve -1 si no lo encuentra.
        IO.println(saludo.indexOf("u"));

        System.out.println("--- modificacion");
        // siguientes metodos devuelven un NUEVO String, no reemplazan el original
        String original = " Retos de MoureDev";
        IO.println(original.length());
        IO.println(original.indexOf("M"));
        // substring(int inicio, int fin): Extrae una parte de la cadena. El índice fin
        // es exclusivo (no se incluye)
        String cortado = original.substring(0, 10);
        IO.println(cortado);
        // .trim() <-- Quita espacios del principio y del final
        IO.println(original.trim());
        // .toLowerCase y .toUpperCase
        String enMayus = original.toUpperCase();
        String enMinus = original.toLowerCase();
        IO.println(enMayus + " : " + enMinus);
        // replace <- remplaza caracteres o secuencias
        String kit = "kit";
        String reemplazado = kit.replace("i", "a");
        IO.println(kit + "-" + reemplazado);
        


        System.out.println("--- Dividir y unir");
        System.out.println(".split()");
        // Util con texto separado por comas , lineas, puntos .... DEvuelven un array
        // split()
        String listaContactos = "Juan, Alfredo, RodrigoGit87, MoureDev, El gato volador";
        String[] contactos = listaContactos.split(",");
        for (String c : contactos) {
            System.out.print(c);
        }
        // String.join() <-- Une texto separado
        System.out.println("\n.join()");
        String años = String.join(",", "2020", "2021", "2022", "2023");
        IO.println(años);
        // es mas usado para ArrayList
        ArrayList<String> añosList = new ArrayList<>();
        añosList.add(" 2024");
        añosList.add(" 2025");
        añosList.add(" 2026");
        añosList.add(" 2027");

        String resultado = String.join("/", añosList);
        IO.println(resultado);

        System.out.println("--- Conversion");
        String numRandom = "500";
        // Integer.valueOf() <-- De String a Integer (objeto wrapper), q es util cuando
        // queremos usar lo devuelto para añadir a una List por ejemplo
        int añosInteger = Integer.valueOf(numRandom);
        IO.println("Integer: " + añosInteger);
        // Integer.parseInt(): Devuelve un int (tipo primitivo)., q es mas usado en
        // operaciones aritméticas
        int añosInt = Integer.parseInt(numRandom);
        IO.println("int: " + añosInt);
        // String.valueOf(): Convierte cualquier tipo primitivo (int, double, boolean) a
        // String
        double estatura = 1.81;
        String altura = String.valueOf(estatura);
        IO.println(altura);
        // forma rápida (y menos purista) añadiendo una cadena vacia al int, se
        // convierte en String automaticamente por Java
        String alturaRapida = estatura + "";
        //tocharArray <- Convierte un string en un array de caracteres
        String palabra = "palabra";
        char[] letras = palabra.toCharArray();
        IO.println(letras); 
        // Arrays.sort (ordena un array de caracteres pro orden alfabetico ' o numerico')
        Arrays.sort(letras);
        IO.println(letras);
            //podemos usar el metodo de comparacion equals con los arrays tambien
            char[] letras2 = {'a','b','c'};
            IO.println(Arrays.equals(letras, letras2));        


        System.out.println("\n\n========================================");
        System.out.println(" EXTRA: ");
        System.out.println("========================================");

        // Ejemplo 1: Palíndromos
        checkWord("ana", "oso");

        // Ejemplo 2: Anagramas
        checkWord("amor", "roma");

        // Ejemplo 3: Isogramas
        checkWord("murcielago", "python");

        // Ejemplo 4: Combinación
        checkWord("reconocer", "arenero");
    }
}
