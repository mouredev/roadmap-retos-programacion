import java.util.Scanner;

public class SDM29GH {

    public static void main(String[] args) {
        
        String ejemploCadena = "Operaciones de cadena de caracteres";
        String cadena1 = "Hola Mundo"; String cadena2 = "Bienvenido"; String cadena3 = "Bienvenido"; String cadena4 = "BIENVENIDO";
        String cadena5 = "Mundo"; String cadena6 = "Hola"; String cadenaVacía = "";
        
        System.out.println(ejemploCadena);

        /* Método charAt(int index):Retorna el caracter específico en la posición que indica el index.
        Para n cantidad de caracteres, primer posición = 0 y ultima posición = n-1*/
        System.out.println("El primer caracter del ejemplo de la cadena es: " + ejemploCadena.charAt(0));
        System.out.println("El septimo caracter del ejemplo de la cadena es: " + ejemploCadena.charAt(6));
        System.out.println("El ultimo caracter del ejemplo de la cadena es: " + ejemploCadena.charAt(34));

        // Método equals(String str): Sirve para comparar si dos cadenas son iguales.Retona true de ser igual y false si no.
        System.out.println("Método equals(String str)");
        System.out.println("Se compara entre cadena1 y cadena2: "+cadena1.equals(cadena2));
        System.out.println("Se compara entre cadena2 y cadena3: "+cadena2.equals(cadena3));

        /* Método equalsIgnoreCase(String str): Sirve para comparar si dos cadenas son iguales, ignorando la grafía de la palabra. 
        Devuelve true ser iguales y false si no.*/
        System.out.println("Método equalsIgnoreCase(String str)");
        System.out.println("Se compara entre ejemploCadena y cadena1: "+ejemploCadena.equalsIgnoreCase(cadena1));
        System.out.println("Se compara entre cadena2 y cadena1: "+cadena2.equalsIgnoreCase(cadena3));
        System.out.println("Se compara entre cadena3 y cadena4: "+cadena3.equalsIgnoreCase(cadena4));

        /* Método compareTo(String otraCadena): Compara dos cadenas de caracteres alfabéticamente. Retorna 0 por iguales, entero negativo 
        si la primera es menor o entero positivo si la primera es mayor.*/
        System.out.println("Método compareTo(String otraCadena)");
        System.out.println("Se compara entre cadena1 y cadena2: " + cadena1.compareTo(cadena2));
        System.out.println("Se compara entre cadena2 y cadena1: " + cadena2.compareTo(cadena1));
        System.out.println("Se compara entre cadena2 y cadena3: " + cadena2.compareTo(cadena3));

        // Método concat(String st): Concatena la cadena del parámetro al final de la primera cadena.
        System.out.println("Método concat(String st)");
        System.out.println("Concatenación entre cadena1 y cadena2: " + cadena1.concat(cadena2));

        // Método contains(CharSequence s): Retorna true si la cadena contiene la secuencia tipo char del parámetro.
        System.out.println("Método contains(CharSequence)");
        System.out.println("Para saber si cadena1 contiene la secuencia cadena5: "+ cadena1.contains(cadena5));
        System.out.println("Para saber si cadena1 contiene la secuencia cadena6: "+ cadena1.contains(cadena6));

        // Método endsWith(String suffix): Retorna verdadero si la cadena es igual al final del parámetro
        System.out.println("Método endsWith(String suffix)");
        System.out.println("Para saber si cadena5 es igual al final de cadena1: " + cadena1.endsWith(cadena5));
        System.out.println("Para saber si cadena6 es igual al final de cadena1: " + cadena1.endsWith(cadena6));


        // Método indexOf(String str): Retorna el índice de la primera ocurrencia de la cadena del parámetro
        System.out.println("Método indexOf(String str) en la frase: " + ejemploCadena );
        System.out.println("La palabra cadena está desde el índice: " + ejemploCadena.indexOf("cadena"));

        // Método is Empty(): Retorna verdadero si la longitud de la cadena es 0
        System.out.println("Método isEmpty()");
        System.out.println("Para saber si cadena1 está vacía: " + cadena1.isEmpty());
        System.out.println("Para saber si cadena1 está vacía: " + cadenaVacía.isEmpty());

        // Método length(): Para tener la longitud de la cadena
        System.out.println("La longitud del ejemplo de la cadena es: " + ejemploCadena.length() + "caracteres");

        /* Método replaceAll(String regex, String replacement): Reemplaza todas las ocurrencias de la cadena del primer parámetro 
        por la del segundo */
        System.out.println("Método replaceAll(String regex, String replacement)");
        System.out.println("Reemplazar la palabra cadena por texto ejemploCadena: " + ejemploCadena.replaceAll("cadena", "texto"));


        // Método split(String regex): Divide la cadena en subcadenas y las guarda en un arreglo
        System.out.println("Método split(String regex)");
        String[] arreglo = ejemploCadena.split(" ");
        System.out.println("La cadena se divide en: " + arreglo.length + " palabras");
        for (int i = 0; i < arreglo.length; i++) {
            System.out.println("Palabra " + (i + 1) + ": " + arreglo[i]);
        }


        // Método startsWith(String prefix): Retorna verdadero si la cadena comienza con la cadena del parámetro
        System.out.println("Método startsWith(String prefix)");
        System.out.println("Para saber si cadena1 comienza con la palabra Hola: " + cadena1.startsWith("Hola"));
        System.out.println("Para saber si cadena1 comienza con la palabra Bienvenido: " + cadena1.startsWith("Bienvenido"));
        System.out.println("Para saber si cadena1 comienza con la palabra Bienvenido: " + cadena1.startsWith("Bienvenido"));


        /* Método substring(int beginIndex, int endIndex): Retorna una subcadena desde el índice del primer parámetro 
        hasta el índice del segundo parámetro */
        System.out.println("Método substring(int beginIndex, int endIndex)");
        System.out.println("La subcadena de cadena1 desde el índice 0 hasta el índice 3 es: " + cadena1.substring(0, 3));
        System.out.println("La subcadena de cadena1 desde el índice 1 hasta el índice 5 es: " + cadena1.substring(1, 5));
        System.out.println("La subcadena de cadena1 desde el índice 2 hasta el índice 6 es: " + cadena1.substring(2, 6));


        // Método toLowerCase(): Convierte la cadena a minúsculas
        System.out.println("Método toLowerCase()");
        System.out.println("La cadena1 en minúsculas es: " + cadena1.toLowerCase());
        System.out.println("La cadena2 en minúsculas es: " + cadena2.toLowerCase());
        System.out.println("La cadena3 en minúsculas es: " + cadena3.toLowerCase());
        System.out.println("La cadena4 en minúsculas es: " + cadena4.toLowerCase());
        System.out.println("La cadena5 en minúsculas es: " + cadena5.toLowerCase());
        System.out.println("La cadena6 en minúsculas es: " + cadena6.toLowerCase());


        // Método toUpperCase(): Convierte la cadena a mayúsculas
        System.out.println("Método toUpperCase()");
        System.out.println("La cadena1 en mayúsculas es: " + cadena1.toUpperCase());
        System.out.println("La cadena2 en mayúsculas es: " + cadena2.toUpperCase());
        System.out.println("La cadena3 en mayúsculas es: " + cadena3.toUpperCase());
        System.out.println("La cadena4 en mayúsculas es: " + cadena4.toUpperCase());
        System.out.println("La cadena5 en mayúsculas es: " + cadena5.toUpperCase());
        System.out.println("La cadena6 en mayúsculas es: " + cadena6.toUpperCase());
        
        // EXTRA

        /* PALÍNDROMO: palabra, frase, número o cualquier otra secuencia de unidades
        que tiene la propiedad de leerse igual hacia adelante que hacia atrás. */ 
        /*Ejemplo:
        Palabra: "anilina", "arenera".
        Frase: "Anita lava la tina".
        Número: 12321. */
        
        System.out.println("Método Palíndromo");

        Scanner entrada = new Scanner(System.in);

        System.out.println("Ingrese la palabra, frase o número: ");
        String palabra = entrada.nextLine();
        System.out.println("La palabra, frase o número " + palabra + " ¿es un palíndromo?");
        palíndromo(palabra);
        
    }
    public static void palíndromo(String palabra) {
        String cadenaInvertida = "";
        for (int i = palabra.length() - 1; i >= 0; i--) {
            cadenaInvertida += palabra.charAt(i);
        }
        if (palabra.equals(cadenaInvertida)) {
            System.out.println("Es Palíndromo");
        } else {
            System.out.println("No es palíndromo");
        }
    }

}

