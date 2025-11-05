import java.util.regex.Matcher;
import java.util.regex.Pattern;

import static java.lang.String.*;

public class JimsimroDev {
/*
 * EJERCICIO:
 * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
 * creando una que sea capaz de encontrar y extraer todos los números
 * de un texto.
 */
public static void regexTest1(String texto){
    Pattern patron = Pattern.compile("\\d+");
    patron.matcher(texto).results()
        .forEach(match -> System.out.println("Número encontrado: " + match.group()));
  }
    /*
     * DIFICULTAD EXTRA (opcional):
     * Crea 3 expresiones regulares (a tu criterio) capaces de:
     * - Validar un email.
     * - Validar un número de teléfono.
     * - Validar una url.
     */
    public static boolean validarMail(String mail){
        Pattern pattern = Pattern.compile("^[\\w\\.]+@[\\w\\.]+\\.[\\w]+$");
      return matcherTest(mail, pattern);
    }
    public static boolean validarPhone(String phone){
        Pattern pattern = Pattern.compile("^(\\+?\\d{1,3}\s*)?\\d{3}-\\d{3}-\\d{4}$");
       return  matcherTest(phone,pattern);
    }

    public static boolean validarUrl(String url){
        Pattern pattern = Pattern.compile("^https?:\\/\\/(?:www\\.)?[\\w-]+\\.[a-z]{2,3}$");
        return matcherTest(url,pattern);
    }

    public static boolean matcherTest(String texts, Pattern pattern){
        Matcher matcher = pattern.matcher(texts);
        return matcher.find();
    }
    public static void main(String[] args) {
        // Expresiones regulares en Java
        String texto = "Hola, mi número de teléfono es 123-456-7890 y mi correo es pepito@gmail.com";
        regexTest1(texto);
   //Extra
        //valid si el correo es valido
   String mail = "cualquier@gmail.com";
   System.out.printf((validarMail(mail) ? "El correo %s es valido" : "El email %s no es valido") + "%n", mail);

   //valida si el telfono es valido
   String phone = "+57300-734-27414";
   System.out.printf((validarPhone(phone) ? "El phone %s es valido" : "El phone %s no es valido") + "%n", phone);
   //valida si la url es valida
        String url = "https://www.google.com";
       System.out.printf((validarUrl(url) ? "La url %s es valida" : "La url %s no es valida") + "%n", url);
 }
}
