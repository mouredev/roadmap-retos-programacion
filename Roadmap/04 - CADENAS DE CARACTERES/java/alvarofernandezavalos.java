import java.util.Arrays;

public class alvarofernandezavalos {

  public static void main(String[] args) {

    String palabra = "Alvaro.Fernandez.Avalos";

    System.out.println("Longitud: "+palabra.length());
    System.out.println("Mayúsculas: "+palabra.toUpperCase());
    System.out.println("Minúsculas: "+palabra.toLowerCase());
    System.out.println("Reemplazo: "+palabra.replace('a', 'i'));
    String [] split = palabra.split("\\.");
    for (String string : split) {
      System.out.println("División: "+string);
    }
    StringBuilder builder = new StringBuilder();
    builder.append("Hola ! ")
      .append(palabra.replace('.', ' '))
      .append(" !");
    System.out.println("String Builder: "+builder.toString());
    System.out.println("Recortar: "+palabra.replace('.', ' ').trim());

    String palabra1 = "Raton";
    String palabra2 = "Notar";
    System.out.println(palabra1 + " y " + palabra2 +" son palíndromos "+ palindromo(palabra1, palabra2));

    palabra1 = "Nacionalista";
    palabra2 = "Altisonancia";
    System.out.println(palabra1 + " y " + palabra2 +" son anagramas "+ anagramas(palabra1, palabra2));

    palabra1 = "Dermatoglyphics";
    System.out.println(palabra1 + "es isograma" + isograma(palabra1));
  }

  private static boolean isograma(String palabra1) {
    for (int i = 0; i < palabra1.length(); i++) {
      for (int x = i + 1; x < palabra1.length(); x++) {
        if (palabra1.charAt(i) == palabra1.charAt(x)) {
            return false;
        }
      }
    }
    return true;
  }

  private static boolean palindromo(String palabra1, String palabra2) {
    if (palabra1.length()!=palabra2.length()) return false;
    for (int i = 0, x = palabra2.length() -1 ; i < palabra1.length() - 1; i++, x--) {
      if (palabra1.toLowerCase().charAt(i)!=palabra2.toLowerCase().charAt(x)) return false;
    }
    return true;
  }

  private static boolean anagramas(String palabra1, String palabra2) {
    char[] charsPalabra1 = palabra1.toLowerCase().toCharArray();
    char[] charsPalabra2 = palabra2.toLowerCase().toCharArray();
    Arrays.sort(charsPalabra1);
    Arrays.sort(charsPalabra2);
    return Arrays.equals(charsPalabra1, charsPalabra2);
  }


}
