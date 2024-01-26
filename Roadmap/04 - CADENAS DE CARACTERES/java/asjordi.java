public class Main {

    public static void main(String[] args) {
        // Operaciones con Strings
        opStrings();

        String str1 = "oso";
        String str2 = "oso";

        System.out.println(str1 + " es palíndromo de " + str2 + ": " + esPalindromo(str1, str2));
        System.out.println(str1 + " es anagrama de " + str2 + ": " + esAnagrama(str1, str2));
        System.out.println(str1 + " es isograma de " + str2 + ": " + esIsograma(str1, str2));

    }

    public static void opStrings() {
        // Declarar un String
        String str = "lorem ipsum dolor sit amet consectetur adipiscing elit";
        // Obtener longitud de un String
        System.out.println("Longitud de str: " + str.length());
        // Obtener un caracter de un String
        System.out.println("Primer caracter de str: " + str.charAt(0));
        // Obtener un substring de un String
        System.out.println("Substring de str: " + str.substring(0, 5));
        // Obtener la posición (índice) de un carácter en un String
        System.out.println("Posición de 'i' en str: " + str.indexOf('i'));
        // Obtener el índice de la última posición de un carácter en un String
        System.out.println("Ultima posición de 'i' en str: " + str.lastIndexOf('i'));
        // Obtener un arreglo de Strings a partir de un String
        System.out.println("Arreglo de Strings a partir de str: " + str.split(" "));
        // Obtener un arreglo de caracteres a partir de un String
        System.out.println("Arreglo de caracteres a partir de str: " + str.toCharArray());
        // Obtener un String a partir de un arreglo de caracteres
        System.out.println("String a partir de un arreglo de caracteres: " + new String(str.toCharArray()));
        // Obtener un String a partir de un arreglo de Strings
        System.out.println("String a partir de un arreglo de Strings: " + String.join(" ", str.split(" ")));
        // Repetir un String n veces
        System.out.println("Repetir un String n veces: " + str.repeat(2));
        // Obtener un String en mayúsculas
        System.out.println("String en mayúsculas: " + str.toUpperCase());
        // Obtener un String en minúsculas
        System.out.println("String en minúsculas: " + str.toLowerCase());
        // Obtener un String sin espacios al inicio y al final
        System.out.println("String sin espacios al inicio y al final: " + str.trim());
        // Obtener un String reemplazando caracteres
        System.out.println("String reemplazando caracteres: " + str.replace('i', 'a'));
        // Obtener un String reemplazando caracteres con expresiones regulares
        System.out.println("String reemplazando caracteres con expresiones regulares: " + str.replaceAll("i", "a"));
        // Comparar Strings case sensitive
        System.out.println("Comparar Strings: " + str.equals("lorem ipsum"));
        // Comparar Strings case insensitive
        System.out.println("Comparar Strings: " + str.equalsIgnoreCase("lorem ipsum"));
        // Verificar si un String empieza con un prefijo
        System.out.println("Verificar si un String empieza con un prefijo: " + str.startsWith("lorem"));
        // Verificar si un String termina con un sufijo
        System.out.println("Verificar si un String termina con un sufijo: " + str.endsWith("elit"));
        // Verificar si un String es vacío
        System.out.println("Verificar si un String es vacío: " + str.isEmpty());
        // Verificar si un String no es vacío y no contiene espacios en blanco
        System.out.println("Verificar si un String no es vacío y no contiene espacios en blanco: " + str.isBlank());
        // Concatenar Strings
        System.out.println("Concatenar Strings: " + str.concat(" dolor sit amet"));
        System.out.println();
    }

    /**
     * Crea un programa que analice dos palabras diferentes y realice comprobaciones para descubrir si son:
     * Palíndromos
     * Anagramas
     * Isogramas
     */

    public static boolean esPalindromo(String str1, String str2) {
        return str1.equals(new StringBuilder(str2).reverse().toString());
    }

    public static boolean esAnagrama(String str1, String str2) {
        String sortedStr1 = str1.chars().sorted().collect(StringBuilder::new, StringBuilder::appendCodePoint, StringBuilder::append).toString();
        String sortedStr2 = str2.chars().sorted().collect(StringBuilder::new, StringBuilder::appendCodePoint, StringBuilder::append).toString();
        return sortedStr1.equals(sortedStr2);
    }

    public static boolean esIsograma(String str1, String str2) {
        String distinctStr1 = str1.chars().distinct().collect(StringBuilder::new, StringBuilder::appendCodePoint, StringBuilder::append).toString();
        String distinctStr2 = str2.chars().distinct().collect(StringBuilder::new, StringBuilder::appendCodePoint, StringBuilder::append).toString();
        return distinctStr1.equals(distinctStr2);
    }


}
