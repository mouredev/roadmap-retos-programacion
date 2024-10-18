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

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class JimsimroDev {

  public static void print(String... strs) {
    for (String str : strs) {
      System.out.print(" " + str);
    }
    System.out.println();
  }

  public static void main(String[] args) {
    String divLine = ":::::::::::::::::::::::::::::";
    // operaciones
    String str = "Hola";
    String str1 = "Java";

    // concatenación
    System.out.println(divLine);
    print(str + ",", str1 + "!");
    System.out.println(str.concat(", " + str1 + "!"));

    // repetición
    System.out.println(divLine);
    System.out.println(str.repeat(4));
    for (int i = 0; i < 3; i++) {
      System.out.println(str);
    }

    // Indexacion
    System.out.println(divLine);
    String caracteres = String.valueOf(str.charAt(0)) + str.charAt(1) + str.charAt(2) + str.charAt(3);
    System.out.println(caracteres);

    // longitud
    System.out.println(divLine);
    System.out.println(str1.length());

    // porcion
    System.out.println(divLine);
    System.out.println(str.substring(1, 4));
    System.out.println(str.substring(0, 2));
    System.out.println(str.substring(1));

    // Busqueda
    System.out.println(divLine);
    System.out.println(str.contains("l"));
    System.out.println(str.contains("q"));

    // Reemplazo
    System.out.println(divLine);
    String remplazar = "Primera línea Segunda línea Tercera línea";
    System.out.println(str.replace("o", "a"));
    System.out.println(remplazar.replaceAll(" ", "#"));// reemplazo los espacios por * puedes remplazar todas las
                                                       // Ocurrencias de lo que quieras asi

    // División
    System.out.println(divLine);
    String[] parte = str1.split("v");
    System.out.println(Arrays.toString(parte));

    // Dive la cande por el salto de linea e imprime cada linea
    System.out.println(divLine);
    String miString = "Primera línea\nSegunda línea\nTercera línea";
    System.out.println(miString);

    // Valida si la candena esta vacia o esta en blanco devuelve true
    System.out.println(miString.isBlank());
    String cadena = "";
    String cadena1 = " ";
    System.out.println(cadena.isBlank());
    System.out.println(cadena1.isBlank());

    // Valida si esta vacia la cadena y si es 0 devuelve true
    System.out.println(cadena.isEmpty());
    System.out.println(cadena1.isEmpty());

    // mayúsculas, minúsculas y letras en mayúsculas
    System.out.println(divLine);
    print(str.toUpperCase());
    print(str.toLowerCase());

    // Eliminación de espacio al principion y al final
    System.out.println(divLine);
    System.out.println(divLine);
    System.out.println(" Jimmis J ".trim() + "Simanca");

    // Busqueda al principio y al final
    System.out.println(divLine);
    System.out.println(str.startsWith("Ho"));
    System.out.println(str.startsWith("Ja"));
    System.out.println(str.endsWith("la"));
    System.out.println(str.endsWith("va"));

    // Busqueda de la posción
    System.out.println(divLine);
    String str2 = "Java es tremendo y es el mas robusto";
    System.out.println(divLine);
    System.out.println(str2.indexOf("es"));
    System.out.println(str2.indexOf("tremendo"));
    System.out.println(str2.indexOf('n'));
    System.out.println(str2.lastIndexOf("es"));

    // Ocurrencias
    System.out.println(divLine);
    int contador = 0;
    for (int i = 0; i < str2.length(); i++) {
      if (str2.charAt(i) == 'e') {
        contador++;
      }
    }
    System.out.println(contador);

    // Formateo
    System.out.println(divLine);
    System.out.printf("Saludo: %s, lenguaje: %s", str, str1);
    String s = String.format("\nSaludo: %s, lenguaje: %s\n", str, str2);
    System.out.println(s);

    // Transformar lista a cadenas
    print(divLine);
    List<String> lista = Arrays.asList(str, ",", str1, "!");
    print(String.join(" ", lista));

    // Transformaciones
    print(divLine);
    String str3 = "1234567";
    System.out.println(Integer.valueOf(str3));

    String str4 = "1234567.123";
    System.out.println(Double.valueOf(str4));

    // EXTRA
    print(divLine);
    comprobar("anilina", "locos");
    print(divLine);
    comprobar("amor", "roma");
    print(divLine);

    Map<Character, Integer> strDic = new HashMap<>();
    String lenguaje = "phytonphytonphytonphyton";
    for (int i = 0; i < lenguaje.length(); i++) {
      char letraActual = lenguaje.charAt(i);
      strDic.put(letraActual, strDic.getOrDefault(letraActual, 0) + 1);
    }

    boolean isograma = true;
    List<Integer> valores = new ArrayList<>(strDic.values());
    Integer longitud = valores.get(0);
    for (Integer contar : valores) {
      if (contar != longitud) {
        isograma = false;
        break;
      }
    }
    System.out.println(isograma);
  }

  public static void comprobar(String str, String str1) {
    System.out.println("Palindromo!");
    validarPalindromo(str);
    validarPalindromo(str1);
    System.out.println(isPalindromo1(str));
    System.out.println(isPalindromo1(str1));

    System.out.println("Anagramas!");
    String strOrdenada = sort(str);
    String str1Ordenada = sort(str1);
    System.out.printf("%s es un anagrama de %s ? %b\n", str, str1, strOrdenada.equals(str1Ordenada));

  }

  private static boolean isPalindromo(String str) {
    for (int i = 0; i < str.length() / 2; i++) {
      if (str.charAt(i) == str.charAt(str.length() - 1)) {
        return true;
      }
    }
    return false;
  }

  private static boolean isPalindromo1(String str) {
    String invertida = new StringBuilder(str).reverse().toString();
    if (str.equals(invertida)) {
      return true;
    }
    return false;
  }

  private static void validarPalindromo(String str) {
    if (isPalindromo(str)) {
      System.out.printf("La palabra %s es un Palindromo\n", str);
    } else {
      System.out.printf("La palabra %s no es un Palindromo\n", str);
    }
  }

  private static String sort(String str) {
    char[] strArray = str.toCharArray();
    Arrays.sort(strArray);
    String ordanada = new String(strArray);
    return ordanada;
  }
}
