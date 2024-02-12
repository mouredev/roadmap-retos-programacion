import java.util.Arrays;
import java.util.Collection;
import java.util.HashMap;


public class kleyner098 {
    /*
     * EJERCICIO:
     * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de
     * caracteres en tu lenguaje. Algunas de esas operaciones podrían ser (busca
     * todas las que puedas):
     * - Acceso a caracteres específicos, subcadenas, longitud,
     * concatenación,repetición, recorrido,conversión a mayúsculas y minúsculas,
     * reemplazo, división, unión,interpolación, verificación...
     */

    public static void main(String[] args) {
        // Declaración e inicialización de una cadena
        String cadena1 = "hola";
        String cadena2 = "mundo";
        String cadena3 = "HOLA";
        String cadena4 = "Un lago AZUL";
        String cadena5 = "Vamos al lago azul";
        String cadena6 = "cadena";
        String cadena7 = "";
        String cadena8 = "deshacer";

        // Mostrar la longittud de la cadena
        System.out.println("Longitud: " + cadena1.length());
        // Obtener un caracter específicando un indice
        System.out.println("El carácter que ocupa la posicion 3 es :" + cadena1.charAt(3));
        // Obtener un cadena específicando un indice
        System.out.println("Obteción de la cadena: " + cadena4.substring(3, 7));
        // Obtener el índice de la primera ocurrencia de un caráter
        System.out.println("El índice del caracter h en la palabra \"hola\" es: " + cadena1.indexOf('h'));
        // Obtener el índice de la primera ocurrencia de una cadena
        System.out.println("El índice del la cadena \"un\" en la palabra \"mundo\" es: " + cadena2.indexOf("un"));
        // Obtener el índice de la primera ocurrencia de una cadena empezando por la
        // derecha
        System.out.println("El índice del la caráter \'a\' en la palabra \"cadena\"  empezando por la derecha es: "
                + cadena6.lastIndexOf('a'));

        // Conparación de cadena
        System.out.println("Comparación entre \"hola\" y la \"HOLA\" con método equals(): " + cadena1.equals(cadena3));
        // Conparación de cadena ignorando mayúscula y minúscula
        System.out.println(
                "Comparación entre \"hola\" y la \"HOLA\" con método equalsIgnoreCase(), ignorando mayúscula y minúscula: "
                        + cadena1.equalsIgnoreCase(cadena3));
        // String es una clase, por lo que utilizar el comparador == no sirve, ya que
        // estaría comparando las referencia de los objetos String
        // Comparar fragmento de candenas
        System.out.println("Comprobación de frgamento de cadena: " + cadena4.regionMatches(3, cadena5, 9, 4));
        // Comparar fragmento de candenas ignorando mayúscula y minúscula
        System.out.println("Comprobación de frgamento de cadena: " + cadena4.regionMatches(true, 8, cadena5, 14, 4));
        // Comparación alfabética, devuelve un int. Si es cero, son iguales; si es
        // negativo, la cadena invocante va antes en orden alfabetico que la cadena
        // pasada por parámetro; si es positivo va despues.
        System.out.println("Comprobación alfabética de cadenas: " + cadena1.compareTo(cadena2));
        // Comparación alfabética ignorando ignorando mayúscula y minúscula
        System.out.println("Comprobación alfabética de cadenas: " + cadena1.compareToIgnoreCase(cadena3));
        // Comprobación de cadena vacía
        System.out.println("Cadena vacía: " + cadena7.isEmpty());
        // Comprobar si una cadena contine una subcadena
        System.out.println("Comprobación de si contiene: " + cadena5.contains("azul"));
        // Comprobación de prefijo y sufijo
        System.out.println("Comprobación de prefijo \"des\" en la palabra \"deshacer\": " + cadena8.startsWith("des"));
        System.out.println("Comprobación de sufijo \"er\" en la palabra \"deshacer\": " + cadena8.endsWith("er"));
        // Concatenación
        String nuevaCadena = cadena1 + " " + cadena2;
        System.out.println("Concatenación: " + nuevaCadena);
        // Otra forma de concatenar
        System.out.println("Otra forma de concatenación: " + cadena1.concat(" " + cadena2));
        // Conversión de tipos
        int num = 1;
        boolean boleano = false;
        double otherNum = 43.23;
        System.out.println("Conversión de tipos de variable: Int-" + String.valueOf(num) + ", boolean-"
                + String.valueOf(boleano) + ", double-" + String.valueOf(otherNum));
        //Conversión a miniscúlas
        System.out.println(cadena4.toLowerCase());
        //Conversión a miniscúlas
        System.out.println(cadena4.toUpperCase());
        //Sustituir cadena 
        System.out.println(cadena5.replace("azul", "rojo"));
        //Romper cadena 
        String[] cadenaArray = cadena5.split(" ");
        System.out.println(Arrays.toString(cadenaArray));
        //Unión de cadenas
        System.out.println(String.join(" ", cadena1,cadena2,cadena3,cadena2));
        // Crear una array de caracteres
        char[] charArray = cadena5.toCharArray();
        System.out.println(Arrays.toString(charArray));

        //Palíndromos
        
        String palabra1 = "zorra";
        String palabra2 = "arroz";
        System.out.printf("Las palabras %1$s y %2$s son palíndromos: %3$s\n",palabra1,palabra2, palindromos(palabra1, palabra2));
        System.out.printf("Las palabras %1$s y %2$s son anagramas: %3$s\n",palabra1,palabra2, palindromos(palabra1, palabra2));
        String palabra3 = "intestinos";
        System.out.printf("La palabra %1$s es isograma: %2$s\n",palabra3, isograma(palabra3));
    }

    /* 
    * DIFICULTAD EXTRA (opcional):
     * Crea un programa que analice dos palabras diferentes y realice comprobaciones
     * para descubrir si son:
     * - Palíndromos
     * - Anagramas
     * - Isogramas
     */
    static public boolean palindromos(String cadena1, String cadena2){
        boolean palindromo = false;
        String cadInvertida = "";
        for (int i = cadena2.length() -1 ; i >= 0; i--) {
            cadInvertida += cadena2.charAt(i);
        }
        if (cadInvertida.toLowerCase().equals(cadena1.toLowerCase())) {
            palindromo = true;
        }
        return palindromo;
    }

    static public boolean anagrama(String cadena1, String cadena2){
        boolean anagrama = false;
        if (cadena1.length() == cadena2.length()) {
            char[] charArray1 = cadena1.toCharArray();
            Arrays.sort(charArray1);
            char[] charArray2 = cadena2.toCharArray();
            Arrays.sort(charArray2);
            if(charArray1.equals(charArray2)){
                anagrama = true;
            }
        }
        return anagrama;
    }

    static public boolean isograma(String cadena){
        boolean isograma = true;
        HashMap<Character,Integer> palabra = new HashMap<>();
        for (int i = 0; i < cadena.length(); i++) {
            if(!(palabra.containsKey(cadena.charAt(i)))){
                palabra.put(cadena.charAt(i), 1);
            }else{
                Integer nuevoValor = palabra.get(cadena.charAt(i)) + 1;
                palabra.put(cadena.charAt(i), nuevoValor);
            }

            Collection<Integer> contadorLetras = palabra.values();
            for (Integer values : contadorLetras) {
                if(values != 1 && values % 2 != 0){
                    isograma = false;
                    break;
                }
            }
        }
        return isograma;
    }
}
