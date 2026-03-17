import java.util.Map;
import java.util.function.Function;
import java.util.stream.Collectors;

/**
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
 * 
 * @version v1.0
 * 
 * @since 04/03/2026
 * 
 * 
 * @author Guillermo-Munoz
 */

public class GuillermoMunoz {

    
    public static void main(String[] args) {

        //Declaramos dos cadenas de caracteres
        // → Crea SIEMPRE un objeto nuevo en el HEAP general
        String cadenaUno = new String("Me apasiona la programación"); // Instanciamos la clase String. Que sería una creación explicita de la clase.
        String cadenaDos = new String("Donde esta el maltido bug"); // Instanciamos la clase String. Que sería una creación explicita de la clase.
        // → Va al "String Pool" (una zona especial dentro del HEAP)
        // Si ya existe esa cadena, reutiliza la referencia
        String cadenaTres = "Me apasiona la programación"; //Crear implícitamente la cadena de texto. Es decir, simplemente le asignamos el valor al objeto.
        String cadenaCuatro = "Donde esta el maltido bug"; //Crear implícitamente la cadena de texto. Es decir, simplemente le asignamos el valor al objeto.

        // == Comparacion referencias (direcciones de memoria)
        System.out.println("****  Metodo ==  ****");
        System.out.println("Comparacion referencias: " + (cadenaUno == cadenaTres)); //false, porque son objetos diferentes en memoria
        System.out.println("Comparacion referencias: " + (cadenaDos == cadenaCuatro)); //false, porque son objetos diferentes en memoria

        // equals() Comparacion de contenido
        System.out.println("****  Metodo equals()  ****");
        System.out.println("Comparacion contenido: " + cadenaUno.equals(cadenaTres)); //true, porque el contenido es el mismo
        System.out.println("Comparacion contenido: " + cadenaDos.equals(cadenaCuatro)); //true, porque el contenido es el mismo  

        // Longitud de la cadena
        System.out.println("****  Metodo length()  ****");
        System.out.println("Longitud cadenaUno: " + cadenaUno.length());
        System.out.println("Longitud cadenaDos: " + cadenaDos.length());
        System.out.println("Longitud cadenaTres: " + cadenaTres.length());
        System.out.println("Longitud cadenaCuatro: " + cadenaCuatro.length());

        //Subcadena
        System.out.println("****  Metodo substring()  ****");
        System.out.println("Subcadena cadenaUno (0, 2): " + cadenaUno.substring(0, 2)); // "Me"
        System.out.println("Subcadena cadenaDos (0, 6): " + cadenaDos.substring(0, 6)); // "Donde"  

        // Concatenación
        System.out.println("****  Metodo concat()  ****");
        System.out.println("Concatenacion cadenaUno + cadenaDos: " + cadenaUno.concat(cadenaDos)); // "Me apasiona la programaciónDonde esta el maltido bug"
        System.out.println("Concatenación cadenaTres + Palabra : " + cadenaTres.concat(" es genial")); // "Me apasiona la programación es genial"

        //Repetición
        System.out.println("****  Metodo repeat()  ****");  
        System.out.println("Repeticion cadenaUno 3 veces: " + cadenaUno.repeat(3)); // "Me apasiona la programaciónMe apasiona la programaciónMe apasiona la programación"
        System.out.println("Repeticion cadenaDos 2 veces: " + cadenaDos.repeat(2)); // "Donde esta el maltido bugDonde esta el maltido bug"

        //Recorrido
        System.out.println("****  Metodo charAt()  ****");  
        for (int i = 0; i < cadenaUno.length(); i++){
            System.out.println("Caracter en posicion " + i + ": " + cadenaUno.charAt(i)); // Imprime cada caracter de la cadenaUno
        }
        
        // Conversión a mayúsculas y minúsculas
        System.out.println("****  Metodo toUpperCase() y toLowerCase()  ****");
        System.out.println("CadenaUno en mayusculas: " + cadenaUno.toUpperCase()); // "ME APASIONA LA PROGRAMACIÓN"
        System.out.println("CadenaDos en minusculas: " + cadenaDos.toLowerCase()); // "donde esta el maltido bug"

        // Reemplazo
        System.out.println("****  Metodo replace()  ****"); 
        System.out.println("Reemplazo en cadenaUno (programación por coding): " + cadenaUno.replace("programación", "coding")); // "Me apasiona la coding"
        System.out.println("Reemplazo en cadenaDos (bug por error): " + cadenaDos.replace("bug", "error")); // "Donde esta el maltido error"

        // División
        System.out.println("****  Metodo split()  ****");
        String[] palabrasCadenaUno = cadenaUno.split(" "); // Divide la cadenaUno en palabras
        System.out.println("Division cadenaUno en palabras: ");
        for (String palabra : palabrasCadenaUno) {
            System.out.println(palabra); // Imprime cada palabra de la cadenaUno
        }

        // Unión
        System.out.println("****  Metodo join()  ****");        
        String[] palabras = {"Me", "apasiona", "la", "programación"};
        String cadenaUnida = String.join(" ", palabras); // Une las palabras con un espacio
        System.out.println("Union de palabras: " + cadenaUnida); // "Me apasiona la programación"
        // Interpolación (en Java se puede hacer con String.format)
        System.out.println("****  Metodo String.format()  ****");
        String nombre = "Guillermo";
        int edad = 100;
        String mensajeInterpolado = String.format("Hola, mi nombre es %s y tengo %d años.", nombre, edad); // Interpola las variables en la cadena
        System.out.println("Mensaje interpolado: " + mensajeInterpolado); // "Hola, mi nombre es Guillermo y tengo 100 años."    

        // Verificación
        System.out.println("****  Metodo startsWith() y endsWith()  ****");
        System.out.println("¿cadenaUno empieza con 'Me'? " + cadenaUno.startsWith("Me")); // true
        System.out.println("¿cadenaDos termina con 'bug'? " + cadenaDos.endsWith("bug")); // true
        System.out.println("¿cadenaTres contiene 'teclado'? " + cadenaTres.contains("teclado")); // false
        System.out.println("¿cadenaCuatro contiene 'ratón'? " + cadenaCuatro.contains("ratón")); // false

        // Comprobamos el metodo esPalindromo
        System.out.println("****  Metodo esPalindromo()  ****");  
        System.out.println("OTTO es palindromo?: " + esPalindormo("OTTO"));
        System.out.println("PESO es palindromo?: " + esPalindormo("PESO"));

        // Comprobamor el metodo anagrama
        System.out.println("****  Metodo esAnagrama()  ****");  
        System.out.println("La palabra casa es anagrama de saca?: " + esAnagrama("casa", "saca"));
        System.out.println("La palabra casa es anagrama de tarta?: " + esAnagrama("casa", "tarta"));

        // Comprobar el metodo Isograma
        System.out.println("****  Metodo esIsograma()  ****");  
        System.out.println("La palabra aro es un isograma?: " + esIsograma("aro"));
        System.out.println("La palagra carro es isograma?: " + esIsograma("carro"));





    }


// Ejercicio Extra Crea un programa que analice dos palabras diferentes y realice comprobaciones para descubrir si son: - Palíndromos- Anagramas- Isogramas

