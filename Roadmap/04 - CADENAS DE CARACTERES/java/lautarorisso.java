public class LogicaJava04 {

    public static void main(String[] args) {

        // Crear Strings
        String texto = "Backend Java";
        String otro = "Developer";

        System.out.println("Texto original: " + texto);

        // Longitud
        System.out.println("Longitud: " + texto.length());

        // Acceso a un carácter
        System.out.println("Primer carácter: " + texto.charAt(0));

        // Subcadena
        System.out.println("Subcadena (0,7): " + texto.substring(0, 7));

        // Concatenación
        String concatenado = texto + " " + otro;
        System.out.println("Concatenado: " + concatenado);
        String resultado = texto.concat(" Developer");
        System.out.println(resultado);

        // Repetición
        String repetido = "Ja".repeat(3);
        System.out.println("Repetido: " + repetido);

        // Recorrido carácter por carácter
        System.out.print("Recorrido: ");
        for (int i = 0; i < texto.length(); i++) {
            System.out.print(texto.charAt(i) + " ");
        }
        System.out.println();

        // Mayúsculas y minúsculas
        System.out.println("Mayúsculas: " + texto.toUpperCase());
        System.out.println("Minúsculas: " + texto.toLowerCase());

        // Reemplazo
        System.out.println("Reemplazo: " + texto.replace("Java", "Spring"));

        // Dividir (split)
        String[] partes = texto.split(" ");
        System.out.println("Split:");
        for (String p : partes) {
            System.out.println("- " + p);
        }

        // Unir (join)
        String unido = String.join(" | ", "Java", "Spring", "Backend");
        System.out.println("Join: " + unido);

        // Interpolación (String.format)
        String nombre = "Lau";
        int edad = 21;
        String mensaje = String.format("Hola %s, tenés %d años", nombre, edad);
        System.out.println("Interpolación: " + mensaje);

        // Verificaciones
        System.out.println("Contiene 'Java': " + texto.contains("Java"));
        System.out.println("Empieza con 'Back': " + texto.startsWith("Back"));
        System.out.println("Termina con 'Java': " + texto.endsWith("Java"));

        // Comparación de Strings
        String a = "Hola";
        String b = "Hola";
        System.out.println("equals(): " + a.equals(b)); // true
        System.out.println("== : " + (a == b));         // puede ser true o false

        // Vacío / espacios
        String vacio = "";
        String espacios = "   ";
        System.out.println("isEmpty(): " + vacio.isEmpty());
        System.out.println("isBlank(): " + espacios.isBlank());

        // Trim
        String conEspacios = "   Java   ";
        System.out.println("Trim: '" + conEspacios.trim() + "'");

        // Conversión String ↔ número
        int numero = Integer.parseInt("123");
        String numeroTexto = String.valueOf(456);
        System.out.println("String a int: " + numero);
        System.out.println("Int a String: " + numeroTexto);

        // Comparación lexicográfica
        System.out.println("compareTo: " + "abc".compareTo("abd")); // < 0

    }
}
