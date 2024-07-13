/** #04 - Java -> Jesus Antonio Escamilla */

import java.util.Arrays;

public class JesusAntonioEEscamilla {
    public static void main(String[] args) {
    //---EJERCIÓ---
    // Cadenas de caracteres
        //--STRING--
        String str = "Hola Mundo";
        System.out.println("STRING -> " + str);
        char ch = str.charAt(3);
        System.out.println("Carácter -> " + ch);

        //--SUB-CADENA--
        String subStr = str.substring(5, 10);
        System.out.println("Sub-Cadena -> " + subStr);

        //--LONGITUD--
        int length = str.length();
        System.out.println("Longitud -> " + length);

        //--CONCATENACIÓN--
        String str1 = "Jesus";
        String resultado = str.concat(", soy " + str1);
        System.out.println("Concatenación -> " + resultado);

        //--REPETICIÓN--
        //No hay método directo en Java, pero se puede usar StringBuilder
        String repeated = str.repeat(3);
        System.out.println("Repetición -> " + repeated);

        //--MAYÚSCULAS Y MINÚSCULAS--
        String upper = str.toUpperCase();
        String lower = str.toLowerCase();
        System.out.println("Mayúsculas -> " + upper);
        System.out.println("Minúsculas -> " + lower);

        //--REMPLAZO--
        String replaced = str.replace("Mundo", "Java");
        System.out.println("Remplazo -> " + replaced);

        //--DIVISION--
        String str__ = "Hola,Mundo,Java";
        String[] parts = str__.split(",");
        System.out.println("Division -> " + Arrays.toString(parts));

        //--UNION--
        String[] words = {"Hola", "Mundo", "Java"};
        String joined = String.join("", words);
        System.out.println("Union -> " + joined);

        //--INTERPOLACIÓN--
        String nombre = "Antonio";
        String str_ = String.format("Hola %s", nombre);
        System.out.println("Interpolación -> " + str_);

        //--VERIFICACIÓN--
        // -IGUALDAD-
        String str3 = "Hola Mundo";
        boolean isEqual = str.equals(str3);
        System.out.println("Verificación-Igualdad (Hola Mundo = Hola Mundo) -> " + isEqual);

        // -EMPIEZA-
        boolean startsWith = str.startsWith("Hola");
        System.out.println("Verificación-Principio (Hola Mundo = Hola) -> " + startsWith);

        // -TERMINA-
        boolean endsWith = str.endsWith("Mundo");
        System.out.println("Verificación-Termina (Hola Mundo = Mundo) -> " + endsWith);

        // -CONTIENE-
        boolean contains = str.contains("Mundo");
        System.out.println("Verificación-Contiene (Hola Mundo = Hola-Mundo) -> " + contains);

        // EXTRA()
    }

    /**-----DIFICULTAD EXTRA-----*/

    //Pendiente

    /**-----DIFICULTAD EXTRA-----*/
}