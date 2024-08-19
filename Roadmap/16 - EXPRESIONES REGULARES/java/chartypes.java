
import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class chartypes {
    public static void main(String[] args) {
        exercise();
        extra();

    }

    private static void exercise() {
        String regex = "\\d+";
        String input = "3456efg78";
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(input);

        while (matcher.find())
            System.out.println(matcher.group(0));
    }

    private static boolean validateEmail(String email) {
        String regex = "^\\D\\w+@\\w+.\\D{3,5}$";
        return Pattern.matches(regex, email);
    }

    private static boolean validatePhoneNumber(String phoneNumber) {
        String regex = "^(\\+\\d{1,4}(-|\s)?)?(\\d{1,3}(-|\s)?){2}\\d{1,4}$";
        return Pattern.matches(regex, phoneNumber);
    }

    private static boolean validateURL(String url) {
        String regex = "^http(s)?://(w{3}.)?\\w+\\.\\D{3,5}$";
        return Pattern.matches(regex, url);
    }

    private static void extra() {

        String email = "asdfsdf@ssaf22.com";
        String phoneNumber = "+1-123-123-3210";
        String url = "https://carlosperezm.com";

        System.out.println(validateEmail(email));
        System.out.println(validatePhoneNumber(phoneNumber));
        System.out.println(validateURL(url));

    }

}
