package roadmap.ejercicio_49;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Scanner;

/*
 * EJERCICIO: Papá Noel tiene que comenzar a repartir los regalos... ¡Pero ha
 * olvidado el código secreto de apertura del almacén!
 *
 * Crea un programa donde introducir códigos y obtener pistas.
 *
 * Código: - El código es una combinación de letras y números aleatorios de
 * longitud 4. (Letras: de la A a la C, Números: del 1 al 3) - No hay repetidos.
 * - Se genera de manera aleatoria al iniciar el programa.
 *
 * Usuario: - Dispone de 10 intentos para acertarlo. - En cada turno deberá
 * escribir un código de 4 caracteres, y el programa le indicará para cada uno
 * lo siguiente: - Correcto: Si el caracter está en la posición correcta. -
 * Presente: Si el caracter existe, pero esa no es su posición. - Incorrecto: Si
 * el caracter no existe en el código secreto. - Deben controlarse errores de
 * longitud y caracteres soportados.
 *
 * Finalización: - Papa Noel gana si descrifra el código antes de 10 intentos. -
 * Pierde si no lo logra, ya que no podría entregar los regalos.
 */
public class JesusWay69 {

    public static void main(String[] args) {

        Character hiddenCode[] = {'?', '?', '?', '?'};
        final char allow[] = {'A', 'B', 'C', '1', '2', '3'};
        int attempts = 10;
        Scanner sc = new Scanner(System.in);
        var  password = new HashSet<Character>();
        while (password.size() < 4) password.add(allow[(char) (Math.random() * 6)]);
        
        System.out.println("Introduzca una clave de 4 caracteres que contenga A, B, C, 1, 2 0 3 sin repeticiones: ");

        while (attempts > 0) {
            System.out.print("Introduzca la clave: ");
            String attempt = sc.next().toUpperCase();
            if (attempt.matches("[A-C1-3]{4}")) {
                    int i =0;
                    for (char key : password) {
                        if (attempt.charAt(i) == key) {
                            System.out.println("El caracter " + attempt.charAt(i) + " está en la contraseña en su posición ");
                            hiddenCode[i] = attempt.charAt(i);
                        } else if (password.contains(attempt.charAt(i))) {
                            System.out.println("El caracter " + attempt.charAt(i) + " está en la contraseña pero no lo has puesto en su posición");
                        } else {
                            System.out.println("El caracter " + attempt.charAt(i) + " no está en la contraseña");
                        }
                            i++;
                    }
                    
                    System.out.print("Contraseña: ");
                    for (char element : hiddenCode) System.out.print(element + " ");
                    if (!Arrays.asList(hiddenCode).contains('?')){
                        System.out.println("\n\n¡¡ENHORABUENA, HAS ADIVINADO LA CONTRASEÑA!!");
                        System.out.println("\n      *****FELIZ NAVIDAD*****\n");
                        break;
                    }

            } else {
                System.out.println("\nEl código introducido tiene una longitud diferente a 4 o tiene algún caracter no válido.");
            }
            attempts--;
            if (attempts > 0) System.out.println((attempts > 1) ? "\nTe quedan " + attempts + " intentos"  : "\nTe queda 1 intento");
            if (attempts == 0) System.out.println("\n\nSe te han acabado los intentos, Papá Noel no podrá entregar los regalos 😔"); 
        }

    }

}
