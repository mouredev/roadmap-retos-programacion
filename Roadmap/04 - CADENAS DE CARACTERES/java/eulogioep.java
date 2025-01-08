public class eulogioep {
    public static void main(String[] args) {
        // Declaración de una cadena
        String texto = "Hola, mundo!";

        // 1. Acceso a caracteres específicos
        char primerCaracter = texto.charAt(0);
        System.out.println("1. Primer carácter: " + primerCaracter);

        // 2. Subcadenas
        String subcadena = texto.substring(0, 4);
        System.out.println("2. Subcadena: " + subcadena);

        // 3. Longitud
        int longitud = texto.length();
        System.out.println("3. Longitud: " + longitud);

        // 4. Concatenación
        String otraCadena = " Bienvenidos";
        String concatenacion = texto.concat(otraCadena);
        System.out.println("4. Concatenación: " + concatenacion);

        // 5. Repetición
        String repetida = texto.repeat(3);
        System.out.println("5. Repetición: " + repetida);

        // 6. Recorrido
        System.out.print("6. Recorrido: ");
        for (char c : texto.toCharArray()) {
            System.out.print(c + " ");
        }
        System.out.println();

        // 7. Conversión a mayúsculas y minúsculas
        System.out.println("7. Mayúsculas: " + texto.toUpperCase());
        System.out.println("   Minúsculas: " + texto.toLowerCase());

        // 8. Reemplazo
        String reemplazo = texto.replace("mundo", "Java");
        System.out.println("8. Reemplazo: " + reemplazo);

        // 9. División
        String[] palabras = texto.split(", ");
        System.out.println("9. División: " + String.join(" | ", palabras));

        // 10. Unión
        String[] arrayPalabras = {"Java", "es", "genial"};
        String union = String.join(" ", arrayPalabras);
        System.out.println("10. Unión: " + union);

        // 11. Interpolación (en Java se usa concat o StringBuilder)
        String nombre = "Alice";
        int edad = 30;
        String interpolacion = "Me llamo " + nombre + " y tengo " + edad + " años.";
        System.out.println("11. Interpolación: " + interpolacion);

        // 12. Verificación
        boolean empiezaCon = texto.startsWith("Hola");
        boolean terminaCon = texto.endsWith("!");
        boolean contiene = texto.contains("mundo");
        System.out.println("12. Empieza con 'Hola': " + empiezaCon);
        System.out.println("    Termina con '!': " + terminaCon);
        System.out.println("    Contiene 'mundo': " + contiene);

        // DIFICULTAD EXTRA
        System.out.println("\nDIFICULTAD EXTRA:");
        String palabra1 = "amor";
        String palabra2 = "roma";

        System.out.println("Palabra 1: " + palabra1);
        System.out.println("Palabra 2: " + palabra2);
        System.out.println("¿Son palíndromos? " + esPalindromo(palabra1) + ", " + esPalindromo(palabra2));
        System.out.println("¿Son anagramas? " + sonAnagramas(palabra1, palabra2));
        System.out.println("¿Son isogramas? " + esIsograma(palabra1) + ", " + esIsograma(palabra2));
    }

    // Método para verificar si una palabra es un palíndromo
    public static boolean esPalindromo(String palabra) {
        String reversa = new StringBuilder(palabra).reverse().toString();
        return palabra.equalsIgnoreCase(reversa);
    }

    // Método para verificar si dos palabras son anagramas
    public static boolean sonAnagramas(String palabra1, String palabra2) {
        if (palabra1.length() != palabra2.length()) {
            return false;
        }
        char[] chars1 = palabra1.toLowerCase().toCharArray();
        char[] chars2 = palabra2.toLowerCase().toCharArray();
        java.util.Arrays.sort(chars1);
        java.util.Arrays.sort(chars2);
        return java.util.Arrays.equals(chars1, chars2);
    }

    // Método para verificar si una palabra es un isograma
    public static boolean esIsograma(String palabra) {
        return palabra.length() == palabra.toLowerCase().chars().distinct().count();
    }
}