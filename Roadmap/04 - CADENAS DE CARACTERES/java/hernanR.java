public class hernanR {
    public static void main(String[] args) {
        // Crear una cadena
        String cadena = "Hola Mundo";
        System.out.println(cadena);

        // Concatenar cadenas
        String cadena2 = " desde Java";
        System.out.println(cadena + cadena2);

        // Obtener la longitud de una cadena
        System.out.println(cadena.length());

        // Acceder a un carácter específico
        System.out.println(cadena.charAt(0));

        // Comparar cadenas
        String cadena3 = "Hola Mundo";
        System.out.println(cadena.equals(cadena3));

        // Buscar en una cadena
        System.out.println(cadena.contains("Mundo"));

        // Extraer una subcadena
        System.out.println(cadena.substring(5, 10));

        // Convertir a mayúsculas o minúsculas
        System.out.println(cadena.toUpperCase());
        System.out.println(cadena.toLowerCase());

        // Reemplazar caracteres o palabras
        System.out.println(cadena.replace("Mundo", "Hernan"));

        // Eliminar espacios en blanco
        String cadena4 = "    Hola Mundo    ";
        System.out.println(cadena4.trim());

        // Dividir una cadena
        String cadena5 = "Hola,Mundo";
        String[] partes = cadena5.split(",");
        for (String parte : partes) {
            System.out.println(parte);
        }

        // Convertir otros tipos a cadena
        int numero = 123;
        System.out.println(String.valueOf(numero));

        // Comprobar si está vacía
        System.out.println(cadena.isEmpty());

        // Repetir una cadena
        System.out.println(cadena.repeat(3));

        // Convertir a un array de caracteres
        char[] caracteres = cadena.toCharArray();
        for (char caracter : caracteres) {
            System.out.println(caracter);
        }

        /*
         * * DIFICULTAD EXTRA (opcional):
         * Crea un programa que analice dos palabras diferentes y realice comprobaciones
         * para descubrir si son:
         * - Palíndromos
         * - Anagramas
         * - Isogramas
         */
        String palabra1 = "reconocer";
        String palabra2 = "recorren";
        System.out.println(esPalindromo(palabra1));
        System.out.println(sonAnagramas(palabra1, palabra2));

    }

    // Método para comprobar si una palabra es palíndromo
    public static boolean esPalindromo(String palabra) {
        return palabra.equals(new StringBuilder(palabra).reverse().toString());
    }

    // Método para comprobar si dos palabras son anagramas
    public static boolean sonAnagramas(String palabra1, String palabra2) {
        return palabra1.length() == palabra2.length()
                && new StringBuilder(palabra1).reverse().toString().equals(palabra2);
    }

    // Método para comprobar si una palabra es isograma
    public static boolean esIsograma(String palabra) {
        return palabra.length() == palabra.chars().distinct().count();
    }
}
