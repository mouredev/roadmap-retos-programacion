import java.security.SecureRandom;
import java.util.Random;
import java.util.Scanner;

public class Main {

    private final Random r = new SecureRandom();
    private final Scanner sc = new Scanner(System.in);
    private final String ALPHABET = "ABC123";
    private final int CODE_LENGTH = 4;
    private final String secretCode;

    public static void main(String[] args) {
        Main m = new Main();
        m.start();
    }

    public Main() {
        this.secretCode = generateSecretCode();
    }

    private String generateSecretCode() {
        StringBuilder sb = new StringBuilder();
        while (sb.length() < CODE_LENGTH) {
            char c = ALPHABET.charAt(r.nextInt(ALPHABET.length()));
            if (sb.indexOf(String.valueOf(c)) == -1) sb.append(c);
        }

        return sb.toString();
    }

    public void start() {
        int attempts = 0;

        while (attempts < 10) {
            System.out.println("Enter a code:");
            String code = sc.nextLine();
            checkCode(code.toUpperCase());
            attempts++;
        }

    }

    public void checkCode(String code) {
        if (code.isBlank()) {
            System.out.println("Please enter a code");
            return;
        }

        if (code.length() != CODE_LENGTH) {
            System.out.println("The code must be 4 characters long");
            return;
        }

        if (code.equals(secretCode)) {
            System.out.println("Congratulations! You have guessed the secret code.");
            System.exit(0);
        }

        for (int i = 0; i < CODE_LENGTH; i++) {
            char current = code.charAt(i);

            if (current == secretCode.charAt(i)) System.out.println("Character " + current + " is in the correct position");
            else if (secretCode.indexOf(current) != -1) System.out.println("Character " + current + " is in the secret code, but in the wrong position");
            else System.out.println("Character " + current + " is not in the secret code");
        }

    }

}
