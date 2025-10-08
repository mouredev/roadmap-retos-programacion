import java.util.regex.*;
import java.util.*;

public class AnaLauDB {
    public static void main(String[] args) {
        // Extraer todos los números de un texto
        String texto = "Mi número es 1234, tengo 2 gatos y 1 perro. El año es 2025.";
        Pattern patronNumeros = Pattern.compile("\\d+");
        Matcher matcher = patronNumeros.matcher(texto);

        System.out.println("Números encontrados en el texto:");
        while (matcher.find()) {
            System.out.println(matcher.group());
        }

        // DIFICULTAD EXTRA

        // 1. Validar email
        String email = "correo.ejemplo@dominio.com";
        Pattern patronEmail = Pattern.compile("^[\\w.-]+@[\\w.-]+\\.[a-zA-Z]{2,}$");
        System.out.println("\n¿Email válido?: " + patronEmail.matcher(email).matches());

        // 2. Validar número de teléfono (ejemplo: 10 dígitos)
        String telefono = "5512345678";
        Pattern patronTelefono = Pattern.compile("^\\d{10}$");
        System.out.println("¿Teléfono válido?: " + patronTelefono.matcher(telefono).matches());

        // 3. Validar URL
        String url = "https://www.ejemplo.com/path?query=valor";
        Pattern patronUrl = Pattern.compile("^(https?://)?([\\w.-]+)\\.([a-zA-Z]{2,})(/\\S*)?$");
        System.out.println("¿URL válida?: " + patronUrl.matcher(url).matches());
    }
}
