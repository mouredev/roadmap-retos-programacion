import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class simonguzman {
    public static void main(String[] args) {
        extractNumbersOfText();
    }

    static void extractNumbersOfText(){
        String text = "Este es un texto con numeros: 1,23,456,7890,0.5";
        Pattern pattern = Pattern.compile("\\d+(\\.\\d+)?"); //Expresion regular para encontrar numeros
        Matcher matcher = pattern.matcher(text);

        while(matcher.find()){
            System.out.println("Numero encontrado: "+matcher.group());
        }
    } 
}
