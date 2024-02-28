import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.Scanner;

/**
 * GustavoGomez19
 */
public class GustavoGomez19 {

    public static void main(String[] args) {
        // Ejemplos de las operaciones con cadenas de carácteres en Java

        // Creación de una cadena de forma literal
        String name = "Gustavo";
        // Creacupin de una cadena por medio de instancia
        String lastName = new String("Gomez");
        // Concatenacion de Strings
        String fullName = name + lastName;
        // Comparción si son el mismo objeto
        boolean mismoObj = name == lastName;

        /* EJEMPLO STRING MÉTODOS */
        String nombreCompleto = "Gustavo Adolfo Gómez Quiñones";
        // Conocer el número de carácteres de una cadena
        System.out.println("Cantidad de carácteres: " + nombreCompleto.length());
        // Convertir la cadena a MAYÚSCULA
        System.out.println("Cadena en mayúscula: " + nombreCompleto.toUpperCase());
        // Convertir la cadena a minúscula
        System.out.println("Cadena en minúscula: " + nombreCompleto.toLowerCase());
        // Comparación de String a nivel de valor
        System.out.println("Gustavo".equals(nombreCompleto));
        // Comparación de String a nivel de valor ignorando mayúsculas
        System.out.println("gustavo adolfo gómez quiñones".equalsIgnoreCase(nombreCompleto));
        // Comparación de carácteres. Comparación de orden léxico - gráfico
        // Si el valor es 0 las cadenas son iguales
        System.out.println("Gustavo Adolfo Gómez Quiñones".compareTo(nombreCompleto));
        // Si el valor es negativo la cadena es menor a 'nombreCompleto'
        System.out.println("Gustavo".compareTo(nombreCompleto));
        // Si el valor es positivo la cadena es mayor a "Gustavo"
        System.out.println(nombreCompleto.compareTo("Gustavo"));
        // Obtener un carácter en especial
        System.out.println("Carácter del indice 5: " + nombreCompleto.charAt(5));
        // Obtener de forma dinámica el último carácter
        System.out.println("Último carácter: " + nombreCompleto.charAt(nombreCompleto.length() - 1));
        // Obtener un fragmento del String .subString(int a, int b) puede recibir 1 o 2
        // argumentos
        // y siempre el primer argumento es inclusive
        System.out.println("subString con un argumento: " + nombreCompleto.substring(15));
        System.out.println("subString con dos argumentos: " + nombreCompleto.substring(0, 14));
        /*
         * Método replace(). Sirve para reemplazar un carácter por otro, recibe 2
         * parámetros, uno
         * es el carácter a cambiar que es conocido como 'target' y el otro parámetro es
         * por el cual
         * será reemplazado y es conocido como replacement
         */
        String cadena = "Hijo";
        System.out.println("Antes del cambio: " + cadena);
        System.out.println("Después del cambio: " + cadena.replace("o", "@"));
        /*
         * Método indexOf(). Permite saber si se encuentra algún carácter dentro del
         * String y retorna el índice
         * de la primer incidencia, puede recibir como parámetro un String o un char
         */
        System.out.println("Número del indice de la letra solicitada: " + nombreCompleto.indexOf('a'));
        /*
         * Método lastIndexOf(). Permite saber si se encuentra algún carácter dentro del
         * String y retorna el índice
         * de la última incidencia, puede recibir como parámetro un String o un char, si
         * no encuentra coincidencia,
         * retorna un número negativo
         */
        System.out.println("Número del indice de la letra solicitada: " + nombreCompleto.lastIndexOf('s'));
        /*
         * Método contains(). Recibe una cadena y retorna true o false, dependiendo el
         * caso
         */
        System.out.println("Contiene? " + nombreCompleto.contains("Adolfo"));
        /*
         * Método startsWith(). Recibe una secuencia de carácteres, se usa para saber
         * con cual carácter o cadena
         * empieza la cadena y retorna true o false dependiendo el caso
         */
        System.out.println("inicia? " + nombreCompleto.startsWith("G"));
        /*
         * Método endsWith(). Recibe una secuencia de carácteres, se usa para saber con
         * cual carácter o cadena
         * finaliza la cadena y retorna true o false dependiendo el caso
         */
        System.out.println("Finaliza? " + nombreCompleto.endsWith("."));
        /*
         * Método trim(). Elimina los espacios en blanco al principio y al final que
         * pueda tener el String
         */
        String ejemplo = "   Ejemplo   ";
        System.out.println(ejemplo);
        System.out.println(ejemplo.trim());

        /*
         * Ejercicio dificultad extra
         * Crea un programa que analice dos palabras diferentes y realice comprobaciones
         * para descubrir si son:
         * - Palíndromos
         * - Anagramas
         * - Isogramas
         */
        Scanner input = new Scanner(System.in);
        System.out.print("Ingrese la primer palabra: ");
        String palabraUno = input.nextLine();
        System.out.print("Ingrese la segunda palabra: ");
        String palabraDos = input.nextLine();

        
        // Anagrama
        if (esAnagrama(palabraUno, palabraDos)) {
            System.out.println("Las palabras " + palabraUno + " y " + palabraDos + " son anagramas");
        } else {
            System.out.println("Las palabras " + palabraUno + " y " + palabraDos + " no son anagramas");
        }

        //Palindromo
        String frase = "anita lava la tina";
        if (esPalindromo(frase)) {
            System.out.println("La frase '" + frase + "' es un palindromo");
        } else {
            System.out.println("La frase " + frase + " no es un palindromo");
        }

        // Isograma
        String isograma = "murcielago";
        if (esIsograma(isograma)) {
            System.out.println("La palabra " + isograma + " es un isograma.");
        } else {
            System.out.println("La palabra " + isograma + " no es un isograma.");
        }
        

    }

