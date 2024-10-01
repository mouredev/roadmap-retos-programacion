import java.util.Arrays;

public class DanielBelenguer {
/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 *   interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */

public static void main(String[] args) {
    
    // Creación de cadenas de caracteres
    String cadena = "Hola";

    // Acceso a los caracteres específicos
    System.out.println(cadena.charAt(0)); // H
    System.out.println(cadena.charAt(2)); // l

    // Concatenación o unión
    String cadena2 = " Mundo!";
    cadena = cadena.concat(cadena2);

    System.out.println(cadena); // Hola Mundo!

    // Repetición
    System.out.println(cadena.repeat(3)); // Hola Mundo!Hola Mundo!Hola Mundo!

    // Subcadenas
    System.out.println(cadena); // Esta es la cadena que partimos y vamos a separarla en 2 subcadenas

    String subcadena1 = cadena.substring(0, 4); 
    String subcadena2 = cadena.substring(5, 11);

    System.out.println("Subcadena 1: " + subcadena1);
    System.out.println("Subcadena 2: " + subcadena2);

    // Longitud
    int longitud = cadena.length();
    System.out.println("Longitud de la cadena: " + longitud);

    // Recorrido
    
    for (int i = 0; i < cadena.length(); i++) {
        System.out.println(cadena.charAt(i));
    }

    int sizecadena = 0;
    while (sizecadena < cadena.length()) {
        System.out.println(cadena.charAt(sizecadena));
        sizecadena++;
    }

    for (char caracter : cadena.toCharArray()) {
        System.out.println(caracter);   
        
    }

    // Conversión a mayúsculas y minúsculas

    System.out.println(cadena.toUpperCase());

    System.out.println(cadena.toLowerCase());

    // Reemplazo
    System.out.println(cadena.replace("Hola", "Adios"));

    // División
    String[] palabras = cadena.split(" ");
    for (String palabra : palabras) {
        System.out.println(palabra);
    } /* Con esto lo que conseguimos es separar por el espacio en blanco, si quieres separar por otra cosa, solo tienes que cambiar 
        el argumento del método split */

    // Interpolación
        String nombre = "Daniel";
        int edad = 35;
        String mensaje = String.format ("Hola, mi nombre es %s y tengo %d años", nombre, edad);
        System.out.println(mensaje);

    // Verificación
    
    System.out.println(cadena.contains("Hola")); // true
    System.out.println(cadena.contains("Adios")); // false


    // Ejercicio extra

    String palabra1 = "arroz";
    String palabra2 = "zorra";

    // Comprobacion si son Palíndromos
    if (palabra2.equals(new StringBuilder(palabra1).reverse().toString())) {
        System.out.println("La palabra " + palabra1 + " es un palíndromo");
    } else {
        System.out.println("La palabra " + palabra1 + " no es un palíndromo");
    }

    // Comprobacion si son Anagramas
    if (palabra1.length() == palabra2.length()) {
        char[] palabra1Array = palabra1.toCharArray();
        char[] palabra2Array = palabra2.toCharArray();
        Arrays.sort(palabra1Array);
        Arrays.sort(palabra2Array);
        if (Arrays.equals(palabra1Array, palabra2Array)) {
            System.out.println("Las palabras " + palabra1 + " y " + palabra2 + " son anagramas");
        } else {
            System.out.println("Las palabras " + palabra1 + " y " + palabra2 + " no son anagramas");
        }
    } else {
        System.out.println("Las palabras " + palabra1 + " y " + palabra2 + " no son anagramas");
    }

    // Comprobacion si son Isogramas
    boolean isIsograma = true;
    for (int i = 0; i < palabra1.length(); i++) {
        for (int j = i + 1; j < palabra1.length(); j++) {
            if (palabra1.charAt(i) == palabra1.charAt(j)) {
                isIsograma = false;
                break;
            }
        }
    }
    System.out.println(isIsograma ? "La palabra " + palabra1 + " es un isograma" : "La palabra " + palabra1 + " no es un isograma");




}
}
