import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class eulogioep {
    public static void main(String[] args) {
        // Texto de ejemplo para probar las expresiones regulares
        String texto = "Hola, mi número es 123-456-789. Mi email es usuario@dominio.com " +
                       "y mi sitio web es https://www.ejemplo.com. Tengo 25 años y otro " +
                       "teléfono es +34 612 345 678.";
        
        // 1. Encontrar y extraer todos los números del texto
        System.out.println("1. Extracción de números:");
        extraerNumeros(texto);
        
        // DIFICULTAD EXTRA
        // 2. Validación de email
        System.out.println("\n2. Validación de email:");
        validarEmail("usuario@dominio.com");
        validarEmail("email_invalido.com");
        
        // 3. Validación de número de teléfono
        System.out.println("\n3. Validación de número de teléfono:");
        validarTelefono("123-456-789");
        validarTelefono("+34 612 345 678");
        validarTelefono("1234");
        
        // 4. Validación de URL
        System.out.println("\n4. Validación de URL:");
        validarURL("https://www.ejemplo.com");
        validarURL("http://ejemplo");
    }
    
    /**
     * Encuentra y extrae todos los números de un texto.
     * Utiliza la expresión regular \\d+ que significa:
     * \\d - cualquier dígito (0-9)
     * +   - uno o más dígitos
     */
    public static void extraerNumeros(String texto) {
        Pattern patron = Pattern.compile("\\d+");
        Matcher matcher = patron.matcher(texto);
        
        while (matcher.find()) {
            System.out.println("Número encontrado: " + matcher.group());
        }
    }
    
    /**
     * Valida un email usando una expresión regular.
     * ^[A-Za-z0-9+_.-]+@(.+)$ significa:
     * ^ - inicio de la línea
     * [A-Za-z0-9+_.-]+ - uno o más caracteres alfanuméricos, más algunos símbolos permitidos
     * @ - el símbolo @
     * (.+) - cualquier carácter (el dominio)
     * $ - fin de la línea
     */
    public static void validarEmail(String email) {
        String patronEmail = "^[A-Za-z0-9+_.-]+@(.+)$";
        System.out.println(email + " es válido: " + email.matches(patronEmail));
    }
    
    /**
     * Valida un número de teléfono usando una expresión regular.
     * ^(\\+\\d{1,3}\\s?)?(\\d{3}[-\\s]?){2}\\d{3}$ significa:
     * ^        - inicio de la línea
     * (\\+\\d{1,3}\\s?)? - código de país opcional (+34 )
     * (\\d{3}[-\\s]?)    - grupos de 3 dígitos separados por guión o espacio
     * \\d{3}$            - últimos 3 dígitos y fin de línea
     */
    public static void validarTelefono(String telefono) {
        String patronTelefono = "^(\\+\\d{1,3}\\s?)?(\\d{3}[-\\s]?){2}\\d{3}$";
        System.out.println(telefono + " es válido: " + telefono.matches(patronTelefono));
    }
    
    /**
     * Valida una URL usando una expresión regular.
     * ^(https?:\\/\\/)(www\\.)?([\\w]+\\.)+[\\w]{2,63}\\/?$ significa:
     * ^(https?:\\/\\/)   - inicio con http:// o https://
     * (www\\.)?          - www. opcional
     * ([\\w]+\\.)+       - uno o más subdominios
     * [\\w]{2,63}        - dominio de nivel superior (2-63 caracteres)
     * \\/?$              - barra final opcional y fin de línea
     */
    public static void validarURL(String url) {
        String patronURL = "^(https?:\\/\\/)(www\\.)?([\\w]+\\.)+[\\w]{2,63}\\/?$";
        System.out.println(url + " es válido: " + url.matches(patronURL));
    }
}