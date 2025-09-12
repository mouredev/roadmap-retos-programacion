import java.util.regex.*;
import java.util.*;

public class miguelex {
    public static void regExpr(String cadena) {
        String patron = "-?\\d+(\\.\\d+)?";
        Pattern p = Pattern.compile(patron);
        Matcher m = p.matcher(cadena);

        System.out.println("Números encontrados:");
        while (m.find()) {
            System.out.println(m.group());
        }
        System.out.println();
    }

    public static void main(String[] args) {
        String texto = "Este es un texto con números como 123, 45.6, -7 y 1000.";
        System.out.println("Vamos a analizar el siguiente texto:");
        System.out.println("'" + texto + "'\n");
        regExpr(texto);

        texto = "123Erase una vez un número 1234567890 y otro 0987654321. Y para terminar456";
        System.out.println("Vamos a analizar el siguiente texto:");
        System.out.println("'" + texto + "'\n");
        regExpr(texto);

        // Extra
        emailValidation("correo@correo.com");
        emailValidation("correo@correo");

        phoneValidation("+34 123456789");
        phoneValidation("123456789");

        urlValidation("http://www.google.com");
        urlValidation("www.google.com");
    }

    public static void emailValidation(String email) {
        String patron = "^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,4}$";
        Pattern p = Pattern.compile(patron);
        Matcher m = p.matcher(email);
        if (m.matches()) {
            System.out.println("El email " + email + " es válido.");
        } else {
            System.out.println("El email " + email + " no es válido.");
        }
    }

    public static void phoneValidation(String phone) {
        String patron = "^\\+?(\\d{2,3})?[-. ]?\\d{9}$";
        Pattern p = Pattern.compile(patron);
        Matcher m = p.matcher(phone);
        if (m.matches()) {
            System.out.println("El teléfono " + phone + " es válido.");
        } else {
            System.out.println("El teléfono " + phone + " no es válido.");
        }
    }

    public static void urlValidation(String url) {
        String patron = "^(http|https):\\/\\/[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,4}";
        Pattern p = Pattern.compile(patron);
        Matcher m = p.matcher(url);
        if (m.matches()) {
            System.out.println("La URL " + url + " es válida.");
        } else {
            System.out.println("La URL " + url + " no es válida.");
        }
    }
}
