package Cadena_de_caracteres;
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
public class Cadena_de_caracteres {
    //Creando una cadena de caracteres
   static String mi_cadena = "Soy una cadena de caracteres";

    public static void main(String[] args){
        //Acceder a caracteres específicos
        System.out.println(mi_cadena.charAt(2));

        //Creación de subcadenas
        System.out.println(mi_cadena.substring(8,14));

        //Calcular la longitud de la cadena de caracteres
        System.out.println(mi_cadena.length());

        //Concatenación de cadenas
        System.out.println(mi_cadena.concat(" y estoy creada por alexdevrep"));

        //Repetición de una cadena de caracteres
        System.out.println(mi_cadena.repeat(3));

        //Recorrido de la cadena de caracteres
        for ( int i=0; i<mi_cadena.length();i++){
            System.out.println(mi_cadena.charAt(i));

        }

        //Conversión de la cadena a mayúsculas
        System.out.println(mi_cadena.toUpperCase());

        //Conversión de la cadena a minúsculas
        System.out.println(mi_cadena.toLowerCase());

        //Reemplazo de los caracteres de la cadena
        System.out.println(mi_cadena.replace('c','k'));

        //División de la cadena de caracteres
        System.out.println(mi_cadena.split(" "));

        //Unión de una cadena de caracteres
        String[] partes ={"Hola","mundo"};
        System.out.println(String.join(",",partes));

        //Interpolación de texto en la cadena de caracteres
        String nombre = "Alexdevrep";
        System.out.println(String.format("Hola, %s", nombre));

        //Verificación de caracteres
        System.out.println(mi_cadena.startsWith("S"));






    }


}


