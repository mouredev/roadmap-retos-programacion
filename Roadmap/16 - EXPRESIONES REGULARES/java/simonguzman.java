import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class simonguzman {
    public static void main(String[] args) {
        extractNumbersOfText();
        validateEmail();
        validatePhoneNumber();
        validateUrl();
    }

    static void extractNumbersOfText(){
        String text = "Este es un texto con numeros: 1,23,456,7890,0.5";
        Pattern pattern = Pattern.compile("\\d+(\\.\\d+)?"); //Expresion regular para encontrar numeros
        Matcher matcher = pattern.matcher(text);

        while(matcher.find()){
            System.out.println("Numero encontrado: "+matcher.group());
        }
    } 

    static void validateEmail(){
        String email = "siguzman@unicauca.edu.co";
        String pattern = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$"; //Expresion regular para validaar el email
        if (Pattern.matches(pattern, email)){
            System.out.println("Email valido");
        }else{
            System.out.println("Email no valido");
        }
    }

    static void validatePhoneNumber(){
        String number = "+1 123 456 7890";
        String pattern = "^\\+?\\d{1,3}?[- .]?\\(?(?:\\d{2,3})\\)?[- .]?\\d\\d\\d[- .]?\\d\\d\\d\\d$"; // expresión regular para validar número de teléfono
        if (Pattern.matches(pattern, number)){
            System.out.println("Número de teléfono válido");
        }else{
            System.out.println("Numero de telefono no valido");
        }
    }

    static void validateUrl(){
        String url = "https://www.example.com/path/to/resource";
        String pattern = "^((http|https)://)(www.)?[a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%_\\+.~#?&//=]*)$"; // expresión regular para validar URL
        if(Pattern.matches(pattern, url)){
            System.out.println("Url valido.");
        }else{
            System.out.println("Url no valido");
        }

    }
}
