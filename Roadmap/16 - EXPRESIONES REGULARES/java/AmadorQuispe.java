

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class RegularExpresion {
    public static void main(String[] args) {
        String text = "El precio del producto es de $99.99 y hay 100 unidades disponibles, oferta de 45.56%";
        String email = "correo.dev@gmail.com";
        String phone = "+051 999 888 666";
        String url = "https://amsoft.dev";
        // EJERCICIO
        extractNumbers(text);
        // EXTRA
        System.out.println(String.format("Formato de email %s es %s", email, isFormatEmail(email)));
        System.out.println(String.format("Formato de phone %s es %s", phone, isFormatPhone(phone)));
        System.out.println(String.format("Formato de url %s es %s", url, isFormarUrl(url)));

    }

    private static void extractNumbers(String text) {
        Pattern pattern = Pattern.compile("\\d+\\.\\d+|\\d+");
        Matcher matcher = pattern.matcher(text);
        while (matcher.find()) {
            System.out.println(matcher.group());
        }
    }

    private static Boolean isFormatEmail(String email) {
        String regex = "^[a-zA-Z0-9._%+-]+@[a-zA-Z.-]+\\.[a-zA-Z]{2,}$";
        return email.matches(regex);

    }

    private static Boolean isFormatPhone(String phone) {
        String regex = "\\+051\\s\\d{3}\\s\\d{3}\\s\\d{3}";
        return phone.matches(regex);
    }

    private static Boolean isFormarUrl(String url) {
        String regex = "^(http|https)://[a-zA-Z0-9-]+(\\.[a-zA-Z0-9-]+)*(:\\d+)?(/\\S*)?$";
        return url.matches(regex);
    }

}
