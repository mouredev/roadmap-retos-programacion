import java.util.Arrays;

public class AmadorQuispe {
    public static void main(String[] args) {
        opStrins();
        String string1 = " taco cat";
        long startTime = System.nanoTime();
        System.out.println("Es palindrome :" + isPalindrome(string1));
        System.out.println(System.nanoTime() - startTime);

        long startTime1 = System.nanoTime();
        System.out.println("Es anagrama con conteo : " + isAnagramWithCounting("termo", "remot"));
        System.out.println(System.nanoTime() - startTime1);

        long startTime2 = System.nanoTime();
        System.out.println("Es anagrama con oredenamiento : " + isAnagramWithSort("termo", "remot"));
        System.out.println(System.nanoTime() - startTime2);

        long startTime3 = System.nanoTime();
        System.out.println("Es isogram : " + isIsogram("termometro"));
        System.out.println(System.nanoTime() - startTime3);

    }

    private static void opStrins() {
        String string = "Hello World, RoadMap 2024";
        String anotherString = new String("Hello World, Roadmap 2024");
        // length(), numero de caracteres
        System.out.println("longitud :" + string.length());
        // charAt - Devuelve el valor del carácter en el índice especificado
        System.out.println("Carácter en el indice 1: " + string.charAt(1));

        // compareTo(String anotherString) Compara dos cadenas lexicográficamente.
        // retorna 0 si son iguales y diferente a 0 si no lo son
        System.out.println("Comparación : " + string.compareTo(anotherString));
        // compareToIgnoreCase(String anotherString) hace lo mismo que compareTo pero
        // ignora diferencias mayúsculas y minúsculas
        System.out.println("Comparación IgnoreCase : " + string.compareToIgnoreCase(anotherString));
        // concat(String str) , Concatena la cadena especificada al final de esta cadena
        System.out.println("Concatenación : " + string.concat("!!!"));
        // contains(CharSequence s), Devuelve verdadero si y sólo si esta cadena
        // contiene la secuencia especificada de valores de caracteres
        System.out.println("Contiene? :" + string.contains("2024"));
        // contentEquals(CharSequence s) se utiliza para comparar cos cadenas
        System.out.println("Comparar : " + string.contentEquals(anotherString));
        // endsWith(String suffix) Prueba si esta cadena termina con el sufijo
        // especificado
        System.out.println("Termina con 2024? : " + string.endsWith("2024"));
        // equals(Object anObject), Compara dos cadenas con el objeto especificado
        System.out.println("Es igual ? : " + string.equals(anotherString));
        // equalsIgnoreCase(Object anObject), Compara dos cadenas con el objeto
        // especificado, ignora mayúsculas de minúsculas
        System.out.println("Es igual IgnoreCase? : " + string.equalsIgnoreCase(anotherString));
        // format(String format, Object... args), Devuelve una cadena formateada
        // utilizando la cadena de formato y los argumentos especificados.
        System.out.println("Formateo: " + String.format("Inicio %s final!!!", string));
        // indexOf(String str), Devuelve el índice dentro de esta cadena de la primera
        // aparición de la sub cadena especificada
        System.out.println("Indice de 'W' : " + string.indexOf("W"));
        // join(CharSequence delimiter, CharSequence... elements)
        // Devuelve una nueva cadena compuesta por copias de los elementos CharSequence
        // unidas con una copia del delimitador especificado
        System.out.println("Unión: " + String.join(" - ", string, anotherString));
        // matches(String regex), Indica si esta cadena coincide o no con la expresión
        // regular dada
        System.out.println("Uso de expresiones regulares : " + string.matches("[A-Z].*"));
        // replace(char oldChar, char newChar), Devuelve una cadena resultante de
        // reemplazar todas las apariciones de oldChar en esta cadena con newChar.
        System.out.println("Reemplazo:  " + string.replace("o", "0"));
        // replaceAll(String regex, String replacement)
        // Reemplaza cada sub cadena de esta cadena que coincide con la expresión
        // regular dada con el reemplazo dado
        System.out.println("Reemplazo regex: " + string.replaceAll("[0-9]", "-"));
        // replaceFirst(String regex, String replacement)
        // Reemplaza la primera sub cadena de esta cadena que coincide con la expresión
        // regular dada con el reemplazo dado.
        System.out.println("Reemplazo regex primera aparición: " + string.replaceFirst("o", "#"));
        // split(String regex)
        // Divide la cadena entre coincidencias de la expresión regular dada
        String[] strings = string.split(" ");
        System.out.println("Division: " + Arrays.toString(strings));
        // startsWith(String prefix), Prueba si esta cadena comienza con el prefijo
        // especificado
        System.out.println("Empieza con ?: " + string.startsWith("H"));
        // substring(int beginIndex, int endIndex)
        // Devuelve una cadena que es una sub cadena de esta cadena. endIndex(exclusivo)
        System.out.println("Sub cadena: " + string.substring(0, 5));
        // toLowerCase(), Convierte todos los caracteres de esta cadena a minúsculas
        // utilizando las reglas de la configuración regional predeterminada.
        System.out.println("A minúsculas: " + string.toLowerCase());
        // toUpperCase(), Convierte todos los caracteres de esta cadena a mayúsculas
        // utilizando las reglas de la configuración regional predeterminada.
        System.out.println("A mayúsculas: " + string.toUpperCase());
        // trim(), elimina espacios al inicio y al final
        System.out.println("Sin espacios inicio y final:" + string.trim());
    }

    private static boolean isPalindrome(String str) {
        String strWithoutSpaces = str.replaceAll("\s", "");
        int lRight = strWithoutSpaces.length() - 1;
        int lLeft = 0;
        while (lLeft < lRight) {
            char s1 = strWithoutSpaces.charAt(lLeft++);
            char s2 = strWithoutSpaces.charAt(lRight--);
            if (s1 != s2)
                return false;
        }
        return true;
        // o este
        // return strWithoutSpaces.contentEquals(new
        // StringBuffer(strWithoutSpaces).reverse());
    }

    private static boolean isAnagramWithSort(String str1, String str2) {
        if (str1.length() != str2.length())
            return false;
        char[] arr1 = str1.toCharArray();
        char[] arr2 = str2.toCharArray();
        Arrays.sort(arr1);
        Arrays.sort(arr2);

        return Arrays.equals(arr1, arr2);
    }

    private static boolean isAnagramWithCounting(String str1, String str2) {
        int CHARACTER_RANGE = 256;
        if (str1.length() != str2.length())
            return false;
        int count[] = new int[CHARACTER_RANGE];
        for (int i = 0; i < str1.length(); i++) {
            count[str1.charAt(i)]++;
            count[str2.charAt(i)]--;
        }
        for (int i = 0; i < CHARACTER_RANGE; i++) {
            if (count[i] != 0) {
                return false;
            }
        }
        return true;
    }

    private static boolean isIsogram(String str) {
        str = str.toLowerCase();
        int len = str.length();

        char arr[] = str.toCharArray();

        Arrays.sort(arr);
        for (int i = 0; i < len - 1; i++) {
            if (arr[i] == arr[i + 1])
                return false;
        }
        return true;
    }
}
