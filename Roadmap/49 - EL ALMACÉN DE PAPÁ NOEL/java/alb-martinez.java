import java.util.*;

public class alb-martinez {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        // Generación del código secreto aleatorio
        String secretCode = generateSecretCode();

        // Contador de intentos
        int attempts = 0;
        boolean guessedCorrectly = false;

        // Bucle hasta que el usuario se quede sin intentos o adivine el código
        while (attempts < 10 && !guessedCorrectly) {
            System.out.println("Attempt " + (attempts + 1) + " - Enter a 4-character code (A-C and 1-3): ");
            String userGuess = scanner.nextLine();

            // Validar longitud y caracteres
            if (userGuess.length() != 4 || !isValidCode(userGuess)) {
                System.out.println("Invalid code! Make sure to use a 4 characters between A-C and 1-3.");
                continue;
            }

            // Comprobar el intento del usuario y dar pistas
            String hint = getHint(secretCode, userGuess);
            System.out.println("Hints: " + hint);

            // Comprobar si el usuario ha adivinado el código secreto
            if (userGuess.equals(secretCode)) {
                guessedCorrectly = true;
                System.out.println("Congratulations! You've guessed the secret code!");
            }

            attempts++;
        }

        // Si el usuario no adivina el codigo en 10 intentos
        if (!guessedCorrectly) {
            System.out.println("Sorry, you've exhausted your 10 attemps! The secret code was: " + secretCode);
        }

        scanner.close();
    }

    // Metodo para generar el código secreto
    private static String generateSecretCode() {
        List<Character> availableChars = Arrays.asList('A', 'B', 'C', '1', '2', '3');
        Collections.shuffle(availableChars);

        // Tomamos los primeros 4 caracteres de la lista barajada
        StringBuilder code = new StringBuilder();
        for (int i = 0; i < 4; i++) {
            code.append(availableChars.get(i));
        }

        return code.toString();
    }

    // Método para validar si el código ingresado es correcto
    private static boolean isValidCode(String code) {
        return code.matches("[A-C1-3]{4}");
    }

    // Método para comparar el código secreto con el intento del usuario y dar pistas
    private static String getHint(String secretCode, String userGuess) {
        StringBuilder hint = new StringBuilder();

        // Recorremos cada carácter del intento y los comparamos con el código secreto
        for (int i = 0; i < 4; i++) {
            char c = userGuess.charAt(i);
            if (c == secretCode.charAt(i)) {
                hint.append("Correct ");
            } else if (secretCode.contains(String.valueOf(c))) {
                hint.append("Present ");
            } else {
                hint.append("Incorrect ");
            }
        }

        return hint.toString().trim();
    }
}
