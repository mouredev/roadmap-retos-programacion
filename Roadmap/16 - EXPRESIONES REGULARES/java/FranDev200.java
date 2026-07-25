import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class FranDev200 {


    static void main() {

        /*
         * EJERCICIO:
         * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
         * creando una que sea capaz de encontrar y extraer todos los números
         * de un texto.
         */

        String patron = "\\d+";

        String texto =
                "Usuario: PaulaS40\n" +
                        "Email: paula.sanchez84@gmail.com\n" +
                        "Teléfono: +34 612-345-789\n" +
                        "CódigoPostal: 28013\n" +
                        "FechaNacimiento: 12/05/1984\n" +
                        "HoraRegistro: 09:45:32\n" +
                        "Password: P@ssw0rd_2026\n" +
                        "Dirección: CalleMayor123, Madrid\n" +
                        "IP: 192.168.1.45\n" +
                        "UUID: a3f1-9B2c-77Xz\n" +
                        "PrecioProducto: 19.99€\n" +
                        "Descuento: 15%\n" +
                        "PedidoID: ORD-2026-0045\n" +
                        "Tarjeta: 1234-5678-9012-3456\n";

        Pattern pattern = Pattern.compile(patron);
        Matcher matcher = pattern.matcher(texto);

        while (matcher.find()) {
            System.out.println(matcher.group());
        }

        /*
        DIFICULTAD EXTRA (opcional):
         * Crea 3 expresiones regulares (a tu criterio) capaces de:
         * - Validar un email.
         * - Validar un número de teléfono.
         * - Validar una url.
        */

        String ptrEmail = "([a-zA-Z]*\\d*\\w.)*@gmail.com";
        String ptrNumero = "^\\d{9}$";
        String ptrUrl = "http(s)?:(.)+";

        String emails = "Fr4aBAv1ano.32dd2@gmail.com\n" +
                "Fr4aBAv1ano.32dd2@gmail\n" +
                "Fr4aBAv1ano.32dd2@gmail.es";

        String numeros = "624893413\n" +
                "9672944\n" +
                "3346753573";

        String urls = "https://regex101.com/\n" +
                "https://codegym.cc/es/groups/posts/es.130.expresiones-regulares-en-java\n" +
                "htts://codegym.cc/es/groups/posts/es.130.expresiones-regulares-en-java";

        System.out.println("\nVALIDANDO EMAILS (se mostraran los correctos)");
        System.out.println("- - - - - - - - - - - - - - - - - - - - - - - -");
        pattern =  Pattern.compile(ptrEmail);
        matcher = pattern.matcher(emails);

        while (matcher.find()) {
            System.out.println(matcher.group());
        }

        System.out.println("\nVALIDANDO NÚMEROS DE TELÉFONO (se mostraran los correctos)");
        System.out.println("- - - - - - - - - - - - - - - - - - - - - - - -");
        pattern =  Pattern.compile(ptrNumero, Pattern.MULTILINE);
        matcher = pattern.matcher(numeros);

        while (matcher.find()) {
            System.out.println(matcher.group());
        }

        System.out.println("\nVALIDANDO URLs (se mostraran los correctos)");
        System.out.println("- - - - - - - - - - - - - - - - - - - - - - - -");
        pattern =  Pattern.compile(ptrUrl);
        matcher = pattern.matcher(urls);

        while (matcher.find()) {
            System.out.println(matcher.group());
        }


    }

}
