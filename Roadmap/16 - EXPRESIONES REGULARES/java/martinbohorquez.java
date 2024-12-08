import java.util.List;
import java.util.regex.Pattern;

/**
 * #16 EXPRESIONES REGULARES
 *
 * @author martinbohorquez
 */
public class martinbohorquez {

    public static void main(String[] args) {
        String texto = "Achieve your goals in 2024 by setting 3 milestones per quarter, " +
                "and track your progress every 30 days consistently!";
        String regex = "\\D+";// Split by non-digit characters
        Pattern pattern = Pattern.compile(regex);

        List<String> digits = pattern.splitAsStream(texto)
                .filter(s -> !s.isBlank())// Filter empty elements
                .toList();

        System.out.println(digits);

        /*
         * DIFICULTAD EXTRA
         */
        String email = "email";
        match(email, "ma.boh_26@gmail.com");
        match(email, "ma.boh-26@gmail-peru01.com.pe");
        match(email, "ma.boh.26@gmail.com");
        match(email, "ma_boh+26@gmail.com.pe");
        match(email, "ma.boh+26@gmail.com.pe");
        String phoneNumber = "phoneNumber";
        match(phoneNumber, "+51 999 345 654");
        match(phoneNumber, "+(51) 999 345 654");
        match(phoneNumber, "999345654");
        match(phoneNumber, "+51 123 345");
        match(phoneNumber, "32 999345654");
        String url = "url";
        match(url, "http://www.google.com?name=pepe");
        match(url, "https://www.facebook.com.pe/user/id=1");
        match(url, "m.tiktok.com/live/@mark");
        match(url, "www.peru-champions.com.pe/portal/id=3");
        match(url, "instagram.com.br/login?");
    }

    private static void match(String tipo, String texto) {
        String regexEmail = "^([\\w.+-]+@[\\w.-]+)$";
        String regexPhoneNumber = "^\\+?(\\(?\\d{1,3}\\)?)?(\\s\\d+)*|\\d{3,}(\\s\\d+)*$";
        String regexUrl = "^(?:https?://)?(?:(?:www|m)\\.)?((?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,})([/?]+\\S*)?$";

        switch (tipo) {
            case "email" ->
                    System.out.printf("El correo electrónico '%s' es válido: %b", texto, texto.matches(regexEmail));
            case "phoneNumber" ->
                    System.out.printf("El número telefónico '%s' es válido: %b", texto, texto.matches(regexPhoneNumber));
            case "url" -> System.out.printf("La URL '%s' es válida: %b", texto, texto.matches(regexUrl));
        }
    }
}

