import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class danhingar {

    public static void main(String[] args) {
        String texto = "efe4325 f2erf tfr8r743ry";
        System.out.println(findNumbers(texto));

        // Extra
        validateEmail("example@gmail.com");
        validatePhone("6123456789");
        validateUrl("http://www.google.com");
    }

    private static List<String> findNumbers(String text) {
        Pattern pattern = Pattern.compile("\\d");
        Matcher matcher = pattern.matcher(text);
        List<String> matches = new ArrayList<>();
        while (matcher.find()) {
            matches.add(matcher.group());
        }
        return matches;
    }

    private static void validateEmail(String mail) {
        Pattern pattern = Pattern.compile("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$");
        Matcher matcher = pattern.matcher(mail);
        if (matcher.find()) {
            System.out.println("Email válido");
        } else {
            System.out.println("Email inválido");
        }
    }

    private static void validatePhone(String number) {
        Pattern pattern = Pattern.compile("^(\\+\\d{1,3}[- ]?)?\\(?\\d{1,4}\\)?[- ]?\\d{1,4}[- ]?\\d{1,4}$");
        Matcher matcher = pattern.matcher(number);
        if (matcher.find()) {
            System.out.println("Teléfono válido");
        } else {
            System.out.println("Teléfono inválido");
        }
    }

    private static void validateUrl(String url) {
        Pattern pattern = Pattern.compile("^(https?|ftp):\\/\\/[^\s/$.?#].[^\s]*$");
        Matcher matcher = pattern.matcher(url);
        if (matcher.find()) {
            System.out.println("Url válida");
        } else {
            System.out.println("Url inválida");
        }
    }

}
