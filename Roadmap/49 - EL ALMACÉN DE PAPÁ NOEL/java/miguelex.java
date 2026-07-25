import java.util.*;

public class miguelex {
    public static void main(String[] args) {
        List<Character> chars = Arrays.asList('A', 'B', 'C', '1', '2', '3');
        Collections.shuffle(chars);
        String code = chars.subList(0, 4).stream().map(String::valueOf).reduce("", String::concat);

        Scanner scanner = new Scanner(System.in);
        int attempts = 10;

        System.out.println("¡Bienvenido! Tienes 10 intentos para descifrar el código.");

        while (attempts > 0) {
            System.out.println("Intento #" + attempts + ": Ingresa un código de 4 caracteres:");
            String input = scanner.nextLine().toUpperCase();

            if (input.length() != 4 || !input.matches("[A-C1-3]{4}")) {
                System.out.println("Código inválido. Debe tener 4 caracteres (letras A-C, números 1-3).");
                continue;
            }

            StringBuilder result = new StringBuilder();
            for (int i = 0; i < 4; i++) {
                if (input.charAt(i) == code.charAt(i)) {
                    result.append("Correcto, ");
                } else if (code.indexOf(input.charAt(i)) != -1) {
                    result.append("Presente, ");
                } else {
                    result.append("Incorrecto, ");
                }
            }

            System.out.println(result.substring(0, result.length() - 2));

            if (input.equals(code)) {
                System.out.println("¡Felicidades! Descifraste el código: " + code);
                return;
            }

            attempts--;
        }

        System.out.println("Lo siento, no lograste descifrar el código: " + code);
    }
}
