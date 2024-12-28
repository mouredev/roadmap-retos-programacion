package retosProgramacion;

import java.util.Arrays;
import java.util.Scanner;

public class RetoCinco {

    public static void main(String[] args) {

        //Operaciones con cadenas de caracteres
        //Concatenación
        String a = "Hola";
        String b = "Java";
        System.out.println(a + " " + b + "!");

        //Repetición
        System.out.println(a + " " + a + " " + a);

        //Indexación 
        System.out.println(a.charAt(0));

        //Longitud
        System.out.println(b.length());

        //Búsqueda ||comprobar si una cadena contiene algo
        System.out.println(a.contains("H"));

        //Comprobar si una cadena esta vacía o si contiene algo
        System.out.println(b.isEmpty());

        //Reemplazo
        System.out.println(a.replace("H", "h"));

        //Mayúsculas y minúsculas
        System.out.println(a.toUpperCase());
        System.out.println(b.toLowerCase());

        //Eliminación de espacios al principio y al final
        System.out.println(" Kilianhc ".trim() + "@hotmail.com");

        //División*****
        System.out.println(a.split("l", 2));

        //Comparación
        System.out.println(a.equals(b));
        System.out.println(a.equalsIgnoreCase("holA"));

        //Buscar posición
        System.out.println(a.indexOf("l"));

        //Verificar el comienzo y final de la cadena
        System.out.println(b.startsWith("J"));
        System.out.println(b.endsWith("A"));

        //Obtener una parte de la cadena
        System.out.println(b.substring(1, 3));

        //Convertir cadena en array*****
        char[] array = b.toCharArray();
        System.out.println(array);

        //Formatear cadenas
        System.out.printf("Hola, %s\n", b);

        //Convertir un tipo primitivo a cadena
        int numero = 123;
        String numeroCadena = String.valueOf(numero);
        System.out.println(numeroCadena);

        //Concatenación de múltiples cadenas (usando toString)
        StringBuilder builder = new StringBuilder();
        builder.append(a);
        builder.append(" ");
        builder.append(b);
        String mensajeFinal = builder.toString();
        System.out.println(mensajeFinal);

        //Comparación de cadenas con orden lexicográfico
        System.out.println(a.compareTo(b));

        //Invertir una cadena
        String invertida = new StringBuilder(a).reverse().toString();
        System.out.println(invertida);

        RetoCinco cadenas = new RetoCinco();
        cadenas.palindromo();

    }

    //EXTRA
    public void palindromo() {
        Scanner leer = new Scanner(System.in);
        boolean analisis = true;

        while (analisis) {
            System.out.println("---------Análisis de palabras---------\n"
                    + "Elige una opción para analizar las palabras: \n"
                    + "1. Palíndromos\n"
                    + "2. Anagramas\n"
                    + "3. Isogramas\n"
                    + "4. Salir del programa\n");

            int opcion = leer.nextInt();
            String palabra1;
            String palabra2;

            switch (opcion) {
                case 1:
                    System.out.println("Ingrese la primera palabra: \n");
                    palabra1 = leer.next().replaceAll(" ", "a");
                    String invertida1 = new StringBuilder(palabra1).reverse().toString();
                    System.out.println("Ingrese la segunda palabra: \n");
                    palabra2 = leer.next().replaceAll(" ", "a");
                    String invertida2 = new StringBuilder(palabra2).reverse().toString();
                    if (palabra1.equalsIgnoreCase(invertida1) && palabra2.equalsIgnoreCase(invertida2)) {
                        System.out.println("Las dos palabras son palíndromos\n");
                    } else if (palabra1.equalsIgnoreCase(invertida1)) {
                        System.out.println("Sólo la primera palabra es un palíndromo\n");
                    } else if (palabra2.equalsIgnoreCase(invertida2)) {
                        System.out.println("Sólo la segunda palabra es un palíndromo\n");
                    } else {
                        System.out.println("Ninguna de las 2 palabras es un palíndromo\n");
                    }
                    break;
                case 2:
                    System.out.println("Ingrese la primera palabra: \n");
                    palabra1 = leer.next().replaceAll(" ", "a").toLowerCase();
                    char[] letra1 = palabra1.toCharArray();
                    Arrays.sort(letra1);
                    System.out.println("Ingrese la segunda palabra: \n");
                    palabra2 = leer.next().replaceAll(" ", "a").toLowerCase();
                    char[] letra2 = palabra2.toCharArray();
                    Arrays.sort(letra2);
                    if (palabra1.length() == palabra2.length() && Arrays.equals(letra1, letra2)) {
                        System.out.println("Las palabras son anagramas\n");
                    } else {
                        System.out.println("Las palabras no son anagramas");
                    }
                    break;
                case 3:
                    System.out.println("Ingrese la primera palabra: \n");
                    palabra1 = leer.next().replaceAll(" ", "a").toLowerCase();
                    System.out.println("Ingrese la segunda palabra: \n");
                    palabra2 = leer.next().replaceAll(" ", "a").toLowerCase();
                    if (palabra1.length() == palabra1.chars().distinct().count() && palabra2.length() == palabra2.chars().distinct().count()) {
                        System.out.println("Las dos palabras son isogramas");
                    } else if (palabra1.length() == palabra1.chars().distinct().count()) {
                        System.out.println("Sólo la primera palabra es un isograma");
                    } else if (palabra2.length() == palabra2.chars().distinct().count()) {
                        System.out.println("Sólo la segunda palabra es un isograma");
                    } else {
                        System.out.println("Ninguna de las palabras es un isograma");
                    }
                    break;
                case 4:
                    System.out.println("Salió del programa");
                    analisis = false;
                    break;
            }

        }
        leer.close();
    }

}


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
