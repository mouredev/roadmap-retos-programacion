import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Main {
    public static void main(String[] args) {
        var numbers = findNumbers("Hay más de -2 y menos de 10 números aquí, o quizás solo hay 1.");
        var email = validateEmail("algo@gmail.com");
        var phone = validatePhoneNumber("123-456-7890");
        var url = validateUrl("https://www.google.com");
    }

    /**
     * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
     * creando una que sea capaz de encontrar y extraer todos los números
     * de un texto.
     */
    static List<String> findNumbers(String str) {
        List<String> numbers = new LinkedList<>();
        Pattern p = Pattern.compile("-?\\d+");
        Matcher m = p.matcher(str);

        while (m.find()) numbers.add(m.group());

        return numbers;
    }

    /**
     * Valida un correo electrónico.
     * @param email
     * @return
     */
    static boolean validateEmail(String email) {
        Pattern p = Pattern.compile("^(?=.{1,64}@)[A-Za-z0-9_-]+(\\.[A-Za-z0-9_-]+)*@[^-][A-Za-z0-9-]+(\\.[A-Za-z0-9-]+)*(\\.[A-Za-z]{2,})$");
        Matcher m = p.matcher(email);
        return m.matches();
    }

    /**
     * Valida un número de teléfono.
     * @param phone
     * @return
     */
    static boolean validatePhoneNumber(String phone) {
        Pattern p = Pattern.compile("\\d{10}|(?:\\d{3}-){2}\\d{4}|\\(\\d{3}\\)\\d{3}-?\\d{4}");
        Matcher m = p.matcher(phone);
        return m.matches();
    }

    /**
     * Valida una URL.
     * @param url
     * @return
     */
    static boolean validateUrl(String url) {
        Pattern p = Pattern.compile("^(https?|ftp|file)://[-a-zA-Z0-9+&@#/%?=~_|!:,.;]*[-a-zA-Z0-9+&@#/%=~_|]");
        Matcher m = p.matcher(url);
        return m .matches();
    }

}