    // Palindromos
    public static boolean esPalindormo(String palabra){

        // Limpieza
        palabra = palabra.toLowerCase().replaceAll("\\s", "");
        String finalPalabra = palabra;

        return java.util.stream.IntStream
                        .range(0, palabra.length() / 2 )
                        .allMatch(i -> finalPalabra.charAt(i) == 
                                        finalPalabra.charAt(finalPalabra.length() - 1 - i));
        
    }

    // Anagrama
    public static boolean esAnagrama(String a, String b){

        // Limpieza
        a = a.toLowerCase().replaceAll("\\s", "");
        b = b.toLowerCase().replaceAll("\\s", "");

        // Comprobar si tiene la misma longitud
        if(a.length() != b.length()) return false;

        Map<Character, Long> mapa1 = a.chars()
                .mapToObj(c -> (char) c)
                .collect(Collectors.groupingBy(
                    Function.identity(),
                    Collectors.counting()
                ));

        Map<Character, Long>  mapa2 = b.chars()
                .mapToObj(c -> (char) c)
                .collect(Collectors.groupingBy(
                    Function.identity(),
                    Collectors.counting()
                ));        
                

        return mapa1.equals(mapa2);
    }

    // Isograma
    public static Boolean esIsograma(String a){

        // Limpieza
        a = a.toLowerCase().replaceAll("\\s", "");

        Map<Character, Long> frecuencia = a.chars()
        .mapToObj(c -> (char) c )
        .collect(Collectors.groupingBy(
            Function.identity(),
            Collectors.counting()
        ));

        return frecuencia.values().stream()
                .allMatch(count -> count == 1);
    }




}
