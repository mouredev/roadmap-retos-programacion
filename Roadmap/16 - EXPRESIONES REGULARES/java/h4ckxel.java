/*
    * #16 EXPRESIONES REGULARES
*/
import java.util.regex.*;

public class Main {
    public static void main(String[] args) {
        String texto = "Este texto contiene 5 numeros del 1 al 5: 1,2,3,4,5";
        String regexNumeros = "\\d+";
        Pattern pattern = Pattern.compile(regexNumeros);
        Matcher matcher = pattern.matcher(texto);
        while (matcher.find()) {
            System.out.println(matcher.group());
        }
        System.out.println("------------------");
        /*
         * DIFICULTAD EXTRA 
        */

        String emailCorrecto = "abc@mail.com";
        String emailIncorrecto = "abcmail.com";
        String regexEmail = "^[a-zA-Z0-9._+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,4}$";

        System.out.println(emailCorrecto + " es un email valido? " + emailCorrecto.matches(regexEmail));
        System.out.println(emailIncorrecto + " es un email valido? " + emailIncorrecto.matches(regexEmail));

        String numeroCorrecto = "+51 987654321";
        String numeroIncorrecto = "987654321";
        String regexNumero = "^\\+[0-9]{2}\\s[0-9]{9}$";

        System.out.println(numeroCorrecto + " es un numero valido? " + numeroCorrecto.matches(regexNumero));
        System.out.println(numeroIncorrecto + " es un numero valido? " + numeroIncorrecto.matches(regexNumero));

        String urlCorrecta = "https://retosdeprogramacion.com";
        String urlIncorrecta = "retosdeprogramacion.com/";
        String regexUrl = "^https?://(www\\.)?[a-zA-Z0-9-]+\\.[a-zA-Z]{2,}$";

        System.out.println(urlCorrecta + " es una url valida? " + urlCorrecta.matches(regexUrl));
        System.out.println(urlIncorrecta + " es una url valida? " + urlIncorrecta.matches(regexUrl));
    }
}
