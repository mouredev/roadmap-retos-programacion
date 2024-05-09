public class Worlion {
    /*
 * EJERCICIO: #04 CADENAS DE CARACTERES
 */

    public static void main(String[] args) {
        String cadena = "Hola Mundo";
        System.out.println("Cadena original: " + cadena);

        // Acceso a caracteres específicos
        System.out.println("Primer caracter: " + cadena.charAt(0));
        System.out.println("Último caracter: " + cadena.charAt(cadena.length() - 1));

        // Subcadenas
        System.out.println("Subcadena desde la posición 5: " + cadena.substring(5));
        System.out.println("Subcadena desde la posición 5 hasta la 7: " + cadena.substring(5, 8));

        // Longitud
        System.out.println("Longitud de la cadena: " + cadena.length());

        // Concatenación
        System.out.println("Concatenación: " + cadena.concat(" desde Java"));

        // Repetición
        System.out.println("Repetición: " + cadena.repeat(3));

        // Recorrido
        for (int i = 0; i < cadena.length(); i++) {
            System.out.println("Caracter en la posición " + i + ": " + cadena.charAt(i));
        }

        // Conversión a mayúsculas y minúsculas
        System.out.println("Mayúsculas: " + cadena.toUpperCase());
        System.out.println("Minúsculas: " + cadena.toLowerCase());

        // Reemplazo
        System.out.println("Reemplazo de 'Hola' por 'Adiós': " + cadena.replace("Hola", "Adiós"));

        // División
        String[] palabras = cadena.split(" ");
        for (String palabra : palabras) {
            System.out.println("Palabra: " + palabra);
        }

        // Unión
        System.out.println("Unión de palabras: " + String.join(" ", palabras));

        // Interpolación
        String nombre = "Mundo";
        System.out.println("Interpolación: Hola " + nombre);

        // Verificación
        System.out.println("¿La cadena contiene 'Mundo'?: " + cadena.contains("Mundo"));
    }

}
