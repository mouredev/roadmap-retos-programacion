public class AnaLauraDB {
    public static void main(String[] args) {
        String text1 = "Ana Laura";
        String text2 = "estas repasando logica de programacion";

        // Concatenar cadenas de caracteres
        String concatenated = text1 + " " + text2;
        System.out.println(" " + concatenated);

        // Obtener la longitud de una cadena
        int length = concatenated.length();
        System.out.println("La longitud de la cadena es: " + length);

        // Convertir a mayusculas
        String upperCase = concatenated.toUpperCase();
        System.out.println("La cadena en mayusculas es: " + upperCase);

        // Convertir a minusculas
        String lowerCase = concatenated.toLowerCase();
        System.out.println("La cadena en minusculas es: " + lowerCase);

        // Reemplazar una subcadena
        String replaced = concatenated.replace("Ana", "Ana Lau");
        System.out.println("La cadena con reemplazo es: " + replaced);

        // Dividir la cadena en un arreglo de subcadenas
        String[] split = concatenated.split(" ");
        System.out.println("La cadena dividida en subcadenas es:");
        for (String str : split) {
            System.out.println(str);
        }

        // Comparar cadenas si son iguales
        String anotherText = "Ana Laura estas repasando Logica de Programacion";
        boolean areEqual = concatenated.equals(anotherText);
        System.out.println("Las cadenas son iguales: " + areEqual);
        // Comparar cadenas ignorando mayusculas y minusculas
        boolean areEqualIgnoreCase = concatenated.equalsIgnoreCase(anotherText);
        System.out.println("Las cadenas son iguales (ignorando mayusculas y minusculas):" + areEqualIgnoreCase);

        // Interpoacion de cadenas
        String interpolated = String.format("Hola %s, %s", text1, text2);
        System.out.println("Interpoacion de cadenas: " + interpolated);

        // Verificar si una cadena contiene otra
        boolean contains = concatenated.contains("repasando");
        System.out.println("La cadena contiene 'repasando': " + contains);

        // EXTRA
        // --- Análisis de dos palabras ---
        String palabra1 = "amor";
        String palabra2 = "roma";

        // Palíndromo
        boolean esPalindromo1 = palabra1.equalsIgnoreCase(new StringBuilder(palabra1).reverse().toString());
        boolean esPalindromo2 = palabra2.equalsIgnoreCase(new StringBuilder(palabra2).reverse().toString());
        System.out.println("¿'" + palabra1 + "' es palíndromo?: " + esPalindromo1);
        System.out.println("¿'" + palabra2 + "' es palíndromo?: " + esPalindromo2);

        // Anagrama
        boolean sonAnagramas = sonAnagramas(palabra1, palabra2);
        System.out.println("¿'" + palabra1 + "' y '" + palabra2 + "' son anagramas?: " + sonAnagramas);

        // Isograma
        boolean esIsograma1 = esIsograma(palabra1);
        boolean esIsograma2 = esIsograma(palabra2);
        System.out.println("¿'" + palabra1 + "' es isograma?: " + esIsograma1);
        System.out.println("¿'" + palabra2 + "' es isograma?: " + esIsograma2);
    }

    // Función para comprobar anagramas
    public static boolean sonAnagramas(String w1, String w2) {
        w1 = w1.replaceAll("\\s+", "").toLowerCase();
        w2 = w2.replaceAll("\\s+", "").toLowerCase();
        if (w1.length() != w2.length())
            return false;
        char[] arr1 = w1.toCharArray();
        char[] arr2 = w2.toCharArray();
        java.util.Arrays.sort(arr1);
        java.util.Arrays.sort(arr2);
        return java.util.Arrays.equals(arr1, arr2);
    }

    // Función para comprobar isogramas
    public static boolean esIsograma(String palabra) {
        palabra = palabra.toLowerCase();
        java.util.HashSet<Character> letras = new java.util.HashSet<>();
        for (char c : palabra.toCharArray()) {
            if (letras.contains(c))
                return false;
            letras.add(c);
        }
        return true;

    }
}
