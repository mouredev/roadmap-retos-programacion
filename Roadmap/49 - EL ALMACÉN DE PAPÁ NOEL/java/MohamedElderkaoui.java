import java.util.*;

public class MohamedElderkaoui {
    public static void main(String[] args) {
        /*
 * EJERCICIO:
 * Papá Noel tiene que comenzar a repartir los regalos...
 * ¡Pero ha olvidado el código secreto de apertura del almacén!
 *
 * Crea un programa donde introducir códigos y obtener pistas.
 * 
 * Código:
 * - El código es una combinación de letras y números aleatorios
 *   de longitud 4. (Letras: de la A a la C, Números: del 1 al 3)
 * - No hay repetidos.
 * - Se genera de manera aleatoria al iniciar el programa.
 * 
 * Usuario:
 * - Dispone de 10 intentos para acertarlo.
 * - En cada turno deberá escribir un código de 4 caracteres, y 
 *   el programa le indicará para cada uno lo siguiente:
 *   - Correcto: Si el caracter está en la posición correcta.
 *   - Presente: Si el caracter existe, pero esa no es su posición.
 *   - Incorrecto: Si el caracter no existe en el código secreto.
 * - Deben controlarse errores de longitud y caracteres soportados.
 * 
 * Finalización:
 * - Papa Noel gana si descrifra el código antes de 10 intentos.
 * - Pierde si no lo logra, ya que no podría entregar los regalos.
 */

 // Aquí va tu código...

 String secretCode = generateSecretCode();
 System.out.println("¡El almacén de Papá Noel está cerrado!");
 System.out.println("Intenta adivinar el código secreto de 4 caracteres (Letras: A-C, Números: 1-3).");
 System.out.println("Tienes 10 intentos. ¡Buena suerte!");
 
 Scanner scanner = new Scanner(System.in);
 int attempts = 0;
 boolean hasGuessed = false;

 while (attempts < 10 && !hasGuessed) {
     System.out.printf("Intento %d/10: ", attempts + 1);
     String userInput = scanner.nextLine().toUpperCase();

     // Validar entrada del usuario
     if (!isValidInput(userInput)) {
         System.out.println("Entrada inválida. Asegúrate de que sea de 4 caracteres (A-C y 1-3) sin repetidos.");
         continue;
     }

     // Evaluar el intento
     String feedback = evaluateGuess(userInput, secretCode);
     System.out.println(feedback);

     if (userInput.equals(secretCode)) {
         hasGuessed = true;
     } else {
         attempts++;
     }
 }

 // Resultado final
 if (hasGuessed) {
     System.out.println("¡Felicidades! Has descifrado el código secreto y salvado la Navidad. 🎅🎁");
 } else {
     System.out.println("Oh no, no has logrado descifrar el código. 😔 El código era: " + secretCode);
 }

 scanner.close();
}

// Genera un código secreto de 4 caracteres aleatorios sin repetidos
private static String generateSecretCode() {
 List<Character> pool = Arrays.asList('A', 'B', 'C', '1', '2', '3');
 Collections.shuffle(pool);
 StringBuilder code = new StringBuilder();
 for (int i = 0; i < 4; i++) {
     code.append(pool.get(i));
 }
 return code.toString();
}

// Valida que la entrada del usuario sea de 4 caracteres, sin repetidos y permitidos
private static boolean isValidInput(String input) {
 if (input.length() != 4) {
     return false;
 }
 Set<Character> validChars = new HashSet<>(Arrays.asList('A', 'B', 'C', '1', '2', '3'));
 Set<Character> seenChars = new HashSet<>();
 for (char c : input.toCharArray()) {
     if (!validChars.contains(c) || seenChars.contains(c)) {
         return false;
     }
     seenChars.add(c);
 }
 return true;
}

// Evalúa el intento del usuario y genera pistas
private static String evaluateGuess(String guess, String secretCode) {
 StringBuilder feedback = new StringBuilder();
 for (int i = 0; i < guess.length(); i++) {
     char userChar = guess.charAt(i);
     if (userChar == secretCode.charAt(i)) {
         feedback.append(userChar).append(": Correcto ");
     } else if (secretCode.indexOf(userChar) != -1) {
         feedback.append(userChar).append(": Presente ");
     } else {
         feedback.append(userChar).append(": Incorrecto ");
     }
 }
 return feedback.toString().trim();
}
}