    // Método para saber si dos palabras son anagramas
    public static boolean esAnagrama(String palabraUno, String palabraDos){
        palabraUno = palabraUno.replaceAll("\\s", "").toLowerCase();
        palabraDos = palabraDos.replaceAll("\\s", "").toLowerCase();

        // Verificación si las dos palabras son diferentes en su longitud
        if (palabraUno.length() != palabraDos.length()) {
            return false;
        }

        // Conversión de las palabras en arreglos de carácteres y se ordenan
        char[] arrayPalabraUno = palabraUno.toCharArray();
        char[] arrayPalabraDos = palabraDos.toCharArray();
        Arrays.sort(arrayPalabraUno);
        Arrays.sort(arrayPalabraDos);

        // Comparación de los arrays de carácteres
        return Arrays.equals(arrayPalabraUno, arrayPalabraDos);
    }

    // Método para saber si una frase es palindromo
    public static boolean esPalindromo(String frase){
        frase = frase.replaceAll("\\s", "").toLowerCase();
        // Longitud de la frase
        int longitud = frase.length();

        // Comparación de los carácteres de la frase desde los extremsos hacía adentro
        for (int i = 0; i < longitud / 2; i++) {
            if (frase.charAt(i) != frase.charAt(longitud - 1 - i)) {
                return false; // En caso de que los carácteres no coincidan, no es un palindromo.
            }
        }
        return true; // La frase es un palindromo
    }

    // Método para deterninar un anagrama
    public static boolean esIsograma(String isograma){
        isograma = isograma.replaceAll("\\s", "").toLowerCase();

        // Arreglo que almacena la frecuencia de cada letra
        int[] frecuenciaLetra = new int[26]; // Se toma en consideración las letras del alfabeto ingles

        // Iteración sobre cada letra de la palabra
        for (char letra : isograma.toCharArray()) {
            int indice = letra - 'a'; // Se convierte la letra en un indice entre 0 y 25
            if (frecuenciaLetra[indice] > 0) {
                return false; // Si se encuentra que la letra ya ha aparecido, no es un isograma
            }
            frecuenciaLetra[indice]++; //Se incrementa la frecuencia de la letra
        }
        return true; // La palabra es un isograma
    }

}