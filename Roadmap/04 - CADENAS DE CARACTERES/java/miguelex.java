public class miguelex {

    public static boolean isPalindromo(String cadena) {
        return cadena.toLowerCase().contentEquals(new StringBuilder(cadena.toLowerCase()).reverse());
    }

    public static boolean isAnagrama(String cadena1, String cadena2) {
        if (cadena1.length() != cadena2.length()) return false;
        String str1 = cadena1.toLowerCase().chars().sorted().collect(StringBuilder::new, StringBuilder::appendCodePoint, StringBuilder::append).toString();
        String str2 = cadena2.toLowerCase().chars().sorted().collect(StringBuilder::new, StringBuilder::appendCodePoint, StringBuilder::append).toString();
        return str1.equals(str2);
    }

    public static boolean isIsograma(String cadena) {
        return cadena.toLowerCase().chars().distinct().count() == cadena.length();
    }
    public static void main(String[] args) {
        String cadena = "Hola Mundo";
        System.out.println(cadena);
        System.out.println(cadena.replace("a","m"));
        System.out.println(cadena.toLowerCase());
        System.out.println(cadena.toUpperCase());
        System.out.println(cadena.concat(" desde Java"));
        System.out.println(cadena.charAt(2));
        System.out.println(cadena.substring(1,3));
        System.out.println(cadena.contains("en"));
        System.out.println(cadena.repeat(3));
        System.out.println(cadena.split(" "));
        System.out.println("Es Ana un palindromo? " + isPalindromo("Ana"));
        System.out.println("Es Amanecer un palindromo? " + isPalindromo("Amanecer"));
        System.out.println("Amor y Roma son anagramas? "+ isAnagrama("Amor","Roma"));
        System.out.println("Carbon y Petroleo son anagramas? "+ isAnagrama("Carbon","Petroleo"));
        System.out.println("Murcielago es un isograma? "+ isIsograma("Murcielago"));
        System.out.println("Miguelex es un isograma? "+ isIsograma("Miguelex"));

    }
}
